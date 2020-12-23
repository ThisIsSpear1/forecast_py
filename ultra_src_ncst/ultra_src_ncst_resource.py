# import xml.etree.ElementTree as tree
# import json
import datetime
import ultra_src_ncst_category

# response_dict = json.loads(response.text)
# print(json.dumps(response_dict, indent= 4))


def print_ncst(response_data):
    if response_data['response']['header']['resultCode'] == '00':
        items = response_data['response']['body']['items']['item']
        for i in items:
            # print("base date : ", i['baseDate'], "base time : ", i['baseTime'],  "category : ", i['category'], "obsrValue", i['obsrValue'])
            ultra_src_ncst_category.category_value(i['category'], i['obsrValue'])
    else:
        print("no data")

