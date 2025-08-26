import requests
import sys
import os
import time
from colorama import Fore, Style, init

init()

def print_banner():
    banner = f"""
{Fore.CYAN}
    ███████╗██╗   ██╗███████╗███████╗███████╗██████╗ 
    ██╔════╝██║   ██║╚══███╔╝╚══███╔╝╚══███╔╝██╔══██╗
    █████╗  ██║   ██║  ███╔╝   ███╔╝   ███╔╝ ██████╔╝
    ██╔══╝  ██║   ██║ ███╔╝   ███╔╝   ███╔╝  ██╔══██╗
    ██║     ╚██████╔╝███████╗███████╗███████╗██║  ██║
    ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
{Style.RESET_ALL}
            API Endpoint Fuzzer by 0xm45kf4c3.xp
{Fore.YELLOW}==========================================================={Style.RESET_ALL}
"""
    print(banner)

def fuzz():
    print_banner()
    url = input(f"{Fore.GREEN}[?]{Style.RESET_ALL} Enter target URL: ").rstrip('/')
    try:
        delay = float(input(f"{Fore.GREEN}[?]{Style.RESET_ALL} Delay between requests (seconds): "))
    except ValueError:
        print(f"{Fore.YELLOW}[!]{Style.RESET_ALL} Invalid delay. Using default of 1 second.")
        delay = 1.0
    wordlist_file = "wordlist.txt"
    if not os.path.isfile(wordlist_file):
        print(f"{Fore.RED}[!]{Style.RESET_ALL} Error: Wordlist file '{wordlist_file}' not found in current directory")
        sys.exit(1)
    with open(wordlist_file, 'r') as f:
        total_words = sum(1 for line in f)
    print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Loaded {total_words} words from {wordlist_file}")
    print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Starting fuzzing against: {url}")
    print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Only showing successful responses (status codes 200-399)")
    print(f"{Fore.YELLOW}==========================================================={Style.RESET_ALL}")
    found_count = 0
    with open(wordlist_file, 'r') as f:
        current_word = 0
        for word in f:
            current_word += 1
            word = word.strip()
            if not word:
                continue
            target_url = f"{url}{word}"
            progress = (current_word / total_words) * 100
            print(f"{Fore.CYAN}[{current_word}/{total_words} - {progress:.1f}%]{Style.RESET_ALL} Testing: {target_url}", end="\r")
            try:
                r = requests.get(target_url)
                if 200 <= r.status_code < 400:
                    found_count += 1
                    print(f"\n{Fore.GREEN}[FOUND]{Style.RESET_ALL} {target_url} {Fore.GREEN}(Status: {r.status_code}){Style.RESET_ALL}")
                    try:
                        data = r.json()
                        print(f"{Fore.GREEN}[DATA]{Style.RESET_ALL} {data}")
                    except ValueError:
                        print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Non-JSON response")
                    print(f"{Fore.YELLOW}---------------------------------------------{Style.RESET_ALL}")
            except requests.exceptions.RequestException as e:
                print(f"\n{Fore.RED}[ERROR]{Style.RESET_ALL} {target_url}: {e}")
            time.sleep(delay)
    print(f"\n{Fore.GREEN}[+]{Style.RESET_ALL} Fuzzing completed! Found {found_count} valid endpoints.")
    print(f"{Fore.YELLOW}==========================================================={Style.RESET_ALL}")

fuzz()
