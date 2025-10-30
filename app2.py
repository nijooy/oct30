for i in range(1,101):
    tr = str(i).count("3") + str(i).count("6") + str(i).count("9")
    if tr < 1:
        print(i)
    else:
        print(i, ("짝" * tr))