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

# BURADAN DEVAM 0008