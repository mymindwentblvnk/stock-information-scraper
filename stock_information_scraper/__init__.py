class CsvHeader:
    ticker = "Ticker"
    company = "Company"
    max_year = "Max Year"
    roic_max_year = "Return on Capital ROIC (Max Year)"
    roic_max_year_minus_1 = "Return on Capital ROIC (Max Year - 1)"
    roic_max_year_minus_2 = "Return on Capital ROIC (Max Year - 2)"
    roic_max_year_minus_3 = "Return on Capital ROIC (Max Year - 3)"
    roic_max_year_minus_4 = "Return on Capital ROIC (Max Year - 4)"
    roic_max_year_minus_5 = "Return on Capital ROIC (Max Year - 5)"
    roic_max_year_minus_6 = "Return on Capital ROIC (Max Year - 6)"
    roic_max_year_minus_7 = "Return on Capital ROIC (Max Year - 7)"
    roic_max_year_minus_8 = "Return on Capital ROIC (Max Year - 8)"
    roic_max_year_minus_9 = "Return on Capital ROIC (Max Year - 9)"
    book_value_max_year = "Book Value per Share (Max Year)"
    book_value_max_year_minus_1 = "Book Value per Share (Max Year - 1)"
    book_value_max_year_minus_2 = "Book Value per Share (Max Year - 2)"
    book_value_max_year_minus_3 = "Book Value per Share (Max Year - 3)"
    book_value_max_year_minus_4 = "Book Value per Share (Max Year - 4)"
    book_value_max_year_minus_5 = "Book Value per Share (Max Year - 5)"
    book_value_max_year_minus_6 = "Book Value per Share (Max Year - 6)"
    book_value_max_year_minus_7 = "Book Value per Share (Max Year - 7)"
    book_value_max_year_minus_8 = "Book Value per Share (Max Year - 8)"
    book_value_max_year_minus_9 = "Book Value per Share (Max Year - 9)"
    eps_max_year = "EPS Diluted (Max Year)"
    eps_max_year_minus_1 = "EPS Diluted (Max Year - 1)"
    eps_max_year_minus_2 = "EPS Diluted (Max Year - 2)"
    eps_max_year_minus_3 = "EPS Diluted (Max Year - 3)"
    eps_max_year_minus_4 = "EPS Diluted (Max Year - 4)"
    eps_max_year_minus_5 = "EPS Diluted (Max Year - 5)"
    eps_max_year_minus_6 = "EPS Diluted (Max Year - 6)"
    eps_max_year_minus_7 = "EPS Diluted (Max Year - 7)"
    eps_max_year_minus_8 = "EPS Diluted (Max Year - 8)"
    eps_max_year_minus_9 = "EPS Diluted (Max Year - 9)"
    revenue_max_year = "Revenue (Max Year)"
    revenue_max_year_minus_1 = "Revenue (Max Year - 1)"
    revenue_max_year_minus_2 = "Revenue (Max Year - 2)"
    revenue_max_year_minus_3 = "Revenue (Max Year - 3)"
    revenue_max_year_minus_4 = "Revenue (Max Year - 4)"
    revenue_max_year_minus_5 = "Revenue (Max Year - 5)"
    revenue_max_year_minus_6 = "Revenue (Max Year - 6)"
    revenue_max_year_minus_7 = "Revenue (Max Year - 7)"
    revenue_max_year_minus_8 = "Revenue (Max Year - 8)"
    revenue_max_year_minus_9 = "Revenue (Max Year - 9)"
    free_cash_flow_max_year = "Free Cash Flow (Max Year)"
    free_cash_flow_max_year_minus_1 = "Free Cash Flow (Max Year - 1)"
    free_cash_flow_max_year_minus_2 = "Free Cash Flow (Max Year - 2)"
    free_cash_flow_max_year_minus_3 = "Free Cash Flow (Max Year - 3)"
    free_cash_flow_max_year_minus_4 = "Free Cash Flow (Max Year - 4)"
    free_cash_flow_max_year_minus_5 = "Free Cash Flow (Max Year - 5)"
    free_cash_flow_max_year_minus_6 = "Free Cash Flow (Max Year - 6)"
    free_cash_flow_max_year_minus_7 = "Free Cash Flow (Max Year - 7)"
    free_cash_flow_max_year_minus_8 = "Free Cash Flow (Max Year - 8)"
    free_cash_flow_max_year_minus_9 = "Free Cash Flow (Max Year - 9)"
    growth_estimates = "Growth Estimates Next 5 Years"
    pe_ratio_min = "PE Ratio (Min)"
    pe_ratio_max = "PE Ratio (Max)"

    def to_list(self):
        return [
            self.ticker,
            self.company,
            self.max_year,
            self.roic_max_year,
            self.roic_max_year_minus_1,
            self.roic_max_year_minus_2,
            self.roic_max_year_minus_3,
            self.roic_max_year_minus_4,
            self.roic_max_year_minus_5,
            self.roic_max_year_minus_6,
            self.roic_max_year_minus_7,
            self.roic_max_year_minus_8,
            self.roic_max_year_minus_9,
            self.book_value_max_year,
            self.book_value_max_year_minus_1,
            self.book_value_max_year_minus_2,
            self.book_value_max_year_minus_3,
            self.book_value_max_year_minus_4,
            self.book_value_max_year_minus_5,
            self.book_value_max_year_minus_6,
            self.book_value_max_year_minus_7,
            self.book_value_max_year_minus_8,
            self.book_value_max_year_minus_9,
            self.eps_max_year,
            self.eps_max_year_minus_1,
            self.eps_max_year_minus_2,
            self.eps_max_year_minus_3,
            self.eps_max_year_minus_4,
            self.eps_max_year_minus_5,
            self.eps_max_year_minus_6,
            self.eps_max_year_minus_7,
            self.eps_max_year_minus_8,
            self.eps_max_year_minus_9,
            self.revenue_max_year,
            self.revenue_max_year_minus_1,
            self.revenue_max_year_minus_2,
            self.revenue_max_year_minus_3,
            self.revenue_max_year_minus_4,
            self.revenue_max_year_minus_5,
            self.revenue_max_year_minus_6,
            self.revenue_max_year_minus_7,
            self.revenue_max_year_minus_8,
            self.revenue_max_year_minus_9,
            self.free_cash_flow_max_year,
            self.free_cash_flow_max_year_minus_1,
            self.free_cash_flow_max_year_minus_2,
            self.free_cash_flow_max_year_minus_3,
            self.free_cash_flow_max_year_minus_4,
            self.free_cash_flow_max_year_minus_5,
            self.free_cash_flow_max_year_minus_6,
            self.free_cash_flow_max_year_minus_7,
            self.free_cash_flow_max_year_minus_8,
            self.free_cash_flow_max_year_minus_9,
            self.growth_estimates,
            self.pe_ratio_min,
            self.pe_ratio_max,
        ]
