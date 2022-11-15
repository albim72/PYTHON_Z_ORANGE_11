from osoba import Osoba
from pracownik import Pracownik
from student import Student

p1 = Osoba("Jan",38,89,174)
p1.print_osoba()
print(f"wiek za 10 lat: {p1.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({p1.czypracownik()})")

print("_________________________________________________________")
p2 = Osoba("Olga",27,54,168)
p2.kolor_oczu = "niebieskie"
p2.print_osoba()
print(f"wiek za 10 lat: {p2.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({p2.czypracownik()})")

print("_________________________________________________________")

em1 = Pracownik("Karol",50,80,178,"ABC","dyrektor",12,10900)
em1.print_osoba()
em1.print_pracownik()
print(f"wiek za 10 lat: {em1.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({em1.czypracownik()})")

print("_________________________________________________________")
s1 = Student("Olaf",22,77,177,453453,"Budowlany","Konstrukcja mostów",3)
s1.print_osoba()
s1.print_student()
print(f"wiek za 10 lat: {s1.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({s1.czypracownik()})")

print("_________________________________________________________")
s2 = Student("Olga",21,52,166,765465,"Ekonomia","Makroekonomia",2,"XYZ SA","sekretarka",1,2300)
s2.print_osoba()
s2.print_student()
s2.print_pracownik()
print(f"wiek za 10 lat: {s2.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({s2.czypracownik()})")

print("_________________________________________________________")
s3 = Student("Jacek",22,83,188,76643,"Automatyka, Elektronika i Informatyka","Informatyka",3,
             dyscyplina="Biegi Ultra",lata_upr=5,best_wynik="102km 19h 51min 3s")
s3.print_osoba()
s3.print_student()
s3.infosport()
print(f"wiek za 10 lat: {s3.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({s3.czypracownik()})")

