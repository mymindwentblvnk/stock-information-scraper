import time
from dataclasses import dataclass

import requests


@dataclass
class SourceHtmls:
    ticker: str
    return_on_capital_roic_html: str
    book_value_per_share_html: str
    eps_diluted_html: str
    revenue_html: str
    free_cash_flow_per_share_html: str
    growth_estimates_next_5_years_html: str
    pe_ratio_min_html: str
    pe_ratio_max_html: str


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

        return_on_capital_roic_url = (
            f"{stock_analysis_base_url}/{ticker}/financials/ratios/"
        )
        return_on_capital_roic_html = _fetch_html(url=return_on_capital_roic_url)
        print(f"Loaded Return on ROIC from {return_on_capital_roic_url}")

        book_value_per_share_url = (
            f"{stock_analysis_base_url}/{ticker}/financials/balance-sheet/"
        )
        book_value_per_share_html = _fetch_html(url=book_value_per_share_url)
        print(f"Loaded Book Value per Share from {book_value_per_share_url}")

        eps_diluted_url = f"{stock_analysis_base_url}/{ticker}/financials/"
        eps_diluted_html = _fetch_html(url=eps_diluted_url)
        print(f"Loaded EPS Diluted from {eps_diluted_url}")

        revenue_url = f"{stock_analysis_base_url}/{ticker}/financials/"
        revenue_html = _fetch_html(url=revenue_url)
        print(f"Loaded Revenue from {revenue_url}")

        free_cash_flow_per_share_url = (
            f"{stock_analysis_base_url}/{ticker}/financials/cash-flow-statement/"
        )
        free_cash_flow_per_share_html = _fetch_html(url=free_cash_flow_per_share_url)
        print(f"Loaded Free Cash Flow per Share from {free_cash_flow_per_share_url}")

        growth_estimates_next_5_years_url = (
            f"{zack_base_url}/{ticker}/detailed-earning-estimates"
        )
        growth_estimates_next_5_years_html = _fetch_html(
            url=growth_estimates_next_5_years_url
        )
        print(f"Loaded Growth Estimates from {growth_estimates_next_5_years_url}")

        pe_ratio_min_url = f"{ycharts_base_url}/{ticker}/pe_ratio"
        pe_ratio_min_html = _fetch_html(url=pe_ratio_min_url)
        print(f"Loaded PE Ratio MIN from {pe_ratio_min_url}")

        pe_ratio_max_url = f"{ycharts_base_url}/{ticker}/pe_ratio"
        pe_ratio_max_html = _fetch_html(url=pe_ratio_max_url)
        print(f"Loaded PE Ratio MAX from {pe_ratio_max_url}")

        return SourceHtmls(
            ticker=ticker,
            return_on_capital_roic_html=return_on_capital_roic_html,
            book_value_per_share_html=book_value_per_share_html,
            eps_diluted_html=eps_diluted_html,
            revenue_html=revenue_html,
            free_cash_flow_per_share_html=free_cash_flow_per_share_html,
            growth_estimates_next_5_years_html=growth_estimates_next_5_years_html,
            pe_ratio_min_html=pe_ratio_min_html,
            pe_ratio_max_html=pe_ratio_max_html,
        )
