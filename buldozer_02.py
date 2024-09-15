def zadavacka(pozadavek): #požaduje nenulové číslo
    while True:
        try:
            zadek = float(input(f"Jaká je {pozadavek} pacienta? \n").strip().lower().replace(",","."))
            if 200 > zadek > 0:
                return zadek
            else:
                print("Zadej prosím normální číslo!!! (0-200kg)")
        except ValueError:
            print("Zadej prosím číslo!!!")

hp = zadavacka("hmotnost pacienta") #hmotnost pacienta jako globální proměnná (aka špinavá cesta)

def davky1(dose:float) -> float: #zadávám obvyklou dávku v mg/kg
    """Fce pro léky s danou dávkou na kg"""
    davka=round(dose*hp, ndigits=2)
    return davka
    
def davky2(min, max) -> tuple: #zadávám min a max dávku v mg/kg
    """Fce pro léky s min. a max. dávkou na kg"""
    min_dose=round(min*hp, ndigits=2)
    max_dose=round(max*hp, ndigits=2)
    return (min_dose, max_dose)

def topcap(dose, tc): #zadavam davku v mg/kg, max. kg pac (vetne)
    """Fce pro léky s horním hmotnostním omezením, při překročení vrátí false"""
    if hp <= tc:
        return round(dose*hp, ndigits=2)
    else:
        return False

def maxdose(dose, md) -> float: #zadavam davku mg/kg, max davku v mg
    """Fce pro léky s maximální dávkou, při dosažení md vrátí její hodnotu"""
    davka=round(hp*dose, ndigits=2)
    if davka <= md:
        return davka
    else:
        return md
    
def infuze(inf:bool) -> float: #spocita bazál a rychlost za hodinu
    """Při inputu 0 vrátí bazál, při inputu 1 vrátí rychlost infuze za hodinu."""
    if hp<=10:
        basal=round(hp*100,ndigits=1)
    elif hp<=20:
        basal=round(1000+(hp-10)*50, ndigits=1)
    else:
        basal=round((hp-20)*20+1500, ndigits=1)
    
    if inf == 0:
        return basal
    else:
        return round(basal/24, ndigits = 1)

def nadpis(obsah):
    print(f"\n \n------ {obsah} ------")
    
def main():
    nadpis("Infuzní terapie")
    # infuze()
    
    # nadpis("Analgezie")
    # davky2(10,15,"Paracetamol")
    # davky2(10,15,"Novalgin")
    # davky2(5,10,"Ibuprofen")
    # davky2(0.1, 0.2, "Nalbufin po 3 - 6 hod")
    
    # nadpis("Tlumení")
    # davky1(0.1, "Midazolam")
    # topcap(1, 12.5, "Chloralhydrát")
    
    nadpis("ATBs")
    paralen= davky2(10,15)
    print(f"Paracetamol == {paralen[0]} mg - {paralen[1]} mg.")
    

if __name__ == "__main__":
    main()