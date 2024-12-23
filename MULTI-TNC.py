import os
import random
import time
import string
import subprocess

# Define Clearing Terminal
def clear():
    os.system('cls')
clear()

# ASCII - Gen
def ascii():
    print("""
___  ___        _  _    _          _____  _   _  _____ 
|  \/  |       | || |  (_)        |_   _|| \ | |/  __ |
| .  . | _   _ | || |_  _  ______   | |  |  \| || /  \|
| |\/| || | | || || __|| ||______|  | |  | . ` || |    
| |  | || |_| || || |_ | |          | |  | |\  || \__/|
\_|  |_/ \__,_||_| \__||_|          \_/  \_| \_/ \____|


    """)

while True:

    clear()
    ascii()

    userInput = input("Please select a tool to use:\n 1: Random Number Generator\n 2: Temp Cleaner\n 3: Secure Password Generator \n YT: Opens Youtube \n TV: Opens Twitch.tv \n GS: Google Search \n ")

    if userInput == '1':

        finalDigit = ''
        clear()

        numgenInput = input("How many digits is the random number?\n")

        if numgenInput == '':

            print("You didn't input a number.")

        else:

          for generator in range(int(numgenInput)):
            digit = str(random.randint(0,9))
            finalDigit += digit

          print(finalDigit)
          time.sleep(3)



    #####################################################
    elif userInput == '2':
        clear()
        print("Deleting temporary files...")
        with open(os.devnull, 'w') as devnull:
            os.system('del /q %temp%\\*.* > NUL 2>&1')
            os.system('for /d %i in ("%temp%\\*") do rd /s /q "%i" > NUL 2>&1')
        clear()
        print("Temporary files deleted.")
        time.sleep(2)
    #####################################################
    #####################################################
    elif userInput == '3':
        passUser = input('What is the username for this service?\n\n')
        passName = input('What is this password for?\n\n')
        finalPass = ''
        for password in range(32):
            char = random.choice(string.ascii_letters)
            finalPass += char

        if passName == '':
            input("You didn't enter a password name! Press enter to restart")
        else:
            passcmd = subprocess.run(['dir'], shell=True, capture_output=True, text=True)
            folderCheck = passcmd.stdout

            if 'passwords' not in folderCheck:
                os.system('mkdir passwords')
                if ' ' in passName:
                    newPassName = str.replace(passName, ' ', '_')
                    finalPass = f'Username: {passUser}  Password: {finalPass}'
                    os.system(f'cd passwords && echo {finalPass} > {newPassName}.txt')
                    print(
                        f'Your information for {passName} is {finalPass}\nIt has been saved to a txt file named {passName}')
                    time.sleep(5)
                else:
                    finalPass = f'Username: {passUser}  Password: {finalPass}'
                    os.system(f'cd passwords && echo {finalPass} > {passName}.txt')
                    print(
                        f'Your information for {passName} is {finalPass}\nIt has been saved to a txt file named {passName}')
                    time.sleep(5)
            else:
                if ' ' in passName:
                    newPassName = str.replace(passName, ' ', '_')
                    finalPass = f'Username: {passUser}  Password: {finalPass}'
                    os.system(f'cd passwords && echo {finalPass} > {newPassName}.txt')
                    print(
                        f'Your information for {passName} is {finalPass}\nIt has been saved to a txt file named {passName}')
                    time.sleep(5)
                else:
                 finalPass = f'Username: {passUser}  Password: {finalPass}'
                 os.system(f'cd passwords && echo {finalPass} > {passName}.txt')
                 print(
                    f'Your information for {passName} is {finalPass}\nIt has been saved to a txt file named {passName}')
                 time.sleep(5)









    #####################################################
    #####################################################
    elif userInput.lower() == 'yt':
        clear()
        print("Opening YouTube...")
        os.system('start https://youtube.com')
        clear()
        print("Opened YouTube.")
        time.sleep(2)
    #####################################################
    #####################################################
    elif userInput.lower() == 'tv':
        clear()
        print("Opening Twitch...")
        os.system('start https://twitch.tv')
        clear()
        print("Opened Twitch.")
        time.sleep(2 )
    #####################################################
    #####################################################
    elif userInput.lower() == 'gs':
        clear()
        gsUserInput = input('What would you like to search?: ')
        clear()
        print("Searching...")
        os.system('start https://google.com/search?q=' + gsUserInput)