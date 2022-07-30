import numpy as np
import random
import statistics
from stage_A import stage_A
from stage_B import stage_B
from stage_C import stage_C


def congestion_rate(lay):
    '''
    assume that people spend 8 hours awake at their house,
    and assume that people spend half an hour in the bathroom daily.
    calculate the rate of times there is no free bathroom for user.
    :param lay: our house
    :param family_size:
    :return: rate of occupied bathrooms
    '''
    options = lay.bathroom_num
    family_size = lay.family_size
    problems_vec = np.zeros(1000)
    for j in range(1, 1000):
        problem = 0
        rand_vec = np.zeros(family_size)
        for i in range(1, family_size):
            rand_vec[i] = random.randint(1, 16)
            if np.count_nonzero(rand_vec == rand_vec[i]) > options:
                problem += 1
        problems_vec[j] = problem
    return statistics.mean(problems_vec)




def grade_layout(lay, type):
    num_of_fea = 4
    fea_vec = np.zeros(num_of_fea)
    #first feature - is the layout crowded?
    fea_vec[0] = lay.not_crowded()
    #second feature - size of layout (normalized)
    fea_vec[1] = lay.size/110
    #third feature - accessibility
    fea_vec[2] = lay.is_acc()
    #fourth feature - congestion rate in bathrooms
    fea_vec[3] = 1 - congestion_rate(lay)
    #print(fea_vec)
    print("Quality grade for house " + type + ", for family of " + str(lay.family_size) + ", is " + str(np.linalg.norm(fea_vec).round(2)))



if __name__ == '__main__':
    family_sizes = [2, 3, 4, 5, 6, 7, 8]
    for size in family_sizes:
        hA = stage_A(size, size - 2)
        hB = stage_B(size, size - 2)
        hC = stage_C(size, size - 2)
        grade_layout(hA, 'A')
        grade_layout(hB, 'B')
        grade_layout(hC, 'C')

