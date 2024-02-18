import unittest

from hamcrest import assert_that, equal_to, has_length, is_not

from stock_information_scraper.csv_generator import CsvGenerator


class TestCsvGenerator(unittest.TestCase):

    def test_(self):
        # Given
        stock_information = None
        csv_generator = CsvGenerator(stock_information_list=stock_information)
        temp_file = None

        # When
        csv_generator.save_csv(file_name=temp_file)

        # Then
        # Assert on CSV content of temp file
