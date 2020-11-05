from time import sleep

import os
import pyautogui
from keyboard import press


def end():  # Exit function with a message
    print('\nprogram has ended')
    exit(0)


def main():  # main function
    os.system('cls')
    print("DELLHOAK")

    spam = input("Enter your message:\n-> ")  # Gets the input from the user and stores it as the spam text
    num = input(
        "\nEnter the spam amount):\n-> ")  # sets number of time to spam
    if num == "":  # if num is blank sets num to 999999.
        num = 999999

    print('\nThe spam will begin in 10 seconds... BRACE YOURSELF !!!\n')
    print("Return to this window and press 'ctrl/cmd + c' to stop the spam anytime\n\n")
    sleep(10)

    for _ in range(int(num)):
        sleep(0.3)  # stop the spam for 0.3 seconds every loop
        pyautogui.typewrite(spam)  # types the spam text in the input box
        press('enter')  # hits enter

    end()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Stopping the script')
        end()
