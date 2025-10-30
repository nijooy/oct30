for i in range(100, 1, -1):
  if str(i).count('3') > 0:
    count = str(i).count('3')
    print('짝' * count)
  else:
    print(i)