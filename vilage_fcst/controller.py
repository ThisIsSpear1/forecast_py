import vilage_fcst_request
import vilage_fcst_resource
import datetime


def next_time_data(now_date):
    now_date += datetime.timedelta(hours=3)
    return now_date


today = datetime.datetime.now()

base_date = today.strftime("%Y%m%d")
base_time = datetime.datetime.combine(datetime.datetime.today(), datetime.time(0))+datetime.timedelta(hours=2)
row_of_num = 10
page_no = 1
response_data = vilage_fcst_request.request_message(base_date, base_time.strftime("%H00"), row_of_num, page_no)

# while response_data['response']['header']['resultCode'] == '00':
total_count = int(response_data['response']['body']['totalCount'])


has_next = True
while has_next:
    print("\n기준 시각 ", base_time)
    vilage_fcst_resource.print_ncst(response_data)
    response_data = vilage_fcst_request.request_message(base_date, base_time.strftime("%H00"), row_of_num, page_no)
    current_page_num = int(response_data['response']['body']['pageNo'])
    if row_of_num*current_page_num >= total_count:
        has_next = False
    page_no += 1
    # base_time = next_time_data(base_time)
