# Seedly Forum - Text Classification Challenge

<img src="logo-1.png" width="300"/>


## Problem Statement
This project aims to build a text classifier that is able to classify questions using a suitable model. The selected model should be able to correctly classify a given post to either Real Estate or Stocks investment. We will be exploring 2 vectorisers (CountVec and TFIDF) to create a feature vocabulary and evaluating 3 classifiers: Logistic Regression, Multinomial Naive Bayes and Support Vector Classifier. We would be using the Matthews Correlation Coefficient as the primary metric to determine the best model having the lowest number of misclassified posts.


## Executive Summary

Launched in 2016, [Seedly](https://seedly.sg) helps users make smarter financial decisions with its expense tracking app which allows users to sync their financial accounts and better manage their cash-flow.

Over the years, we've introduced a community feature which allows users to crowdsource knowledge from peers before making a financial decision; an unbiased reviews platform for a myriad of products ranging from travel insurance to robo-advisors; as well as comparison tools for the open electricity market and SIM-only mobile plans. As the number of topics expands in line with the number of readers, there is a growing need to classify the questions and display them in the most appropiate section within the forum.

The data science team @ Seedly would be solving this challenge by building an effective model to analyse and provide a binary classification. Focusing on Seedly's core offerings, we would be classifying posts between Real estate and Stocks investments. Due to the ease of extracting data through an API, we would be mining the 2 relevant subreddits to create a corpus to train our model on. We would then parse the data and lemmatize it before we create the feature vocabulary. After fitting and tuning the model, we will be evaluating the trained model on actual blind queries from the Seedly.SG discussion forums. Finally, we would be creating a web app to test out the delivery of the model.


## The Data Science Process

### 1. Get the Data
The data corpus will be extracted from 2 subreddits, by making Reddit API calls.


### 2. EDA  & Data Cleaning
* Dropped null values
* Removed http links, non-word characters, digits
* Lemmatized across various POS tags: 
    * Verb (v)
    * Noun (n)
    * Proverb (r)
    * Adjective (a)
* Created custom stopword list on top of NLTK stopwords


### 3. Modelling
* Created 6 pipeline permutations using 2 transformers and 3 classifiers:
    * Transformers: CountVectoriser and TF-IDF Vectoriser
    * Classifiers: Logistic Regression, Multinomial Naive Bayes and Support Vector Classifier
* Ran model on default parameters then tuned hyperparameters


### 4. Evaluate the model
* Key metric used to evaluate models: Matthews Correlation Coefficient (MCC)

###### Consolidated model results using default hyperparameters
   Transformer/Classifier|MCC|Misclassified<br /> RealEstate|Misclassified<br /> Stocks|                    
  ------|------|:------:|:----:|   
   CV & Log Reg|0.8883|9|5| 
   TF & Log Reg|0.9050|9|3|
   CV & Multinomial NB|0.8974|3|10 |
   **TF & Multinomial NB**|**0.9211**|**2**|**8**|
   CV & SVC|0.8558|18 |1|
   TF & SVC|0.8974|10|3|


###### Consolidated model results after tuning hyperparameters
   
  Transformer/Classifier|MCC|Misclassified<br /> RealEstate|Misclassified<br /> Stocks|                    
  ------|------|:------:|:----:|   
   CV & Log Reg|0.8807|10|5 | 
   TF & Log Reg|0.8983|11|2|
   CV & Multinomial NB|0.9120|5|6 |
   **TF & Multinomial NB**|**0.9280**|**5**|**4**|
   CV & SVC|0.8702|16 |1|
   TF & SVC|0.9122|7|4| 
   
* Running the Naive Bayes classifier using the TF-IDF vectoriser produced the least number of misclassfied posts


### 5. Answer the DS problem
* Built an text classifier model that could distinguish, with a reasonable accuracy (>90%), between 2 classes: Real Estate and Stocks Investment



## Recommendations
Our Multinomial Naive Bayes model using a TF-IDF vectoriser came out tops again, even slightly beating the default parameter model's MCC score. It can also be observed that the TF-IDF models generally had a better MCC score than models using CountVectoriser.

This mainly could be due to the fact that TD-IDF benefits from the lemmatization. Lemmatization is also important for training word vectors, since accurate counts within the window of a word would be disrupted by an irrelevant inflection like a simple plural or present tense inflection. This is also the reason we had lemmatised our corpus across multiple parts-of-speech tags , i.e verb, noun, proverb and adjective. Based on the MCC scores, we believe the NB model would allow a good measure of generalisation that would perform relatively well on our blind data later on. However for our eventual model of choice, we would be going with the TF-SVC model, which fared a reasonable MCC score.

The key factor that led us to choosing the SVC model is that Naive Bayes treats corpus terms as independent features, whereas SVC looks at the interactions between them to a certain degree. As our blind test might have more variations to the terms gathered from our subreddit, we forsee the SVC model will be better at the classification task, under a production environment.

We have succesfully built a text classifier model and have throughly evaluated its performance. In our blind test, our SVC model has done tremendously well in the Stocks category, however it has misclassified 3 Real Estate posts.
Zooming into the first misclassification, the word 'portfolio' was a strong determinant of the Stocks category and taking a look at the other 2 posts, there were very few deterministic terms in the text.

There was a mention of the word 'CPF', which would be a term commonly used in Real Estate Investments locally. This underscores the need to provide more deterministic terms by feeding more local forum posts under these 2 classes, to improve the model's local context.
