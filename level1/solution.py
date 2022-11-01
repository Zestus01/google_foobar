import math

area = input('Area: ')

def solution(area, passed_list = []):
    ans_list = passed_list
    area = int(area)
    square = area
    sq_root = (math.sqrt(square))
    sq_root_check = sq_root - int(sq_root)
    while(square <= 3 and square != 0):
        ans_list.append(1)
        square -= 1
    if(square == 0):
        return ans_list
    while(sq_root_check > 0):
        square -= 1
        sq_root = (math.sqrt(square))
        sq_root_check = sq_root - int(sq_root)
    area -= int(sq_root * sq_root)
    sq_root = int(sq_root * sq_root)
    ans_list.append(sq_root)
    return solution(area, ans_list)

print(solution(area))