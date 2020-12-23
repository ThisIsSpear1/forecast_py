import wind_component as wind_component

#동네 예보 조회


class VilageFcst:

    def __init__(self, category, fcstValue):
        self.category = category
        self.fcstValue = fcstValue




def vilage_fcst(category, fcst_value):
    if category == "POP":
        print("현재 강수확률은 {0}% 입니다.".format(fcst_value))
    elif category == "PTY":
        print("강수 형태 {0} 단위는 코드값입니다.".format(fcst_value))
    elif category == "R06":
        print("6시간 강수량 {0} 단위는 범주 1mm 입니다.".format(fcst_value))
    elif category == "REH":
        print("습도 {0}%입니다.".format(fcst_value))
    elif category == "S06":
        print("6시간 신적설 {0} 단위는 범주 1cm 입니다.".format(fcst_value))
    elif category == "SKY":
        print("하늘상태 {0} 단위는 코드 값입니다.".format(fcst_value))
    elif category == "T3H":
        print("3시간 기온 {0}'C입니다.".format(fcst_value))
    elif category == "TMN":
        print("아침 최저기온 {0}'C입니다.".format(fcst_value))
    elif category == "TMX":
        print("낮 최고기온 {0}'C입니다. ".format(fcst_value))
    elif category == "UUU":
        wind_component.wind_component(category, fcst_value)
    elif category == "VVV":
        wind_component.wind_component(category, fcst_value)
    elif category == "WAV":
        print("파고 {0}M입니다.".format(fcst_value))
    elif category == "VEC":
        print("풍향 {0}m/s 입니다.".format(fcst_value))
    elif category == "WSD":
        print("풍속 {0}m/s 입니다.".format(fcst_value))
