import argparse
from typing import List

from stock_information_scraper.csv_generator import CsvGenerator
from stock_information_scraper.html_fetcher import HtmlFetcher
from stock_information_scraper.stock_information import StockInformationGenerator


def create_tickers(ticker_file_path: str) -> List[str]:
    print(f"Reading tickers from {ticker_file_path}")
    result = []
    with open(ticker_file_path, "r") as ticker_file:
        for line in ticker_file:
            clean_line = line.split("#")[0].strip()
            if clean_line:
                result.append(clean_line)
            else:
                print(f"> '{line.strip()}' could not be read.")

    print(f"Tickers found: {', '.join(result)}")
    return result


if __name__ == "__main__":
    # Read args
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--ticker_file", type=str, help="Path to a ticker file.", nargs="?"
    )
    parser.add_argument(
        "-o", "--out_file", type=str, help="Name of CSV output file.", nargs="?"
    )
    args = parser.parse_args()

    # Get list of tickers
    ticker_file_path = "../tickers.txt"  # args.ticker_file
    tickers = create_tickers(ticker_file_path=ticker_file_path)

    # For each ticker get HtmlSources
    source_html_list = []
    for ticker in tickers:
        html_fetcher = HtmlFetcher(ticker=ticker)
        htmls = html_fetcher.get_source_htmls()
        source_html_list.append(htmls)

    # For each ticker get StockInformation from HtmlSources
    stock_information_list = []
    for source_html in source_html_list:
        stock_information_generator = StockInformationGenerator(
            source_htmls=source_html
        )
        stock_information = stock_information_generator.get_stock_information()
        stock_information_list.append(stock_information)

    # Put all StockInformation in CsvGenerator
    output_file = args.out_file if args.out_file else f'numbers_{"-".join(tickers)}.csv'
    csv_generator = CsvGenerator(stock_information_list=stock_information_list)
    csv_generator.save_csv(file_name=output_file)
