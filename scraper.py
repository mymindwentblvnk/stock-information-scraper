import csv
from typing import Dict, List

from bs4 import BeautifulSoup

import requests as requests

URL_RATIOS = 'https://stockanalysis.com/stocks/{ticker}/financials/ratios/'
URL_BALANCE_SHEET = 'https://stockanalysis.com/stocks/{ticker}/financials/balance-sheet/'
URL_FINANCIALS = 'https://stockanalysis.com/stocks/{ticker}/financials/'
URL_CASH_FLOW_STATEMENT = 'https://stockanalysis.com/stocks/{ticker}/financials/cash-flow-statement/'
URL_DETAILED_EARNING_ESTIMATES = 'https://www.zacks.com/stock/quote/{ticker}/detailed-earning-estimates'
URL_PE_RATIO = 'https://ycharts.com/companies/{ticker}/pe_ratio'

CSV_HEADER = [
    'ticker',

    'roic_current', 'roic_2022', 'roic_2021', 'roic_2020', 'roic_2019', 'roic_2018', 'roic_2017', 'roic_2016',
    'roic_2015', 'roic_2014', 'roic_2013',

    'bvps_2022', 'bvps_2021', 'bvps_2020', 'bvps_2019', 'bvps_2018', 'bvps_2017', 'bvps_2016', 'bvps_2015', 'bvps_2014',
    'bvps_2013',

    'eps_diluted_2022', 'eps_diluted_2021', 'eps_diluted_2020', 'eps_diluted_2019', 'eps_diluted_2018',
    'eps_diluted_2017', 'eps_diluted_2016', 'eps_diluted_2015', 'eps_diluted_2014', 'eps_diluted_2013',

    'revenue_2022', 'revenue_2021', 'revenue_2020', 'revenue_2019', 'revenue_2018', 'revenue_2017', 'revenue_2016',
    'revenue_2015', 'revenue_2014', 'revenue_2013',

    'fcfps_2022', 'fcfps_2021', 'fcfps_2020', 'fcfps_2019', 'fcfps_2018', 'fcfps_2017', 'fcfps_2016',
    'fcfps_2015', 'fcfps_2014', 'fcfps_2013',

    'growth_estimates',

    'pe_ratio_min', 'pe_ratio_max',
]


def get_soup(url: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'
        # nopep8: E501
    }
    response = requests.get(url, headers=headers)
    return BeautifulSoup(response.content, 'html.parser')


def extract_row_values(row_title: str, url: str, cast_method) -> List:
    soup = get_soup(url)
    table_rows = soup.select('table[data-test="financials"] > tbody > tr')
    for r in table_rows:
        if row_title == r.select('td')[0].text.strip():
            table_row = r
            break
    raw_numbers = []
    for td in table_row.select('td'):
        if "Upgrade" in td.text or row_title == td.text.strip():
            continue
        else:
            raw_numbers.append(td.text.strip())
    return [cast_method(n) for n in raw_numbers]


def extract_growth_estimates(row_title: str, url: str, cast_method) -> List:
    soup = get_soup(url)
    table_rows = soup.find('div', id='earnings_growth_estimates').select('table > tbody > tr')
    for r in table_rows:
        if row_title == r.select('td')[0].text.strip():
            return [cast_method(r.select('td')[1].text.strip())]


def extract_pe_ratio(url: str, cast_method) -> List:
    soup = get_soup(url)
    divs = soup.find_all('div', class_='key-stat')
    for div in divs:
        if "Minimum" in div.text:
            minimum = div.find('div', class_='key-stat-title').text.strip()
        elif "Maximum" in div.text:
            maximum = div.find('div', class_='key-stat-title').text.strip()
        else:
            pass
    return [cast_method(minimum), cast_method(maximum)]


def get_numbers_for_ticker(ticker: str) -> List:
    """
    Fetches the needed numbers for a ticker
    :param ticker:
    :return:
    """
    print(f"*** {ticker} ***")
    numbers = [ticker]

    # 1 Get ROIC (Return on Capital)
    roic_numbers: List = extract_row_values(url=URL_RATIOS.format(ticker=ticker),
                                            row_title="Return on Capital (ROIC)",
                                            cast_method=lambda x: float(x.replace('%', '')))
    print(f"ROIC: {roic_numbers}")
    numbers.extend(roic_numbers)

    # 2 Get Book Value per Share
    bvps_numbers: List = extract_row_values(url=URL_BALANCE_SHEET.format(ticker=ticker),
                                            row_title="Book Value Per Share",
                                            cast_method=lambda x: float(x.replace(',', '.')))
    print(f"Book Value per Share: {bvps_numbers}")
    numbers.extend(bvps_numbers)

    # 3 Get EPS (Diluted)
    eps_numbers: List = extract_row_values(url=URL_FINANCIALS.format(ticker=ticker),
                                           row_title="EPS (Diluted)",
                                           cast_method=lambda x: float(x.replace(',', '.')))
    print(f"EPS (Diluted): {eps_numbers}")
    numbers.extend(eps_numbers)

    # 4 Revenue
    revenue_numbers: List = extract_row_values(url=URL_FINANCIALS.format(ticker=ticker),
                                               row_title="Revenue",
                                               cast_method=lambda x: float(x.replace(',', '.')))
    print(f"Revenue: {revenue_numbers}")
    numbers.extend(revenue_numbers)

    # 5 Free Cash Flow per Share
    fcfps_numbers: List = extract_row_values(url=URL_CASH_FLOW_STATEMENT.format(ticker=ticker),
                                             row_title="Free Cash Flow Per Share",
                                             cast_method=lambda x: float(x.replace(',', '.')))
    print(f"Free Cash Flow Per Share: {fcfps_numbers}")
    numbers.extend(fcfps_numbers)

    # 6 Growth Estimates - Next 5 Years
    growth_estimates_numbers: List = extract_growth_estimates(url=URL_DETAILED_EARNING_ESTIMATES.format(ticker=ticker),
                                                              row_title="Next 5 Years",
                                                              cast_method=lambda x: float(x.replace(',', '.')))
    print(f"Growth Estimates - Next 5 Years: {growth_estimates_numbers}")
    numbers.extend(growth_estimates_numbers)

    # 7 PE Ratio - Minimum & Maximum - Past 5 Years
    pe_ratio_numbers: List = extract_pe_ratio(url=URL_PE_RATIO.format(ticker=ticker),
                                              cast_method=lambda x: float(x.replace(',', '.')))
    print(f"PE Ratio: {pe_ratio_numbers}")
    numbers.extend(pe_ratio_numbers)

    return numbers


def save_numbers_to_csv(numbers: List[List], file_name: str):
    csv_data = [CSV_HEADER]
    csv_data.extend(numbers)
    assert len(CSV_HEADER) == len(numbers[0])

    with open(file_name, 'w') as ticker_numbers_csv:
        csv.writer(ticker_numbers_csv, delimiter=",").writerows(csv_data)


if __name__ == '__main__':
    all_tickers = ['META', 'AAPL', 'MSFT']
    all_numbers = [get_numbers_for_ticker(t) for t in all_tickers]
    save_numbers_to_csv(all_numbers, 'ticker_numbers.csv')
