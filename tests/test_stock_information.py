import pytest
from hamcrest import assert_that, equal_to

from stock_information_scraper.html_fetcher import SourceHtmls
from stock_information_scraper.stock_information import StockInformationGenerator


@pytest.fixture
def meta_source_htmls() -> SourceHtmls:
    return SourceHtmls(
        ticker="META",
        roic_html=open("data/meta_roic.html", "r").read(),
        book_value_html=open("data/meta_book_value.html", "r").read(),
        eps_html=open("data/meta_eps.html", "r").read(),
        revenue_html=open("data/meta_revenue.html", "r").read(),
        cash_flow_html=open("data/meta_cash_flow.html", "r").read(),
        growth_estimates_html=open("data/meta_growth_estimates.html", "r").read(),
        pe_min_html=open("data/meta_pe_ratio_min.html", "r").read(),
        pe_max_html=open("data/meta_pe_ratio_max.html", "r").read(),
    )


@pytest.fixture
def lly_source_htmls() -> SourceHtmls:
    return SourceHtmls(
        ticker="LLY",
        roic_html=open("data/lly_roic.html", "r").read(),
        book_value_html=open("data/lly_book_value.html", "r").read(),
        eps_html=open("data/lly_eps.html", "r").read(),
        revenue_html=open("data/lly_revenue.html", "r").read(),
        cash_flow_html=open("data/lly_cash_flow.html", "r").read(),
        growth_estimates_html=open("data/lly_growth_estimates.html", "r").read(),
        pe_min_html=open("data/lly_pe_ratio_min.html", "r").read(),
        pe_max_html=open("data/lly_pe_ratio_max.html", "r").read(),
    )


