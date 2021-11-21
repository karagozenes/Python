series = [1,1]
while True:
    if len(str(series[-1])) >= 1000:
        break
    else:
        series.append(series[-1] + series[-2])

print(len(series))