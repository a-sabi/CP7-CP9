def c(A, D):
    if A * (2) ** 0.5 <= D:
        return "YES"
    return "NO"

    
    
while True:
    try:
        A = int(input("Введите натуральное число A: "))
        if A <= 0:
            raise Exeption()
        D = int(input("Введите натуральное число D: "))
        if D <= 0:
            raise Exeption()
        else:
            print (c(A, D))
    except:
        print ("Введено не натуральное число")
        continue
    break