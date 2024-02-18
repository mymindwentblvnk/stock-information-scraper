import time
from dataclasses import dataclass

import requests


@dataclass
class SourceHtmls:
    ticker: str
    roic_html: str
    book_value_html: str
    eps_html: str
    revenue_html: str
    cash_flow_html: str
    growth_estimates_html: str
    pe_min_html: str
    pe_max_html: str


def _fetch_html(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    while response.status_code != 200:
        print("Still loading...")
        time.sleep(10)
        response = requests.get(url, headers=headers)
    return response.text


class HtmlFetcher:

    def __init__(self, ticker: str):
        self.ticker = ticker

    def get_source_htmls(self) -> SourceHtmls:
        stock_analysis_base_url = "https://stockanalysis.com/stocks"
        zack_base_url = "https://www.zacks.com/stock/quote"
        ycharts_base_url = "https://ycharts.com/companies"
        ticker = self.ticker

        roic_url = f"{stock_analysis_base_url}/{ticker}/financials/ratios/"
        roic_html = _fetch_html(url=roic_url)
        print(f"Loaded Return on ROIC from {roic_url}")

        book_value_url = f"{stock_analysis_base_url}/{ticker}/financials/balance-sheet/"
        book_value_html = _fetch_html(url=book_value_url)
        print(f"Loaded Book Value per Share from {book_value_url}")

        eps_url = f"{stock_analysis_base_url}/{ticker}/financials/"
        eps_html = _fetch_html(url=eps_url)
        print(f"Loaded EPS Diluted from {eps_url}")

        revenue_url = f"{stock_analysis_base_url}/{ticker}/financials/"
        revenue_html = _fetch_html(url=revenue_url)
        print(f"Loaded Revenue from {revenue_url}")

        cash_flow_url = f"{stock_analysis_base_url}/{ticker}/financials/cash-flow-statement/"
        cash_flow_html = _fetch_html(url=cash_flow_url)
        print(f"Loaded Free Cash Flow per Share from {cash_flow_url}")

        growth_estimates_url = f"{zack_base_url}/{ticker}/detailed-earning-estimates"
        growth_estimates_html = _fetch_html(url=growth_estimates_url)
        print(f"Loaded Growth Estimates from {growth_estimates_url}")

        pe_min_url = f"{ycharts_base_url}/{ticker}/pe_ratio"
        pe_min_html = _fetch_html(url=pe_min_url)
        print(f"Loaded PE Ratio MIN from {pe_min_url}")

        pe_max_url = f"{ycharts_base_url}/{ticker}/pe_ratio"
        pe_max_html = _fetch_html(url=pe_max_url)
        print(f"Loaded PE Ratio MAX from {pe_max_url}")

        return SourceHtmls(
            ticker=ticker,
            roic_html=roic_html,
            book_value_html=book_value_html,
            eps_html=eps_html,
            revenue_html=revenue_html,
            cash_flow_html=cash_flow_html,
            growth_estimates_html=growth_estimates_html,
            pe_min_html=pe_min_html,
            pe_max_html=pe_max_html,
        )
