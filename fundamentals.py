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

class Financial_Modelling_Rest_Client:
  API_KEY = "6b5abd973247689c7e82d6f016ed183c"
  URL_Prefix = "https://financialmodelingprep.com/api/v3"
  INCOME_STATEMENT = "income-statement"
  BALANCE_SHEET = "balance-sheet-statement"
  COMPANY_PROFILE = "profile"

class Financials_Rest_Client (Financial_Modelling_Rest_Client):
      def __init__(self):
        super().__init__()

      def get_Anual_Income_Statement(self, ticker):
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


class Anual_Income_Statement:
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

  def __init__(self):
    super().__init__
  
  def getFY(self):
    if self.date != None :
      if isinstance(self.date, datetime.datetime):
        return self.date.year
    # Better to return an Exception
    return None

class Income_statement_Manager:
  
  @staticmethod
  def transform_annual_income_statement(req_income_json):
    ais = Anual_Income_Statement()
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
  def transform_company_profile(req_comp_profile_json):
        cp = Company_Profile()
        cp.symbol = req_comp_profile_json["symbol"]
        cp.price = req_comp_profile_json["price"]
        cp.beta = req_comp_profile_json["beta"]
        cp.volAvg = req_comp_profile_json["volAvg"]
        cp.mktCap = req_comp_profile_json["mktCap"]
        cp.lastDiv = req_comp_profile_json["lastDiv"]
        cp.range = req_comp_profile_json["range"]
        cp.changes = req_comp_profile_json["changes"]
        cp.companyName = req_comp_profile_json["companyName"]
        cp.exchange = req_comp_profile_json["exchange"]
        cp.exchangeShortName = req_comp_profile_json["exchangeShortName"]
        cp.industry = req_comp_profile_json["industry"]
        cp.website = req_comp_profile_json["website"]
        cp.description = req_comp_profile_json["description"]
        cp.ceo = req_comp_profile_json["ceo"]
        cp.sector = req_comp_profile_json["sector"]
        cp.country = req_comp_profile_json["country"]
        cp.fullTimeEmployees = req_comp_profile_json["fullTimeEmployees"]
        cp.phone = req_comp_profile_json["phone"]
        cp.address = req_comp_profile_json["address"]
        cp.city = req_comp_profile_json["city"]
        cp.state = req_comp_profile_json["state"]
        cp.zip = req_comp_profile_json["zip"]
        cp.dcfDiff = req_comp_profile_json["dcfDiff"]
        cp.dcf = req_comp_profile_json["dcf"]
        cp.image = req_comp_profile_json["image"]
        return cp
  
  @staticmethod
  def load_Company_Profile(self, ticker):
    url = Company_Profile_Rest_Client.get_Company_Profile(ticker)
    req_profile = requests.get(url)
    req_profile = req_profile.json()
    company_profile = self.transform_company_profile(req_profile)
    return company_profile
    

class Income_Statement:
  date = None
  anual_income_statements = {}

  def __init__(self):
    super().__init__()

  def add_Annual_Income_Statement(self, ais):
    year = ais.getFY()
    if year != None:      
      self.anual_income_statements[str(year)] = copy.copy(ais)
      return True
    return False

  def get_Years(self):
    return np.array(list(self.anual_income_statements.keys()))
    #for key,value in self.anual_income_statements.items():
    #  print(key)

class Financials:
  rest_client = Financials_Rest_Client()
  income_statement = Income_Statement()

  def __init__(self, ticker):
    self.load_Income_Statement(ticker)
    super().__init__()      

  def load_Income_Statement(self, ticker):
    url = self.rest_client.get_Anual_Income_Statement(ticker)
    req_incomes = requests.get(url)
    req_incomes = req_incomes.json()
    for income in req_incomes:
      ais = Income_statement_Manager.transform_annual_income_statement(income)
      self.income_statement.add_Annual_Income_Statement(ais)
      
    
      #liabilities_i = year['totalLiabilities']
      #liabilities.append(liabilities_i)
    
      #equity_i = year['totalStockholdersEquity']
      #equity.append(equity_i)

class Stocks:
  stocks_df = None
  year_data_df = None

  def __init__(self, ticker = 'GOOG', start = datetime.datetime(2016, 1, 1), end = datetime.datetime(2019, 1, 1)):
    self.stocks_df = web.DataReader(ticker, data_source='yahoo', start=start, end=end)
    self.stocks_df['year'] = self.stocks_df.DatetimeIndex(self.stocks_df.index).year
    self.stocks_df['year-mean'] = self.stocks_df.groupby('year')['Adj Close'].mean()
    super().__init__()

  def initYearData(self):
    self.year_data_df = pd.DataFrame({'year': self.stocks_df.groupby('year'), 'mean': self.stocks_df.groupby('year')['Adj Close'].mean(), 'max': self.stocks_df.groupby('year')['Adj Close'].max(), 'min': self.stocks_df.groupby('year')['Adj Close'].min()}, columns=['year', 'mean', 'max', 'min'])
    self.year_data_df['voletality'] = (self.year_data_df['max']-self.year_data_df['min'])/self.year_data_df['mean']
    self.year_data_df['mean_next_year'] = self.year_data_df['mean'].shift(periods=1)
    self.year_data_df['grow'] = (1.-self.year_data_df['mean_next_year']/self.year_data_df['mean'])*100
    self.year_data_df['grow'] = (1.-self.year_data_df['mean_next_year']/self.year_data_df['mean'])*100 
  
  def compound_annual_grow_rate(self, stock_start_price = 0, stock_end_price = 0, num_years = 1):
    return (stock_end_price / stock_start_price) ** (1 / (num_years - 1)) - 1

  def plot_data(self):
    ax = self.year_data_df.plot('year',['mean', 'max', 'min'])
    ax1 = ax.twinx()
    self.year_data_df.plot('year','grow',ax=ax1, color='r')

class Company_Profile:
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

  def __init__(self):
        super().__init__


class Company:
  name = None
  ticker = None
  financials = None
  stocks = None

  def __init__ (self, ticker = 'GOOG'):
    self.ticker = ticker
    self.financials = Financials(ticker)
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
    return self.financials.income_statement.get_Years()

  def plot(self):
    self.stocks.plot_data()

comp = Company("GOOG")
print(comp)
years = comp.get_Annual_Statement_Years()
comp.plot()
