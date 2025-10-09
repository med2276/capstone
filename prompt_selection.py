"""
This python script is used to randomly select a prompt and allows a user
to specify it meets certain criteria.
"""
# Global Constants
FILEPATH = "prompt_database.csv"

# Imports
import pandas as pd

def openCsv():
    """
    Opens a CSV file and returns its contents as a list of lists.
    """
    df = pd.read_csv(FILEPATH, usecols=["id", "en"], index_col="id")





def main ():
    """
    Main function to run the prompt selector.
    """
    print("Welcome to the prompt selector!")
    openCsv()

if __name__ == "__main__":
    main()

