
precipitation = 6

if precipitation < 0.1:
    print("0mm 또는 없음")
elif 0.1 <= precipitation < 1:
    print("1mm 미만")
elif 1 <= precipitation < 5:
    print("1mm~4mm")
elif 5 <= precipitation < 10:
    print("5mm~9mm")
elif 10 <= precipitation < 20:
    print("10mm~19mm")
elif 20 <= precipitation < 40:
    print("20mm~39mm")
elif 40 <= precipitation < 70:
    print("40mm~70mm")
elif precipitation >= 70:
    print("70mm 이상")
