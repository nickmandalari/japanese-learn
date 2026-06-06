# Main entry point for the Japanese learning app

import json # For loading and saving user data
import random # For randomizing quiz questions

with open("Vocab_List.json", "r") as file: # Load the vocabulary data from a JSON file
    parsed_vocab = json.load(file) # Load the vocabulary data from the JSON file
    # No need to call file.close() because the 'with' statement automatically handles it

def quiz_user():

    play = "yes" # Initialize the variable to control the quiz loop

    while play.lower() == "yes": # Loop to allow the user to take the quiz

        # Ask the user how many words they want to be quizzed on
        num_words = int(input("Welcome! How many words would you like to be quizzed on? ")) 

        if num_words <= 0:
            print("Please enter a positive number of words to be quizzed on.") # If the user enters a non-positive number, prompt them to enter a valid number
            num_words = int(input("How many words would you like to be quizzed on? ")) # Ask the user again for a valid number of words
        elif num_words > len(parsed_vocab):
            print(f"Sorry, we only have {len(parsed_vocab)} words available. Please enter a number less than or equal to {len(parsed_vocab)}.") # If the user asks for more words than are available, inform them of the maximum number
            num_words = int(input("How many words would you like to be quizzed on? ")) # Ask the user again for a valid number of words
        else:
            return quiz_user() # If the user enters a valid number, start the quiz
    
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

# The main entry point of the script    
if __name__ == "__main__":
    quiz_user() # Start the quiz when the script is run
