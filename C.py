def ab(a, b, t): 

    proba = o/t
    probbga = b/(t - 1)
    proband = proba * probbga

    return round (proband, 3)

o = int(input("Enter orange balls: "))
b = int(input("Enter blue balls"))
t = o + b

print("Probability of getting 1st orange and 2nd blue: ")
print(ab(o, b , t))