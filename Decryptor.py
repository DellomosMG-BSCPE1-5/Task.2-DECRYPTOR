#Title
import pyfiglet
from colorama import Fore, Back, Style
print(Fore.YELLOW + pyfiglet.figlet_format(" Decrypt It!", font = "roman", width = 1000))

#Greeting
from pyboxen import boxen
print(
    boxen(
        "This program will help you to convert an encrypted message back to its origial and readable format.",
            title="WELCOME TO DECRYPT IT!",
            title_alignment="center",
            color="bold magenta",
            padding=1,
    )
)

#Ask the user for the encrypted text he/she wants to decrypt
print(Fore.MAGENTA + Style.NORMAL + "Kindly enter the encrypted text that you want to decrypt: ", end = "")
user_input = input(Fore.WHITE + "")

#Decrypt the text by replacing/changing the following characters with their corresponding alphabet
#Processing the Output/Loading
#Display the decrypted text to the user
#Ask the user if he/she wants to try again the program.