try:
    n = int(input("Introdueix un nombre enter positiu: "))
    if n < 1:
        print("Valor no vàlid: el número ha de ser positiu.")
    else:
        for num in range(2, n + 1):
            és_primer = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    és_primer = False
                    break
            if és_primer:
                print(num, end=" ")
except ValueError:
    print("Valor no vàlid: has d'introduir un nombre enter.")
