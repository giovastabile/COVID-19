import pandas as pd
import matplotlib.pyplot as plt

countries = ["Italy","Germany","US","Spain"]
Confirmed = True
Deaths = False
Recovered = False
df_c = pd.read_csv('../csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')
df_d = pd.read_csv('../csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv')
df_r = pd.read_csv('../csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv')
for i in countries:
	a = df_c.loc[df_c['Country/Region'] == i].values[0,4:]
	b = df_d.loc[df_d['Country/Region'] == i].values[0,4:]
	c = df_r.loc[df_r['Country/Region'] == i].values[0,4:]
	if(Confirmed):
		plt.plot(range(len(a)),a,label='Confirmed '+i)
	if(Deaths):
		plt.plot(range(len(b)),b,label='Deaths '+i)
	if(Recovered):
		plt.plot(range(len(c)),c,label='Recovered '+i)


plt.grid()
plt.legend()
plt.show()