import requests


call_back_url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst'
serviceKey = '1cM0fca7x9v9lVDH7x/Ys0Sg9uzmVsLqRY/yRtnbxpefDmZHVQf2zdR768cNW8Qrx5GlwWK0RyMa2ekGH4bJSg=='


def request_message(base_date, base_time, row_of_num = 10, page_no=1):
    payload = {'ServiceKey': serviceKey,
               'numOfRows': row_of_num,
               'pageNo': page_no,
               'dataType': 'json',
               'base_date': base_date,
               'base_time': base_time,
               'nx': '92',
               'ny': '83'
               }

    response = requests.get(call_back_url, payload)
    response_data = response.json()
    return response_data
