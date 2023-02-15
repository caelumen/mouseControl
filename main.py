import pyautogui
import time
import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument("-i","--interval", dest="interval", default=10)
parser.add_argument("-N","--N", dest="N", default=100)
parser.add_argument("-sx","--start_x", dest="sx", default=300)
parser.add_argument("-sy","--start_y", dest="sy", default=300)
parser.add_argument("-ex","--end_x", dest="ex", default=800)
parser.add_argument("-ey","--end_y", dest="ey", default=800)
args = parser.parse_args()

# start_x, start_y = 300, 300
# end_x, end_y = 800, 800
# interval = 100
# N = 10

start_x, start_y = args.sx, args.sy
end_x, end_y = args.ex, args.ey
interval, N = args.interval, args.N

print(f' - interval : {interval}, Loop N: {N}')
print(f' - start_x : {start_x}, start_y : {start_y}, end_x : {end_x}, end_y : {end_y}')


def doMouseAction(sx=400, sy=400, ex=400, ey=400, inter=10, button='left'):
    pyautogui.moveTo(x=sx,y=sy)
    time.sleep(inter)
    pyautogui.click(x=ex,y=ey, button=button)
    time.sleep(inter)
    pyautogui.scroll(-100)
    time.sleep(inter)
    pyautogui.scroll(100)
    

def main():
    print(' # Starting Controll mouse action #')
    for i in range(N):
        if i % 10 ==0:
            print('')
            print(f' {i} ', end="->")
        else:
            print(f' {i} ', end="->")
        doMouseAction()
        sys.stdout.flush()
        time.sleep(1)
    print('Finished')
    
    return 1



if __name__ == '__main__':
    main()