# Data Tipleri
# Text Type
x = "Men AzTU-nun 3.kurs telebesi Imanli Elisahib "
print(x)
print(type(x))

# Numeratic Type (int)
y = 34
print(y)
print(type(y))

# Numeratic Type (float)
z =3.4
print(z)
print(type(z))

#Complex
a = 34j
print(a)
print(type(a))

# Ardicilliqlar (list)
e = ["Armud","Ananas","Albali"]
print(e)
print(type(e))

# Ardicilliqlar (tuple)
r = ["Armud","Ananas","Albali"]
print(r)
print(type(r))

# # range
t = range(34)
print(t)
print(type(t))

# bool
d = True
print(d)
print(type(d))

# Global Deyisen
w = "Imanli"
def myFunc():
    w = "Elisahib"
    print("Adim " + w)
myFunc()
print("Adim " + w)

# Operatorlar (Riyazi Operatorlar)

n = 30
m = 15

print(n + m)
print(n - m)
print(n * m)
print(n / m)
print(n % m)
print(n ** m)
print(n // m)

# Operatorlar (Teyinat Operatorlar)
f = 5
print(f)
f += 5
print(f)
f -= 5
print(f)
f *= 5
print(f)
f /= 5
print(f)
f %= 2
print(f)
f //= 5
print(f)
f **= 5
print(f)

# Operatorlar (Muqayise Operatorlar)
u = 68
i = 34
print(u == i)
print(u != i)
print(u > i)
print(u < i)
print(u <= i)
print(u >= i)

# Operatorlar (Mentiqi Operatorlar)
s = 34
print(s > 33 and s < 35)
print(s > 33 or s > 220)
print(not(s > 33 or s > 220))

# Sert Operatoru (if else)
g = 68
h = 34
if g > h:
  print("g boyukdur h-dan")
elif g == h:
  print("g ve h beraberdir")
else:
  print("g kicikdir -dan")