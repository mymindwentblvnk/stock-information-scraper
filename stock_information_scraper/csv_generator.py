import csv
from typing import List

from stock_information_scraper import CsvHeader
from stock_information_scraper.stock_information import StockInformation


class CsvGenerator:

    def __init__(self, stock_information_list: List[StockInformation]):
        self.stock_information = stock_information_list

    def save_csv(self, file_name: str, csv_headers: List = CsvHeader().to_list()):
        print(f"Data will be saved to {file_name}")
        data = [info.to_dict() for info in self.stock_information]
        with open(file_name, "w") as ticker_numbers_csv:
            writer = csv.DictWriter(ticker_numbers_csv, fieldnames=csv_headers)
            writer.writeheader()
            assert csv_headers == list(data[0].keys())
            writer.writerows(rowdicts=data)
