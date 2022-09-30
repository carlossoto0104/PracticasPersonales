print("Bienvenido, este algortimo le indicara si un numero es repunit y si la suma de sus digitos es un numero cuadrado")

number = input("Por favor ingrese un numero para su comprobacion:")
while not number.isnumeric():
    number = input("ERROR, por favor ingrese un numero nuevamente:")

isRepunit=True
firstDigit= number [0]
for digit in number:
    if digit != firstDigit:
        isRepunit=False

