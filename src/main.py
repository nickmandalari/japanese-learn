# Main entry point for the Japanese learning app

import json # For loading and saving user data
import random # For randomizing quiz questions

with open("Vocab_List.json", "r") as file: # Load the vocabulary data from a JSON file
    parsed_vocab = json.load(file) # Load the vocabulary data from the JSON file
    # No need to call file.close() because the 'with' statement automatically handles it

def quiz_user():

    play = "yes" # Initialize the variable to control the quiz loop

    while play.lower() == "yes": # Loop to allow the user to take the quiz

        while True: # Loop to validate the user's input for the number of words
            try:
                # Get the number of words the user wants to be quizzed on, and inform them of how many words are available
                num_words = int(input(f"How many words would you like to be quizzed on? There are currently {len(parsed_vocab)} words available. ")) 
                if 1 <= num_words <= len(parsed_vocab): # Check if the number of words is valid
                    break # If the input is valid, exit the loop
                print(f"Please enter a number between 1 and {len(parsed_vocab)}.") # If the input is invalid, prompt the user to enter a valid number
            except ValueError: # Handle the case where the user enters a non-integer value
                print("Invalid input. Please enter a valid number.") # Inform the user of the invalid input and prompt them again
    
        # Randomly select the specified number of words from the vocabulary data
        quiz_words = random.sample(parsed_vocab, min(num_words, len(parsed_vocab))) # Ensure we don't ask for more words than we have
        score = 0 # Initialize the user's score

        for word in quiz_words: # Loop through each selected word and quiz the user
            print(f"What is the English translation of '{word['japanese']}'?") # Ask the user for the English translation
            answer = input("Your answer: ") # Get the user's answer
            if answer.strip().lower() == word['english'].lower(): # Check if the answer is correct (case-insensitive), strip removes spaces
                print("Correct!") # If the answer is correct, inform the user
                score += 1 # Increment the user's score
            else:
                print(f"Incorrect. The correct answer is '{word['english']}'.") # If the answer is incorrect, show the correct answer
    
        percentage = (score / num_words) * 100 # Calculate the user's score as a percentage
        print(f"Your final score is {score}/{num_words} ({percentage:.2f}%).") # After the quiz, show the user's final score
        play = input("Would you like to play again? (yes/no) ") # Ask the user if they want to play again

def new_vocab():
    add_vocab = "yes" # Initialize the variable to control the loop for adding new vocabulary words
    
    while add_vocab.lower() == "yes": # Loop to allow the user to add multiple vocabulary words
    
        new_japanese = input("Enter the new Japanese word: ") # Get the new Japanese word from the user
        new_english = input("Enter the English translation: ") # Get the English translation from the user

        new_entry = {"japanese": new_japanese, "english": new_english} # Create a new dictionary entry for the vocabulary word
        parsed_vocab.append(new_entry) # Add the new entry to the existing vocabulary list

        add_vocab = input("Would you like to add another vocabulary word? (yes/no) ") # Ask the user if they want to add another word

    with open("Vocab_List.json", "w") as file: # Open the JSON file in write mode to save the updated vocabulary list
        json.dump(parsed_vocab, file, indent=4) # Write the updated vocabulary list back to the JSON file with indentation for readability

def user_options():
    print("Welcome to the Japanese Learning App!") # Welcome message for the user
    print("You can choose to add new vocabulary words or take a quiz to test your knowledge.") # Inform the user of their options
    print("Let's get started!") # Encourage the user to start using the app 
    
    user_choice = input("Please choose one of the following options:\n1. Add new vocabulary words\n2. Take a quiz\n3. Exit\n\nEnter the number of your choice: ") # Prompt the user to choose an option

    while user_choice not in ["1","2","3"]: # Validate the user's input to ensure it's one of the valid options
        while True: # Loop to validate the user's input for the options
            try:
                if user_choice in ["1","2","3"]: # Check if the input is valid
                    break # If the input is valid, exit the loop
            except ValueError:
                pass # If the input is invalid, ignore the error and prompt the user again
        user_choice = input("Invalid choice. Please enter 1, 2, or 3: ") # If the input is invalid, prompt the user again
    
    while user_choice != "3": # Loop to allow the user to continue using the app until they choose to exit
        if user_choice == "1": # If the user chooses to add new vocabulary words
            new_vocab() # Call the function to add new vocabulary words
            user_choice = input("Please choose one of the following options:\n1. Add new vocabulary words\n2. Take a quiz\n3. Exit\n\nEnter the number of your choice: ") # Prompt the user to choose an option again after adding new words
        elif user_choice == "2": # If the user chooses to take a quiz
            quiz_user() # Call the function to start the quiz
            user_choice = input("Please choose one of the following options:\n1. Add new vocabulary words\n2. Take a quiz\n3. Exit\n\nEnter the number of your choice: ") # Prompt the user to choose an option again after taking the quiz
       
    print("Thank you for using the Japanese Learning App! Goodbye!") # Farewell message for the user
    exit() # Exit the program   

# The main entry point of the script    
if __name__ == "__main__":
    user_options() # Call the function to display user options and start the app
