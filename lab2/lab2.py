import numpy as np
from time import time
def solve(A: list[list], B: list):
    A = np.array(A).astype(float)
    Gauss = np.c_[A, B]
    result = [0]*len(B)
    
    already_satisfied = [] #tablica wierszy, ktore juz zrobilem, nie ruszac wiecej

    for change in range(len(Gauss)):
        
        #znajdz rzad z najw elementem
        maxi, max_index = 0, 0
        for r in range(len(Gauss)):
            if abs(Gauss[r][change]) > maxi and r not in already_satisfied:
                maxi = Gauss[r][change]
                max_index = r
        already_satisfied.append(max_index)

        for r in range(len(Gauss)):
            if r == max_index: continue
            #zmodyfikuj wspolczynniki
            Gauss[r] -=  (Gauss[r][change]/maxi)*Gauss[max_index] #= ta wartosc, na ktora mam zmienic
        Gauss[max_index] /= maxi
    
    for i in range(len(B)):
        result[i] = Gauss[already_satisfied[i]][-1]

    return result
                
def ex_1_test():
    for i in range(10):
        print("TEST ", i, "WIELKOSC: ", 500 + i*50)

        A = np.random.rand(500 + i*50, 500 + i*50)
        B = np.random.rand(500 + i*50, 1)

        start = time()
        solve(A, B)
        end = time()
        print("\tCzas mojej implementacji: ", end - start)
    
        start = time()
        np.linalg.solve(A, B)
        end = time()
        print("\tCzas funkcji biblioteczej: ", end - start)

#ex_1_test()

def LU_factorization(A: list[list]):
    Gauss = np.array(A).astype(float)
    
    for change in range(len(Gauss)):
        for r in range(change+1, len(Gauss)):
            #zmodyfikuj wspolczynniki
            factor = (Gauss[r][change]/Gauss[change][change])
            Gauss[r][change:] -=  factor*Gauss[change][change:] #= ta wartosc, na ktora mam zmienic
            Gauss[r][change] = factor

    L = np.tril(Gauss)
    for i in range(len(L)):
        L[i][i] = 1
    U = np.triu(Gauss)

    return L, U

def ex_2_test():
    tests = ""
    for i in range(10):
        print("TEST ", i, "WIELKOSC: ", 500 + i*50)

        A = np.random.rand(500 + i*50, 500 + i*50)
        L, U = LU_factorization(A)

        if np.linalg.det(A - np.matmul(L, U)) != 0:
            print("Wyznacznik różny od 0: ", np.det(A - np.matmul(L, U)))
            tests = tests + "W"
        else:
            tests = tests + "A"
    return len(tests), tests

print(ex_2_test())