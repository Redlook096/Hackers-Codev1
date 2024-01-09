import random
import os
import time
money = "0"
str(money)
alarms = "on"
savings = "0"
ls = "While hacking, you have no personal directory"
name = input("Enter name: ")
pwd = "/home/" + name
home = "/home/" + name
ls = "While hacking, you have no personal directory"

while True:
    command = input(name + "@Laptop-0984P1KH:~$ ")

    if command == "pwd":
        print(pwd)

    elif command == "pingser":
        device1 = f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}"
        device2 = f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}"
        device3 = f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}"
        device4 = f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}"
        print(device1)
        print(device2)
        print(device3)
        print(device4)

    elif command == "v/mnt/":
        mnt = input("Enter IP address to mount: ")
        if any(device in mnt for device in [device1, device2, device3, device4]):
            pwd = "/home/" + name + "/" + mnt
            print("Virtual mount successful")
            alarms = "on"
            ls = "Desktop  Documents  Downloads"
        elif mnt == "":
            print("IP not found")
        else:
            print("IP not found")
    elif command == "ls":
	    print(ls)
    elif command == "cd Downloads" and ls == "Desktop  Documents  Downloads":
                pwd = "/home/" + name + "/" + mnt + "/Downloads"
                ls = "get_bank_account.sh  silence_alarms.sh"
    elif command == "./silence_alarms.sh" and ls == "get_bank_account.sh  silence_alarms.sh":
                alarms = "off"
                print("Alarms silenced")
    elif command == "./get_bank_account.sh" and ls == "get_bank_account.sh  silence_alarms.sh":
                if alarms == "off":
                        print("Running get_bank_account.sh...")
                        time.sleep(0.2)
                        print("Downloading files...")
                        time.sleep(1)
                        print("Unpacking files...")
                        time.sleep(0.1)
                        print("Unpacking data_scan.sh...")
                        time.sleep(0.1)
                        print("Unpacking bank_data...")
                        time.sleep(0.1)
                        print("Unpacking data_transfer.sh...")
                        time.sleep(0.1)
                        print("Unpacking auto_authentication.sh...")
                        time.sleep(0.1)
                        print("Connecting to bank network...")
                        time.sleep(0.3)
                        print("Connection sucsessfull")
                        time.sleep(0.1)
                        print("Running auto_authentication.sh...")
                        time.sleep(0.1)
                        print("Log in sucsessfull")
                        time.sleep(0.1)
                        print("Running data_scan.sh...")
                        time.sleep(0.1)
                        float(savings)
                        savings = random.randint(1,25)
                        savings = savings * 10
                        str(savings)
                        time.sleep(0.1)
                        print("Account Savings: $" + str(savings))
                        time.sleep(4)
                        print("Transfering money to your account...")
                        float(savings)
                        time.sleep(1)
                        savings = float(savings)
                        money = float(money)
                        money = money + savings
                        print("Transaction sucsessfull")
                        time.sleep(0.1)
                        print("Dismounting IP...")
                        time.sleep(0.1)
                        print("Mount disconnected")
                        ls = "While hacking, you have no personal directory"
                        pwd = "/home/" + name
                        str(money)
                elif alarms == "on":
                      print("Running get_bank_account.sh...")
                      time.sleep(0.1)
                      print("Alarm triggered")
                      time.sleep(0.1)
                      print("Disconnecitng mount...")
                      time.sleep(0.1)
                      print("Mount disconnected")
                      ls = "While hacking, you have no personal directory"
                      pwd = "/home/" + name
                      str(money)
    elif command == "cd Desktop" and ls == "Desktop  Documents  Downloads":
        print("Directory acsess denied")
    elif command == "cd Documents" and ls == "Desktop  Documents  Downloads":
        print("Directory acsess denied")
    elif command == "$money" and ls == "While hacking, you have no personal directory":
        str(money)
        print("Balance: $" + str(money))
    elif command == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif command == "exit" :
        print("Thankyou for playing hackers code")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Game ended")
        exit()
    else:
        print("Command not found")
