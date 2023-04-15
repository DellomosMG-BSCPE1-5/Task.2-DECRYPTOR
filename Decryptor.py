while True:
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
    chars_substitute = {"*": "a", "&": "e", "#": "i", "+": "o", "!":"u"}
    decrypted_txt = ""
    for letter in user_input:
        if letter in chars_substitute:
            decrypted_txt += chars_substitute[letter]
        else:
            decrypted_txt += letter

    #Processing the Output/Loading
    from rich.console import Console
    from rich.progress import track
    from time import sleep
    print("\n")
    def process_data():
        sleep(0.02)
    for _ in track(range(100), description='[yellow]Processing data'):
        process_data()

    #Display the decrypted text to the user
    print("\n")
    print(Fore.MAGENTA + "=" * 105)
    console = Console()
    console.print("[bold magenta]Here is the decrypted format of your input[/bold magenta]:", decrypted_txt)
    print(Fore.MAGENTA + "=" * 105)

    #Ask the user if he/she wants to try again the program.
    check = input(Fore.YELLOW + "\nDo you want to start again? enter Y to restart or press another key to end: ")
    if check.upper() == "Y":
        continue
    break