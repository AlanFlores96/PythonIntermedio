def divisors(num):
    try:
        if num < 0:
            raise ValueError("no debes ingresar numeros negativos")
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)
        return False


def run():
    try:
        num = int(input("Ingresa un numero: "))
        print(divisors(num))
        print("Termino mi programa")
    except ValueError as ve:
        print("Debes ingresar un núumero")

    # try:
    #     if num < 0:
    #         raise ValueError("No se puede ingresar un numero negativo")
    # except ValueError as ve:
    #     print(ve)


if __name__=="__main__":
    run()