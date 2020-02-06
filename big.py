import random
import time

all = []
last = []

for i in range(1, 50):
    all.append(i)


def one():
    print('這是一個樂透機器')
    while True:
        all = []
        last = []
        n = 0
        for i in range(1, 50):
            all.append(i)
        ch = input('要刪除數字嗎(Y/N):')
        if ch == 'y' or ch == 'Y':
            print('如果不要繼續，請直接按Enter')
            time.sleep(1)
            try:
                del_num = eval(input('您要刪除什麼數字(用逗號隔開):'))
                for d2 in del_num:
                    d2 -= 1
                    del all[d2 - n]
                    n += 1
                ct = 6
                while True:
                    last_num = random.choice(all)
                    ct -= 1
                    last.append(last_num)
                    if ct == 0:
                        print("今年的樂透是: {}".format(last))
                        break
            except:
                print("您輸入的格式是錯的")
                time.sleep(1)
                print("請仔細檢查!")
                time.sleep(1)
        else:
            ct = 6
            while True:
                last_num = random.choice(all)
                ct -= 1
                last.append(last_num)
                if ct == 0:
                    print("今年的樂透是: {}".format(last))
                    break
        print('是否在一次:')
        print('1. 是 2. 否')
        q = input('')
        if q == '2':
            break


one()
