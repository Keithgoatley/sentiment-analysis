# -*- coding: utf-8 -*-
"""Sentiment Analysis_hugging face_transformers library

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BRnhGgD7ztccGfebTzCT_nntp-nFlnCb
"""

!pip install transformers

from transformers import pipeline

from transformers import pipeline

sentiment_analysis = pipeline("sentiment-analysis")

sample_text = "I don't know whether or not I truly enjoy this song or not"
result = sentiment_analysis(sample_text)
print(result)

texts = ["I love using AI to solve problems!", "This is the worst service ever.", "I'm feeling neutral about this."]
results = sentiment_analysis(texts)
for text, sentiment in zip(texts, results):
    print(f"Text: {text} - Sentiment: {sentiment}")

# Clone your new repository to your local machine
git clone https://github.com/Keithgoatley/sentiment-analysis
cd your-repository

# Copy the downloaded .ipynb file and the sentiment_results.csv file to the cloned repository directory
# You can use the file explorer on your computer to do this or use command line tools

# Add and commit the files to your repository
git add .
git commit -m "Initial commit with sentiment analysis project"
git push origin main