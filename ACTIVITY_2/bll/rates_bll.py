from dal.rates_dal import RatesJsonDao
from utils.util import format_value

class RatesBll:
    
    def __init__(self):
        self.__rates__dao =  RatesJsonDao()
    
    def retrieve_rates(self):
        return self.__rates__dao.retrieve_rates()
    
    def convert_currency(self, source_currency, target_currency, amount):
         rates_data = self.__rates__dao.search_rates(source_currency, target_currency)
         return format_value((amount * rates_data["source_rate"]) / rates_data["target_rate"])
    
    def retrieve_currencies(self):
        return self.__rates__dao.retrieve_currencies()
    