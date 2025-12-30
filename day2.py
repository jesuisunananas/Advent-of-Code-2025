from utils import file_utils
import os

CURRENT_DIR = os.getcwd()

def construct_ranges(f):
    # ["36-56, 25-35"] -> input
    # [[36, 56], [25, 35]] -> output
    a = f[0].split(',')
    # ["36-56", "25-35"]
    return [i.split('-') for i in a]
    # [['36','56'], ['25', '35']]
    #return [[int(j) for j in i] for i in b]

def main():
    ctr_invalid_id = 0
    res = construct_ranges(file_utils.handle_file(os.path.join(CURRENT_DIR, 'input_2')))
    for i in res:
        for j in range(int(i[0]), int(i[1]) + 1):
            if j // 2 != 0:
                continue
            k = str(j)
            c = len(k)
            start, mid = 0, int(c/2)-1
            check = True
            while mid != c-1:
                if k[start] != k[mid]:
                    check = False
                start += 1
                mid += 1
            if check:
                ctr_invalid_id += 1
    print(ctr_invalid_id)

if __name__ == "__main__":
    main()