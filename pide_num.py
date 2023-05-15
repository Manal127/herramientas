def pideUnNum():
    msg = "Dame un num: "
    entrada = ''
    invalido = False
    while not entrada.isnumeric():
        if invalido:
            print("Obligatoriamente debe ser un número")
        invalido = True
        entrada = input(msg)
    return int(entrada)

if __name__ == "__main__":
    print(pideUnNum())
