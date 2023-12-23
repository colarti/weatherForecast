import requests
from datetime import datetime
import os

#Reference: https://openweathermap.org/forecast5#name5

def get_data(place, days, option):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid=ea685bb1a536171a57fd08b997a65d54'
    data = requests.get(url)
    content = data.json()
    filtered_data = content['list']
    print(len(filtered_data))
    filtered_data = filtered_data[:8 * days]
    print(len(filtered_data))

    if option == 'Temperature':
        filtered_data = [ x['main']['temp'] for x in filtered_data]
    elif option == 'Sky':
        filtered_data = [ x['weather'][0]['main'] for x in filtered_data]
    else:
        filtered_data = None    
    
    print(filtered_data)

    return filtered_data
    
    # info = list()
    # for x in content['list']:
    #     date = datetime.fromtimestamp(x['dt']).strftime('%Y-%m-%d <> %H:%M:%S')
    #     mintemp = x['main']['temp_min']
    #     maxtemp = x['main']['temp_max']
    #     humidity = x['main']['humidity']
    #     sky = x['weather'][0]['description']

    #     info.append({'date':date, 'mintemp':mintemp, 'maxtemp':maxtemp, 'humidity':humidity, 'sky':sky})

    # return info

if __name__ == '__main__':


    info = get_data('tokyo', 2, 'Sky')
    # for x in info:
    #     print(x)