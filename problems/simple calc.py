num1, num2 = 0, 0
int(num1), int(num2)
num1, num2, num3 = [float(x) for x in input().split()]
num4, num5 = 0, 0
int(num4), int(num5)
num4, num5, num6 = [float(y) for y in input().split()]
result = (num2 * num3) + (num5 * num6)
print("VALOR A PAGAR: R$", format(result, ".2f"))