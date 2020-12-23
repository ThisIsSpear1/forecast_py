# import xml.etree.ElementTree as tree
# import json
import datetime
import vilage_fcst_category

# response_dict = json.loads(response.text)
# print(json.dumps(response_dict, indent= 4))


def print_ncst(response_data):
    if response_data['response']['header']['resultCode'] == '00':
        items = response_data['response']['body']['items']['item']
        for i in items:
            print("base date : ", i['baseDate'], "base time : ", i['baseTime'],  "category : ", i['category'], "fcstValue", i['fcstValue'], "fcstDate", i['fcstDate'],
                  "fcstTime", i['fcstTime'])
            #vilage_fcst_category.vilage_fcst(i['category'], i['fcstValue'])
    else:
        print("no data")
