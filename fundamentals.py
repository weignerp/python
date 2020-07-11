import datetime as datetime

#Exmple for dznamic properties
class AnyDataClass:
  def __init__(self, dictionary):
    for k, v in dictionary.items():
      setattr(self, k, v)

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
    x = 0
  
  def getFY(self):
    if self.date != None :
      if isinstance(self.date, datetime.datetime):
        return self.date.year
    # Better to return an Exception
    return None

class Income_statement_Manager:
  
  @staticmethod
  def transform_annual_income_statement(req_income_json):
    x = 0
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

import numpy as np

class Income_Statement:
  date = None
  anual_income_statements = {}

  def __init__(self):
    #Balance_Sheet
    x = 0

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

class Financials_Rest_Client:
  API_KEY = "6b5abd973247689c7e82d6f016ed183c"
  URL_Prefix = "https://financialmodelingprep.com/api/v3"
  INCOME_STATEMENT = "income-statement"
  BALANCE_SHEET = "balance-sheet-statement"
  
  def get_Anual_Income_Statement(self, ticker):
    print( f"{self.URL_Prefix}/{self.INCOME_STATEMENT}/{ticker}?apikey={self.API_KEY}")
    return f"{self.URL_Prefix}/{self.INCOME_STATEMENT}/{ticker}?apikey={self.API_KEY}"
  
  def get_Balance_Sheet(self, ticker):
    return f"{self.URL_Prefix}/{self.BALANCE_SHEET}/{ticker}?apikey={self.API_KEY}"

import copy
import requests

class Financials:
  rest_client = Financials_Rest_Client()
  income_statement = Income_Statement()

  def __init__(self, ticker):
    self.load_Income_Statement(ticker)        

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


class Company:
  name = None
  ticker = None
  financials = None

  def __init__ (self, ticker):
    self.ticker = ticker
    self.financials = Financials(ticker)
   
  def __str__(self):
    res = f"Company Info\n"
    res = res + f"--------------------------------\n"
    res = res + f"Name:\t{self.name}\n"
    res = res + f"Ticker:\t{self.ticker}\n"
    res = res + f"--------------------------------\n"
    return res
    
  def get_Annual_Statement_Years(self):
    return self.financials.income_statement.get_Years()

comp = Company("GOOG")
print(comp)
years = comp.get_Annual_Statement_Years()
for year in years:
  print(year)