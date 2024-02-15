import argparse
import csv
from typing import List

from stock_information import DataProvider, get_years, StockInformation


def save_csv(csv_data: List[List], file_name: str):
    print(f"Data will be saved to {file_name}")
    with open(file_name, "w") as ticker_numbers_csv:
        csv.writer(ticker_numbers_csv, delimiter=",").writerows(csv_data)


def create_csv_data(information: List[StockInformation]) -> List[List]:
    min_year = min([i.min_year for i in information])
    max_year = max([i.max_year for i in information])
    years = list(reversed(range(min_year, max_year + 1)))

    # Build header
    header = []
    header.append("Ticker")
    header.extend([f"Return On Capital ({year})" for year in years])
    header.extend([f"Book Value per Share ({year})" for year in years])
    header.extend([f"EPS (Diluted) ({year})" for year in years])
    header.extend([f"Revenue ({year})" for year in years])
    header.extend([f"Free Cash Flow Per Share ({year})" for year in years])
    header.append("Growth Estimates - Next 5 Years")
    header.append("PE Ratio (Min)")
    header.append("PE Ratio (Max)")

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
        ticker_numbers.extend([bvps[year] if bvps[year] else "" for year in years])
        # EPS (Diluted)
        eps = ticker_info.eps_diluted
        ticker_numbers.extend([eps[year] if eps[year] else "" for year in years])
        # Revenue
        revenue = ticker_info.revenue
        ticker_numbers.extend(
            [revenue[year] if revenue[year] else "" for year in years]
        )
        # Free Cash Flow Per Share
        fcfps = ticker_info.free_cash_flow_per_share
        ticker_numbers.extend([fcfps[year] if fcfps[year] else "" for year in years])
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
    return csv_data


def create_tickers(ticker_file_path: str):
    print(f"Reading tickers from {ticker_file_path}")
    tickers = []
    with open(ticker_file_path, "r") as ticker_file:
        for line in ticker_file:
            clean_line = line.split("#")[0].strip()
            if clean_line:
                tickers.append(clean_line)
            else:
                print(f"> '{line.strip()}' could not be read.")

    print(f"Tickers found: {', '.join(tickers)}")
    return tickers


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--ticker_file", type=str, help="Path to a ticker file.", nargs="?"
    )
    parser.add_argument(
        "-o", "--out_file", type=str, help="Name of CSV output file.", nargs="?"
    )
    args = parser.parse_args()

    all_tickers = create_tickers(args.ticker_file)
    output_file = (
        args.out_file if args.out_file else f'numbers_{"-".join(all_tickers)}.csv'
    )

    years = get_years()
    print(f"Processing years: {', '.join([str(y) for y in years])}")
    print(f"Result will be written to {output_file}")
    stock_information = [
        DataProvider(ticker).get_stock_information(years) for ticker in all_tickers
    ]
    csv_data = create_csv_data(stock_information)
    save_csv(csv_data=csv_data, file_name=output_file)
