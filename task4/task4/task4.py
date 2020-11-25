print("Эта программа предназначена для сравнени двух строк.\nВ случае, если строки одинаковы, программа выведет 'ОК'. В противном случае программа выведет 'КО'.")
print("Введите первую строку: ")
str1 = str(input())
print("Введите вторую строку: ")
str2 = str(input())

def CompareStrings (str1, str2):
    count = 0
    if '*' in str2:
        if str2[0] != '*' and str2[0] != str1[0]: return("КО")
        else:
            for i in str2:
                y = 0
                if i != '*':
                    for j in str1:
                        y = y+1
                        if i != j: count = count+1
                        else: count = count-(y-1);
            if count != 0: return("КО")
            else: return("ОК")
    else:
        if str1 == str2: return("ОК")
        else: return("КО")
print("Результат сравнение строк: ")
print(CompareStrings (str1, str2))