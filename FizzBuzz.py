num = int(input(" Selecciona un número entre 1 y 100 "))

print(num)
print("")


for x  in range(num):

    if x % 15 == 0:
        print("FizzBuzz")

    elif x % 5 == 0:
        print("Buzz")

    elif x % 3 == 0:
        print("Fizz")

    else:
        print(x)




