import random
import time
#import colorama
import tkinter as tk
#from colorama import Fore,Back,Style
#colorama.init(autoreset=True)
#Calculator , user , result , program#

one = 1
Text = ""

#time.sleep(0.2)

#random_num = random.randint(1,100) + one
#random_num2 = random.randint(1,100) + one

#print("MAHT PROBLEM:",random_num,"+",random_num2)
#time.sleep(0.6)

#User_INPUT = int(input("USER INPUT:"))


#result = random_num+random_num2

#if User_INPUT == result:
 #   print(Fore.GREEN+"TRUE")
 #   time.sleep(0.2)
 #   print(Fore.LIGHTGREEN_EX+str(User_INPUT))
#else:
 #   print(Fore.RED+"FALSE")
#    print(Fore.GREEN+str(result))
#print("PROGRAM NAME: MATH PROBLEM")

def Calculator():
    Start = input("PRESS ENTER TO START:")
    time.sleep(0.6)
    print("...")
    time.sleep(1)
    co = 0
    if Start == Start:

        big_num = [10,100,1000]
        random_3 = random.randint(0,2)

        random_big_num = big_num[random_3]

        random_num = random.randint(1,random_big_num) + one
        random_num2 = random.randint(1,random_big_num) + one

        print("MATH PROBLEM:",random_num,"+",random_num2)
        time.sleep(0.6)
        # User input#

        User_INPUT = int(input("USER INPUT:"))
        co+=1

        result = random_num+random_num2

        if User_INPUT == result:
            print("...")
            print("TRUE")

            root_2 = tk.Tk()

            etwas = tk.Label(root_2, text="True")

            root_2.mainloop()

            time.sleep(0.2)
            print(str(User_INPUT))

        else:
            print("...")
            print("FALSE:")
            print(str(str(User_INPUT)))
            root_1 = tk.Tk()
            etwas = tk.Label(root_1,text="False")
            root_1.mainloop()
            print("")
            wow = random_num, "+", random_num2, "=", result
            print(random_num, "+", random_num2, "=", result)
        print("")
        print("NEXT PROBLEM")


start = input("start:")
while True:
    Calculator()




