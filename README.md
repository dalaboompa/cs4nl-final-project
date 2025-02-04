# Emotion Recognition with r/mcmaster Subreddit posts/comments

## r/mcmaster Subreddit Dataset

### Disclaimer on Sensitive Content
> [!WARNING] 
> This dataset contains user-generated content from Reddit. Some instances may include strong language, offensive remarks, or discussions of sensitive topics such as discrimination or violence. Annotators should be careful of potential emotional impact while working with the data. If you feel uncomfortable, please take necessary breaks and seek support if needed.

### Dataset Overview
This dataset consists of posts and comments collected from the r/mcmaster subreddit. The data is intended for emotion classification and annotation based on the semantic and emotional content of the text. The goal of this project is to categorize each data point into predefined emotion labels: Anger, Disgust, Fear, Happiness, Sadness, Surprise, or Ambiguous.

### Data Collection
- **Source**: The dataset was gathered from publicly available posts and comments on the r/mcmaster subreddit.
- **Collection Methodology**: The dataset is collected using a crawler that calls Reddit API. The posts are collected via the `https://www.reddit.com/r/mcmaster/new.json` endpoint, and the comments of a post is collected via the `https://www.reddit.com/r/mcmaster/comments/{post_id}.json` endpoint. First, we collect as many posts as possible (Reddit allows us to get at most 1000 posts), and then only posts with more than 5 words are kept. Next, we randomly pick a post from these posts and collect their comments. Similarly, only comments with more than 5 words are collected. The collection stops once we have 1200 datapoints. Finally, the collected posts and comments are combined.
- **Format**: The dataset is stored in XLSX format, with three rows `id`, `text`, and `label`, and each row representing a single post or comment.
- **Size**: There are 1200 unique datapoints, and the first 15% of the dataset is duplicated so as the result we have $1200 \times 1.15 = 1380$ datapoints to annotate.

## Data Annotation

### Annotation Guideline
Each text instance is labeled based on the emotional content it expresses. The labels are:
- **A (Anger)**: Expresses annoyance or displeasure.
- **D (Disgust)**: Shows strong disapproval or offense.
- **F (Fear)**: Reflects a sense of danger, threat, or anxiety.
- **H (Happiness)**: Conveys a positive sentiment or approval.
- **S (Sadness)**: Expresses grief, disappointment, or helplessness.
- **U (Surprise)**: Describes an unexpected or astonishing event.
- **M (Ambiguous)**: Emotion is neutral, unclear, or mixed.

***See more details in the annotation instructions.***

### Estimated Annotation Time
Annotating each data point takes approximately 10 seconds to 20 seconds. So in total we need $20 \times 1380 = 27600s \approx 7.67h$ to annotate the entire dataset.

## Annotation
Open the corresponding `mcmaster_reddit_part_{part#}.xlsx`. Feel free to resize the font or column/row size but please do not change the file structure. Put the corresponding label (one letter) to the "label" column. Save frequently.

### Contact
If you have any questions regarding the dataset or annotation process, please contact:

| Team Member | Email |
|-------------|------------------------|
| Jingxin Huang | huanj121@mcmaster.ca  |
| Kunhan Liang | liangk17@mcmaster.ca  |
| Zitong Gu | guz38@mcmaster.ca  |

