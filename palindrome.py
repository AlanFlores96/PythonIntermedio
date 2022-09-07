def palindrome(string):
  try:
    if len(string) == 0:
      raise ValueError('No se puede ingresar cadenas vacias')
    elif string.isnumeric() == True:
        raise ValueError("No se puede ingresar numeros")
    return string == string[::-1]
  except ValueError as ve:
    print(ve)
    return False


def run():
    # try:
        string=input("Escribe una palabra: ")
        if palindrome(string):
            print("Es palindromo")
        else:
            print("no es palindromo")
    # except TypeError:
    #     print("Solo se pueden ingresar strings")


if __name__=="__main__":
    run()