def test_lly(lly_source_htmls: SourceHtmls):
    # Given
    generator = StockInformationGenerator(source_htmls=lly_source_htmls)

    # When
    stock_information = generator.get_stock_information()

    # Then
    assert_that(stock_information.ticker.value, equal_to("LLY"))
    assert_that(stock_information.company.value, equal_to("Eli Lilly and Company"))
    assert_that(stock_information.max_year.value, equal_to(2022))
    assert_that(stock_information.roic_max_year.value, equal_to(23.22))
    assert_that(stock_information.roic_max_year_minus_1.value, equal_to(21.58))
    assert_that(stock_information.roic_max_year_minus_2.value, equal_to(27.85))
    assert_that(stock_information.roic_max_year_minus_3.value, equal_to(27.32))
    assert_that(stock_information.roic_max_year_minus_4.value, equal_to(15.71))
    assert_that(stock_information.roic_max_year_minus_5.value, equal_to(-0.85))
    assert_that(stock_information.roic_max_year_minus_6.value, equal_to(11.26))
    assert_that(stock_information.roic_max_year_minus_7.value, equal_to(10.68))
    assert_that(stock_information.roic_max_year_minus_8.value, equal_to(10.22))
    assert_that(stock_information.roic_max_year_minus_9.value, equal_to(20.51))
    assert_that(stock_information.book_value_max_year.value, equal_to(11.81))
    assert_that(stock_information.book_value_max_year_minus_1.value, equal_to(9.90))
    assert_that(stock_information.book_value_max_year_minus_2.value, equal_to(6.22))
    assert_that(stock_information.book_value_max_year_minus_3.value, equal_to(2.80))
    assert_that(stock_information.book_value_max_year_minus_4.value, equal_to(9.56))
    assert_that(stock_information.book_value_max_year_minus_5.value, equal_to(11.02))
    assert_that(stock_information.book_value_max_year_minus_6.value, equal_to(13.24))
    assert_that(stock_information.book_value_max_year_minus_7.value, equal_to(13.72))
    assert_that(stock_information.book_value_max_year_minus_8.value, equal_to(14.37))
    assert_that(stock_information.book_value_max_year_minus_9.value, equal_to(16.31))
    assert_that(stock_information.eps_max_year.value, equal_to(6.90))
    assert_that(stock_information.eps_max_year_minus_1.value, equal_to(6.12))
    assert_that(stock_information.eps_max_year_minus_2.value, equal_to(6.79))
    assert_that(stock_information.eps_max_year_minus_3.value, equal_to(8.89))
    assert_that(stock_information.eps_max_year_minus_4.value, equal_to(3.13))
    assert_that(stock_information.eps_max_year_minus_5.value, equal_to(-0.19))
    assert_that(stock_information.eps_max_year_minus_6.value, equal_to(2.58))
    assert_that(stock_information.eps_max_year_minus_7.value, equal_to(2.26))
    assert_that(stock_information.eps_max_year_minus_8.value, equal_to(2.23))
    assert_that(stock_information.eps_max_year_minus_9.value, equal_to(4.32))
    assert_that(stock_information.revenue_max_year.value, equal_to(28.54))
    assert_that(stock_information.revenue_max_year_minus_1.value, equal_to(28.32))
    assert_that(stock_information.revenue_max_year_minus_2.value, equal_to(24.54))
    assert_that(stock_information.revenue_max_year_minus_3.value, equal_to(22.32))
    assert_that(stock_information.revenue_max_year_minus_4.value, equal_to(21.49))
    assert_that(stock_information.revenue_max_year_minus_5.value, equal_to(19.97))
    assert_that(stock_information.revenue_max_year_minus_6.value, equal_to(21.22))
    assert_that(stock_information.revenue_max_year_minus_7.value, equal_to(19.96))
    assert_that(stock_information.revenue_max_year_minus_8.value, equal_to(19.62))
    assert_that(stock_information.revenue_max_year_minus_9.value, equal_to(23.11))
    assert_that(stock_information.cash_flow_max_year.value, equal_to(5.80))
    assert_that(stock_information.cash_flow_max_year_minus_1.value, equal_to(6.56))
    assert_that(stock_information.cash_flow_max_year_minus_2.value, equal_to(5.63))
    assert_that(stock_information.cash_flow_max_year_minus_3.value, equal_to(4.08))
    assert_that(stock_information.cash_flow_max_year_minus_4.value, equal_to(4.20))
    assert_that(stock_information.cash_flow_max_year_minus_5.value, equal_to(4.31))
    assert_that(stock_information.cash_flow_max_year_minus_6.value, equal_to(3.67))
    assert_that(stock_information.cash_flow_max_year_minus_7.value, equal_to(1.88))
    assert_that(stock_information.cash_flow_max_year_minus_8.value, equal_to(3.10))
    assert_that(stock_information.cash_flow_max_year_minus_9.value, equal_to(4.54))
    assert_that(stock_information.growth_estimates.value, equal_to(36.30))
    assert_that(stock_information.pe_min.value, equal_to(13.06))
    assert_that(stock_information.pe_max.value, equal_to(137.53))


