# Main entry point for the Japanese learning app

import json # For loading and saving user data
import random # For randomizing quiz questions

# Sample vocabulary data (in a real app, this would likely come from a database or external file)
vocab_japanese = ["こんにちは", "ありがとう", "すみません", "はい","いいえ","水","人","食べる","行く","見る"]
vocab_english = ["Hello", "Thank you", "Excuse me", "Yes","No","Water","Person","Eat","Go","See"]

# Combine Japanese and English vocab into a list of dictionaries
vocab_data = [{"japanese": jp, "english": en} for jp, en in zip(vocab_japanese, vocab_english)] 

# Save the vocabulary data to a JSON file for later use
with open("user_data.json", "w") as file:
    json.dump(vocab_data, file, indent=4)

parsed_vocab = json.load(open("user_data.json", "r")) # Load the vocabulary data from the JSON file

def quiz_user():
    # Ask the user how many words they want to be quizzed on
    num_words = int(input("Welcome! How many words would you like to be quizzed on? ")) 

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

# The main entry point of the script    
if __name__ == "__main__":
    quiz_user() # Start the quiz when the script is run
