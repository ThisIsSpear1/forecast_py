# 초단기 실황 조회
import forecast.snow_condition as snow_condition
import forecast.wind_component as wind_component

class SrcNcst:

    def __init__(self, category, obsrValue):
        self.__category = category
        self.__obsrValue = obsrValue

    @property
    def category(self):
        return self.__category

    def obsrValue(self):
        return self.__obsrValue


def category_value(category, obsrValue):
    if category == "T1H":
        print("현재 기온   {0:>10}'C 입니다.".format(obsrValue))
    elif category == "RN1":
        print("1시간 강수량{0:>10}mm 입니다. ".format(obsrValue))
    elif category == "UUU":
        wind_component.wind_component(category, obsrValue)
    elif category == "VVV":
        wind_component.wind_component(category, obsrValue)
    elif category == "VEC":
        print("풍향       {0:>10}입니다.단위는 0입니다.".format(obsrValue))
    elif category == "WSD":
        print("풍속       {0:>10}입니다.단위는 m/s 입니다.".format(obsrValue))
    elif category == "PTY":
        print("강수 형태   {0:>10}입니다.단위는 코드값입니다. ".format(obsrValue))
    elif category == "REH":
        print("습도       {0:>10}% 입니다. ".format(obsrValue))
