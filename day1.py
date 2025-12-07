from utils import file_utils
import os

CURRENT_DIR = os.getcwd()

CURRENT_POINT = 50

def main():
    global CURRENT_POINT
    strs = file_utils.handle_file(os.path.join(CURRENT_DIR, 'input'))
    #strs = ["L50", "R1000"]
    #strs = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    res = 0
    for rotation in strs:
        # if CURRENT_POINT == 0:
        #     res += 1
        if rotation[0] == 'L':
            # CURRENT_POINT -= int(rotation[1:])
            # CURRENT_POINT, steps = modulo(CURRENT_POINT)
            # res += steps
            delta = -int(rotation[1:])
        else:
            # CURRENT_POINT += int(rotation[1:])
            # CURRENT_POINT, steps = modulo(CURRENT_POINT)
            # res += steps
            delta = int(rotation[1:])
        CURRENT_POINT, hits = modulo(CURRENT_POINT, delta)
        res += hits
    print(res)

def modulo(start: int, delta: int) -> tuple[int, int]:
    # if num < 100 and num >= 0:
    #     return num, iters
    # if num >= 100:
    #     return modulo(num - 100, iters + 1)
    # elif num < 0:
    #     return modulo(num + 100, iters + 1)
    # n = num
    # if n >= 0:
    #     hits = n//100
    # else:
    #     hits = (-n + 99)//100
    # final = n%100
    # return final, hits

    final = (start + delta) % 100
    if delta == 0:
        return final, 0
    if delta > 0:
        hits = (start+delta) // 100
        return final, hits
    d = -delta
    if start == 0:
        if d < 100:
            hits = 0
        else:
            hits = 1 + (d-100) // 100
    else:
        if d < start:
            hits = 0
        else:
            hits = 1 + (d-start) // 100
    return final, hits


if __name__ == "__main__":
    main()