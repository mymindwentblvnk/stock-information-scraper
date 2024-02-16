import time
from datetime import datetime
from enum import Enum
from typing import List, Dict

import requests
from bs4 import BeautifulSoup


def string_to_float(value: str) -> float:
    if value not in {"-", "NA", "--"}:
        return float(value.replace(",", ""))


def percent_to_float(value: str) -> float:
    return string_to_float(value.replace("%", ""))


class DataType(Enum):
    RETURN_ON_CAPITAL_ROIC = {
        "title": "Return on Capital (ROIC)",
        "cast_method": percent_to_float,
    }
    BOOK_VALUE_PER_SHARE = {
        "title": "Book Value per Share",
        "cast_method": string_to_float,
    }
    EPS_DILUTED = {"title": "EPS (Diluted)", "cast_method": string_to_float}
    REVENUE = {"title": "Revenue", "cast_method": string_to_float}
    FREE_CASH_FLOW_PER_SHARE = {
        "title": "Free Cash Flow Per Share",
        "cast_method": string_to_float,
    }
    GROWTH_ESTIMATES_NEXT_5_YEARS = {
        "title": "Growth Estimates - Next 5 Years",
        "cast_method": string_to_float,
    }
    PE_RATIO_MIN = {"title": "PE Ratio Min", "cast_method": string_to_float}
    PE_RATIO_MAX = {"title": "PE Ratio Max", "cast_method": string_to_float}


