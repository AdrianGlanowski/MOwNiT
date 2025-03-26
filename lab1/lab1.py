#blad 4-5% to jest mega duzy blad
#jedyne poprawne rozw to algorythm kahana
#diagram bifurkacji
#na za tydzien metoda eliminacji gaussa
import numpy as np
import matplotlib.pyplot as plt
from time import time
def different_way_of_summing(number: float):
    def ex_1_iteration(number: float) -> float:
        size = 10**7
        indices = []
        relative_errors = []

        sum_val = np.float32(0)  # Accumulate error in float32

        start = time()
        for i in range(1, size + 1):
            sum_val += np.float32(number)
            
            if i % 25000 == 0:
                expected_sum = i * number  # Theoretical correct sum
                absolute_error = abs(expected_sum - sum_val)  # How much we are off
                relative_error = absolute_error / expected_sum  # Normalize
                
                indices.append(i)
                relative_errors.append(relative_error)
        
        #Plot the relative error trend
        # plt.figure(figsize=(10, 5))
        # plt.plot(indices, relative_errors, label="Relative Error", color='red', linestyle='dashed')
        # plt.xlabel("Iteration")
        # plt.ylabel("Relative Error")
        # plt.title("Accumulated Floating-Point Error in Summation")
        # plt.legend()
        # plt.grid(True)
        # plt.show()
        
        # Final error after the full loop
        final_expected_sum = size * number
        final_absolute_error = abs(final_expected_sum - sum_val)
        final_relative_error = final_absolute_error / final_expected_sum
        end = time()
        return sum_val, final_absolute_error, final_relative_error, end-start

    def ex_1_recursion(number: float) -> float:
        size = 10**7
        array = [np.float32(number)]*size
        def recursive_sum(arr):
            if len(arr) == 1:
                return arr[0]

            mid = len(arr) // 2
            left_sum = recursive_sum(arr[:mid])
            right_sum = recursive_sum(arr[mid:])

            return left_sum + right_sum
        start = time()
        sum = recursive_sum(array)
        end = time()
        return sum, size*number - sum, (size*number - sum)/size*number, end - start


    def ex_2_Kahan(number: float) -> float:
        size = 10**7
        array = [np.float32(number)]*size
        sum = np.float32(0)
        err = np.float32(0)
        start = time()
        for i in range(size):
            y = np.float32(array[i] - err)
            temp = np.float32(sum + y)
            err = (temp - sum) - y
            sum = temp
        end = time()
        return sum, size*number - sum, (size*number - sum)/size*number, end - start

    #blad wzgledny jest tak duzy ze wzgledu na utrate informacji dodajac duza i mala liczbe
    print("Iteration: ", ex_1_iteration(number))
    print("Recursion: ", ex_1_recursion(number))
    print("Kahan's: ", ex_2_Kahan(number))

#different_way_of_summing(0.377832)

def ex_3():
    args = [2, 3.6667, 5, 7.2, 10]
    n = [50, 100, 200, 500, 1000]

    def dzeta_Riemann_increasing(s, n):
        sum = np.float32(0)
        for i in range(1, n+1):
            sum += np.float32(1/i**s)
        return sum

    def dzeta_Riemann_decreasing(s, n):
        sum = np.float32(0)
        for i in range(n, 0, -1):
            sum += np.float32(1/i**s)
        return sum
    
    def eta_Dirichlet_increasing(s, n): 
        sum = np.float32(0)
        for i in range(1, n+1):
            sum += np.float32((1/i**s) * (-1)**(i-1))
        return sum

    def eta_Dirichlet_decreasing(s, n):
        sum = np.float32(0)
        for i in range(n, 0, -1):
            sum += np.float32((1/i**s) * (-1)**(i-1))
        return sum
    
    for s in args:
        print("s value is ", s, "\n")
        for count in n:
            print("\tn value is ", count, "\n")
            print("\tdzeta_increasing: ", dzeta_Riemann_increasing(s, count))
            print("\tdzeta_decreasing: ", dzeta_Riemann_decreasing(s, count))
            print("\teta_increasing: ", eta_Dirichlet_increasing(s, count))
            print("\teta_decreasing: ", eta_Dirichlet_decreasing(s, count))
            print("\n")

#ex_3()
def population_over_time(x, r, n):
    values = []
    indecies = []
    for i in range(n):
        values.append(x)
        indecies.append(i)
        x = r*x*(1-x)

    return values

def ex_4(x=0.5):
    
    def population_over_rate(x):
        values = []
        indecies = []
        r = 0
        while r < 4:
            values += population_over_time(0.5, r, 50)[-10:]
            indecies += [r]*10
            r += 0.0001

        plt.plot(indecies, values, ",")
        plt.xlabel("Growth Rate (r)")
        plt.ylabel("Population")
        plt.suptitle("Bifurcation Diagram")
        plt.title("Starting population %.2f" %x, fontsize=10)
        plt.show()
        return

    population_over_rate(x)

ex_4(0.5)