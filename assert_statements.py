def if_integer(string):
    try: 
        int(string)
        return True
    except ValueError:
        return False


def divisors(num):  
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors
    

def run():
    num = input("Ingresa un numero: ")
    if if_integer(num) == True:
        assert int(num) > 0, "Debes ingresar un número positivo"
        print(divisors(int(num)))
        print("Termino mi programa")
    else:
        assert num.isnumeric(), "Debes ingresar un número"
    # print(divisors(int(num)))
    # print("Termino mi programa")
    # elif if_integer(num) == False:
    # assert num.isnumeric(), "Debes ingresar un número"
    
    
    


if __name__=="__main__":
    run()