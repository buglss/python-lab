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

help(print) # Pycharm'da ?print ifadesi de help gibi çıktı verir.
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

#############################################################################
# Docstring - Herkesin anlayabileceği ortak bir dille bilgi notu ekleme yolu.
#############################################################################


def summer(arg1, arg2):
    ########################
    # Google ve NumPy Formatları Vardır
    ########################

    # NumPy
    """
    Sum of two numbers

    Parameters/Args
    ----------
    arg1: int, float
    arg2: int, float

    Returns
    ----------
    int, float

    """

    # Google
    """
    Sum of two numbers

    Args:
        arg1: int, float
        arg2: int, float

    Returns:
        int, float

    """
    
    print(arg1 + arg2)

#############################################################################
# Fonksiyonların Statement/Body Bölümü
#############################################################################

# def function_Name(parameters/arguments):
#     statements (function body)

def say_hi(string):
    print(string)
    print("Hi")
    print("Hello")

# say_hi() # TypeError: say_hi() missing 1 required positional argument: 'string'

say_hi("buglss")
'''
buglss
Hi
Hello
'''

def multiplication(a, b):
    c = a * b
    print(c)

multiplication(10, 9) # 90

# Girilen değerleri bir liste içinde saklayacak fonksiyon.

list_store = [] # Global scope

def add_element(a, b): # Lokal scope
    c = a * b
    list_store.append(c) # Kalıcı değişiklik meydana getirir (mutable)
    print(list_store)

add_element(1, 8) # [8]
add_element(18, 8) # [8, 144]
add_element(180, 10) # [8, 144, 1800]

#############################################################################
# Ön Tanımlı Argümanlar/Parametreler (Default Parameters/Arguments)
#############################################################################

def divide(a, b):
    print(a / b)

divide(1, 2) # 0.5
divide(10) # TypeError: divide() missing 1 required positional argument: 'b'

def divide(a, b=1): # b'nin ön tanımlı değeri 1. Fonksiyon çağırırken boş bırakırsan b, 1 değerini alır
    print(a / b)

divide(1) # 1
