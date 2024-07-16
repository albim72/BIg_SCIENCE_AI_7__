# import dane
# import dane as dn
from dane import nrfilii as nf
from dane import book as bk
from funkcje.kolekcje import czytaj_liste,czytaj_slownik


print("użycie modułów poprzez import...")
# CTRL+D - powielanie linii/bloku kodu
# CTRL + / komentowanie/odkomentowanie bloku kodu

print(nf)
print(bk)

print("użycie funkcji: czytaj_liste():")
czytaj_liste(nf)

print("użycie funkcji: czytaj_slownik():")
czytaj_slownik(bk)
