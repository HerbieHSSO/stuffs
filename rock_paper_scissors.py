#Rock! Paper! Scissors!

#_version = "2.3"

from os import name as os_name, system as console_command
import random

if os_name == "nt":
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("Rock! Paper! Scissors!")

def clearConsole():
    if os_name == "nt":
        console_command("cls")
    else:
        console_command("clear")

class Main():
    def __init__(self):
        self.score = 0
        self.highscore = 0
        self.hadWon = False
        self.hadLost = False
        self.wasADraw = False
        valid_list = ["1", "2", "3"]

        while True:
            clearConsole()
            print(f"Score:{self.score}\nHighscore:{self.highscore}\n\n[1]Rock\n[2]Paper\n[3]Scissors\n")   
            self.player_input = input(">")
            while self.player_input not in valid_list:
                clearConsole() 
                print(f"Score:{self.score}\nHighscore:{self.highscore}\n\n[1]Rock\n[2]Paper\n[3]Scissors\n")   
                self.player_input = input(">")
                
            self.computer_input = random.choice(valid_list)
                    
            self.compare()
            self.handle_scores()
                
            clearConsole()
            print(f"You: {self.player_display}\nComputer: {self.computer_display}\nResults: {self.results}\nScore: {self.score}\nHighScore: {self.highscore}\n")
            print("Do you want to exit? Type 'yes' or 'y' to exit, Type anything else or Press Enter to continue.")

            console = input(">")

            if console in ["yes", "y"]:
                clearConsole()
                break
            
    def compare(self):
        if self.player_input == "1":
            self.rock()
        elif self.player_input == "2":
            self.paper()
        elif self.player_input == "3":
            self.scissors()
    
    def rock(self):
        #Rock
        if self.computer_input == "1":
            self.player_display = "Rock"
            self.computer_display = "Rock"
            self.results = "Draw"
            self.wasADraw = True
            
        elif self.computer_input == "2":
            self.player_display = "Rock"
            self.computer_display = "Paper"
            self.results = "You Lost"
            self.hadLost = True  
            
        elif self.computer_input == "3":
            self.player_display = "Rock"
            self.computer_display = "Scissors"
            self.results = "You Won"
            self.hadWon = True
            
    def paper(self):
        #Paper
        if self.computer_input == "1":
            self.player_display = "Paper"
            self.computer_display = "Rock"
            self.results = "You Won"
            self.hadWon = True
            
        elif self.computer_input == "2":
            self.player_display = "Paper"
            self.computer_display = "Paper"
            self.results = "Draw"
            self.wasADraw = True
            
        elif self.computer_input == "3":
            self.player_display = "Paper"
            self.computer_display = "Scissors"
            self.results = "You Lost"
            self.hadLost = True

    def scissors(self):
        #Scissors
        if self.computer_input == "1":
            self.player_display = "Scissors"
            self.computer_display = "Rock"
            self.results = "You Lost"
            self.hadLost = True
            
        elif self.computer_input == "2":
            self.player_display = "Scissors"
            self.computer_display = "Paper"
            self.results = "You Won"
            self.hadWon = True
            
        elif self.computer_input == "3":
            self.player_display = "Scissors"
            self.computer_display = "Scissors"
            self.results = "Draw"
            self.wasADraw = True

    def handle_scores(self):
        #Add 1-2-Score
        if self.hadWon:
            self.score += 1
            self.hadWon = False

        #HighScore
        elif self.hadLost:
            if self.score > self.highscore:
                self.highscore = self.score
                self.score = 0
            self.hadLost = False

        #etc
        elif self.wasADraw:
            self.wasADraw = False

if __name__ == "__main__":
    Main()