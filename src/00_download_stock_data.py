"""
Description:
    This script downloads historical data for NASDAQ stock using yfinance package.
Author: Prasoon Karmacharya
Github: karma271
Last Update: 11/15/2020
"""

from datetime import date
import pandas as pd
from pathlib import Path
import time
from tqdm import tqdm
import yfinance as yf


NASDAQ_TRADED_URL = "http://www.nasdaqtrader.com/dynamic/SymDir/nasdaqtraded.txt"
HISTORICAL_NASDAQ_PATH = Path("../assets/data/historical_NASDAQ")

START_DATE = date(2000,1,1)
END_DATE = date(2020,11,6)
FIRST_N_TICKERS = False

def get_NASDAQ_tickers():
    """
    Returns: 
        (list) of all traded NASDAQ symobols without reported Test Issues
        (list) of all traded NASDAQ ETF symbols without reported Test Issues
        (list) of all traded NASDAQ stock symbols without reported Test Issues
    """
    data = pd.read_csv(NASDAQ_TRADED_URL, sep = "|")
    
    all_symbols =  data[data["Test Issue"] == "N"]['NASDAQ Symbol'].tolist()
    ETF_symbols = data[(data["Test Issue"] == "N") & (data["ETF"] == "Y")]['NASDAQ Symbol'].tolist()
    stock_symbols = data[(data["Test Issue"] == "N") & (data["ETF"] == "N")]['NASDAQ Symbol'].tolist()
    
    return all_symbols, ETF_symbols, stock_symbols


def dataframe_to_csv(dataframe, ticker, output_folder = HISTORICAL_NASDAQ_PATH):
    """
    Param(s):
        dataframe : (pandas dataframe)
        ticker    : (str)  stockticker symbol
        output_older : (str) Path to the data folder
    Return
        "No data" if the data file has no data
         excetion (e) if any
        "Success" otherwise

    """
    output_file_path = output_folder / f'{ticker}.csv'
    _df = dataframe
    
    if _df.shape[0] == 0:        
        return "No data"
    else:
        try:
            _df.to_csv(output_file_path)
            return "Success"
        except Exception as e:
            return e
    
def get_NASDAQ_data(TICKERS_LIST, START_DATE, END_DATE):
    """
    Saves data to .csv
    Param(s):
        TICKERS_LIST : (list) containing list of stock symbols
        START_DATE : (str) Date string for the start of the data
        END_DATE : (str) Date string for the end of the data
    """
    for ticker in tqdm(TICKERS_LIST):
        time.sleep(0.3)
        
        # getting data
        try:
            _data = yf.download(ticker, start=START_DATE, end=END_DATE)
        except Exception as e:
            print(f"Error occured when downloading data for {ticker}. Please see the error message.")
            print(f"Error message: \n {e}")
            
        # saving file to csv
        result = dataframe_to_csv(dataframe=_data, ticker=ticker, output_folder = HISTORICAL_NASDAQ_PATH)
        
        if result == "Success":
            print(f"Successful saving data for {ticker}")
        elif result == "No data":
            print(f"No data found for {ticker}. Symbol may be delisted. Not saving to .csv")            
        else:
            print(f"Error occured when saving data for {ticker}")
            print(f"Error message: \n {result}")

    return "Done"

if __name__ == "__main__":
    start_time = time.time()
    
    TICKERS_LIST, ETF_LIST, STOCK_LIST = get_NASDAQ_tickers()
    
    if FIRST_N_TICKERS:
        STOCK_LIST = STOCK_LIST[0:FIRST_N_TICKERS]
    else:
        STOCK_LIST = STOCK_LIST
    
    get_NASDAQ_data(STOCK_LIST, START_DATE, END_DATE)
    print(len(STOCK_LIST))

    end_time = time.time()
    
    print(f"Total time to download the data:{round(end_time-start_time,2)} seconds")
                  
