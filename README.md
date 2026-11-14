# data_engineering_stocks

This repo is designed to explore free options to perform data engineering and data analysis on stocks.

Due to the breadth of data and sources I will be working with the US Index of the S&P500. 

The constraints I will mainly be working with are around the daily retrieval of data.

## Getting Started

The first step, the historical data, is actually very easy to retrieve by using this free site: `https://fred.stlouisfed.org/series/SP500`

Select `10Y`, `Download`, and choose either `CSV` or `Excel`.

Then upload this to Excel locally or Excel for Web (other csv editors are available)

## Daily Updating option 1 - With Python + CSV

- Download data as .csv from fred. *(Should look like the csv in this directory)*
- Ensure python and pandas install i.e. `pip install pandas` 
- Automate `bash_script` which will call `web_scraper.py` and conditionally append extra lines (days) to your csv

```
# add service instructions here
```

## Daily Updating option 2 - With Power Automate + Excel

tbc

## Analysis 

tbc
