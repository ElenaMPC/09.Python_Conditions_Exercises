print("Hey, hola! Vamos a convertir millas en km")

km = int(input("¿Cuántos km quieres pasar a millas? "))
print(str(km), "km es igual a:", km*0.621371, "millas")


while True:
    Conversion = input("Quieres hacer otra conversión (s/n)?? ")

    if Conversion == "s":
        km = int(input("¿Cuántos km quieres pasar a millas? "))
        print(str(km) + " km son las siguientes millas:")
        print(km * 0.621371)

    else:
        print("Vale!, ¡hasta luego!")
        break


