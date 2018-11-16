#%matplotlib inline
import json, requests, os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

OWM_URL = 'http://api.openweathermap.org/data/2.5/forecast?q='
LOCATION = 'Shanghai,CN'
APPID='&APPID=c9e521b6df9556fdecb07e21bc4dc965'
UNITS = '&units=metric'

# caculate the offset between local time to UTC
def offset_local_utc():
    local_now = datetime.now()
    utc_now = datetime.utcfromtimestamp(local_now.timestamp())
    return local_now-utc_now

# convert UTC timestamp to local date time
def timestamp_to_local_datetime(timestamp):
    utc_datetime = datetime.utcfromtimestamp(timestamp)
    local_datetime = utc_datetime + TIME_OFFSET
    return local_datetime


TIME_OFFSET = offset_local_utc()

url = OWM_URL + LOCATION + UNITS + APPID
response = requests.get(url)
response.raise_for_status()

weather_all = json.loads(response.text)
print('cnt: {}'.format(weather_all['cnt']))
weather_list = weather_all['list']

temp = []
weather = []
w_desc = []
dt_text = []
ticks = []

for data in weather_list:
    temp.append(data['main']['temp'])
    weather.append(data['weather'][0]['main'])
    w_desc.append(data['weather'][0]['description'])
    dt_text.append(data['dt_txt'])

    # loal hour
    local_datetime = timestamp_to_local_datetime(
        data['dt'])
    ticks.append(str(local_datetime.hour))

#    print(data['dt_txt'])

dic = {}
dic['dt_txt'] = dt_text
dic['weather'] = weather
dic['weather description'] = w_desc
dic['temp'] = temp
dic['x-tick'] = ticks

dfs = pd.DataFrame(dic)

dfs.plot(figsize=(15,8))
plt.xticks(np.arange(len(dfs['x-tick'])), dfs['x-tick'])
plt.xlim(0, len(dfs['x-tick']))
plt.xlabel('Hour')
plt.show()
