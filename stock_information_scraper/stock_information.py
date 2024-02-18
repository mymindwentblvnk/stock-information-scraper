from dataclasses import dataclass
from typing import Optional, Union

from bs4 import BeautifulSoup

from stock_information_scraper import CsvHeader
from stock_information_scraper.html_fetcher import SourceHtmls

HEADERS = CsvHeader()


def string_to_float(value: str) -> float:
    if value not in {"-", "NA", "--"}:
        return float(value.replace(",", ""))


def percent_to_float(value: str) -> float:
    return string_to_float(value.replace("%", ""))


@dataclass
class SourceSoups:
    roic_soup: BeautifulSoup
    book_value_soup: BeautifulSoup
    eps_soup: BeautifulSoup
    revenue_soup: BeautifulSoup
    cash_flow_soup: BeautifulSoup
    growth_estimates_soup: BeautifulSoup
    pe_min_soup: BeautifulSoup
    pe_max_soup: BeautifulSoup


def source_htmls_to_source_soups(sources: SourceHtmls) -> SourceSoups:
    def _get_soup(html: str) -> BeautifulSoup:
        return BeautifulSoup(html, "html.parser")

    return SourceSoups(
        roic_soup=_get_soup(sources.roic_html),
        book_value_soup=_get_soup(sources.book_value_html),
        eps_soup=_get_soup(sources.eps_html),
        revenue_soup=_get_soup(sources.revenue_html),
        cash_flow_soup=_get_soup(sources.cash_flow_html),
        growth_estimates_soup=_get_soup(sources.growth_estimates_html),
        pe_min_soup=_get_soup(sources.pe_min_html),
        pe_max_soup=_get_soup(sources.pe_max_html),
    )


@dataclass()
class StockInformationEntry:
    csv_header: str
    value: Optional[Union[float, str]]


@dataclass()
class StockInformation:
    ticker: StockInformationEntry
    company: StockInformationEntry
    max_year: StockInformationEntry
    roic_max_year: StockInformationEntry
    roic_max_year_minus_1: StockInformationEntry
    roic_max_year_minus_2: StockInformationEntry
    roic_max_year_minus_3: StockInformationEntry
    roic_max_year_minus_4: StockInformationEntry
    roic_max_year_minus_5: StockInformationEntry
    roic_max_year_minus_6: StockInformationEntry
    roic_max_year_minus_7: StockInformationEntry
    roic_max_year_minus_8: StockInformationEntry
    roic_max_year_minus_9: StockInformationEntry
    book_value_max_year: StockInformationEntry
    book_value_max_year_minus_1: StockInformationEntry
    book_value_max_year_minus_2: StockInformationEntry
    book_value_max_year_minus_3: StockInformationEntry
    book_value_max_year_minus_4: StockInformationEntry
    book_value_max_year_minus_5: StockInformationEntry
    book_value_max_year_minus_6: StockInformationEntry
    book_value_max_year_minus_7: StockInformationEntry
    book_value_max_year_minus_8: StockInformationEntry
    book_value_max_year_minus_9: StockInformationEntry
    eps_max_year: StockInformationEntry
    eps_max_year_minus_1: StockInformationEntry
    eps_max_year_minus_2: StockInformationEntry
    eps_max_year_minus_3: StockInformationEntry
    eps_max_year_minus_4: StockInformationEntry
    eps_max_year_minus_5: StockInformationEntry
    eps_max_year_minus_6: StockInformationEntry
    eps_max_year_minus_7: StockInformationEntry
    eps_max_year_minus_8: StockInformationEntry
    eps_max_year_minus_9: StockInformationEntry
    revenue_max_year: StockInformationEntry
    revenue_max_year_minus_1: StockInformationEntry
    revenue_max_year_minus_2: StockInformationEntry
    revenue_max_year_minus_3: StockInformationEntry
    revenue_max_year_minus_4: StockInformationEntry
    revenue_max_year_minus_5: StockInformationEntry
    revenue_max_year_minus_6: StockInformationEntry
    revenue_max_year_minus_7: StockInformationEntry
    revenue_max_year_minus_8: StockInformationEntry
    revenue_max_year_minus_9: StockInformationEntry
    cash_flow_max_year: StockInformationEntry
    cash_flow_max_year_minus_1: StockInformationEntry
    cash_flow_max_year_minus_2: StockInformationEntry
    cash_flow_max_year_minus_3: StockInformationEntry
    cash_flow_max_year_minus_4: StockInformationEntry
    cash_flow_max_year_minus_5: StockInformationEntry
    cash_flow_max_year_minus_6: StockInformationEntry
    cash_flow_max_year_minus_7: StockInformationEntry
    cash_flow_max_year_minus_8: StockInformationEntry
    cash_flow_max_year_minus_9: StockInformationEntry
    growth_estimates: StockInformationEntry
    pe_min: StockInformationEntry
    pe_max: StockInformationEntry

    def to_dict(self):
        result = {}
        for _, stock_information_entry in self.__dict__.items():
            result[stock_information_entry.csv_header] = stock_information_entry.value
        return result


