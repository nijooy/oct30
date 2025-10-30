for i in range(1,101):
    tr = str(i).count("3") + str(i).count("6") + str(i).count("9")
    if tr < 1:
        print(i)
    else:
        print(i, ("짝" * tr))
# 3,6,9 라서 6,9도 포함되는 경우로 선택했습니다!