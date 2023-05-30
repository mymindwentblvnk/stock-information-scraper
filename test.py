import unittest

from hamcrest import assert_that, equal_to, has_length

from stock_information import get_years, DataProvider, DataType
from main import create_csv_data


class TestScraper(unittest.TestCase):

    def test_META_stock_information(self):
        years = get_years()
        info = DataProvider('META').get_stock_information(years)
        assert_that(info.ticker, equal_to('META'))
        assert_that(info.return_on_capital[2019], equal_to(30.10))
        assert_that(info.book_value_per_share[2013], equal_to(6.39))
        assert_that(info.eps_diluted[2022], equal_to(8.59))
        assert_that(info.revenue[2020], equal_to(85965))
        assert_that(info.free_cash_flow_per_share[2014], equal_to(2.10))
        # This changes regularly. See https://www.zacks.com/stock/quote/META/detailed-earning-estimates for current value
        # assert_that(info.growth_estimates_next_5_years, equal_to(19.5))
        assert_that(info.pe_ratio_min, equal_to(8.476))
        assert_that(info.pe_ratio_max, equal_to(37.11))

    def test_LLY_stock_information(self):
        revenue_2022 = DataProvider('LLY').get_specific_value(DataType.REVENUE, 2022)
        assert_that(revenue_2022, equal_to(28541.4))

    def test_PANW_stock_information(self):
        pe_ratio_min = DataProvider('PANW').get_specific_value(DataType.PE_RATIO_MIN, -1)
        assert_that(pe_ratio_min, equal_to(280.78))

    def test_max_min_year(self):
        info = DataProvider('GOGL').get_stock_information([2023, 2022, 2019, 2018, 2000])
        assert_that(info.max_year, equal_to(2022))  # Since 2023 is not closed yet
        assert_that(info.min_year, equal_to(2018))  # Since we can only retrieve data for 10 years, 2000 will be None


class TestGetYears(unittest.TestCase):

    def test_get_years_desc(self):
        years = get_years(start_year=2000, number_of_years=3, desc=True)
        assert_that(years, equal_to([2000, 1999, 1998]))

    def test_get_years_asc(self):
        years = get_years(start_year=2000, number_of_years=3, desc=False)
        assert_that(years, equal_to([2000, 2001, 2002]))

    def test_get_years_returns_10_years(self):
        assert_that(get_years(number_of_years=10), has_length(10))


class TestCSV(unittest.TestCase):

    def test_META_csv(self):
        years = get_years()
        info = DataProvider('META').get_stock_information(years)
        csv_data = create_csv_data([info])

        # Check header
        header = csv_data[0]
        assert_that(header[0], equal_to("Ticker"))
        assert_that(header[1], equal_to("Return On Capital (2022)"))
        assert_that(header[4], equal_to("Return On Capital (2019)"))
        assert_that(header[20], equal_to("Book Value per Share (2013)"))
        assert_that(header[-1], equal_to("PE Ratio (Max)"))

        # Check data
        data = csv_data[1]
        assert_that(data[0], equal_to('META'))
        assert_that(data[1], equal_to(21.1))
        assert_that(data[4], equal_to(30.10))
        assert_that(data[20], equal_to(6.39))
        assert_that(data[-1], equal_to(37.11))
