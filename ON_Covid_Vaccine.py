import csv
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import pandas as pd
import matplotlib.pyplot as plt
import requests



response = requests.get('https://raw.githubusercontent.com/ccodwg/Covid19Canada/master/timeseries_prov/vaccine_administration_timeseries_prov.csv', stream=True)

response.raise_for_status()

with open("vaccine_administration_timeseries_prov.csv", 'wb') as handle:
    for block in response.iter_content(1024):
        handle.write(block)



vaccine_Data = pd.read_csv("vaccine_administration_timeseries_prov.csv")


ON_vaccine_data = vaccine_Data.loc[vaccine_Data['province'] == "Ontario"]



values = pd.date_range(start="14-12-2020",end=datetime.date.today(), periods = 18)



fig = plt.figure(figsize=(24, 12))
plt.plot(ON_vaccine_data["date_vaccine_administered"], 1 * ON_vaccine_data["avaccine"], label="Administered vaccine on the day")
plt.xticks(ON_vaccine_data["date_vaccine_administered"]), values
plt.locator_params(axis='x', nbins=13)
plt.title("Ontario Vaccine administration data", fontsize=22)
plt.xlabel('Date', fontsize=18)
plt.ylabel('Shots Administered', fontsize=20)
plt.ticklabel_format(axis="y", style="sci", scilimits=(3,3))
fig.autofmt_xdate()
plt.legend()
plt.savefig('ON_Vaccine_Graph by Day.png')



fig = plt.figure(figsize=(24, 12))
plt.plot(ON_vaccine_data["date_vaccine_administered"] , ON_vaccine_data["cumulative_avaccine"], label="Cumulative vaccine administered")
plt.xticks(ON_vaccine_data["date_vaccine_administered"]), values
plt.locator_params(axis='x', nbins=13)
plt.title("Ontario Vaccine administration data", fontsize=22)
plt.xlabel('Date', fontsize=18)
plt.ylabel('Shots Administered', fontsize=20)
plt.ticklabel_format(axis="y", style="sci", scilimits=(6,6))
fig.autofmt_xdate()
plt.legend()
plt.savefig('ON_Vaccine_Graph Cummulative.png')