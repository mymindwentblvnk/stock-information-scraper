from dataclasses import dataclass
from enum import Enum
from typing import Optional, Union

from bs4 import BeautifulSoup

from stock_information_scraper.html_fetcher import SourceHtmls


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


@dataclass
class SourceSoups:
    return_on_capital_roic_soup: BeautifulSoup
    book_value_per_share_soup: BeautifulSoup
    eps_diluted_soup: BeautifulSoup
    revenue_soup: BeautifulSoup
    free_cash_flow_per_share_soup: BeautifulSoup
    growth_estimates_next_5_years_soup: BeautifulSoup
    pe_ratio_min_soup: BeautifulSoup
    pe_ratio_max_soup: BeautifulSoup


def source_htmls_to_source_soups(sources: SourceHtmls) -> SourceSoups:
    def _get_soup(html: str) -> BeautifulSoup:
        return BeautifulSoup(html, "html.parser")

    return SourceSoups(
        return_on_capital_roic_soup=_get_soup(sources.return_on_capital_roic_html),
        book_value_per_share_soup=_get_soup(sources.book_value_per_share_html),
        eps_diluted_soup=_get_soup(sources.eps_diluted_html),
        revenue_soup=_get_soup(sources.revenue_html),
        free_cash_flow_per_share_soup=_get_soup(sources.free_cash_flow_per_share_html),
        growth_estimates_next_5_years_soup=_get_soup(
            sources.growth_estimates_next_5_years_html
        ),
        pe_ratio_min_soup=_get_soup(sources.pe_ratio_min_html),
        pe_ratio_max_soup=_get_soup(sources.pe_ratio_max_html),
    )


@dataclass()
class StockInformationEntry:
    key: str
    value: Optional[Union[float, str]]


@dataclass()
class StockInformation:
    ticker: StockInformationEntry
    company: StockInformationEntry
    max_year: StockInformationEntry
    return_on_capital_max_year: StockInformationEntry
    return_on_capital_max_year_minus_1: StockInformationEntry
    return_on_capital_max_year_minus_2: StockInformationEntry
    return_on_capital_max_year_minus_3: StockInformationEntry
    return_on_capital_max_year_minus_4: StockInformationEntry
    return_on_capital_max_year_minus_5: StockInformationEntry
    return_on_capital_max_year_minus_6: StockInformationEntry
    return_on_capital_max_year_minus_7: StockInformationEntry
    return_on_capital_max_year_minus_8: StockInformationEntry
    return_on_capital_max_year_minus_9: StockInformationEntry
    book_value_per_share_max_year: StockInformationEntry
    book_value_per_share_max_year_minus_1: StockInformationEntry
    book_value_per_share_max_year_minus_2: StockInformationEntry
    book_value_per_share_max_year_minus_3: StockInformationEntry
    book_value_per_share_max_year_minus_4: StockInformationEntry
    book_value_per_share_max_year_minus_5: StockInformationEntry
    book_value_per_share_max_year_minus_6: StockInformationEntry
    book_value_per_share_max_year_minus_7: StockInformationEntry
    book_value_per_share_max_year_minus_8: StockInformationEntry
    book_value_per_share_max_year_minus_9: StockInformationEntry
    eps_diluted_max_year: StockInformationEntry
    eps_diluted_max_year_minus_1: StockInformationEntry
    eps_diluted_max_year_minus_2: StockInformationEntry
    eps_diluted_max_year_minus_3: StockInformationEntry
    eps_diluted_max_year_minus_4: StockInformationEntry
    eps_diluted_max_year_minus_5: StockInformationEntry
    eps_diluted_max_year_minus_6: StockInformationEntry
    eps_diluted_max_year_minus_7: StockInformationEntry
    eps_diluted_max_year_minus_8: StockInformationEntry
    eps_diluted_max_year_minus_9: StockInformationEntry
    revenue_max_year: StockInformationEntry
    revenue_max_year_minus_1: StockInformationEntry
    revenue_max_year_minus_2: StockInformationEntry
    revenue_max_year_minus_3: StockInformationEntry
    revenue_max_year_minus_4: StockInformationEntry
    revenue_max_year_minus_5: StockInformationEntry
    revenue_max_year_minus_6: StockInformationEntry
    revenue_max_year_minus_7: StockInformationEntry
    revenue_max_year_minus_8: StockInformationEntry
    revenue_max_year_minus_9: StockInformationEntry
    free_cash_flow_per_share_max_year: StockInformationEntry
    free_cash_flow_per_share_max_year_minus_1: StockInformationEntry
    free_cash_flow_per_share_max_year_minus_2: StockInformationEntry
    free_cash_flow_per_share_max_year_minus_3: StockInformationEntry
    free_cash_flow_per_share_max_year_minus_4: StockInformationEntry
    free_cash_flow_per_share_max_year_minus_5: StockInformationEntry
    free_cash_flow_per_share_max_year_minus_6: StockInformationEntry
    free_cash_flow_per_share_max_year_minus_7: StockInformationEntry
    free_cash_flow_per_share_max_year_minus_8: StockInformationEntry
    free_cash_flow_per_share_max_year_minus_9: StockInformationEntry
    growth_estimates_next_5_years: StockInformationEntry
    pe_ratio_min: StockInformationEntry
    pe_ratio_max: StockInformationEntry

    def to_dict(self):
        result = {}
        for _, stock_information_entry in self.__dict__.items():
            result[stock_information_entry.key] = stock_information_entry.value
        return result


