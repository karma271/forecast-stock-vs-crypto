# Can we pick the 'right' asset for 2020?  
**Author:** Prasoon Karmacharya  
**Repository:** https://github.com/karma271/forecast-stock-vs-crypto  


<hr>

# Problem statement

> Can we select a stock or a cryptocurrency that will gives us the best ROI at the end of the year? 
>
>**Criterion:**  
>- Single investment of 100,000 USD on 2020-01-01   
>- Realize gain based on the adjusted close value of the stock on 2020-12-31  
>
>**Goal:**
>Determine a stock that yields the highest return with high confidence

## Directory Structure
| Directory                                                        | Filename                                                                                                       | Description                                                                                             |
|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [src](src)                                                       | [00_download_stock_data.py](src/00_download_stock_data.py)                                                     | python script to download NASDAQ stock data                                                             |
|                                                                  | [01_Search_Performant_Stocks.ipynb](src/01_Search_Performant_Stocks.ipynb)                                     | notebook to pick top 10 performant stocks                                                               |
|                                                                  | [02_Forecast_Preliminary_using_Classical_Model.ipynb](src/02_Forecast_Preliminary_using_Classical_Model.ipynb) | notebook preliminary timeseries modeling                                                                |
|                                                                  | [03_Forecast_2020_using_Classical_Model.ipynb](src/03_Forecast_2020_using_Classical_Model.ipynb)               | notebook 2020 forecasting of top 10 performant stocks                                                   |
|                                                                  | [04_Forecast_2020_top_10_comparison_FANG.ipynb](src/04_Forecast_2020_top_10_comparison_FANG.ipynb)             | notebook Comparison of top 10 stocks with FANG                                                          |
|                                                                  | [05_LSTM_Stock_Forecast-2020.ipynb](src/05_LSTM_Stock_Forecast-2020.ipynb)                                     | (WIP) notebook Deep Neural Network model, LSTM TS forcasting                                            |
| [NASDAQ stock data](assets/data/historical_NASDAQ)               | Over 6000 files                                                                                                | Not uploaded, can be downloaded using [00_download_stock_data.py](src/00_download_stock_data.py) script |
| [Bitcoin data](assets/data/historical_bitcoin)                   | bitcoin.csv                                                                                                    | Can be downloaded from [here](https://www.kaggle.com/mczielinski/bitcoin-historical-data)               |
| [best_models_SARIMAX_2020](assets/data/best_models_SARIMAX_2020) | -                                                                                                              | Need this folder to replicate saving models that will be reused by multiple notebooks                   |
| [processed_data]( assets/data/processed_data)                    | NASDAQ_stock_performance.csv                                                                                   | Forecast profile for 10 performant stocks                                                               |
| [slide deck](Slide_Deck.pdf)                    |    [Slide_Deck.pdf](Slide_Deck.pdf)                                 | Presentation Slide Deck   |

## Notes for replication
* requires python 3.7 or higher
* git clone the repo
* create a virtual environment
* install required libraries `pip install -r requirements.txt`
* ensure that all the folder structure defined in the Directory Structure exist
* run notebooks in a sequential order

*Note: Some scripts and notebooks take a while to run.*
