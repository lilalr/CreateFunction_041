import math

luas_lingkaran = lambda r: math.pi * r**2

r = float (input("Masukan radius = "))
area = luas_lingkaran (r)
print(f"Luas lingkaran {r} adalah: {area:.2f}")