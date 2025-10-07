from utils.util import read_json_as_dict

class RatesJsonDao():
    def retrieve_rates(self):
        return read_json_as_dict("fx_rates.json")
    
    def search_rates(self, source_currency, target_currency):
        result = {
            "source_rate": None,
            "target_rate": None
        }
        rates_data = self.retrieve_rates().get("rates", [])
        
        for rate in rates_data:
            if rate.get("currency") == source_currency:
                result["source_rate"] = rate.get("rate")
            if rate.get("currency") == target_currency:
                result["target_rate"] = rate.get("rate")
        
        return result
    
    def retrieve_currencies(self):
        result = []
        rates_data = self.retrieve_rates().get("rates", [])

        for rate in rates_data:
            result.append(rate.get("currency"))

        return result