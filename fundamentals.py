import datetime as datetime

#Example for dynamic properties
#class AnyDataClass:
#  def __init__(self, dictionary):
#    for k, v in dictionary.items():
#      setattr(self, k, v)

import math
import pandas_datareader.data as web
import pandas_datareader as pdr
import numpy as np
import pandas as pd
import copy
import requests
import inspect

class Financial_Modelling_Rest_Client:
  API_KEY = "6b5abd973247689c7e82d6f016ed183c"
  URL_Prefix = "https://financialmodelingprep.com/api/v3"
  INCOME_STATEMENT = "income-statement"
  BALANCE_SHEET = "balance-sheet-statement"
  COMPANY_PROFILE = "profile"

class Financial_Rest_Client (Financial_Modelling_Rest_Client):
      def __init__(self):
        super().__init__()

      def get_Annual_Income_Statement(self, ticker):
        print( f"{self.URL_Prefix}/{self.INCOME_STATEMENT}/{ticker}?apikey={self.API_KEY}")
        return f"{self.URL_Prefix}/{self.INCOME_STATEMENT}/{ticker}?apikey={self.API_KEY}"
  
      def get_Balance_Sheet(self, ticker):
        return f"{self.URL_Prefix}/{self.BALANCE_SHEET}/{ticker}?apikey={self.API_KEY}"

class Company_Profile_Rest_Client (Financial_Modelling_Rest_Client):
      def __init__(self):
            super().__init__()

      def get_Company_Profile(self, ticker):
            print( f"{self.URL_Prefix}/{self.COMPANY_PROFILE}/{ticker}?apikey={self.API_KEY}")
            return f"{self.URL_Prefix}/{self.COMPANY_PROFILE}/{ticker}?apikey={self.API_KEY}"

class Value_Investment:      
      prop_types = None
      prop_formats = None
      
      def convert_to_type(self, value, type = None, format = '%Y-%m-%d'):
            if isinstance(type, datetime.datetime):
              return datetime.datetime.strptime(value, format)
            elif isinstance(type, int):
              return int(value)
            else:
              return value
            
      def init_prop_types_and_formats(self, length=0, keys=None):
        if keys == None:
            self.prop_types = np.full(length, type(""))
            self.prop_formats = np.full(length, '%Y-%m-%d')
            return
        self.prop_types = {}
        self.prop_formats = {}
        for item in keys:
            self.prop_types[item] = type("")
            self.prop_formats[item] = '%Y-%m-%d'            
          
      def parse_properties(self, prop_dicts):
            for attr in prop_dicts.keys():
                  try:
                    new_value = self.convert_to_type(prop_dicts[attr], self.prop_types[attr], self.prop_formats[attr])
                    self.__setattr__(attr, new_value)
                  except AttributeError:
                    print(f"The attribute:{attr} is not a part of the current object!")
      
      def parse_json_data(self, json_data=None):
        if json_data != None:              
              if self.prop_types == None or self.prop_formats == None:                    
                    self.init_prop_types_and_formats(len(json_data))
              self.parse_properties(json_data)    
      
      def get_properties(self):
            props = inspect.getmembers(self, lambda a:not(inspect.isroutine(a)))
            return props
      
      def __str__(self):
            props = self.get_properties()
            res = f"Object Name:\t" + type(self).__name__ + f"\n"
            res = res + f"--------------------------------\n"
            for item in props:
                  res = res + f"{item}:\t" + self.__getattribute__(item)  + "\n"
            res = res + f"--------------------------------\n"    
            
class Annual_Income_Statement(Value_Investment):
  date = None
  symbol = None
  fillingDate = None
  acceptedDate = None
  period = None
  revenue = None
  costOfRevenue = None
  grossProfit = None
  grossProfitRatio = None
  researchAndDevelopmentExpenses = None
  generalAndAdministrativeExpenses = None
  sellingAndMarketingExpenses = None
  otherExpenses = None
  operatingExpenses = None
  costAndExpenses = None
  interestExpense = None
  depreciationAndAmortization = None
  ebitda = None
  ebitdaratio = None
  operatingIncome = None
  operatingIncomeRatio = None
  totalOtherIncomeExpensesNet = None
  incomeBeforeTax = None
  incomeBeforeTaxRatio = None
  incomeTaxExpense = None
  netIncome = None
  netIncomeRatio = None
  eps = None
  epsdiluted = None
  weightedAverageShsOut = None
  weightedAverageShsOutDil = None
  link = None
  finalLink = None

  def __init__(self, json_data = None, prop_types = None, prop_formats = None):
    super().__init__()
    self.init_prop_types_and_formats(len(json_data), json_data.keys())
    self.prepare_real_types_and_formats()
    self.parse_json_data(json_data)
  
  def prepare_real_types_and_formats(self):
  #TODO: Add all types
        try:
          #dates
          self.prop_types["date"] = type(datetime.datetime)
          self.prop_formats["date"] = '%Y-%m-%d'
          self.prop_types["fillingDate"] = type(datetime.datetime)
          self.prop_formats["fillingDate"] = '%Y-%m-%d'
          self.prop_types["acceptedDate"] = type(datetime.datetime)
          self.prop_formats["acceptedDate"] = '%Y-%m-%d'
        except KeyError:
          print(f"The Key does not exist!")
      
  def getFY(self):
    if self.date != None :
      if isinstance(self.date, datetime.datetime):
        return self.date.year
    # Better to return an Exception
    return None

