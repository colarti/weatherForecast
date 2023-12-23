import requests
from datetime import datetime
import os

#Reference: https://openweathermap.org/forecast5#name5

def get_data(place, days, option):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={os.getenv("WEATHER_API_KEY")}'
    data = requests.get(url)
    content = data.json()
    filtered_data = content['list']
    print(len(filtered_data))
    filtered_data = filtered_data[:8 * days]
    print(len(filtered_data))

    # print(filtered_data)

    dates = [ datetime.fromtimestamp(x['dt']).strftime('%Y-%m-%d %H:%M:%S') for x in filtered_data]
    # print(f'Dates: {dates}')

    if option == 'Temperature':
        filtered_data = [ x['main']['temp']/10 for x in filtered_data]
    elif option == 'Sky':
        filtered_data = [ x['weather'][0]['main'] for x in filtered_data]
    else:
        filtered_data = None    
    
    # print(filtered_data)

    return dates, filtered_data
    
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
    dates, info = get_data('tokyo', 2, 'Sky')
    for d, i in zip(dates, info):
        print(d, i)