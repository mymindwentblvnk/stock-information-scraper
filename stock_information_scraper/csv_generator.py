import csv
from typing import List

from stock_information_scraper.stock_information import StockInformation


class CsvGenerator:

    def __init__(self, stock_information_list: List[StockInformation]):
        self.stock_information = stock_information_list

    def save_csv(self, file_name: str):
        print(f"Data will be saved to {file_name}")
        headers = list(self.stock_information[0].to_dict().keys())
        data = [info.to_dict() for info in self.stock_information]
        with open(file_name, "w") as ticker_numbers_csv:
            writer = csv.DictWriter(ticker_numbers_csv, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rowdicts=data)
