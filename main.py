import csv
from typing import List

from data_providers import DataProvider, get_years, StockInformation


def save_numbers_to_csv(information: List[StockInformation], file_name: str):
    min_year = min([i.min_year for i in information])
    max_year = max([i.max_year for i in information])
    years = list(reversed(range(min_year, max_year + 1)))

    # Build header
    header = []
    header.append('ticker')
    header.extend([f'Return On Capital ({year})' for year in years])
    header.extend([f'Book Value per Share ({year})' for year in years])
    header.extend([f'EPS (Diluted) ({year})' for year in years])
    header.extend([f'Revenue ({year})' for year in years])
    header.extend([f'Free Cash Flow Per Share ({year})' for year in years])
    header.append('Growth Estimates - Next 5 Years')
    header.append('PE Ratio (Min)')
    header.append('PE Ratio (Max)')

    data = []
    # Add numbers
    for ticker_info in information:
        # Build array with numbers
        ticker_numbers = [ticker_info.ticker]
        # Return Of Capital (ROIC)
        roic = ticker_info.return_on_capital
        ticker_numbers.extend([roic[year] for year in years])
        # Book Value per Share
        bvps = ticker_info.book_value_per_share
        ticker_numbers.extend([bvps[year] if bvps[year] else '' for year in years])
        # EPS (Diluted)
        eps = ticker_info.book_value_per_share
        ticker_numbers.extend([eps[year] if eps[year] else '' for year in years])
        # Revenue
        revenue = ticker_info.book_value_per_share
        ticker_numbers.extend([revenue[year] if revenue[year] else '' for year in years])
        # Free Cash Flow Per Share
        fcfps = ticker_info.free_cash_flow_per_share
        ticker_numbers.extend([fcfps[year] if fcfps[year] else '' for year in years])
        # Growth Estimates - Next 5 Years
        ticker_numbers.append(ticker_info.growth_estimates_next_5_years)
        # PE Ratio
        ticker_numbers.append(ticker_info.pe_ratio_min)
        ticker_numbers.append(ticker_info.pe_ratio_max)
        assert len(header) == len(ticker_numbers)

        # Add to data
        data.append(ticker_numbers)

    csv_data = [header]
    csv_data.extend(data)

    with open(file_name, 'w') as ticker_numbers_csv:
        csv.writer(ticker_numbers_csv, delimiter=",").writerows(csv_data)


if __name__ == '__main__':
    all_tickers = ['META', 'AAPL', 'MSFT', 'GOOGL', 'AMD', 'AMZN', 'LLY', 'NVDA', 'FSLR', 'PERI', 'TSLA', 'AGYS', 'NVO', 'WIRE', 'JBL', 'ENPH', 'SPOT', 'ASML', 'PANW', 'CI']
    years = get_years()
    stock_information = [DataProvider(ticker).get_stock_information(years) for ticker in all_tickers]
    save_numbers_to_csv(stock_information, 'numbers.csv')
