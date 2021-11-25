import json

class RatesParser:
    def __init__(self, filepath):
        file_info = self.open_json_file(filepath)
        self.base = file_info.get("base")
        self.date = file_info.get("date")
        #self.GBP = file_info.get("GBP")
        #self.AUD = file_info.get("AUD")
        #self.USD = file_info.get("USD")
        self.rates = file_info.get("rates")
        pass

    def open_json_file(self, filepath):
        with open(filepath) as exchange_rate_info:
            return json.load(exchange_rate_info)

    def exchange_euro(self, euros, currency):
        exchange_rate = self.rates.get(currency)
        if exchange_rate == None:
            return "Currency doesn't exist in this database"
        money = exchange_rate * euros
        return round(money,2)

x = RatesParser("exchange_rate.json")
print(x.exchange_euro(10,'GBP'))
print(x.exchange_euro(10,'QQQ'))
# on initialisation ,read in a provided file path
# Base rate, date,  GBP, AUD, USD attributes
# e.g. self.gbp = 0.89275
# Method called convert
# Takes in a string corresponding to a current in dataset
# Takes in a value (representing in eur)
# Returns the value in the other currency
# inputs 10 eur, GBP returns equvivlent in GBP

# Think about how the concert method should hand being passed a currency not s
# found in the json file