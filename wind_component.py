
def wind_component(category, wind_value):
    wind_value = float(wind_value)
    if category == "UUU":
        if wind_value < 0:
            print("서풍 ", abs(wind_value), "m/s")
        elif wind_value == 0:
            print("현재 동서풍 바람이 불지 않습니다. ")
        else:
            print("동풍 ", abs(wind_value), "m/s")
    elif category == "VVV":
        if wind_value < 0:
            print("남풍 ", abs(wind_value), "m/s")
        elif wind_value == 0:
            print("현재 북남풍 바람이 불지 않습니다. ")
        else:
            print("북풍 ", abs(wind_value), "m/s")
    else:
        print("error")

