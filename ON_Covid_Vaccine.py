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



values = pd.date_range(start="14-12-2020",end=datetime.date.today(), periods = 25)



print("Last 2 days stats are: \n"
    + str(ON_vaccine_data["date_vaccine_administered"].values[-2]) + "  " +  str(ON_vaccine_data["avaccine"].values[-2]) + "\n"
 + str(ON_vaccine_data["date_vaccine_administered"].values[-1]) + "  " + str(ON_vaccine_data["avaccine"].values[-1]))


fig = plt.figure(figsize=(24, 12))
plt.plot(ON_vaccine_data["date_vaccine_administered"], 1 * ON_vaccine_data["avaccine"], label="Administered Shots On The Day",  linewidth=2, color="black")
plt.xticks(ON_vaccine_data["date_vaccine_administered"], fontsize=16)
plt.yticks(fontsize=14)
plt.rc('font', size=14)
plt.locator_params(axis='x', nbins=18)
plt.locator_params(axis='y', nbins=9)
plt.title("Ontario Daily Vaccine Administration Data", fontsize=22, color="black")
plt.xlabel('Date', fontsize=18, color="black")
plt.ylabel('Shots Administered', fontsize=20, color="black")
plt.ticklabel_format(axis="y", style="sci", scilimits=(3,3))
fig.autofmt_xdate()
# fig.patch.set_facecolor('black')
# fig.patch.set_alpha(1)
ax = plt.axes()
# ax.patch.set_facecolor("gray")
# ax.patch.set_alpha(0.6)
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')
ax.yaxis.offsetText.set_fontsize(16)
plt.legend()
plt.savefig('ON_Vaccine_Graph by Day.png')



fig = plt.figure(figsize=(24, 12))
plt.plot(ON_vaccine_data["date_vaccine_administered"] , ON_vaccine_data["cumulative_avaccine"], label="Cumulative Shots Administered", linewidth=2, color="black")
plt.xticks(ON_vaccine_data["date_vaccine_administered"], fontsize=16)
plt.yticks(fontsize=14)
plt.rc('font', size=14)
plt.locator_params(axis='x', nbins=18)
plt.locator_params(axis='y', nbins=9)
plt.title("Ontario Cumulative Vaccine Administration Data", fontsize=22, color="black")
plt.xlabel('Date', fontsize=18, color="black")
plt.ylabel('Shots Administered', fontsize=20, color="black")
plt.ticklabel_format(axis="y", style="sci", scilimits=(6,6))
fig.autofmt_xdate()
# fig.patch.set_facecolor('black')
# fig.patch.set_alpha(1)
ax = plt.axes()
# ax.patch.set_facecolor("gray")
# ax.patch.set_alpha(0.6)
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')
ax.yaxis.offsetText.set_fontsize(16)
plt.legend()
plt.savefig('ON_Vaccine_Graph Cumulative.png')