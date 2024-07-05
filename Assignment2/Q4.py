import requests

url = 'http://api.open-notify.org/iss-now.json'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}
while True:
    try:
        request = requests.get(url, headers=headers)
        print(request.text)
    
        break

    except Exception as e:
        print(e)