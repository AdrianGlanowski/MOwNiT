import numpy as np
def solve(A: list[list], B: list):
    A = np.array(A).astype(float)
    np.c_[A, B]
    
    already_satisfied = [] #tablica wierszy, ktore juz zrobilem, nie ruszac wiecej

    for change in range(len(A)):
        
        #znajdz rzad z najw elementem
        maxi, max_index = 0, 0
        for r in range(len(A)):
            if abs(A[r][change]) > maxi and r not in already_satisfied:
                maxi = A[r][change]
                max_index = r
        already_satisfied.append(max_index)

        for r in range(len(A)):
            if r == max_index: continue
            #zmodyfikuj wspolczynniki
            A[r] -=  (A[r][0]/maxi)*A[max_index] #= ta wartosc, na ktora mam zmienic
        A[max_index] /= maxi
    
    return A
                
print(solve([[2, 2, -1, 1],[-1, 1, 2, 3],[3, -1, 4, -1],[1, 4, -2, 2]], [7, 3, 31, 2]))
