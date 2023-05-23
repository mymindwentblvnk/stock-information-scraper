import time
from datetime import datetime
from enum import Enum
from http.client import responses
from typing import List, Dict

import requests
from bs4 import BeautifulSoup



def string_to_float(value: str) -> float:
    if value not in {'-', 'NA', '--'}:
        return float(value.replace(',', ''))


def percent_to_float(value: str) -> float:
    return string_to_float(value.replace('%', ''))


class DataType(Enum):
    RETURN_ON_CAPITAL_ROIC = {
        'title': "Return on Capital (ROIC)",
        'cast_method': percent_to_float
    }
    BOOK_VALUE_PER_SHARE = {
        'title': "Book Value per Share",
        'cast_method': string_to_float
    }
    EPS_DILUTED = {
        'title': "EPS (Diluted)",
        'cast_method': string_to_float
    }
    REVENUE = {
        'title': "Revenue",
        'cast_method': string_to_float
    }
    FREE_CASH_FLOW_PER_SHARE = {
        'title': "Free Cash Flow Per Share",
        'cast_method': string_to_float
    }
    GROWTH_ESTIMATES_NEXT_5_YEARS = {
        'title': "Growth Estimates - Next 5 Years",
        'cast_method': string_to_float
    }
    PE_RATIO = {
        'title': "PE Ratio",
        'cast_method': string_to_float
    }


def get_soup(url: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    while response.status_code != 200:
        print(f"Waiting 10 seconds, since status is '{responses[response.status_code]} [{response.status_code}]'")
        time.sleep(10)
        response = requests.get(url, headers=headers)
    return BeautifulSoup(response.content, 'html.parser')


def extract_row_value(soup, row_title: str, year: int, cast_method) -> float:
    # Find index of year column
    year_index = 0
    if not year_index:
        return None

    # Find row to process
    table_rows = soup.select('table[data-test="financials"] > tbody > tr')
    row_to_process = None
    for r in table_rows:
        if row_title == r.select('td')[0].text.strip():
            row_to_process = r
            break

    # Return value of cell
    for td in row_to_process.select('td'):
        if "Upgrade" in td.text or row_title == td.text.strip():
            return None
        else:
            return cast_method(td.text.strip())


# def extract_growth_estimates(row_title: str, url: str, cast_method) -> List:
#     soup = get_soup(url)
#     table_rows = soup.find('div', id='earnings_growth_estimates').select('table > tbody > tr')
#     for r in table_rows:
#         if row_title == r.select('td')[0].text.strip():
#             text = r.select('td')[1].text.strip()
#             return [cast_method(text)]
#
#
# def extract_pe_ratio(url: str, cast_method) -> List:
#     soup = get_soup(url)
#     divs = soup.find_all('div', class_='key-stat')
#     for div in divs:
#         if "Minimum" in div.text:
#             minimum = div.find('div', class_='key-stat-title').text.strip()
#         elif "Maximum" in div.text:
#             maximum = div.find('div', class_='key-stat-title').text.strip()
#         else:
#             pass
#     return [cast_method(minimum), cast_method(maximum)]


def get_years(start_year=datetime.today().year, number_of_years=10, desc=True) -> List[int]:
    if desc:
        return list(range(start_year, start_year - number_of_years, -1))
    else:
        return list(range(start_year, start_year + number_of_years))


def _build_soup(ticker: str) -> Dict:
    stock_analysis_base_url = 'https://stockanalysis.com/stocks'
    zack_base_url = 'https://www.zacks.com/stock/quote'
    ycharts_base_url = 'https://ycharts.com/companies'
    return {
        DataType.RETURN_ON_CAPITAL_ROIC: get_soup(f'{stock_analysis_base_url}/{ticker}/financials/ratios/'),
        DataType.BOOK_VALUE_PER_SHARE: get_soup(f'{stock_analysis_base_url}/{ticker}/financials/balance-sheet/'),
        DataType.EPS_DILUTED: get_soup(f'{stock_analysis_base_url}/{ticker}/financials/'),
        DataType.REVENUE: get_soup(f'{stock_analysis_base_url}/{ticker}/financials/'),
        DataType.FREE_CASH_FLOW_PER_SHARE: get_soup(f'{stock_analysis_base_url}/{ticker}/financials/cash-flow-statement/'),
        DataType.GROWTH_ESTIMATES_NEXT_5_YEARS: get_soup(f'{zack_base_url}/{ticker}/detailed-earning-estimates'),
        DataType.PE_RATIO: get_soup(f'{ycharts_base_url}/{ticker}/pe_ratio')
    }


class DataProvider:

    def __init__(self, ticker: str):
        self.ticker = ticker
        self._soup = _build_soup(ticker=self.ticker)

    def get_value(self, data_type: DataType, year: int) -> float:
        if data_type == DataType.GROWTH_ESTIMATES_NEXT_5_YEARS:
            pass
        elif data_type == DataType.PE_RATIO:
            pass
        else:
            return extract_row_value(soup=self._soup[data_type],
                                     row_title=data_type.value['title'],
                                     year=year,
                                     cast_method=data_type.value['cast_method'])

    def get_all_values(self, years: List[int]) -> Dict:
        data = {}
        for data_type in DataType:
            title = data_type.value['title']
            data[title] = {}
            for year in years:
                data[title][year] = self.get_value(data_type, year)

        return {
            'min_year': 0,
            'max_year': 0,
            'data': data
        }


if __name__ == '__main__':
    data_provider = DataProvider('META')
    print(data_provider.get_all_values([2022, 2021]))
