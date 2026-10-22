#############################################################################
# VERİ YAPILARI (DATA STRUCTURES)
#############################################################################
# - Veri Yapılarına Giriş ve Hızlı Özet
# - Sayılar (Numbers): int, float, complex
# - Karakter Dizileri (Strings): str
# - Boolean (TRUE-FALSE): bool
# - Liste (List)
# - Sözlük (Dictionary)
# - Demet (Tuple)
# - Set

#############################################################################
# Veri Yapılarına Giriş ve Hızlı Özet
#############################################################################

# Sayılar: integer
x = 46
type(x)

# Sayılar: float
x = 10.3
type(x)

# Sayılar: complex
x = 2j + 1
type(x)

# String
x = "Hello ai era"
type(x)

# Boolean
True
False
type(True)
5 == 4
3 == 2
1 == 1
type(3 == 2)

# Liste
x = ["btc", "eth", "xrp"]
type(x)

# Sözlük (Dictionary)
x = {"name": "Peter", "Age": 36}
type(x)

# Tuple (Demet) --> Listenin Aksi Huysuz Kardeşi
x = ("python", "ml", "ds")
type(x)

# Set --> Kümeler Gibi
x = {"python", "ml", "ds"}
type(x)

# Not: Liste, tuple, set ve dictionary veri yapıları aynı zamanda Python Collections (Arrays) olarak geçmektedir.

#############################################################################
# Sayılar (Numbers): int, float, complex
#############################################################################

a = 5
b = 10.5

a * 3
a / 7
a * b / 10
a ** 2 # Karesi

#############################################################################
# Tipleri Değiştirmek
#############################################################################

int(b)
float(a)

int(a * b / 10)

c = a * b / 10
int(c)

#############################################################################
# Karakter Dizileri (Strings)
#############################################################################

print("John")
print('John')

"John"
name = "John"
name = 'John'

#############################################################################
# Çok Satırlı Karakter Dizileri
#############################################################################

"""Veri Yapıları: Hızlı Özet,
Sayılar (Numbers): int, float, complex,
Karakter Dizinleri (Strings): str,
List, Dictionary, Tuple, Set,
Boolean (TRUE-FALSE): bool"""

long_str = """Veri Yapıları: Hızlı Özet,
Sayılar (Numbers): int, float, complex,
Karakter Dizinleri (Strings): str,
List, Dictionary, Tuple, Set,
Boolean (TRUE-FALSE): bool"""

#############################################################################
# Karakter Dizilerinin Elemanlarına Erişmek
#############################################################################

name
name[0]
name[3]
name[2]

#############################################################################
# Karakter Dizilerinde Slice İşlemi (Dilimleme İşlemi)
#############################################################################

name[0:2] # 0'dan 2'e kadar git 2 hariç
long_str[0:10]

#############################################################################
# String İçerisinde Karakter Sorgulamak
#############################################################################

long_str
"veri" in long_str # Case Sensitive !!!
"Veri" in long_str
"bool" in long_str

#############################################################################
# String (Karakter Dizisi) Metodları
#############################################################################

dir(int) # hangi metodların olduğunu listeler
dir(str)
dir("foo")

########################
# len
########################

name = "John"
type(name) # str
type(len) # builtin_function_or_method (builtins.py)

len(name) # 4

########################
# Fonksiyon class yapısı içerisinde tanımlıysa metod, değilse fonksiyondur.
########################

########################
# upper() & lower(): küçük-büyük dönüşümleri.
########################

"buglss".upper() # BUGLSS
"BUGLSS".lower() # buglss

# type(upper) # NameError: name 'upper' is not defined

########################
# replace: karakter değiştirir.
########################

hi = "Hello AI Era"
hi.replace("l", "p") # 'Heppo AI Era'

########################
# split: böler.
########################

"Hello AI Era".split() # ['Hello', 'AI', 'Era']

########################
# strip: kırpar.
########################

" ofofo ".strip() # 'ofofo'
"ofofo".strip("o") # 'fof'

########################
# capitalize: ilk harfi büyütür.
########################

"foo".capitalize() # 'Foo'

#############################################################################
# Liste (List) --> Önemli bir yere sahiptir.
#############################################################################

# - Değiştirilebilir
# - Sıralıdır. Index işlemleri yapılabilir.
# - Kapsayıcıdır. --> Birden fazla veri yapısını içerisinde barındırabilir.

notes = [1, 2, 3, 4]
type(notes) # list

names = ["a", "b", "v", "d"]

not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]

