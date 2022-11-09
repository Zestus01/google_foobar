src = int(input('Src:'))
dest = int(input('dest'))

def solution(src, dest):
    #Your code here
    # distance = abs(dest - src)
    num_moves = 0
    splinter = src
    moves = [-17, -15, -10, -6, 6, 10, 15, 17]
    while(src != dest):
        num_moves += 1
        for move in moves:
            if((src + move) == dest):
                src = src + move
                break
            elif()
    return num_moves


print(str(solution(src, dest)))