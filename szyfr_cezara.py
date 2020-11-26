def szyfr_cezara( klucz, napis ):
    wynik = ""
    for litera in napis:
        kod_litery = ord( litera )
        
        if ord("A") <= kod_litery <= ord("Z"):
            numer_litery = kod_litery - ord("A")
            numer_litery_zaszyfr = ( numer_litery + klucz ) % 26
            kod_litery_zaszyfr = numer_litery_zaszyfr + ord("A")
            litera_zaszyfrowana = chr(kod_litery_zaszyfr)
            wynik += litera_zaszyfrowana
        elif ord("a") <= kod_litery <= ord("z"):
            numer_litery = kod_litery - ord("a")
            numer_litery_zaszyfr = ( numer_litery + klucz ) % 26
            kod_litery_zaszyfr = numer_litery_zaszyfr + ord("a")
            litera_zaszyfrowana = chr(kod_litery_zaszyfr)
            wynik += litera_zaszyfrowana
        else:
            wynik += litera

    
    return wynik

k = int(input("Podaj klucz: "))
n = input("Podaj wiadomość:")
z = szyfr_cezara( k, n )
print(f"Po zaszyfrowaniu: {z}")
