# 1. Kérjünk be egy időértéket óra:perc:másodrperc formátumban, és írjuk ki másodpercben!
ido = input('Kérem az aktuális időt [óó:pp:mm]: ')
ido_adatok = ido.split(':')
masodperc = int(ido_adatok[0])*3600 + int(ido_adatok[1])*60 +  int(ido_adatok[2])
print(f'Másodpercben: {masodperc}')

# 2. Kérjünk be egy időértéket másodrpercben, és írjuk ki óra:perc:másodperc formátumban! fgv
def idoatalakit():
    ora = ido//3600
    perc = ido%3600//60
    masodperc = ido%60
    return f'{str(ora).zfill(2)}:{str(perc).zfill(2)}:{str(masodperc).zfill(2)}'


ido = int(input('Kérem az időt [másodperc]: '))
print(idoatalakit(ido))