# data_engineering_stocks

Repo designed to explore methods to retrieve daily stock prices online and append to a local spreadsheet

To do:
- [ ] .service file and automation for Option 1 
- [ ] Test design Option 1
- [ ] Testing
- [ ] Option 2 - Workflow (without paying Microsoft)
- [ ] Analysis - CSV
- [ ] Analysis - Excel (can copy and paste in csv to demo)

## Getting Started

The first step, the historical data, is actually very easy to retrieve by using this free site: `https://fred.stlouisfed.org/series/SP500`

Select `10Y`, `Download`, and choose either `CSV` or `Excel`.

## Daily Updating option 1 - Bash, Python and .csv

- Download data as .csv from fred. *(Should look like the csv in this directory)*
- Ensure python and pandas install i.e. `pip install pandas` 
- Automate `bash_script` which will call `web_scraper.py` and conditionally append extra lines (days) to your csv

```
# add service instructions here
```

## Daily Updating option 2 - Power Automate + Excel

tbc

## Analysis 

tbc
