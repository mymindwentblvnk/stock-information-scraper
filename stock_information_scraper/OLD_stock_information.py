# from typing import List
#
#
# class DataProvider:
#
#     def __init__(self, ticker: str):
#         self.ticker = ticker
#         print(f"Getting stock information for {self.ticker}")
#         self._soup = _build_soup(ticker=self.ticker)
#
#     def get_specific_value(self, data_type: DataType, year: int = None) -> float:
#         if data_type == DataType.GROWTH_ESTIMATES_NEXT_5_YEARS:
#             return _extract_growth_estimates(
#                 soup=self._soup[data_type],
#                 row_title=data_type.value["title"],
#                 cast_method=data_type.value["cast_method"],
#             )
#         elif data_type == DataType.PE_RATIO_MIN:
#             return _extract_pe_ratio_min(
#                 soup=self._soup[data_type], cast_method=data_type.value["cast_method"]
#             )
#         elif data_type == DataType.PE_RATIO_MAX:
#             return _extract_pe_ratio_max(
#                 soup=self._soup[data_type], cast_method=data_type.value["cast_method"]
#             )
#         elif data_type == DataType.REVENUE:
#             return _extract_revenue(
#                 soup=self._soup[data_type],
#                 row_title=data_type.value["title"],
#                 year=year,
#                 cast_method=data_type.value["cast_method"],
#             )
#         else:
#             assert year
#             return _extract_row_value(
#                 soup=self._soup[data_type],
#                 row_title=data_type.value["title"],
#                 year=year,
#                 cast_method=data_type.value["cast_method"],
#             )
#
#     def get_stock_information(self, years: List[int]) -> StockInformation:
#         result = StockInformation()
#         result.ticker = self.ticker
#         result.company = self.company
#         result.return_on_capital = {
#             year: self.get_specific_value(DataType.RETURN_ON_CAPITAL_ROIC, year)
#             for year in years
#         }
#         result.book_value_per_share = {
#             year: self.get_specific_value(DataType.BOOK_VALUE_PER_SHARE, year)
#             for year in years
#         }
#         result.eps_diluted = {
#             year: self.get_specific_value(DataType.EPS_DILUTED, year) for year in years
#         }
#         result.revenue = {
#             year: self.get_specific_value(DataType.REVENUE, year) for year in years
#         }
#         result.free_cash_flow_per_share = {
#             year: self.get_specific_value(DataType.FREE_CASH_FLOW_PER_SHARE, year)
#             for year in years
#         }
#         result.growth_estimates_next_5_years = self.get_specific_value(
#             DataType.GROWTH_ESTIMATES_NEXT_5_YEARS
#         )
#         result.pe_ratio_max = self.get_specific_value(DataType.PE_RATIO_MAX)
#         result.pe_ratio_min = self.get_specific_value(DataType.PE_RATIO_MIN)
#         return result