class StockInformationGenerator:

    def __init__(self, source_htmls: SourceHtmls):
        self.ticker: str = source_htmls.ticker
        self.source_soups: SourceSoups = source_htmls_to_source_soups(source_htmls)

    @property
    def company(self) -> str:
        soup = self.source_soups.revenue_soup  # Reads company name from revenue site
        header = soup.select("h1")[0].text
        header_without_ticker = header.split(f"({self.ticker})")[0].strip()
        return header_without_ticker

    @property
    def max_year(self) -> int:
        soup = self.source_soups.revenue_soup  # Reads company name from revenue site
        return 1986

    def _extract_row_value(
        self, soup: BeautifulSoup, row_title: str, year: int, cast_method
    ) -> Optional[Union[str, float, int]]:
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
        if (
            "Upgrade" in cell_to_process.text
            or row_title == cell_to_process.text.strip()
        ):
            return None
        else:
            return cast_method(cell_to_process.text.strip())

    def _extract_revenue(
        self, soup: BeautifulSoup, row_title: str, year: int, cast_method
    ) -> float | None:
        revenue_in_millions = self._extract_row_value(
            soup, row_title, year, cast_method
        )
        if revenue_in_millions:
            return round(revenue_in_millions / 1000.0, 2)
        else:
            return None

    def _extract_growth_estimates(
        self,
        row_title: str = "Growth Estimates - Next 5 Years",
        cast_method=string_to_float,
    ) -> float:
        soup = self.source_soups.growth_estimates_next_5_years_soup
        table_rows = soup.find("div", id="earnings_growth_estimates").select(
            "table > tbody > tr"
        )
        for r in table_rows:
            if row_title.endswith(r.select("td")[0].text.strip()):
                text = r.select("td")[1].text.strip()
                return cast_method(text)

    def _extract_pe_ratio_min(self, cast_method=string_to_float) -> float:
        soup = self.source_soups.pe_ratio_min_soup
        divs = soup.find_all("div", class_="key-stat")
        for div in divs:
            if "Minimum" in div.text:
                minimum = div.find("div", class_="key-stat-title").text.strip()
                return cast_method(minimum)

    def _extract_pe_ratio_max(self, cast_method=string_to_float) -> Optional[float]:
        soup = self.source_soups.pe_ratio_max_soup
        divs = soup.find_all("div", class_="key-stat")
        for div in divs:
            if "Maximum" in div.text:
                maximum = div.find("div", class_="key-stat-title").text.strip()
                return cast_method(maximum)

    def get_stock_information(self) -> StockInformation:
        growth_estimates = self._extract_growth_estimates()
        pe_ratio_min = self._extract_pe_ratio_min()
        pe_ratio_max = self._extract_pe_ratio_max()

        return StockInformation(
            ticker=StockInformationEntry(key="Ticker", value=self.ticker),
            company=StockInformationEntry(key="Company", value=self.company),
            max_year=StockInformationEntry(key="Max Year", value=self.max_year),
            return_on_capital_max_year=StockInformationEntry(
                key="Return on Capital ROIC (Max Year)", value=None
            ),
            return_on_capital_max_year_minus_1=StockInformationEntry(
                key="Return on Capital ROIC (Max Year - 1)", value=None
            ),
            return_on_capital_max_year_minus_2=StockInformationEntry(
                key="Return on Capital ROIC (Max Year - 2)", value=None
            ),
            return_on_capital_max_year_minus_3=StockInformationEntry(
                key="Return on Capital ROIC (Max Year - 3)", value=None
            ),
            return_on_capital_max_year_minus_4=StockInformationEntry(
                key="Return on Capital ROIC (Max Year - 4)", value=None
            ),
            return_on_capital_max_year_minus_5=StockInformationEntry(
                key="Return on Capital ROIC (Max Year - 5)", value=None
            ),
            return_on_capital_max_year_minus_6=StockInformationEntry(
                key="Return on Capital ROIC (Max Year - 6)", value=None
            ),
            return_on_capital_max_year_minus_7=StockInformationEntry(
                key="Return on Capital ROIC (Max Year - 7)", value=None
            ),
            return_on_capital_max_year_minus_8=StockInformationEntry(
                key="Return on Capital ROIC (Max Year - 8)", value=None
            ),
            return_on_capital_max_year_minus_9=StockInformationEntry(
                key="Return on Capital ROIC (Max Year - 9)", value=None
            ),
            book_value_per_share_max_year=StockInformationEntry(
                key="Book Value per Share (Max Year)", value=None
            ),
            book_value_per_share_max_year_minus_1=StockInformationEntry(
                key="Book Value per Share (Max Year - 1)", value=None
            ),
            book_value_per_share_max_year_minus_2=StockInformationEntry(
                key="Book Value per Share (Max Year - 2)", value=None
            ),
            book_value_per_share_max_year_minus_3=StockInformationEntry(
                key="Book Value per Share (Max Year - 3)", value=None
            ),
            book_value_per_share_max_year_minus_4=StockInformationEntry(
                key="Book Value per Share (Max Year - 4)", value=None
            ),
            book_value_per_share_max_year_minus_5=StockInformationEntry(
                key="Book Value per Share (Max Year - 5)", value=None
            ),
            book_value_per_share_max_year_minus_6=StockInformationEntry(
                key="Book Value per Share (Max Year - 6)", value=None
            ),
            book_value_per_share_max_year_minus_7=StockInformationEntry(
                key="Book Value per Share (Max Year - 7)", value=None
            ),
            book_value_per_share_max_year_minus_8=StockInformationEntry(
                key="Book Value per Share (Max Year - 8)", value=None
            ),
            book_value_per_share_max_year_minus_9=StockInformationEntry(
                key="Book Value per Share (Max Year - 9)", value=None
            ),
            eps_diluted_max_year=StockInformationEntry(
                key="EPS Diluted (Max Year)", value=None
            ),
            eps_diluted_max_year_minus_1=StockInformationEntry(
                key="EPS Diluted (Max Year - 1)", value=None
            ),
            eps_diluted_max_year_minus_2=StockInformationEntry(
                key="EPS Diluted (Max Year - 2)", value=None
            ),
            eps_diluted_max_year_minus_3=StockInformationEntry(
                key="EPS Diluted (Max Year - 3)", value=None
            ),
            eps_diluted_max_year_minus_4=StockInformationEntry(
                key="EPS Diluted (Max Year - 4)", value=None
            ),
            eps_diluted_max_year_minus_5=StockInformationEntry(
                key="EPS Diluted (Max Year - 5)", value=None
            ),
            eps_diluted_max_year_minus_6=StockInformationEntry(
                key="EPS Diluted (Max Year - 6)", value=None
            ),
            eps_diluted_max_year_minus_7=StockInformationEntry(
                key="EPS Diluted (Max Year - 7)", value=None
            ),
            eps_diluted_max_year_minus_8=StockInformationEntry(
                key="EPS Diluted (Max Year - 8)", value=None
            ),
            eps_diluted_max_year_minus_9=StockInformationEntry(
                key="EPS Diluted (Max Year - 9)", value=None
            ),
            revenue_max_year=StockInformationEntry(
                key="Revenue (Max Year)", value=None
            ),
            revenue_max_year_minus_1=StockInformationEntry(
                key="Revenue (Max Year - 1)", value=None
            ),
            revenue_max_year_minus_2=StockInformationEntry(
                key="Revenue (Max Year - 2)", value=None
            ),
            revenue_max_year_minus_3=StockInformationEntry(
                key="Revenue (Max Year - 3)", value=None
            ),
            revenue_max_year_minus_4=StockInformationEntry(
                key="Revenue (Max Year - 4)", value=None
            ),
            revenue_max_year_minus_5=StockInformationEntry(
                key="Revenue (Max Year - 5)", value=None
            ),
            revenue_max_year_minus_6=StockInformationEntry(
                key="Revenue (Max Year - 6)", value=None
            ),
            revenue_max_year_minus_7=StockInformationEntry(
                key="Revenue (Max Year - 7)", value=None
            ),
            revenue_max_year_minus_8=StockInformationEntry(
                key="Revenue (Max Year - 8)", value=None
            ),
            revenue_max_year_minus_9=StockInformationEntry(
                key="Revenue (Max Year - 9)", value=None
            ),
            free_cash_flow_per_share_max_year=StockInformationEntry(
                key="Free Cash Flow (Max Year)", value=None
            ),
            free_cash_flow_per_share_max_year_minus_1=StockInformationEntry(
                key="Free Cash Flow (Max Year - 1)", value=None
            ),
            free_cash_flow_per_share_max_year_minus_2=StockInformationEntry(
                key="Free Cash Flow (Max Year - 2)", value=None
            ),
            free_cash_flow_per_share_max_year_minus_3=StockInformationEntry(
                key="Free Cash Flow (Max Year - 3)", value=None
            ),
            free_cash_flow_per_share_max_year_minus_4=StockInformationEntry(
                key="Free Cash Flow (Max Year - 4)", value=None
            ),
            free_cash_flow_per_share_max_year_minus_5=StockInformationEntry(
                key="Free Cash Flow (Max Year - 5)", value=None
            ),
            free_cash_flow_per_share_max_year_minus_6=StockInformationEntry(
                key="Free Cash Flow (Max Year - 6)", value=None
            ),
            free_cash_flow_per_share_max_year_minus_7=StockInformationEntry(
                key="Free Cash Flow (Max Year - 7)", value=None
            ),
            free_cash_flow_per_share_max_year_minus_8=StockInformationEntry(
                key="Free Cash Flow (Max Year - 8)", value=None
            ),
            free_cash_flow_per_share_max_year_minus_9=StockInformationEntry(
                key="Free Cash Flow (Max Year - 9)", value=None
            ),
            growth_estimates_next_5_years=StockInformationEntry(
                key="Growth Estimates Next 5 Years", value=growth_estimates
            ),
            pe_ratio_min=StockInformationEntry(
                key="PE Ratio (Min)", value=pe_ratio_min
            ),
            pe_ratio_max=StockInformationEntry(
                key="PE Ratio (Max)", value=pe_ratio_max
            ),
        )
        pass
