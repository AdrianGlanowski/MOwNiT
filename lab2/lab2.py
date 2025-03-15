#za kazdym razem dostajemy inny uklad rownan
#zerujemy mentalnie, rzadko kiedy zera w tablicy
#mozna wyskalowac, dzielenie przez najwiekszy element
#cond(A) = ||A|| ||A^-1||
#cond(A) = sigma 1/sigma r
#znajduje najwiekszy element jako ten, na którym pracuje
#partial pivoting (czesciowe poszukiwanie elementu wiodącego) - tylko w kolumnie
#full pivoting - calkowite poszukiwanie
#implementacja Gaussa-Jordana - trojkat w druga strone

#fakturyzacja LU
#rozbicie macierzy kwadratowej na maciej trojk gorna i dolna, gdzie na przekatnej sa 1,
#w pozostalych miejscach sa mnożniki użyte w eliminacji
#Ax = b
#rozbic na
#Ux=y oraz Ly=b, ktore sa kwadratowe
#przydaje sie to dla wielu rownan liniowych
#Ax = bi, i=1,2,...
#O(mn^3)
#a tak to faktoryzacja raz czyli O(n^3) + m*O(n^2)
#PA = LU zapamietujemy pivot (?), nie przestawiamy wierszy, tylko pamietamy jakbysmy to zrobili (????)

#do sprawka wszystkie 3 zadania
#dowolny grafmozna interpretowac jako siec opornikow
#k-reg, k-reg zaburzone, siatki2D, siatki 3D, kilkadziesiat do kilkuset pokolorowane stosownie do przeplywu
#miara centralnosci w grafie, jak wazny jest element w grafie pod wzgledem np przejazdow,
#uzyte, zeby na przyklad znalezc zaleznosci, grupy znajomych albo cos
#dwa rozw, oba, zeby miec maks

#to jest ciekawsze algorytmiczne
#1) Prawa Kirchoffa - sum(in) = sum(out)
#dostaniemy w ciul rownan
#wiec trza tez wykorzystac 2 prawo kirchoffa
#uwaga, zeby nie za duzo rownan (Ax=b, ze A jest prostokatna m>>n)
#aprokrymacja sredniokwadratowa, mnozysz lewostronnie przez macierz transponowana
#uklad rownan normalnych skojarzonhych z tym ukladem
#pseudoodwrotnosc mura penrosea
#x = (A^T*A)^-1*A^T*b - w praktyce sie tak nie liczy, robi sie A = QR
#albo analizujemy dokladnie tyle ile trzeba, zeby miec kwadratowy uklad rownan
#wtedy mozna juz nie swoja implementacje

#to jest prostsze i poprawniejsze
#2) Metody potecjalow wezlowych
#zamiast liczyc natezenia jako niewiadome, 
#to liczymy potencjaly z prawa ohma, wiec caly czas macierz kwadratowa
#potem dzielimy przez opor

#wizualizacja, skrypt, wizualizacja przeplywu (pokolorowanie zgodnie z heatmapa, etykieta z wartoscia)
#force layout

#moze to byc jupyter, pod warunkiem, ze uda sie trudne rzeczy tam wygenerowac (ew colab)
#skomentowac co wybrane, dlaczego, zlozonosc, mozna skorzystac z networkx (biblioteka dla grafow)
#cykle proste zaimplementowac najlepiej samemu
#TERMIN: 2 TYGODNIE

import numpy as np
def solve(A: list[list], B: list):
    A = np.array(A)
    np.c_(A, B)
    
    already_satisfied = [] #tablica wierszy, ktore juz zrobilem, nie ruszac wiecej

    for change in range(len(A)):
        
        #znajdz rzad z najw elementem
        max, max_index = 0, 0
        for r in range(len(A)):
            if abs(A[r][change]) > max and r not in already_satisfied:
                max = A[r][change]
                max_index = r

        for r in range(len(A)):
            if r == max_index: continue
            #zmodyfikuj wspolczynniki
            A[r][change:len(A)] #= ta wartosc, na ktora mam zmienic
        
                

