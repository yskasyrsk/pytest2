from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime


path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()
reader =csv.reader(lines)
header_row = next(reader)

#extract dats and high temperatures

dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

#plot the high temperatures

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')
ax.fill_between(dates,highs,lows, facecolor = 'yellow', alpha = 0.1)
#format plot
ax.set_title("Daily high Temperatures, july 2021", fontsize = 20)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (f)", fontsize = 16)
ax.tick_params(labelsize = 16)

plt.show()

