def TSP(points, T0=1, B=0.98, big_swich = True, eps = 1e-36):
    if T0 < 0 or B < 0:
        raise ValueError

    def distance(point1, point2):
        return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    
    def total_path(points):
        sum_path = 0
        for i in range(n):
            sum_path += distance(points[i], points[(i-1)%n])
        
        return sum_path

    def temperature(T0, B, k):
        temp = T0*B**k
        return temp if temp > 0 else 0

    n = len(points)
    best_path = points
    values = []
    args = []
    probs = []
    prob_args = []

    sum_path = total_path(points)
    args.append(0)
    values.append(sum_path)
    best_pair = [0, sum_path]
    worse_cnt = 0
    k = 0

    while True:
        if big_swich:
            index1 = np.random.randint(0, n)
            index2 = np.random.randint(0, n)
            while index1 == index2:
                index1 = np.random.randint(0, n)
                index2 = np.random.randint(0, n)
            points[[index1, index2]] = points[[index2, index1]]
            
        else:
            index = np.random.randint(1, n)
            points[[index-1, index]] = points[[index, index-1]]
        
        new_sum_path = total_path(points)
        
        if new_sum_path < sum_path:
            args.append(k)
            values.append(new_sum_path)
            if new_sum_path < best_pair[1]:
                best_pair = [k, new_sum_path]
            sum_path = new_sum_path
            best_path = copy(points)
            worse_cnt = 0
        else:
            chance = np.random.uniform(0, 1)
            temp = temperature(T0, B, k)
            probs.append(temp/T0)
            prob_args.append(k)
            if chance > temp/T0:
                if big_swich:
                    points[[index1, index2]] = points[[index2, index1]]
                else:
                    points[[index-1, index]] = points[[index, index-1]]
                if temp < eps:
                    worse_cnt += 1
                    if worse_cnt == int(n/3):
                        break
            else:
                args.append(k)
                values.append(new_sum_path)
                sum_path = new_sum_path
        k += 1
    return args, values, prob_args, probs, best_pair, best_path