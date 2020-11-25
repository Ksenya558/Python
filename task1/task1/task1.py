print("Эта программа переводит число из любой системы счисления, в любую другую.")
print("Введите число (Число должно состоять из цифр и/или заглавных латинских букв): ")
number = str(input())
print("Введите систему счисления в которой записано число (Система счисления должна обозначаться цифрами без пробелов или любых других символов): ")
systemOfCalculation1 = int(input())
print("Введите систему счисления в которую необходимо число перевести (Система счисления должна обозначаться цифрами без пробелов или любых других символов): ")
systemOfCalculation2 = int(input())

def ConvertTheNumberSystem(num, to_base=10, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return ConvertTheNumberSystem(n // to_base, to_base) + alphabet[n % to_base]

print("Результат перевода числа: ")
print(ConvertTheNumberSystem(number, systemOfCalculation2, systemOfCalculation1))