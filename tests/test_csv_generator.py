import csv
import os
import tempfile
from typing import List, Dict

import pytest
from hamcrest import assert_that, equal_to

from stock_information_scraper.csv_generator import CsvGenerator
from stock_information_scraper.stock_information import (
    StockInformation,
    StockInformationEntry,
)


@pytest.fixture
def stock_information_list() -> List[StockInformation]:
    return [
        StockInformation(
            ticker=StockInformationEntry(csv_header="Col 1", value="ticker_1"),
            company=StockInformationEntry(csv_header="Col 2", value="My Fake Company 1"),
            max_year=StockInformationEntry(csv_header="Col 3", value=1986),
            roic_max_year=StockInformationEntry(csv_header="Col 4", value=1.4),
            roic_max_year_minus_1=StockInformationEntry(csv_header="Col 5", value=1.5),
            roic_max_year_minus_2=StockInformationEntry(csv_header="Col 6", value=1.6),
            roic_max_year_minus_3=StockInformationEntry(csv_header="Col 7", value=1.7),
            roic_max_year_minus_4=StockInformationEntry(csv_header="Col 8", value=1.8),
            roic_max_year_minus_5=StockInformationEntry(csv_header="Col 9", value=1.9),
            roic_max_year_minus_6=StockInformationEntry(csv_header="Col 10", value=1.10),
            roic_max_year_minus_7=StockInformationEntry(csv_header="Col 11", value=1.11),
            roic_max_year_minus_8=StockInformationEntry(csv_header="Col 12", value=1.12),
            roic_max_year_minus_9=StockInformationEntry(csv_header="Col 13", value=1.13),
            book_value_max_year=StockInformationEntry(csv_header="Col 14", value=1.14),
            book_value_max_year_minus_1=StockInformationEntry(csv_header="Col 15", value=1.15),
            book_value_max_year_minus_2=StockInformationEntry(csv_header="Col 16", value=1.16),
            book_value_max_year_minus_3=StockInformationEntry(csv_header="Col 17", value=1.17),
            book_value_max_year_minus_4=StockInformationEntry(csv_header="Col 18", value=1.18),
            book_value_max_year_minus_5=StockInformationEntry(csv_header="Col 19", value=1.19),
            book_value_max_year_minus_6=StockInformationEntry(csv_header="Col 20", value=1.20),
            book_value_max_year_minus_7=StockInformationEntry(csv_header="Col 21", value=1.21),
            book_value_max_year_minus_8=StockInformationEntry(csv_header="Col 22", value=1.22),
            book_value_max_year_minus_9=StockInformationEntry(csv_header="Col 23", value=1.23),
            eps_max_year=StockInformationEntry(csv_header="Col 24", value=1.24),
            eps_max_year_minus_1=StockInformationEntry(csv_header="Col 25", value=1.25),
            eps_max_year_minus_2=StockInformationEntry(csv_header="Col 26", value=1.26),
            eps_max_year_minus_3=StockInformationEntry(csv_header="Col 27", value=1.27),
            eps_max_year_minus_4=StockInformationEntry(csv_header="Col 28", value=1.28),
            eps_max_year_minus_5=StockInformationEntry(csv_header="Col 29", value=1.29),
            eps_max_year_minus_6=StockInformationEntry(csv_header="Col 30", value=1.30),
            eps_max_year_minus_7=StockInformationEntry(csv_header="Col 31", value=1.31),
            eps_max_year_minus_8=StockInformationEntry(csv_header="Col 32", value=1.32),
            eps_max_year_minus_9=StockInformationEntry(csv_header="Col 33", value=1.33),
            revenue_max_year=StockInformationEntry(csv_header="Col 34", value=1.34),
            revenue_max_year_minus_1=StockInformationEntry(csv_header="Col 35", value=1.35),
            revenue_max_year_minus_2=StockInformationEntry(csv_header="Col 36", value=1.36),
            revenue_max_year_minus_3=StockInformationEntry(csv_header="Col 37", value=1.37),
            revenue_max_year_minus_4=StockInformationEntry(csv_header="Col 38", value=1.38),
            revenue_max_year_minus_5=StockInformationEntry(csv_header="Col 39", value=1.39),
            revenue_max_year_minus_6=StockInformationEntry(csv_header="Col 40", value=1.40),
            revenue_max_year_minus_7=StockInformationEntry(csv_header="Col 41", value=1.41),
            revenue_max_year_minus_8=StockInformationEntry(csv_header="Col 42", value=1.42),
            revenue_max_year_minus_9=StockInformationEntry(csv_header="Col 43", value=1.43),
            cash_flow_max_year=StockInformationEntry(csv_header="Col 44", value=1.44),
            cash_flow_max_year_minus_1=StockInformationEntry(csv_header="Col 45", value=1.45),
            cash_flow_max_year_minus_2=StockInformationEntry(csv_header="Col 46", value=1.46),
            cash_flow_max_year_minus_3=StockInformationEntry(csv_header="Col 47", value=1.47),
            cash_flow_max_year_minus_4=StockInformationEntry(csv_header="Col 48", value=1.48),
            cash_flow_max_year_minus_5=StockInformationEntry(csv_header="Col 49", value=1.49),
            cash_flow_max_year_minus_6=StockInformationEntry(csv_header="Col 50", value=1.50),
            cash_flow_max_year_minus_7=StockInformationEntry(csv_header="Col 51", value=1.51),
            cash_flow_max_year_minus_8=StockInformationEntry(csv_header="Col 52", value=1.52),
            cash_flow_max_year_minus_9=StockInformationEntry(csv_header="Col 53", value=1.53),
            growth_estimates=StockInformationEntry(csv_header="Col 54", value=1.54),
            pe_min=StockInformationEntry(csv_header="Col 55", value=1.55),
            pe_max=StockInformationEntry(csv_header="Col 56", value=1.56),
        ),
        StockInformation(
            ticker=StockInformationEntry(csv_header="Col 1", value="ticker_2"),
            company=StockInformationEntry(csv_header="Col 2", value="My Fake Company 2"),
            max_year=StockInformationEntry(csv_header="Col 3", value=1986),
            roic_max_year=StockInformationEntry(csv_header="Col 4", value=2.4),
            roic_max_year_minus_1=StockInformationEntry(csv_header="Col 5", value=2.5),
            roic_max_year_minus_2=StockInformationEntry(csv_header="Col 6", value=2.6),
            roic_max_year_minus_3=StockInformationEntry(csv_header="Col 7", value=2.7),
            roic_max_year_minus_4=StockInformationEntry(csv_header="Col 8", value=2.8),
            roic_max_year_minus_5=StockInformationEntry(csv_header="Col 9", value=2.9),
            roic_max_year_minus_6=StockInformationEntry(csv_header="Col 10", value=2.10),
            roic_max_year_minus_7=StockInformationEntry(csv_header="Col 11", value=2.11),
            roic_max_year_minus_8=StockInformationEntry(csv_header="Col 12", value=2.12),
            roic_max_year_minus_9=StockInformationEntry(csv_header="Col 13", value=2.13),
            book_value_max_year=StockInformationEntry(csv_header="Col 14", value=2.14),
            book_value_max_year_minus_1=StockInformationEntry(csv_header="Col 15", value=2.15),
            book_value_max_year_minus_2=StockInformationEntry(csv_header="Col 16", value=2.16),
            book_value_max_year_minus_3=StockInformationEntry(csv_header="Col 17", value=2.17),
            book_value_max_year_minus_4=StockInformationEntry(csv_header="Col 18", value=2.18),
            book_value_max_year_minus_5=StockInformationEntry(csv_header="Col 19", value=2.19),
            book_value_max_year_minus_6=StockInformationEntry(csv_header="Col 20", value=2.20),
            book_value_max_year_minus_7=StockInformationEntry(csv_header="Col 21", value=2.21),
            book_value_max_year_minus_8=StockInformationEntry(csv_header="Col 22", value=2.22),
            book_value_max_year_minus_9=StockInformationEntry(csv_header="Col 23", value=2.23),
            eps_max_year=StockInformationEntry(csv_header="Col 24", value=2.24),
            eps_max_year_minus_1=StockInformationEntry(csv_header="Col 25", value=2.25),
            eps_max_year_minus_2=StockInformationEntry(csv_header="Col 26", value=2.26),
            eps_max_year_minus_3=StockInformationEntry(csv_header="Col 27", value=2.27),
            eps_max_year_minus_4=StockInformationEntry(csv_header="Col 28", value=2.28),
            eps_max_year_minus_5=StockInformationEntry(csv_header="Col 29", value=2.29),
            eps_max_year_minus_6=StockInformationEntry(csv_header="Col 30", value=2.30),
            eps_max_year_minus_7=StockInformationEntry(csv_header="Col 31", value=2.31),
            eps_max_year_minus_8=StockInformationEntry(csv_header="Col 32", value=2.32),
            eps_max_year_minus_9=StockInformationEntry(csv_header="Col 33", value=2.33),
            revenue_max_year=StockInformationEntry(csv_header="Col 34", value=2.34),
            revenue_max_year_minus_1=StockInformationEntry(csv_header="Col 35", value=2.35),
            revenue_max_year_minus_2=StockInformationEntry(csv_header="Col 36", value=2.36),
            revenue_max_year_minus_3=StockInformationEntry(csv_header="Col 37", value=2.37),
            revenue_max_year_minus_4=StockInformationEntry(csv_header="Col 38", value=2.38),
            revenue_max_year_minus_5=StockInformationEntry(csv_header="Col 39", value=2.39),
            revenue_max_year_minus_6=StockInformationEntry(csv_header="Col 40", value=2.40),
            revenue_max_year_minus_7=StockInformationEntry(csv_header="Col 41", value=2.41),
            revenue_max_year_minus_8=StockInformationEntry(csv_header="Col 42", value=2.42),
            revenue_max_year_minus_9=StockInformationEntry(csv_header="Col 43", value=2.43),
            cash_flow_max_year=StockInformationEntry(csv_header="Col 44", value=2.44),
            cash_flow_max_year_minus_1=StockInformationEntry(csv_header="Col 45", value=2.45),
            cash_flow_max_year_minus_2=StockInformationEntry(csv_header="Col 46", value=2.46),
            cash_flow_max_year_minus_3=StockInformationEntry(csv_header="Col 47", value=2.47),
            cash_flow_max_year_minus_4=StockInformationEntry(csv_header="Col 48", value=2.48),
            cash_flow_max_year_minus_5=StockInformationEntry(csv_header="Col 49", value=2.49),
            cash_flow_max_year_minus_6=StockInformationEntry(csv_header="Col 50", value=2.50),
            cash_flow_max_year_minus_7=StockInformationEntry(csv_header="Col 51", value=2.51),
            cash_flow_max_year_minus_8=StockInformationEntry(csv_header="Col 52", value=2.52),
            cash_flow_max_year_minus_9=StockInformationEntry(csv_header="Col 53", value=2.53),
            growth_estimates=StockInformationEntry(csv_header="Col 54", value=2.54),
            pe_min=StockInformationEntry(csv_header="Col 55", value=2.55),
            pe_max=StockInformationEntry(csv_header="Col 56", value=2.56),
        ),
    ]


@pytest.fixture
def csv_headers():
    return [f"Col {i}" for i in range(1, 57)]


@pytest.fixture
def temp_file():
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    yield temp_file.name
    temp_file.close()
    os.unlink(temp_file.name)


def read_csv_as_dict(file_name: str) -> List[Dict]:
    list_of_dicts = []
    with open(file_name, "r") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            list_of_dicts.append(dict(row))
    return list_of_dicts


def test_csv_generator_works(csv_headers: List[str], stock_information_list: List[StockInformation], temp_file):
    # Given
    csv_generator = CsvGenerator(stock_information_list=stock_information_list)

    # When
    csv_generator.save_csv(file_name=temp_file, csv_headers=csv_headers)

    # Then
    dicts = read_csv_as_dict(temp_file)
    dict_1 = dicts[0]
    dict_2 = dicts[1]
    assert_that(dict_1["Col 1"], equal_to("ticker_1"))
    assert_that(dict_1["Col 45"], equal_to("1.45"))
    assert_that(dict_2["Col 55"], equal_to("2.55"))
    assert_that(len(dict_1), equal_to(len(dict_2)))
