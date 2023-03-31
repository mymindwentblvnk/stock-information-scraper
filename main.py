import string

from nicegui import ui

from scraper import get_numbers_for_ticker, save_numbers_to_csv

ALLOWED_TICKER_CHARACTERS = set(string.ascii_uppercase + ',')
ALLOWED_FILE_NAME_CHARACTERS = set(string.digits + string.ascii_letters + '-_.')


def generate_csv(ticker_str: str, file_name: str):
    all_tickers = ticker_str.split(',')
    all_numbers = [get_numbers_for_ticker(t) for t in all_tickers]
    save_numbers_to_csv(all_numbers, file_name)


ui.markdown("# 📈 Stock Information Scraper")
ui.markdown("Please add the tickers you want to retrieve data for into the input field.")
tickers = ui.input('Tickers', validation={"Only uppercase letters and commas are allowed.": lambda x: set(x) <= ALLOWED_TICKER_CHARACTERS})
file_name = ui.input("Output Filename", value='stock-information.csv', validation={"This is not a valid file name. Please only use letters, numbers, hyphens, underscores and dots": lambda x: set(x) <= ALLOWED_FILE_NAME_CHARACTERS and x.endswith('.csv')})
ui.button('Generate CSV', on_click=lambda: generate_csv(tickers.value, file_name.value))

ui.run(reload=False)
