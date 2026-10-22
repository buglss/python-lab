#############################################################################
# Fonksiyonlar, Koşullar, Döngüler, Comprehensions
#############################################################################
# - Fonsiyonlar (Functions)
# - Koşullar (Conditions)
# - Döngüler (Loops)
# - Comprehesions

#############################################################################
# Fonksiyonlar (Functions)
#############################################################################

########################
# Fonksiyon Okuryazarlığı (docstring)
########################

help(print)
print("a", "b", sep="__") # a__b

########################
# Fonksiyon Tanımlama
########################

def calculate(x):
    print(x * 2)


calculate(5) # 10

# İki argümanlı/parametreli bir fonksiyon tanımlayalım.

def summer(arg1, arg2):
    print(arg1 + arg2)

summer(7, 8)
summer(arg2=8, arg1=7) # summer(7, 8)
