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

def davky1(dose:float) -> float: #zadávám obvyklou dávku v mg/kg a název léku
    """Fce pro léky s danou dávkou na kg"""
    davka=round(dose*hp, ndigits=2)
    return davka
    
def davky2(min, max) -> tuple: #zadávám min a max dávku v mg/kg a název léku
    """Fce pro léky s min. a max. dávkou na kg"""
    min_dose=round(min*hp, ndigits=2)
    max_dose=round(max*hp, ndigits=2)
    return (min_dose, max_dose)

def topcap(dose, tc, lek): #zadavam davku v mg/kg, max. kg pac (vetne) a nazev leku
    """Fce pro léky s hmotnostním omezením"""
    if hp <= tc:
        print(f"{lek} v dávce {round(dose*hp, ndigits=2)}mg.")
    else:
        print(f"Na {lek} je už moc velkej (do {tc}kg).")

def maxdose(dose, md, lek): #zadavam davku mg/kg, max advku v mg a nazev leku
    """Fce pro léky s maximální dávkou"""
    davka=round(hp*dose, ndigits=2)
    if davka <= md:
        print(f"{lek} v dávce {davka} mg.")
    else:
        print(f"{lek} v dávce {md} mg. (maximální dávka, jinak by měl dostat {davka})")
    
def infuze(): #spocita bazál a rychlost za hodinu
    if hp<=10:
        basal=round(hp*100,ndigits=1)
    elif hp<=20:
        basal=round(1000+(hp-10)*50, ndigits=1)
    else:
        basal=round((hp-20)*20+1500, ndigits=1)
    print(f"Denní potřeba tekutin = {basal}ml. \ntzn. rychlost infuze ~ {round(basal/24, ndigits=1)} ml/h.")

    
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
    print(f"Paracetamol == {davky2(10,15)}")
    

if __name__ == "__main__":
    main()