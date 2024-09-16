def zadavacka(pozadavek): #požaduje nenulové číslo
    while True:
        try:
            zadek = float(input(f"Jaká je {pozadavek}? \n").strip().lower().replace(",","."))
            if 200 > zadek > 0:
                return zadek
            else:
                print("Zadej prosím normální číslo!!! (0-200kg)")
        except ValueError:
            print("Zadej prosím číslo!!!")

hp = zadavacka("hmotnost pacienta") #hmotnost pacienta jako globální proměnná (aka špinavá cesta)

def davky1(dose:float, lek:str): #zadávám obvyklou dávku v mg/kg a název léku
    """Fce pro léky s danou dávkou na kg"""
    davka=round(dose*hp, ndigits=2)
    print(f"{lek} v dávce {davka} mg.")
    
def davky2(min, max, lek): #zadávám min a max dávku v mg/kg a název léku
    """Fce pro léky s min. a max. dávkou na kg"""
    min_dose=round(min*hp, ndigits=2)
    max_dose=round(max*hp, ndigits=2)
    print(f"{lek} == od {min_dose} mg do {max_dose} mg.")

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
    infuze()
    
    nadpis("Analgezie")
    davky2(10,15,"Paracetamol")
    davky2(10,15,"Novalgin")
    davky2(5,10,"Ibuprofen")
    davky2(0.1, 0.2, "Nalbufin po 3 - 6 hod")
    
    nadpis("Tlumení")
    davky1(0.1, "Midazolam")
    topcap(1, 12.5, "Chloralhydrát")
    
    nadpis("ATBs")
    """Rozhodovací špinavej if pro Amoksiklav"""
    if hp < 40:
        davky1(30, "Amoksiklav á 8h")
        davky1(90, "Amoksiklav celkem za 24h")
    else:
        print("Amoksiklav á 8h == 1.2 g")

    """Ampicilin/sulbaktam rozhodovací strom"""
    if hp < 60:
        davky2(33,50, "Ampicillin/sulbaktam á 8h")
    else:
        print("Ampicillin/Sulbaktam á 8h == 3g  (maximální dávka)")

    """Genťák strom"""
    if hp <= 40:
        davky1(5, "Gentamicin á 24h")
    else:
        print("Gentamicin á 24h == 320mg (maximální dávka)")
    print("     ->kape 30min (ve 20-30ml F1/1)")

    """Klindamycin strom"""
    davky2(7.5,12.5, "Klindamycin á 6h")
    davky2(10,16.66666666666, "Klindamycin á 8h")
    print("     ->preferováno po 6h\n      ->ředění v F1/1, ne víc než 6mg ATB v ml")

    """Metronidazol strom"""
    if hp < 50:
        davky2(6.6666666, 10, "Metronidazol á 8h")
    else:
        print("Metronidazol á 8h == 500mg (od 50kg jednotná dávka)")
    print("     ->kape 60min")

    """Tazocin strom"""
    if hp < 50:
        davky2(50, 75, "Tazocin á 6h")
        davky2(66.666666, 100, "Tazocin á 8h")
    else:
        print("Tazocin á 8h == 4.5g (od 50kg jednotná dávka)")
    print("     ->kape 30min")

if __name__ == "__main__":
    main()