def test_meta(meta_source_htmls: SourceHtmls):
    # Given
    generator = StockInformationGenerator(source_htmls=meta_source_htmls)

    # When
    stock_information = generator.get_stock_information()

    # Then
    assert_that(stock_information.ticker.value, equal_to("META"))
    assert_that(stock_information.company.value, equal_to("Meta Platforms, Inc."))
    assert_that(stock_information.max_year.value, equal_to(2023))
    assert_that(stock_information.roic_max_year.value, equal_to(20.24))
    assert_that(stock_information.roic_max_year_minus_1.value, equal_to(15.30))
    assert_that(stock_information.roic_max_year_minus_2.value, equal_to(28.06))
    assert_that(stock_information.roic_max_year_minus_3.value, equal_to(20.66))
    assert_that(stock_information.roic_max_year_minus_4.value, equal_to(16.04))
    assert_that(stock_information.roic_max_year_minus_5.value, equal_to(25.82))
    assert_that(stock_information.roic_max_year_minus_6.value, equal_to(21.03))
    assert_that(stock_information.roic_max_year_minus_7.value, equal_to(17.13))
    assert_that(stock_information.roic_max_year_minus_8.value, equal_to(8.36))
    assert_that(stock_information.roic_max_year_minus_9.value, equal_to(8.23))
    assert_that(stock_information.book_value_max_year.value, equal_to(59.51))
    assert_that(stock_information.book_value_max_year_minus_1.value, equal_to(46.79))
    assert_that(stock_information.book_value_max_year_minus_2.value, equal_to(44.36))
    assert_that(stock_information.book_value_max_year_minus_3.value, equal_to(45.00))
    assert_that(stock_information.book_value_max_year_minus_4.value, equal_to(35.41))
    assert_that(stock_information.book_value_max_year_minus_5.value, equal_to(29.11))
    assert_that(stock_information.book_value_max_year_minus_6.value, equal_to(25.63))
    assert_that(stock_information.book_value_max_year_minus_7.value, equal_to(20.68))
    assert_that(stock_information.book_value_max_year_minus_8.value, equal_to(15.78))
    assert_that(stock_information.book_value_max_year_minus_9.value, equal_to(13.81))
    assert_that(stock_information.eps_max_year.value, equal_to(14.87))
    assert_that(stock_information.eps_max_year_minus_1.value, equal_to(8.59))
    assert_that(stock_information.eps_max_year_minus_2.value, equal_to(13.77))
    assert_that(stock_information.eps_max_year_minus_3.value, equal_to(10.09))
    assert_that(stock_information.eps_max_year_minus_4.value, equal_to(6.43))
    assert_that(stock_information.eps_max_year_minus_5.value, equal_to(7.57))
    assert_that(stock_information.eps_max_year_minus_6.value, equal_to(5.39))
    assert_that(stock_information.eps_max_year_minus_7.value, equal_to(3.49))
    assert_that(stock_information.eps_max_year_minus_8.value, equal_to(1.29))
    assert_that(stock_information.eps_max_year_minus_9.value, equal_to(1.10))
    assert_that(stock_information.revenue_max_year.value, equal_to(134.9))
    assert_that(stock_information.revenue_max_year_minus_1.value, equal_to(116.61))
    assert_that(stock_information.revenue_max_year_minus_2.value, equal_to(117.93))
    assert_that(stock_information.revenue_max_year_minus_3.value, equal_to(85.97))
    assert_that(stock_information.revenue_max_year_minus_4.value, equal_to(70.7))
    assert_that(stock_information.revenue_max_year_minus_5.value, equal_to(55.84))
    assert_that(stock_information.revenue_max_year_minus_6.value, equal_to(40.65))
    assert_that(stock_information.revenue_max_year_minus_7.value, equal_to(27.64))
    assert_that(stock_information.revenue_max_year_minus_8.value, equal_to(17.93))
    assert_that(stock_information.revenue_max_year_minus_9.value, equal_to(12.47))
    assert_that(stock_information.cash_flow_max_year.value, equal_to(17.12))
    assert_that(stock_information.cash_flow_max_year_minus_1.value, equal_to(7.18))
    assert_that(stock_information.cash_flow_max_year_minus_2.value, equal_to(13.90))
    assert_that(stock_information.cash_flow_max_year_minus_3.value, equal_to(8.29))
    assert_that(stock_information.cash_flow_max_year_minus_4.value, equal_to(7.43))
    assert_that(stock_information.cash_flow_max_year_minus_5.value, equal_to(5.32))
    assert_that(stock_information.cash_flow_max_year_minus_6.value, equal_to(6.03))
    assert_that(stock_information.cash_flow_max_year_minus_7.value, equal_to(4.06))
    assert_that(stock_information.cash_flow_max_year_minus_8.value, equal_to(2.78))
    assert_that(stock_information.cash_flow_max_year_minus_9.value, equal_to(2.10))
    assert_that(stock_information.growth_estimates.value, equal_to(19.50))
    assert_that(stock_information.pe_min.value, equal_to(8.476))
    assert_that(stock_information.pe_max.value, equal_to(37.93))
