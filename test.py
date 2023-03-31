from hamcrest import assert_that, equal_to, has_length
import unittest

from scraper import get_numbers_for_ticker, CSV_HEADER


class TestScraper(unittest.TestCase):

    def test_META_stock_information(self):
        meta_numbers = get_numbers_for_ticker("META")
        assert_that(meta_numbers, has_length(55))
        assert_that(meta_numbers[CSV_HEADER.index('ticker')], equal_to('META'))
        assert_that(meta_numbers[CSV_HEADER.index('roic_2019')], equal_to(30.10))
        assert_that(meta_numbers[CSV_HEADER.index('bvps_2013')], equal_to(6.39))
        assert_that(meta_numbers[CSV_HEADER.index('eps_diluted_2022')], equal_to(8.59))
        assert_that(meta_numbers[CSV_HEADER.index('revenue_2020')], equal_to(85.965))
        assert_that(meta_numbers[CSV_HEADER.index('fcfps_2014')], equal_to(2.10))
        assert_that(meta_numbers[CSV_HEADER.index('growth_estimates')], equal_to(10.6))  # Those will fail in the future
        assert_that(meta_numbers[CSV_HEADER.index('pe_ratio_min')], equal_to(8.476))  # Those will fail in the future
        assert_that(meta_numbers[CSV_HEADER.index('pe_ratio_max')], equal_to(37.11))  # Those will fail in the future
