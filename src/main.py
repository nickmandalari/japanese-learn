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
    add_vocab = input("Would you like to add a new vocabulary word? (yes/no) ") # Ask the user if they want to add a new vocabulary word
    
    while add_vocab.lower() == "yes": # Loop to allow the user to add multiple vocabulary words
    
        new_japanese = input("Enter the new Japanese word: ") # Get the new Japanese word from the user
        new_english = input("Enter the English translation: ") # Get the English translation from the user

        new_entry = {"japanese": new_japanese, "english": new_english} # Create a new dictionary entry for the vocabulary word
        parsed_vocab.append(new_entry) # Add the new entry to the existing vocabulary list

        add_vocab = input("Would you like to add another vocabulary word? (yes/no) ") # Ask the user if they want to add another word

    with open("Vocab_List.json", "w") as file: # Open the JSON file in write mode to save the updated vocabulary list
        json.dump(parsed_vocab, file, indent=4) # Write the updated vocabulary list back to the JSON file with indentation for readability

# The main entry point of the script    
if __name__ == "__main__":
    new_vocab() # Allow the user to add new vocabulary words before starting the quiz
    quiz_user() # Start the quiz when the script is run
