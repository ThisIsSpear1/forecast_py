
#동네 예보 조회


class VilageFcst:

    def __init__(self, category, fcstValue):
        self.category = category
        self.fcstValue = fcstValue


fcst = VilageFcst("POP", -1)

if fcst.category == "POP":
    print("현재 강수확률은 ", fcst.fcstValue, "입니다. ")
    print("단위는 % 입니다. ")
elif fcst.category == "PTY":
    print("강수 형태")
    print("단위는 코드값입니다. ")
elif fcst.category == "R06":
    print("6시간 강수량")
    print("단위는 범주 1mm 입니다. ")
elif fcst.category == "REH":
    print("습도")
    print("단위는 %입니다. ")
elif fcst.category == "S06":
    print("6시간 신적설")
    print("단위는 범주 1cm 입니다. ")
elif fcst.category == "SKY":
    print("하늘상태 ")
    print("단위는 코드 값입니다. ")
elif fcst.category == "T3H":
    print("3시간 기온")
    print("단위는 'C입니다. ")
elif fcst.category == "TMN":
    print("아침 최저기온")
    print("단위는 'C입니다. ")
elif fcst.category == "TMX":
    print("낮 최고기온")
    print("단위는 'C입니다. ")
elif fcst.category == "UUU":
    print("풍속(동서성분) ")
    print("단위는 m/s 입니다.")
elif fcst.category == "VVV":
    print("풍속(남북성분)")
    print("단위는 m/s 입니다.")
elif fcst.category == "WAV":
    print("파고")
    print("단위는 M입니다.")
elif fcst.category == "VEC":
    print("풍향")
    print("단위는 m/s 입니다.")
elif fcst.category == "WSD":
    print("풍속")
    print("단위는 m/s 입니다.")