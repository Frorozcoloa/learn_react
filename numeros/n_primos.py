def n_primo(num):
    primos = {}
    for x in range(2, num+1):
        for i in range(2, x):
            if(x % i) == 0:
                break
            else: continue

        else:
            primos[x] = True
    return primos


def primos_gemelos(primos):
    pri_ge = []
    for i in primos.keys():
        tofind = 2 + i
        try:
            if primos[tofind]:
                print(tofind, i)
                pri_ge.append([i, tofind])
        except:
            continue
    return pri_ge
 
        