def _get_soup(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    while response.status_code != 200:
        print("Still loading...")
        time.sleep(10)
        response = requests.get(url, headers=headers)
    return BeautifulSoup(response.content, "html.parser")


def _extract_row_value(soup, row_title: str, year: int, cast_method) -> float:
    # Find index of year column
    year_index = None
    header_row = soup.select('table[data-test="financials"] > thead > tr')[0]

    for index, td in enumerate(header_row.select("th"), 0):
        # "Current" will be ignored, since we only extract final numbers.
        if td.text.strip() == str(year):
            year_index = index
            break

    if not year_index:
        return None

    # Find row to process
    row_to_process = None
    table_rows = soup.select('table[data-test="financials"] > tbody > tr')
    for r in table_rows:
        if row_title.lower() == r.select("td")[0].text.strip().lower():
            row_to_process = r
            break

    # Return value of cell
    cell_to_process = row_to_process.select("td")[year_index]
    if "Upgrade" in cell_to_process.text or row_title == cell_to_process.text.strip():
        return None
    else:
        return cast_method(cell_to_process.text.strip())


def _extract_growth_estimates(soup, row_title: str, cast_method) -> float:
    table_rows = soup.find("div", id="earnings_growth_estimates").select(
        "table > tbody > tr"
    )
    for r in table_rows:
        if row_title.endswith(r.select("td")[0].text.strip()):
            text = r.select("td")[1].text.strip()
            return cast_method(text)


def _extract_revenue(soup, row_title: str, year: int, cast_method) -> float:
    revenue_in_millions = _extract_row_value(soup, row_title, year, cast_method)
    if revenue_in_millions:
        return round(revenue_in_millions/1000.0, 2)
    else:
        return None

def _extract_pe_ratio_min(soup, cast_method) -> float:
    divs = soup.find_all("div", class_="key-stat")
    for div in divs:
        if "Minimum" in div.text:
            minimum = div.find("div", class_="key-stat-title").text.strip()
            return cast_method(minimum)


def _extract_pe_ratio_max(soup, cast_method) -> float:
    divs = soup.find_all("div", class_="key-stat")
    for div in divs:
        if "Maximum" in div.text:
            maximum = div.find("div", class_="key-stat-title").text.strip()
            return cast_method(maximum)


def get_years(
    start_year=datetime.today().year, number_of_years=11, desc=True
) -> List[int]:
    if desc:
        return list(range(start_year, start_year - number_of_years, -1))
    else:
        return list(range(start_year, start_year + number_of_years))


def _build_soup(ticker: str) -> Dict:
    stock_analysis_base_url = "https://stockanalysis.com/stocks"
    zack_base_url = "https://www.zacks.com/stock/quote"
    ycharts_base_url = "https://ycharts.com/companies"

    return_on_roic_url = f"{stock_analysis_base_url}/{ticker}/financials/ratios/"
    return_on_capital_roic_soup = _get_soup(return_on_roic_url)
    print(f"Loaded Return on ROIC from {return_on_roic_url}")

    book_value_per_share_url = (
        f"{stock_analysis_base_url}/{ticker}/financials/balance-sheet/"
    )
    book_value_per_share_soup = _get_soup(book_value_per_share_url)
    print(f"Book Value per Share from {book_value_per_share_url}")

    eps_diluted_url = f"{stock_analysis_base_url}/{ticker}/financials/"
    eps_diluted_soup = _get_soup(eps_diluted_url)
    print(f"Loaded EPS Diluted from {eps_diluted_url}")

    revenue_url = f"{stock_analysis_base_url}/{ticker}/financials/"
    revenue_soup = _get_soup(revenue_url)
    print(f"Loaded Revenue from {revenue_url}")

    free_cash_flow_per_share_url = (
        f"{stock_analysis_base_url}/{ticker}/financials/cash-flow-statement/"
    )
    free_cash_flow_per_share_soup = _get_soup(free_cash_flow_per_share_url)
    print(f"Loaded Free Cash Flow per Share from {free_cash_flow_per_share_url}")

    growth_estimates_next_5_years_url = (
        f"{zack_base_url}/{ticker}/detailed-earning-estimates"
    )
    growth_estimates_next_5_years_soup = _get_soup(growth_estimates_next_5_years_url)
    print(f"Loaded Growth Estimates from {growth_estimates_next_5_years_url}")

    pe_ratio_min_url = f"{ycharts_base_url}/{ticker}/pe_ratio"
    pe_ratio_min_soup = _get_soup(pe_ratio_min_url)
    print(f"Loaded PE Ratio MIN from {pe_ratio_min_url}")

    pe_ratio_max_url = f"{ycharts_base_url}/{ticker}/pe_ratio"
    pe_ratio_max_soup = _get_soup(pe_ratio_max_url)
    print(f"Loaded PE Ratio MAX from {pe_ratio_max_url}")

    return {
        DataType.RETURN_ON_CAPITAL_ROIC: return_on_capital_roic_soup,
        DataType.BOOK_VALUE_PER_SHARE: book_value_per_share_soup,
        DataType.EPS_DILUTED: eps_diluted_soup,
        DataType.REVENUE: revenue_soup,
        DataType.FREE_CASH_FLOW_PER_SHARE: free_cash_flow_per_share_soup,
        DataType.GROWTH_ESTIMATES_NEXT_5_YEARS: growth_estimates_next_5_years_soup,
        DataType.PE_RATIO_MIN: pe_ratio_min_soup,
        DataType.PE_RATIO_MAX: pe_ratio_max_soup,
    }


class StockInformation:

    ticker: str
    return_on_capital: Dict
    book_value_per_share: Dict
    eps_diluted: Dict
    revenue: Dict
    free_cash_flow_per_share: Dict
    growth_estimates_next_5_years: float
    pe_ratio_min: float
    pe_ratio_max: float

    @property
    def _all_years_with_data(self):
        all_dicts = [
            self.return_on_capital,
            self.book_value_per_share,
            self.eps_diluted,
            self.revenue,
            self.free_cash_flow_per_share,
        ]
        all_years_with_data = []
        for d in all_dicts:
            for year, value in d.items():
                if value:
                    all_years_with_data.append(year)
        return all_years_with_data

    @property
    def min_year(self) -> int:
        return min(self._all_years_with_data)

    @property
    def max_year(self) -> int:
        return max(self._all_years_with_data)


class DataProvider:

    def __init__(self, ticker: str):
        self.ticker = ticker
        print(f"Getting stock information for {self.ticker}")
        self._soup = _build_soup(ticker=self.ticker)

    def get_specific_value(self, data_type: DataType, year: int = None) -> float:
        if data_type == DataType.GROWTH_ESTIMATES_NEXT_5_YEARS:
            return _extract_growth_estimates(
                soup=self._soup[data_type],
                row_title=data_type.value["title"],
                cast_method=data_type.value["cast_method"],
            )
        elif data_type == DataType.PE_RATIO_MIN:
            return _extract_pe_ratio_min(
                soup=self._soup[data_type], cast_method=data_type.value["cast_method"]
            )
        elif data_type == DataType.PE_RATIO_MAX:
            return _extract_pe_ratio_max(
                soup=self._soup[data_type], cast_method=data_type.value["cast_method"]
            )
        elif data_type == DataType.REVENUE:
            return _extract_revenue(
                soup=self._soup[data_type],
                row_title=data_type.value['title'],
                year=year,
                cast_method=data_type.value["cast_method"]
            )
        else:
            assert year
            return _extract_row_value(
                soup=self._soup[data_type],
                row_title=data_type.value["title"],
                year=year,
                cast_method=data_type.value["cast_method"],
            )

    def get_stock_information(self, years: List[int]) -> StockInformation:
        result = StockInformation()
        result.ticker = self.ticker
        result.return_on_capital = {
            year: self.get_specific_value(DataType.RETURN_ON_CAPITAL_ROIC, year)
            for year in years
        }
        result.book_value_per_share = {
            year: self.get_specific_value(DataType.BOOK_VALUE_PER_SHARE, year)
            for year in years
        }
        result.eps_diluted = {
            year: self.get_specific_value(DataType.EPS_DILUTED, year) for year in years
        }
        result.revenue = {
            year: self.get_specific_value(DataType.REVENUE, year) for year in years
        }
        result.free_cash_flow_per_share = {
            year: self.get_specific_value(DataType.FREE_CASH_FLOW_PER_SHARE, year)
            for year in years
        }
        result.growth_estimates_next_5_years = self.get_specific_value(
            DataType.GROWTH_ESTIMATES_NEXT_5_YEARS
        )
        result.pe_ratio_max = self.get_specific_value(DataType.PE_RATIO_MAX)
        result.pe_ratio_min = self.get_specific_value(DataType.PE_RATIO_MIN)
        return result
