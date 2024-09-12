# Sentiment Analysis for Event Reviews
The Sentiment Analysis module in EVNTO analyzes user reviews of events to gauge public opinion and feedback. It works with both English and Egyptian Arabic reviews to determine whether the sentiment is positive, negative, or neutral, providing valuable insights into event performance and user satisfaction.

## Features:
* Analyze event reviews to classify sentiment as positive, negative, or neutral.
* Support for both English and Egyptian Arabic languages.
* Provide insights into event feedback, helping organizers improve future events.

## Technical Details:
* The module uses a pre-trained sentiment analysis model, fine-tuned on datasets with both English and Egyptian Arabic text.
* It leverages huggingface models for NLP tasks such as text tokenization, stemming, and sentiment classification.
* Sentiment data is used to influence the event recommendation system, making personalized suggestions based on user feedback.


## Data collected:
* Mohamed Ali Salama. [Arabic Companies Reviews For Sentiment Analysis](https://www.kaggle.com/datasets/mohamedalisalama/arabic-companies-reviews-for-sentiment-analysis), May 2023. Kaggle.
* Fahd Seddik. [Arabic Company Reviews](https://www.kaggle.com/datasets/fahdseddik/arabic-company-reviews), Sep 2022. Kaggle.
* Suhaib Dweekat. [Sentiment Analysis Arabic Dataset](https://www.kaggle.com/datasets/suhaibdweekat/sentiment-analysis-arabic-dataset-156-thousand), Apr 2023. Kaggle.
