"""
This python script is used to randomly select a prompt and allows a user
to specify it meets certain criteria.
"""
# Global Constants
FILEPATH = "prompt_database.csv"

# Imports
import random
import pandas as pd

def randomPromptReview():
    """
    Randomly selects a prompt and allows user to review it.
    """
    # open the prompt database CSV
    data = pd.read_csv(FILEPATH, usecols=["id", "en", "tags", "pulled","approved","comments","intials"], index_col="id")

    # filter to only the unpulled data
    unpulled = data["pulled"].str.lower() == "no"
    
    # check if there are any unpulled prompts
    if unpulled.empty:
        print("All prompts have been pulled!!")
    
    else:
        # randonly select an ID from the remaining unpulled prompts
        randomID = random.choice(data[unpulled].index)
        selectedPrompt = data.loc[randomID]

        # Print the prompt details
        print("\n --- Review Prompt --- \n")
        print(f"ID:\t {randomID}")
        print(f"TAGS:\t {selectedPrompt['tags']}")
        print(f"PROMPT:\t {selectedPrompt['en']}")

def main ():
    """
    Main function to run the prompt selector.
    """
    print("Welcome to the prompt selector!")
    randomPromptReview()

if __name__ == "__main__":
    main()

