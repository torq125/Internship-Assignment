import requests
import pandas as pd

url = 'http://api.open-notify.org/iss-now.json'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}

data = []

count = 1
while count <= 100:
    try:
        request = requests.get(url, headers=headers)
        json_data = request.json()
        
        data.append({
                    'Latitude': json_data['iss_position']['latitude'],
                    'Longitude': json_data['iss_position']['longitude'],
                    'TimeStamp': json_data['timestamp']})
        
        print(count)
        count+=1
    
    except Exception as e:
        print(e)

df = pd.DataFrame(data)
df.to_csv('iss_data.csv')

print("Data Collected and Saved into iss_data.csv .")