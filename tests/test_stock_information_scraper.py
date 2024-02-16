import unittest

from hamcrest import assert_that, equal_to, has_length, is_not

from stock_information_scraper.main import create_csv_data
from stock_information_scraper.stock_information import (
    get_years,
    DataProvider,
    DataType,
)


class TestScraper(unittest.TestCase):

    def test_META_stock_information(self):
        years = get_years()
        info = DataProvider("META").get_stock_information(years)
        assert_that(info.ticker, equal_to("META"))
        assert_that(info.return_on_capital[2019], equal_to(16.04))
        assert_that(info.book_value_per_share[2019], equal_to(35.41))
        assert_that(info.eps_diluted[2022], equal_to(8.59))
        assert_that(info.revenue[2020], equal_to(85.97))
        assert_that(info.free_cash_flow_per_share[2014], equal_to(2.10))
        # This changes regularly. See https://www.zacks.com/stock/quote/META/detailed-earning-estimates for current value
        # assert_that(info.growth_estimates_next_5_years, equal_to(19.5))
        # assert_that(info.pe_ratio_min, equal_to(8.476))
        # assert_that(info.pe_ratio_max, equal_to(37.11))

    def test_LLY_stock_information(self):
        data_provider = DataProvider("LLY")
        revenue_2022 = data_provider.get_specific_value(DataType.REVENUE, 2022)
        assert_that(revenue_2022, equal_to(28.54))
        eps_diluted_2022 = data_provider.get_specific_value(DataType.EPS_DILUTED, 2022)
        assert_that(eps_diluted_2022, equal_to(6.9))
        book_value_per_share_2022 = data_provider.get_specific_value(
            DataType.BOOK_VALUE_PER_SHARE, 2022
        )
        assert_that(book_value_per_share_2022, equal_to(11.81))

    def test_max_min_year(self):
        info = DataProvider("GOGL").get_stock_information(
            [2023, 2022, 2019, 2018, 2000]
        )
        assert_that(info.max_year, equal_to(2022))  # Since 2023 is not closed yet
        assert_that(
            info.min_year, equal_to(2018)
        )  # Since we can only retrieve data for 10 years, 2000 will be None


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
        info = DataProvider("META").get_stock_information(years)
        csv_data = create_csv_data([info])

        # Check header
        header = csv_data[0]
        assert_that(header[0], equal_to("Ticker"))
        assert_that(header[1], equal_to("Company"))
        assert_that(header[2], equal_to("Return On Capital (2023)"))
        assert_that(header[5], equal_to("Return On Capital (2020)"))
        assert_that(header[21], equal_to("Book Value per Share (2014)"))
        assert_that(header[-1], equal_to("PE Ratio (Max)"))

        # Check data
        data = csv_data[1]
        assert_that(data[0], equal_to("META"))
        assert_that(data[1], equal_to("Meta Platforms, Inc."))

    def test_LLY_csv(self):
        years = get_years()
        info = DataProvider("LLY").get_stock_information(years)
        csv_data = create_csv_data([info])

        # Check header
        header = csv_data[0]
        assert_that(header[0], equal_to("Ticker"))

        # Check data
        data = csv_data[1]
        assert_that(data[0], equal_to("LLY"))
        assert_that(data[11], is_not(equal_to(data[20])))
