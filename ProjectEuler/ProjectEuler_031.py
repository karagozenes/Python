def func():
    count = 1
    for x in range(3):
        for y in range(5):
            if 50*y + 100*x > 200:
                break
            for z in range(11):
                if 20*z + 50*y + 100*x > 200:
                    break
                for k in range(21):
                    if 10*k + 20*z + 50*y + 100*x > 200:
                        break
                    for l in range(41):
                        if 5*l + 10*k + 20*z + 50*y + 100*x > 200:
                            break
                        for m in range(101):
                            if 2*m + 5*l + 10*k + 20*z + 50*y + 100*x > 200:
                                break
                            for n in range(201):
                                if 1*n + 2*m + 5*l + 10*k + 20*z + 50*y + 100*x > 200:
                                    break
                                if 1*n + 2*m + 5*l + 10*k + 20*z + 50*y + 100*x == 200:
                                    count += 1
    return count

print(func())