not_nam[0] # 1
not_nam[5] # True
not_nam[6] # [1, 2, 3]
not_nam[6][1] # 2

type(not_nam[6]) # list
type(not_nam[6][1]) # int

notes[0] = 99 # [99, 2, 3, 4]

not_nam[0:4] # [1, 2, 3, 'a']

########################
# Liste Metodları (List Methods)
########################

dir(notes) # append en yaygın kullanılan metodlar

########################
# len: builtin python fonksiyonu, boyut bilgisi.
########################

len(notes) # 4
len(not_nam) # 7

########################
# append: eleman ekler
########################

notes.append(100) # [99, 2, 3, 4, 100] 

########################
# pop: indexe göre siler
########################

notes.pop(0) # 99, notes -> [2, 3, 4, 100]

########################
# insert: indexe ekler
########################

notes.insert(2, 99) # [2, 3, 99, 4, 100]

#############################################################################
# Sözlük (Dictonary) --> Listelere göre daha az ama yaygın kullanılır.
#############################################################################

# Değiştirilebilir.
# Sırasız. (3.7 sonrası sıralı.)
# Kapsayıcı.

# key-value

dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Reg"}

dictionary["REG"] # 'Regression'

dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE", 20],
              "CART": ["SSE", 30]}

dictionary["CART"][1] # 30

dictionary = {"REG": 10,
              "LOG": 20,
              "CART": 30}

########################
# Key Sorgulama
########################

"REG" in dictionary # True
"YSA" in dictionary # False

########################
# Ket'e Göre Value'ya Erişmek
########################

dictionary["REG"]
dictionary.get("REG")

########################
# Value Değiştirmek
########################

dictionary["REG"] = ["YSA", 10]

########################
# Tüm Key'lere Erişmek
########################

dictionary.keys() # dict_keys(['REG', 'LOG', 'CART'])

dictionary.values() # dict_values([['YSA', 10], ['MSE', 20], ['SSE', 30]])

########################
# Tüm Çiftleri Tuple Halinde Listeye Çevirme
########################

dictionary.items() # dict_items([('REG', ['YSA', 10]), ('LOG', ['MSE', 20]), ('CART', ['SSE', 30])])

########################
# Key-Value Değerini Güncellemek
########################

dictionary.update({"REG": 11}) # {'REG': 11, 'LOG': 20, 'CART': 30}

########################
# Yeni Key-Value Eklemek
########################

dictionary.update({"RF": 10}) # {'REG': 11, 'LOG': 20, 'CART': 30, 'RF': 10}

#############################################################################
# Demet (Tuple) --> Listenin aksi kardeşi, değiştirilemez.
#############################################################################

# - Değiştirilemez.
# - Sıralıdır.
# - Kapsayıcıdır.

t = ("John", "mark", 1, 2)
type(t)

t[0] # 'John'
t[0:3] # ('John', 'mark', 1)

t[0] = 99 # TypeError: 'tuple' object does not support item assignment

t = list(t)
t[0] = 99
t = tuple(t)

#############################################################################
# Set --> Kümeler gibi düşünülebilir. Hız odaklı işlemlerde kullanılır.
#############################################################################

# - Değiştirilebilir.
# - Sırasız + Eşsizdir.
# - Kapsayıcıdır.

########################
# difference(): İki kümenin farkı
########################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

# set1'de olup set2'de olmayanlar.
set1.difference(set2) # 5
set1 - set2 # 5

# set2'de olup set1'de olmayanlar.
set2.difference(set1) # 2

########################
# symmetric_difference(): İki kümede de birbirlerine göre olmayanlar
########################

set1.symmetric_difference(set2) # {2, 5}
set2.symmetric_difference(set1) # {2, 5}

########################
# intersection(): İki kümenin kesişimi
########################

set1.intersection(set2) # {1, 3}
set2.intersection(set1) # {1, 3}

set1 & set2 # {1, 3}

########################
# union(): İki kümenin birleşimi
########################

set1.union(set2) # {1, 2, 3, 5}
set2.union(set1) # {1, 2, 3, 5}

########################
# isdisjoint(): İki kümenin kesişimi boş mu? --> True ya da False (is ile başlıyorsa Boolean döndürür)
########################

set1.isdisjoint(set2) # False
set2.isdisjoint(set1) # False

########################
# isbugset(): Bir küme diğer kümenin alt kümesi mi?
########################

set1.issubset(set2) # False
set2.issubset(set1) # False

########################
# issuperset(): Bir küme diğer kümeyi kapsıyor mu?
########################

set1.issuperset(set2) # False
set2.issuperset(set1) # False