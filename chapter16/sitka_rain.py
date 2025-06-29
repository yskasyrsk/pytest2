import csv
from pathlib import Path
from datetime import datetime
from matplotlib import pyplot as plt

plt.close('all')
from chapter16.sitka_highs import header_row

path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

dates, rain_level = [],[]
for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    rains = row[5]
    dates.append(date)
    rain_level.append(rains)

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.plot(dates, rain_level, color='green')
ax.set_title("Daily rain in sitka, july 2021", fontsize = 18)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("rain level", fontsize = 16)
ax.tick_params(labelsize = 8)
yticks = ax.get_yticks()
plt.yticks(yticks[::5], [f"{tick:.0f}" for tick in yticks[::5]])

plt.show()




