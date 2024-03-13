"""
project_1.py: First project to Engeto Online Python Academy
author: Martina Vesela
email: martina.mvesela@gmail.com
discord: Marta marta_27172
"""
import sys # import the 'sys' module, which provides various functions and variables

texts = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# registered users (name, password)
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

separator = "-" * 40 

# main part of the program
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
        
    if username in users and users[username] == password:
        print(separator)
        print(f"Welcome to the app, {username}")    
        print(f"We have {len(texts)} texts to by analyzed.")
        print(separator)
        
        while True:  # Repeat until the user enters the correct text number
            try:
                selection = int(input("Enter a number btw. 1 and 3 to select: "))  # Choose a text number
                if selection < 1 or selection > len(texts):
                    raise ValueError("Invalid input")

                text_to_analyze = texts[selection - 1]  # Selecting text for analysis
                words = text_to_analyze.split()  # Splitting text into words
                word_lengths = [len(word.strip(".,?!")) for word in words]  # List of word lengths
                word_length_counts = {}  # Dictionary for storing word lengths and the number of their occurrences
                
                # Filling the dictionary with word lengths and their occurrences
                for length in word_lengths:
                    if length in word_length_counts:
                        word_length_counts[length] += 1
                    else:
                        word_length_counts[length] = 1

                # Analysis results
                print(separator)
                print(f"There are {len(words)} words in the selected text.")
                print(f"There are {len([word for word in words if word.istitle()])} titlecase words.")
                print(f"There are {len([word for word in words if word.isupper()])} uppercase words.")
                print(f"There are {len([word for word in words if word.islower()])} lowercase words.")
                print(f"There are {len([word for word in words if word.isdigit()])} numeric strings.")
                print(f"The sum of all the numbers {sum(int(word) for word in words if word.isdigit())}")
                print("----------------------------------------")

                # Bar chart
                print("LEN|  OCCURENCES  |NR.")
                print(separator)
                for length, count in sorted(word_length_counts.items()):
                    print(f"{length:3}|{'*' * count:14}|{count}")

                break  # End of loop for text selection

            except ValueError:
                print("Invalid input. Please enter a number between 1 and 3.")

        break  # End of user login loop

    else:
        print("unregistered user, terminating the program..")  # If the user is not registered, exit the program
        break  # End of main user login loop