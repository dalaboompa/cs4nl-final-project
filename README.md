# Emotion Recognition with r/mcmaster Subreddit posts/comments

## Disclaimer on Sensitive Content
> [!WARNING] 
> This dataset contains user-generated content from Reddit. Some instances may include strong language, offensive remarks, or discussions of sensitive topics such as discrimination or violence. Annotators should be careful of potential emotional impact while working with the data. If you feel uncomfortable, please take necessary breaks and seek support if needed.

## Dataset Overview
This dataset consists of posts and comments collected from the r/mcmaster subreddit. The data is intended for emotion classification and annotation based on the semantic and emotional content of the text. The goal of this project is to categorize each data point into predefined emotion labels: Anger, Disgust, Fear, Happiness, Sadness, Surprise, or Ambiguous.

## Data Collection
- **Source**: The dataset was gathered from publicly available posts and comments on the r/mcmaster subreddit.
- **Collection Methodology**: `TODO: please include details about how and when data was collected`
- **Format**: The dataset is stored in CSV format, with three rows `id`, `text`, and `label`, and each row representing a single post or comment.
- **Size**: `TODO: include number of distinct instances`

## Annotation Guidelines
Each text instance is labeled based on the emotional content it expresses. The labels are:
- **A (Anger)**: Expresses annoyance or displeasure.
- **D (Disgust)**: Shows strong disapproval or offense.
- **F (Fear)**: Reflects a sense of danger, threat, or anxiety.
- **H (Happiness)**: Conveys a positive sentiment or approval.
- **S (Sadness)**: Expresses grief, disappointment, or helplessness.
- **U (Surprise)**: Describes an unexpected or astonishing event.
- **M (Ambiguous)**: Emotion is neutral, unclear, or mixed.

***See more details in the annotation instructions.***

## Estimated Annotation Time
Annotating each data point takes approximately 10 seconds to 15 seconds. 

---

## Annotator Script Documentation

### `annotator.py`
This script helps the annotation process for the r/mcmaster subreddit dataset.

### Usage
1. Run the script:
   ```sh
   python annotator.py 
   ```
2. Enter the name of the input CSV file when prompted.
3. The script will display each text instance one at a time, prompting the annotator to assign a label.
4. Enter the corresponding letter (A, D, F, H, S, U, or M) and press `Enter`.
5. Labeled data will be saved to an output file (`outputX.csv`), where `X` is an incrementing number to avoid overwriting existing files.

### Output Format
The labeled data is stored in a CSV file with the following format:
- **Index**: The original index from `mydata.csv`.
- **Label**: The assigned emotion category (A, D, F, H, S, U, or M).

### Contact
If you have any questions regarding the dataset or annotation process, please contact:

| Team Member | Email |
|-------------|------------------------|
| Jingxin Huang | huanj121@mcmaster.ca  |
| Kunhan Liang | liangk17@mcmaster.ca  |
| Zitong Gu | guz38@mcmaster.ca  |

