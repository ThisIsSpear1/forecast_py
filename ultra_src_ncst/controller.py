import ultra_src_ncst_request
import ultra_src_ncst_resource
import datetime


def data_one_hour_ago(now_date):
    now_date += datetime.timedelta(hours=1)
    return now_date


today = datetime.datetime.now()

base_date = today.strftime("%Y%m%d")
base_time = datetime.datetime.combine(datetime.datetime.today(), datetime.time(0))

response_data = ultra_src_ncst_request.request_message(base_date, base_time.strftime("%H00"))

while response_data['response']['header']['resultCode'] == '00':
        print("\n기준 시각 ", base_time)
        ultra_src_ncst_resource.print_ncst(response_data)
        base_time = data_one_hour_ago(base_time)
        response_data = ultra_src_ncst_request.request_message(base_date, base_time.strftime("%H00"))
