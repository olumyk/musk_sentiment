# musk_sentiment
This pipeline ingests real-time tweets via Twitter API through Kinesis Firehose, processes them in Azure Databricks, stores results in S3, analyzes with Athena, and visualizes with QuickSight

# Twitter Sentiment and Topic Analysis on Elon Musk

This project collects, preprocesses, and analyzes Twitter data mentioning Elon Musk. It involves sentiment analysis, topic modeling, and machine learning to predict sentiment, culminating in a dashboard that visualizes insights from the data.

## Objectives

- Collect Twitter data containing mentions of Elon Musk
- Clean and preprocess the collected data
- Analyze sentiment and derive topics from the tweets
- Train and evaluate machine learning models to predict sentiment
- Create a dashboard to visualize insights from the data

## Methodology

1. Data Collection
   - Integrated the Twitter API with AWS Data Firehose and an S3 bucket via an EC2 instance to collect tweets mentioning Elon Musk.

2. Data Cleaning
   - Securely transferred the dataset from the S3 bucket to MS Azure Databricks for data wrangling and preprocessing.

3. Sentiment Analysis
   - Employed a pretrained model from the Hugging Face Transformer library for Natural Language Processing (NLP) to analyze the sentiment of the tweets.

4. Topic Modeling
   - Applied topic modeling algorithms to identify prevalent themes and discussions in the tweet dataset.

5. Feature Transformation and Model Training
   - Transformed tweets into suitable chunks for training and validating machine learning algorithms to predict sentiment.

6. Pipeline
   - Created pipelines for the trained models and exported the resulting datasets to a private S3 bucket for further analysis.

7. Visualization and Interpretation
   - Generated tables from the stored dataset using AWS Athena (check file named: AthenaSQLqueries)
   - Visualized the curated data in a QuickSight dashboard to provide insights and trends.

NB: "BigDataProject 20240520.dbc" and "full_project.ipynb" has same contents; they include both pipelines and data processing steps
