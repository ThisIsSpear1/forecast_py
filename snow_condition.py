

#적설 S06 범주 및 표시 값
def def_snow_condition(snow_condition):
    if snow_condition < 0.1:
        print("0cm 또는 없음")
    elif 0.1 <= snow_condition < 1:
        print("1cm 미만")
    elif 1 <= snow_condition < 5:
        print("1cm~4cm")
    elif 5 <= snow_condition < 10:
        print("5cm~9cm")
    elif 10 <= snow_condition < 20:
        print("10cm~19cm")
    elif 20 <= snow_condition:
        print("20cm")
