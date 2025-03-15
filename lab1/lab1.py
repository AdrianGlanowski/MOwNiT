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

different_way_of_summing(0.377832)

def ex_3_dzeta_Riemanna(s: float, n: int):
    pass
