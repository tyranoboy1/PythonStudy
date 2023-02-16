import os
from screen import SelectMenu
from screen import theory
from screen import areap
from screen import dayp

def main():

    while True:
        key = SelectMenu()
        if key == '0':
            break
        elif key == '1':
            theory()
        elif key == '2':
            areap()
        elif key == '3':
            dayp()
        else:
            print("잘못 선택하였습니다.")
        main()
if __name__ == '__main__':
    main()
