"""
This python script is used to randomly select a prompt and allows a user
to specify it meets certain criteria.
"""
# Global Constants
FILEPATH = "prompt_database.csv"
PROMPT_APPROVAL_GOAL = 45

# Imports
import random
import pandas as pd

def randomPromptReview():
    """
    Randomly selects a prompt and allows user to review it.
    """
    # open the prompt database CSV
    data = pd.read_csv(FILEPATH, index_col="id")

    # Explicitly cast string columns to object type
    for col in ["comments", "intials"]:
        data[col] = data[col].astype("string")

    # check if the approval goal has been met
    print("\n --- Approval Status ---")
    approved_count = (data["approved"].str.lower() == "yes").sum()
    progress_to_goal = min((approved_count / PROMPT_APPROVAL_GOAL) * 100, 100)
    goal_remaining = max(PROMPT_APPROVAL_GOAL - approved_count, 0)
    print(f"Progress to goal: {progress_to_goal:.2f}% ({approved_count}/{PROMPT_APPROVAL_GOAL})")
    print(f"Prompts remaining to reach goal: {goal_remaining}\n")


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

        # Update pulled status
        data.loc[randomID, "pulled"] = "yes"

        # User Approval
        approval = input("\nDo you approve this prompt? (y/N): ").strip().lower()
        while True:
            if approval == 'y':
                print("Prompt approved!")
                data.loc[randomID, "approved"] = "yes"
                break
            
            elif approval == 'n':
                print("Prompt rejected.")
                # default value is "no", so no need to change
                break
            
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        
        # User comments
        comments = input("\nEnter your comment: ").strip()
        data.loc[randomID, "comments"] = comments

        initials = input("\nEnter your initials: ").strip().upper()
        data.loc[randomID, "intials"] = initials

        # Save the updated DataFrame back to the CSV
        data.to_csv(FILEPATH)
        print(f"\n Prompt {randomID} updated and saved successfully.")

def main ():
    """
    Main function to run the prompt selector.
    """
    print("Welcome to the prompt selector!")
    randomPromptReview()

if __name__ == "__main__":
    main()

