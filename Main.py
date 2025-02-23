import os
import sys
import time
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import pyfiglet
from colorama import Fore, Style, init

init(autoreset=True)

def install_packages():
    try:
        import pyfiglet
        import colorama
        import phonenumbers
    except ImportError:
        print("[+] Installing required packages...")
        os.system(f"{sys.executable} -m pip install pyfiglet colorama phonenumbers")
        os.execv(sys.executable, [sys.executable] + sys.argv)

install_packages()

def setup_theme():
    os.system("cls" if os.name == "nt" else "clear")
    os.system("color 6")
    banner = pyfiglet.figlet_format("Phone Lookup")
    print(Fore.YELLOW + banner)
    print(Fore.YELLOW + "=" * 60)
    print(Fore.WHITE + " [+] Made by Flames | Phone Lookup Tool")
    print(Fore.YELLOW + "=" * 60)

def lookup_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        
        if phonenumbers.is_valid_number(parsed_number):
            print(Fore.YELLOW + "[+] Valid Phone Number!")
            print(Fore.WHITE + f" [+] Country: {geocoder.description_for_number(parsed_number, 'en')}")
            print(Fore.WHITE + f" [+] Carrier: {carrier.name_for_number(parsed_number, 'en')}")
            print(Fore.WHITE + f" [+] Time Zone: {timezone.time_zones_for_number(parsed_number)}")
            print(Fore.WHITE + f" [+] International Format: {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
            print(Fore.WHITE + f" [+] National Format: {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)}")
            print(Fore.WHITE + f" [+] E.164 Format: {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
            print(Fore.WHITE + f" [+] Possible Number: {phonenumbers.is_possible_number(parsed_number)}")
            print(Fore.WHITE + f" [+] Country Code: {parsed_number.country_code}")
            print(Fore.WHITE + f" [+] National Number: {parsed_number.national_number}")
            print(Fore.WHITE + f" [+] Region Code: {phonenumbers.region_code_for_number(parsed_number)}")
        else:
            print(Fore.RED + "[-] Invalid Phone Number!")
    
    except phonenumbers.phonenumberutil.NumberParseException:
        print(Fore.RED + "[!] Invalid format. Make sure to include country code (e.g., +1234567890).")

def main():
    while True:
        setup_theme()
        try:
            print(Fore.WHITE + "Enter the phone number (with country code, e.g., +1234567890):")
            print(Fore.YELLOW + "=" * 60)
            phone_number = input(Fore.WHITE + "--> ")
            
            if phone_number.strip() == "":
                print(Fore.RED + "[!] Please enter a valid phone number.")
                time.sleep(1)
                continue
            
            lookup_phone_number(phone_number)
            input(Fore.WHITE + "\nPress Enter to return to the main menu...")
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n[!] Exiting...")
            break

if __name__ == "__main__":
    main()
