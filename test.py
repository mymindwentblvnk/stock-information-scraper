import unittest

from hamcrest import assert_that, equal_to, has_length

from data_providers import get_years, StockInformation, DataType


class TestScraper(unittest.TestCase):

    def test_META_stock_information(self):
        years = get_years(number_of_years=11)
        info = StockInformation('META').get_all_values(years)
        assert_that(info['ticker'], equal_to('META'))
        assert_that(info['data'][DataType.RETURN_ON_CAPITAL_ROIC.value['title']][2019], equal_to(30.10))
        assert_that(info['data'][DataType.BOOK_VALUE_PER_SHARE.value['title']][2013], equal_to(6.39))
        assert_that(info['data'][DataType.EPS_DILUTED.value['title']][2022], equal_to(8.59))
        assert_that(info['data'][DataType.REVENUE.value['title']][2020], equal_to(85965))
        assert_that(info['data'][DataType.FREE_CASH_FLOW_PER_SHARE.value['title']][2014], equal_to(2.10))
        # assert_that(meta_numbers[CSV_HEADER.index('growth_estimates')], equal_to(10.6))
        # assert_that(meta_numbers[CSV_HEADER.index('pe_ratio_min')], equal_to(8.476))
        # assert_that(meta_numbers[CSV_HEADER.index('pe_ratio_max')], equal_to(37.11))

    def test_LLY_stock_information(self):
        revenue_2022 = StockInformation('LLY').get_value(DataType.REVENUE, 2022)
        assert_that(revenue_2022, equal_to(28541.4))

    def test_max_min_year(self):
        info = StockInformation('GOGL').get_all_values([2023, 2022, 2019, 2018, 2000])
        assert_that(info['max_year'], equal_to(2023))
        assert_that(info['min_year'], equal_to(2000))


class TestGetYears(unittest.TestCase):

    def test_get_years_desc(self):
        years = get_years(start_year=2000, number_of_years=3, desc=True)
        assert_that(years, equal_to([2000, 1999, 1998]))

    def test_get_years_asc(self):
        years = get_years(number_of_years=3, start_year=2000, desc=False)
        assert_that(years, equal_to([2000, 2001, 2002]))

    def test_get_years_returns_10_years(self):
        assert_that(get_years(), has_length(10))