class Income_statement_Manager():
  @staticmethod
  def transform_annual_income_statement(req_income_json):
    ais = Annual_Income_Statement()
    #2015-12-31
    ais.date = datetime.datetime.strptime(req_income_json["date"], '%Y-%m-%d')
    ais.symbol = req_income_json["symbol"]
    ais.fillingDate = req_income_json["fillingDate"]
    ais.acceptedDate = req_income_json["acceptedDate"]
    ais.period = req_income_json["period"]
    ais.revenue = req_income_json["revenue"]
    ais.costOfRevenue = req_income_json["costOfRevenue"]
    ais.grossProfit = req_income_json["grossProfit"]
    ais.grossProfitRatio = req_income_json["grossProfitRatio"]
    ais.researchAndDevelopmentExpenses = req_income_json["researchAndDevelopmentExpenses"]
    ais.generalAndAdministrativeExpenses = req_income_json["generalAndAdministrativeExpenses"]
    ais.sellingAndMarketingExpenses = req_income_json["sellingAndMarketingExpenses"]
    ais.otherExpenses = req_income_json["otherExpenses"]
    ais.operatingExpenses = req_income_json["operatingExpenses"]
    ais.costAndExpenses = req_income_json["costAndExpenses"]
    ais.interestExpense = req_income_json["interestExpense"]
    ais.depreciationAndAmortization = req_income_json["depreciationAndAmortization"]
    ais.ebitda = req_income_json["ebitda"]
    ais.ebitdaratio = req_income_json["ebitdaratio"]
    ais.operatingIncome = req_income_json["operatingIncome"]
    ais.operatingIncomeRatio = req_income_json["operatingIncomeRatio"]
    ais.totalOtherIncomeExpensesNet = req_income_json["totalOtherIncomeExpensesNet"]
    ais.incomeBeforeTax = req_income_json["incomeBeforeTax"]
    ais.incomeBeforeTaxRatio = req_income_json["incomeBeforeTaxRatio"]
    ais.incomeTaxExpense = req_income_json["incomeTaxExpense"]
    ais.netIncome = req_income_json["netIncome"]
    ais.netIncomeRatio = req_income_json["netIncomeRatio"]
    ais.eps = req_income_json["eps"]
    ais.epsdiluted = req_income_json["epsdiluted"]
    ais.weightedAverageShsOut = req_income_json["weightedAverageShsOut"]
    ais.weightedAverageShsOutDil = req_income_json["weightedAverageShsOutDil"]
    ais.link = req_income_json["link"]
    ais.finalLink = req_income_json["finalLink"]
    return ais

class Company_Profile_Manager:  
  
  @staticmethod
  def load_Company_Profile(ticker):
    rc = Company_Profile_Rest_Client()
    url = rc.get_Company_Profile(ticker)
    req_profile = requests.get(url)
    req_profile = req_profile.json()    
    return req_profile
    


class Income_Statement(Value_Investment):
  date = None
  annual_income_statements = {}

  def __init__(self):
    super().__init__()

  def add_Annual_Income_Statement(self, ais):
    year = ais.getFY()
    if year != None:      
      self.annual_income_statements[str(year)] = copy.copy(ais)
      return True
    return False

  def get_Years(self):
    return np.array(list(self.annual_income_statements.keys()))
    #for key,value in self.annual_income_statements.items():
    #  print(key)

class Financial(Value_Investment):
  rest_client = Financial_Rest_Client()
  income_statement = Income_Statement()

  def __init__(self, ticker):
    self.load_Income_Statement(ticker)
    super().__init__()      

  def load_Income_Statement(self, ticker):
    url = self.rest_client.get_Annual_Income_Statement(ticker)
    req_incomes = requests.get(url)
    req_incomes = req_incomes.json()
    for income in req_incomes:
#      ais = Income_statement_Manager.transform_annual_income_statement(income)
      
      ais = Annual_Income_Statement(income)
      self.income_statement.add_Annual_Income_Statement(ais)
      
    
      #liabilities_i = year['totalLiabilities']
      #liabilities.append(liabilities_i)
    
      #equity_i = year['totalStockholdersEquity']
      #equity.append(equity_i)

