import pandas as pd
from pathlib import Path

# Define labels
labels = {
    "A": "Anger",
    "D": "Disgust",
    "F": "Fear",
    "H": "Happiness",
    "S": "Sadness",
    "U": "Surprise",
    "M": "Ambiguous"
}

instructions = """
Thank you for participating in our annotation task!
This task involves labeling posts and comments from a dataset with an appropriate emotion category.
Your job is to assign one of the following labels to each text, based on its semantic meaning and expressed emotion:

Labels:
    A - Anger: Expresses annoyance or displeasure.
    D - Disgust: Shows strong disapproval of something unpleasant or offensive.
    F - Fear: Reflects a sense of danger, threat, or anxiety.
    H - Happiness: Conveys a positive sentiment or approval.
    S - Sadness: Expresses negative emotions such as grief, disappointment, or helplessness.
    U - Surprise: Describes an unexpected or astonishing event.
    M - Ambiguous: Emotion is neutral, unclear, or mixed.

Note:
    - You may enter the label in uppercase or lowercase.
    - Please enter exactly one label per text.
"""

data_col = "text"
delimiter = "=" * 20

def main():
    # Prompt user for input file name
    input_file = input("Enter the name of the input CSV file: ").strip()
    
    try:
        # Load dataset
        my_data = pd.read_csv(input_file)
        my_data = my_data.reset_index()
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        return
    
    # Ensure output file does not overwrite existing files
    out_count = 0
    my_file = Path(f"output{out_count}.csv")
    while my_file.is_file():
        out_count += 1
        my_file = Path(f"output{out_count}.csv")
    
    print(instructions)

    # Annotate each data point
    with open(my_file, "a") as handle:
        for index, row in my_data.iterrows():
            print(delimiter)
            print(f"Instance {index}:")
            print(row[data_col])
            print(" ".join([f"({key}) {value}" for key, value in labels.items()]))
            
            while True:
                label = input("Your label: ").strip().upper()
                if label in labels:
                    break
                print("Invalid label. Please enter a valid label from the list above.")
            
            handle.write(f"{index},{label}\n")

if __name__ == '__main__':
    main()

