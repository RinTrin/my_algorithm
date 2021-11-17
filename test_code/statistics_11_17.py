import numpy as np
import random
from tqdm import tqdm

def count_non_intesection(k): # k: num of lines
    # initalize
    min_int = 0
    line_list = []

    # define area
    width = 100
    area = np.zeros((width, width))
    
    # get 2 points from defined area
    # make line
    for line in range(k):
        x1 = random.randint(min_int, width-1)
        y1 = random.randint(min_int, width-1)
        x2 = random.randint(min_int, width-1)
        y2 = random.randint(min_int, width-1)
        area[x1][y1] = 255.0
        area[x2][y2] = 255.0
        line_list.append([[x1, y1],[x2, y2]])

    # count intersection
    intersection_lines = count_intersection(line_list)

    return k-intersection_lines

def count_intersection(line_list):
    line_num = len(line_list)
    done = False
    bool_list = [True for i in range(line_num)]
    for line1 in range(line_num):
        if not bool_list[line1]:
            continue
        for line2 in range(line1+1, line_num):
            p1, p2 = line_list[line1]
            p3, p4 = line_list[line2]
            if intersect(p1, p2, p3, p4):
                bool_list[line1] = False
                bool_list[line2] = False
                break
            if True not in bool_list:
                done = True
        if done:
            break
    return sum(bool_list)

def intersect(p1, p2, p3, p4):
    tc1 = (p1[0] - p2[0]) * (p3[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p3[0])
    tc2 = (p1[0] - p2[0]) * (p4[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p4[0])
    td1 = (p3[0] - p4[0]) * (p1[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p1[0])
    td2 = (p3[0] - p4[0]) * (p2[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p2[0])
    return tc1*tc2<0 and td1*td2<0


def main(rep, k):
    repetetion = rep
    lines_list = []
    for i in tqdm(range(repetetion)):
        lines = count_non_intesection(k)
        lines_list.append(lines)
    
    n = len(lines_list)
    expected  = np.mean(lines_list)
    std_error = np.std(lines_list) / np.sqrt(n)

    print(f'M        : {rep}')
    print(f'線分の   : {k}')
    print(f'期待値   : {expected:.05f}')
    print(f'標準誤差 : {std_error:.05f}')
    print('##############################\n')


if __name__ == '__main__':
    main(10**2, 10)
    main(10**4, 10)
    main(10**6, 10)
    main(10**4, 100)
    main(10**4, 1000)