def _extract_row_value(
    soup: BeautifulSoup, row_title: str, minus_years: int, cast_method
) -> Optional[Union[str, float, int]]:
    # Find row to process
    row_to_process = None
    table_rows = soup.select('table[data-test="financials"] > tbody > tr')
    for r in table_rows:
        if row_title.lower() == r.select("td")[0].text.strip().lower():
            row_to_process = r
            break

    # Return value of cell
    cell_to_process = row_to_process.select("td")[1 + minus_years]
    if "Upgrade" in cell_to_process.text or row_title == cell_to_process.text.strip():
        return None
    else:
        return cast_method(cell_to_process.text.strip())


class StockInformationGenerator:

    def __init__(self, source_htmls: SourceHtmls):
        self._ticker: str = source_htmls.ticker
        self._source_soups: SourceSoups = source_htmls_to_source_soups(source_htmls)

    @property
    def company(self) -> str:
        soup = self._source_soups.revenue_soup  # Reads company name from revenue site
        header = soup.select("h1")[0].text
        header_without_ticker = header.split(f"({self._ticker})")[0].strip()
        return header_without_ticker

    @property
    def max_year(self) -> int:
        soup = self._source_soups.revenue_soup  # Reads company name from revenue site
        header_row = soup.select('table[data-test="financials"] > thead > tr')[0]
        max_year = header_row.select("th")[1].text
        if max_year:
            return int(max_year)

    def _extract_roic(self, minus_years: int = 0) -> float:
        soup = self._source_soups.roic_soup
        minus_years = minus_years + 1  # To skip "Current" column
        value = _extract_row_value(
            soup=soup,
            row_title="Return on Capital (ROIC)",
            minus_years=minus_years,
            cast_method=percent_to_float,
        )
        return value

    def _extract_book_value(self, minus_years: int = 0) -> float:
        soup = self._source_soups.book_value_soup
        value = _extract_row_value(
            soup=soup,
            row_title="Book Value per Share",
            minus_years=minus_years,
            cast_method=string_to_float,
        )
        return value

    def _extract_eps(self, minus_years: int = 0) -> float:
        soup = self._source_soups.eps_soup
        value = _extract_row_value(
            soup=soup,
            row_title="EPS (Diluted)",
            minus_years=minus_years,
            cast_method=string_to_float,
        )
        return value

    def _extract_cash_flow(self, minus_years: int = 0) -> float:
        soup = self._source_soups.cash_flow_soup
        value = _extract_row_value(
            soup=soup,
            row_title="Free Cash Flow Per Share",
            minus_years=minus_years,
            cast_method=string_to_float,
        )
        return value

    def _extract_revenue(self, minus_years: int = 0) -> float:
        soup = self._source_soups.revenue_soup
        revenue_in_millions = _extract_row_value(soup, "Revenue", minus_years=minus_years, cast_method=string_to_float)
        if revenue_in_millions:
            return round(revenue_in_millions / 1000.0, 2)
        else:
            return None

    def _extract_growth_estimates(
        self,
        cast_method=string_to_float,
    ) -> Optional[float]:
        soup = self._source_soups.growth_estimates_soup
        table_rows = soup.find("div", id="earnings_growth_estimates").select("table > tbody > tr")
        for r in table_rows:
            if "Growth Estimates - Next 5 Years".endswith(r.select("td")[0].text.strip()):
                text = r.select("td")[1].text.strip()
                return cast_method(text)

    def _extract_pe_ratio_min(self, cast_method=string_to_float) -> Optional[float]:
        soup = self._source_soups.pe_min_soup
        divs = soup.find_all("div", class_="key-stat")
        for div in divs:
            if "Minimum" in div.text:
                minimum = div.find("div", class_="key-stat-title").text.strip()
                return cast_method(minimum)

    def _extract_pe_ratio_max(self, cast_method=string_to_float) -> Optional[float]:
        soup = self._source_soups.pe_max_soup
        divs = soup.find_all("div", class_="key-stat")
        for div in divs:
            if "Maximum" in div.text:
                maximum = div.find("div", class_="key-stat-title").text.strip()
                return cast_method(maximum)

    def get_stock_information(self) -> StockInformation:
        return StockInformation(
            ticker=StockInformationEntry(csv_header=HEADERS.ticker, value=self._ticker),
            company=StockInformationEntry(csv_header=HEADERS.company, value=self.company),
            max_year=StockInformationEntry(csv_header=HEADERS.max_year, value=self.max_year),
            # ROIC
            roic_max_year=StockInformationEntry(csv_header=HEADERS.roic_max_year, value=self._extract_roic()),
            roic_max_year_minus_1=StockInformationEntry(
                csv_header=HEADERS.roic_max_year_minus_1,
                value=self._extract_roic(minus_years=1),
            ),
            roic_max_year_minus_2=StockInformationEntry(
                csv_header=HEADERS.roic_max_year_minus_2,
                value=self._extract_roic(minus_years=2),
            ),
            roic_max_year_minus_3=StockInformationEntry(
                csv_header=HEADERS.roic_max_year_minus_3,
                value=self._extract_roic(minus_years=3),
            ),
            roic_max_year_minus_4=StockInformationEntry(
                csv_header=HEADERS.roic_max_year_minus_4,
                value=self._extract_roic(minus_years=4),
            ),
            roic_max_year_minus_5=StockInformationEntry(
                csv_header=HEADERS.roic_max_year_minus_5,
                value=self._extract_roic(minus_years=5),
            ),
            roic_max_year_minus_6=StockInformationEntry(
                csv_header=HEADERS.roic_max_year_minus_6,
                value=self._extract_roic(minus_years=6),
            ),
            roic_max_year_minus_7=StockInformationEntry(
                csv_header=HEADERS.roic_max_year_minus_7,
                value=self._extract_roic(minus_years=7),
            ),
            roic_max_year_minus_8=StockInformationEntry(
                csv_header=HEADERS.roic_max_year_minus_8,
                value=self._extract_roic(minus_years=8),
            ),
            roic_max_year_minus_9=StockInformationEntry(
                csv_header=HEADERS.roic_max_year_minus_9,
                value=self._extract_roic(minus_years=9),
            ),
            # Book Value per Share
            book_value_max_year=StockInformationEntry(
                csv_header=HEADERS.book_value_max_year, value=self._extract_book_value()
            ),
            book_value_max_year_minus_1=StockInformationEntry(
                csv_header=HEADERS.book_value_max_year_minus_1,
                value=self._extract_book_value(minus_years=1),
            ),
            book_value_max_year_minus_2=StockInformationEntry(
                csv_header=HEADERS.book_value_max_year_minus_2,
                value=self._extract_book_value(minus_years=2),
            ),
            book_value_max_year_minus_3=StockInformationEntry(
                csv_header=HEADERS.book_value_max_year_minus_3,
                value=self._extract_book_value(minus_years=3),
            ),
            book_value_max_year_minus_4=StockInformationEntry(
                csv_header=HEADERS.book_value_max_year_minus_4,
                value=self._extract_book_value(minus_years=4),
            ),
            book_value_max_year_minus_5=StockInformationEntry(
                csv_header=HEADERS.book_value_max_year_minus_5,
                value=self._extract_book_value(minus_years=5),
            ),
            book_value_max_year_minus_6=StockInformationEntry(
                csv_header=HEADERS.book_value_max_year_minus_6,
                value=self._extract_book_value(minus_years=6),
            ),
            book_value_max_year_minus_7=StockInformationEntry(
                csv_header=HEADERS.book_value_max_year_minus_7,
                value=self._extract_book_value(minus_years=7),
            ),
            book_value_max_year_minus_8=StockInformationEntry(
                csv_header=HEADERS.book_value_max_year_minus_8,
                value=self._extract_book_value(minus_years=8),
            ),
            book_value_max_year_minus_9=StockInformationEntry(
                csv_header=HEADERS.book_value_max_year_minus_9,
                value=self._extract_book_value(minus_years=9),
            ),
            eps_max_year=StockInformationEntry(csv_header=HEADERS.eps_max_year, value=self._extract_eps()),
            eps_max_year_minus_1=StockInformationEntry(
                csv_header=HEADERS.eps_max_year_minus_1,
                value=self._extract_eps(minus_years=1),
            ),
            eps_max_year_minus_2=StockInformationEntry(
                csv_header=HEADERS.eps_max_year_minus_2,
                value=self._extract_eps(minus_years=2),
            ),
            eps_max_year_minus_3=StockInformationEntry(
                csv_header=HEADERS.eps_max_year_minus_3,
                value=self._extract_eps(minus_years=3),
            ),
            eps_max_year_minus_4=StockInformationEntry(
                csv_header=HEADERS.eps_max_year_minus_4,
                value=self._extract_eps(minus_years=4),
            ),
            eps_max_year_minus_5=StockInformationEntry(
                csv_header=HEADERS.eps_max_year_minus_5,
                value=self._extract_eps(minus_years=5),
            ),
            eps_max_year_minus_6=StockInformationEntry(
                csv_header=HEADERS.eps_max_year_minus_6,
                value=self._extract_eps(minus_years=6),
            ),
            eps_max_year_minus_7=StockInformationEntry(
                csv_header=HEADERS.eps_max_year_minus_7,
                value=self._extract_eps(minus_years=7),
            ),
            eps_max_year_minus_8=StockInformationEntry(
                csv_header=HEADERS.eps_max_year_minus_8,
                value=self._extract_eps(minus_years=8),
            ),
            eps_max_year_minus_9=StockInformationEntry(
                csv_header=HEADERS.eps_max_year_minus_9,
                value=self._extract_eps(minus_years=9),
            ),
            revenue_max_year=StockInformationEntry(csv_header=HEADERS.revenue_max_year, value=self._extract_revenue()),
            revenue_max_year_minus_1=StockInformationEntry(
                csv_header=HEADERS.revenue_max_year_minus_1,
                value=self._extract_revenue(minus_years=1),
            ),
            revenue_max_year_minus_2=StockInformationEntry(
                csv_header=HEADERS.revenue_max_year_minus_2,
                value=self._extract_revenue(minus_years=2),
            ),
            revenue_max_year_minus_3=StockInformationEntry(
                csv_header=HEADERS.revenue_max_year_minus_3,
                value=self._extract_revenue(minus_years=3),
            ),
            revenue_max_year_minus_4=StockInformationEntry(
                csv_header=HEADERS.revenue_max_year_minus_4,
                value=self._extract_revenue(minus_years=4),
            ),
            revenue_max_year_minus_5=StockInformationEntry(
                csv_header=HEADERS.revenue_max_year_minus_5,
                value=self._extract_revenue(minus_years=5),
            ),
            revenue_max_year_minus_6=StockInformationEntry(
                csv_header=HEADERS.revenue_max_year_minus_6,
                value=self._extract_revenue(minus_years=6),
            ),
            revenue_max_year_minus_7=StockInformationEntry(
                csv_header=HEADERS.revenue_max_year_minus_7,
                value=self._extract_revenue(minus_years=7),
            ),
            revenue_max_year_minus_8=StockInformationEntry(
                csv_header=HEADERS.revenue_max_year_minus_8,
                value=self._extract_revenue(minus_years=8),
            ),
            revenue_max_year_minus_9=StockInformationEntry(
                csv_header=HEADERS.revenue_max_year_minus_9,
                value=self._extract_revenue(minus_years=9),
            ),
            cash_flow_max_year=StockInformationEntry(
                csv_header=HEADERS.free_cash_flow_max_year,
                value=self._extract_cash_flow(),
            ),
            cash_flow_max_year_minus_1=StockInformationEntry(
                csv_header=HEADERS.free_cash_flow_max_year_minus_1,
                value=self._extract_cash_flow(minus_years=1),
            ),
            cash_flow_max_year_minus_2=StockInformationEntry(
                csv_header=HEADERS.free_cash_flow_max_year_minus_2,
                value=self._extract_cash_flow(minus_years=2),
            ),
            cash_flow_max_year_minus_3=StockInformationEntry(
                csv_header=HEADERS.free_cash_flow_max_year_minus_3,
                value=self._extract_cash_flow(minus_years=3),
            ),
            cash_flow_max_year_minus_4=StockInformationEntry(
                csv_header=HEADERS.free_cash_flow_max_year_minus_4,
                value=self._extract_cash_flow(minus_years=4),
            ),
            cash_flow_max_year_minus_5=StockInformationEntry(
                csv_header=HEADERS.free_cash_flow_max_year_minus_5,
                value=self._extract_cash_flow(minus_years=5),
            ),
            cash_flow_max_year_minus_6=StockInformationEntry(
                csv_header=HEADERS.free_cash_flow_max_year_minus_6,
                value=self._extract_cash_flow(minus_years=6),
            ),
            cash_flow_max_year_minus_7=StockInformationEntry(
                csv_header=HEADERS.free_cash_flow_max_year_minus_7,
                value=self._extract_cash_flow(minus_years=7),
            ),
            cash_flow_max_year_minus_8=StockInformationEntry(
                csv_header=HEADERS.free_cash_flow_max_year_minus_8,
                value=self._extract_cash_flow(minus_years=8),
            ),
            cash_flow_max_year_minus_9=StockInformationEntry(
                csv_header=HEADERS.free_cash_flow_max_year_minus_9,
                value=self._extract_cash_flow(minus_years=9),
            ),
            growth_estimates=StockInformationEntry(
                csv_header=HEADERS.growth_estimates,
                value=self._extract_growth_estimates(),
            ),
            pe_min=StockInformationEntry(csv_header=HEADERS.pe_ratio_min, value=self._extract_pe_ratio_min()),
            pe_max=StockInformationEntry(csv_header=HEADERS.pe_ratio_max, value=self._extract_pe_ratio_max()),
        )
