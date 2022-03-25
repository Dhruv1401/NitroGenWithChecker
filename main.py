import requests
import random
import string
import os

print("Made by -")
print("██████╗░██╗░░██╗██████╗░██╗░░░██╗██╗░░░██╗  ░░░░░██╗░█████╗░██████╗░░█████╗░██╗░░░██╗")
print("██╔══██╗██║░░██║██╔══██╗██║░░░██║██║░░░██║  ░░░░░██║██╔══██╗██╔══██╗██╔══██╗██║░░░██║")
print("██║░░██║███████║██████╔╝██║░░░██║╚██╗░██╔╝  ░░░░░██║███████║██║░░██║███████║╚██╗░██╔╝")
print("██║░░██║██╔══██║██╔══██╗██║░░░██║░╚████╔╝░  ██╗░░██║██╔══██║██║░░██║██╔══██║░╚████╔╝░")
print("██████╔╝██║░░██║██║░░██║╚██████╔╝░░╚██╔╝░░  ╚█████╔╝██║░░██║██████╔╝██║░░██║░░╚██╔╝░░")
print("╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░  ░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░")
print("Send Friend Request to Dhruv Jadav#1620")
time.sleep(3)
os.system('clear')

num = int(input('Input How Many Codes to Generate and Check:\n'))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Your nitro codes are being generated, be patient!")

    for i in range(num):
        code = "".join(
            random.choices(string.ascii_uppercase + string.digits +
                           string.ascii_lowercase,
                           k=16))

        file.write(f"https://discord.gift/{code}\n")

    print(
        f"Generated {num} codes\nNow checking if there's any valid nitro code."
    )

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(
                f"\n\n Valid | {nitro}\n\n"
            )  #If the nitro code will be valid, it will print nitro code leaving two lines for focus xD.
        else:
            print(f"*",
                  end="")  #It will print "*" if the nitro code won't be valid.

print(
    "\n\n\nYou have generated codes and checked it succesfuly, hope you got some valid ones"
)
