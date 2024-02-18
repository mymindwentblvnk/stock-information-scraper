from stock_information_scraper.stock_information import StockInformationGenerator


def test_META():
    # Given
    source_htmls = None
    generator = StockInformationGenerator(source_htmls=source_htmls)

    # When
    stock_information = generator.get_stock_information()


def test_LLY():
    # Given
    source_htmls = None
    generator = StockInformationGenerator(source_htmls=source_htmls)

    # When
    stock_information = generator.get_stock_information()

    # Then
    # Assert on stock information values
