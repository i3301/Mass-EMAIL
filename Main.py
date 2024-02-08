#Put Google App Password in AppPass.txt
#Then put list of target emails in Emails.txt
#Now run Start.bat
import smtplib
from colorama import Fore

def print_banner():
    try:
        with open("banner.txt", 'r', encoding='utf-8') as file:
            banner_content = file.read()
            print(f"{banner_content}")
    except FileNotFoundError:
        print(f"Error: File 'banner.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print_banner()
    
#Variables
List = "Emails.txt"
AppPassFile = "AppPass.txt"

#Inputs
Email = input(f"{Fore.CYAN}[*]Sender Email: ")
subject = input(f"{Fore.CYAN}[*]SUBJECT: ")
message = input(f"{Fore.CYAN}[*]MESSAGE: ")

text = f"Subject: {subject}\n\n{message}"

#Reads Target List
with open(List) as file:
    Target_List = [line.strip() for line in file.readlines()]

#Reads AppPassFile
with open(AppPassFile) as file:
    AppPass = file.readline().strip()

#Defines Send Function
def sendEmail():
    print(f"{Fore.CYAN}[+]Sending Emails. . .")

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(Email, AppPass)

    server.sendmail(Email, Target_List, text)

    print(f"{Fore.GREEN}[*]Emails Sent With Message",{message})
    input(f"{Fore.CYAN}[!]Press Enter To Exit. . .")

#Calling The Function
if __name__ == "__main__":
    sendEmail()
