import requests

url = 'http://api.open-notify.org/iss-now.json'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}

while True:
    try:
    
        request = requests.get(url, headers=headers)

        json_data = request.json()

        print('Latitude:-', json_data['iss_position']['latitude'])
        print('Longitude:-', json_data['iss_position']['longitude'])
        print('Timestamp:-', json_data['timestamp'])

        break
    except Exception as e:
        print(e)
    