class Stocks(Value_Investment):
  stocks_df = None
  year_data_df = None

  def __init__(self, ticker = 'GOOG', start = datetime.datetime(2016, 1, 1), end = datetime.datetime(2019, 1, 1)):
    self.stocks_df = web.DataReader(ticker, data_source='yahoo', start=start, end=end)
    #self.stocks_df['year'] = self.stocks_df.DatetimeIndex.year
    self.stocks_df['year'] = self.stocks_df.index.year
    self.stocks_df['year-mean'] = self.stocks_df.groupby('year')['Adj Close'].mean()
    super().__init__()

  def initYearData(self):
    self.year_data_df = pd.DataFrame({'year': self.stocks_df.groupby('year'), 'mean': self.stocks_df.groupby('year')['Adj Close'].mean(), 'max': self.stocks_df.groupby('year')['Adj Close'].max(), 'min': self.stocks_df.groupby('year')['Adj Close'].min()}, columns=['year', 'mean', 'max', 'min'])
    self.year_data_df['volatility'] = (self.year_data_df['max']-self.year_data_df['min'])/self.year_data_df['mean']
    self.year_data_df['mean_next_year'] = self.year_data_df['mean'].shift(periods=1)
    self.year_data_df['grow'] = (1.-self.year_data_df['mean_next_year']/self.year_data_df['mean'])*100
    self.year_data_df['grow'] = (1.-self.year_data_df['mean_next_year']/self.year_data_df['mean'])*100 
  
  def compound_annual_grow_rate(self, stock_start_price = 0, stock_end_price = 0, num_years = 1):
    return (stock_end_price / stock_start_price) ** (1 / (num_years - 1)) - 1

  def plot_data(self):
    ax = self.year_data_df.plot('year',['mean', 'max', 'min'])
    ax1 = ax.twinx()
    self.year_data_df.plot('year','grow',ax=ax1, color='r')

class Company_Profile(Value_Investment):
  symbol = None
  price = None
  beta = None
  volAvg = None
  mktCap = None
  lastDiv = None
  range = None
  changes = None
  companyName = None
  exchange = None
  exchangeShortName = None
  industry = None
  website = None
  description = None
  ceo = None
  sector = None
  country = None
  fullTimeEmployees = None
  phone = None
  address = None
  city = None
  state = None
  zip = None
  dcfDiff = None
  dcf = None
  image = None

  def __init__(self, ticker):
        super().__init__
        req_profile = Company_Profile_Manager.load_Company_Profile(ticker)
        self.transform_company_profile(req_profile)
  
  def transform_company_profile(self, req_comp_profiles_json):
        for json_profile in req_comp_profiles_json:
            for key in json_profile:
              #print(key, '->', json_profile[key])
              self.__setattr__(key, json_profile[key])

  
  ''' def __str__(self):
    res = f"Company Profile\n"
    res = res + f"--------------------------------\n"
    res = res + f"symbol\t{self.symbol}\n"
    res = res + f"price\t{self.price}\n"
    res = res + f"beta\t{self.beta}\n"
    res = res + f"volAvg\t{self.volAvg}\n"
    res = res + f"mktCap\t{self.mktCap}\n"
    res = res + f"lastDiv\t{self.lastDiv}\n"
    res = res + f"range\t{self.range}\n"
    res = res + f"changes\t{self.changes}\n"
    res = res + f"companyName\t{self.companyName}\n"
    res = res + f"exchange\t{self.exchange}\n"
    res = res + f"exchangeShortName\t{self.exchangeShortName}\n"
    res = res + f"industry\t{self.industry}\n"
    res = res + f"website\t{self.website}\n"
    res = res + f"description\t{self.description}\n"
    res = res + f"ceo\t{self.ceo}\n"
    res = res + f"sector\t{self.sector}\n"
    res = res + f"country\t{self.country}\n"
    res = res + f"fullTimeEmployees\t{self.fullTimeEmployees}\n"
    res = res + f"phone\t{self.phone}\n"
    res = res + f"address\t{self.address}\n"
    res = res + f"city\t{self.city}\n"
    res = res + f"state\t{self.state}\n"
    res = res + f"zip\t{self.zip}\n"
    res = res + f"dcfDiff\t{self.dcfDiff}\n"
    res = res + f"dcf\t{self.dcf}\n"
    res = res + f"image\t{self.image}\n"
    res = res + f"--------------------------------\n"
    return res '''

class Company(Value_Investment):
  name = None
  ticker = None
  financial = None
  stocks = None
  company_profile = None

  def __init__ (self, ticker = 'GOOG'):
    self.ticker = ticker
    self.company_profile = Company_Profile(ticker)
    self.name = self.company_profile.companyName
    self.financial = Financial(ticker)
    self.stocks = Stocks(ticker)
    
    super().__init__()
   
  def __str__(self):
    res = f"Company Info\n"
    res = res + f"--------------------------------\n"
    res = res + f"Name:\t{self.name}\n"
    res = res + f"Ticker:\t{self.ticker}\n"
    res = res + f"--------------------------------\n"
    return res
    
  def get_Annual_Statement_Years(self):
    return self.financial.income_statement.get_Years()

  def plot(self):
    self.stocks.plot_data()

comp = Company("GOOG")
print(comp)
print(comp.company_profile)
years = comp.get_Annual_Statement_Years()
#comp.plot()
