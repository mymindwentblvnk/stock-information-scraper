from hamcrest import assert_that, equal_to, has_length
import unittest

from data_providers import get_years
from scraper import get_numbers_for_ticker, CSV_HEADER


class TestScraper(unittest.TestCase):

    def test_META_stock_information(self):
        meta_numbers = get_numbers_for_ticker("META")
        assert_that(meta_numbers, has_length(55))
        assert_that(meta_numbers[CSV_HEADER.index('ticker')], equal_to('META'))
        assert_that(meta_numbers[CSV_HEADER.index('roic_2019')], equal_to(30.10))
        assert_that(meta_numbers[CSV_HEADER.index('bvps_2013')], equal_to(6.39))
        assert_that(meta_numbers[CSV_HEADER.index('eps_diluted_2022')], equal_to(8.59))
        assert_that(meta_numbers[CSV_HEADER.index('revenue_2020')], equal_to(85965))
        assert_that(meta_numbers[CSV_HEADER.index('fcfps_2014')], equal_to(2.10))
        assert_that(meta_numbers[CSV_HEADER.index('growth_estimates')], equal_to(10.6))
        assert_that(meta_numbers[CSV_HEADER.index('pe_ratio_min')], equal_to(8.476))
        assert_that(meta_numbers[CSV_HEADER.index('pe_ratio_max')], equal_to(37.11))

    def test_LLY_stock_information(self):
        lly_numbers = get_numbers_for_ticker('LLY')
        assert_that(lly_numbers[CSV_HEADER.index('revenue_2022')], equal_to(28541.4))


class TestGetYears(unittest.TestCase):

    def test_get_years_desc(self):
        years = get_years(3, start_year=2000, desc=True)
        assert_that(years, equal_to([2000, 1999, 1998]))

    def test_get_years_asc(self):
        years = get_years(3, start_year=2000, desc=False)
        assert_that(years, equal_to([2000, 2001, 2002]))
