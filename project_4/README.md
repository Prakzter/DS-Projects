# DSI Project 4: West Nile Virus Prediction


## Problem Statement:
To develop a predictive model that will forecast the probability of WNV presence in 138 mosquito traps around Chicago over the course of a season. We would also be analysing the cost-benefit analysis of spraying to mitigate the effects of the WNV being spread from mosquitos.


## Executive Summary:
West Nile virus (WNV) is a single-stranded RNA virus which causes West Nile fever. While WNV is commonly spread to humans through mosquitoes, the primary hosts and source of WNV are actually in birds. Fortunately, most people who are infected with WNV exhibit no symptoms. However, approximately 1 in 5 people with WNV will develop a fever and other symptoms. Slightly less than 1% of infected patients will serious neurological illnesses that can result in death.

The city of Chicago and the Chicago Department of Public Health (CDPH) has been running a comprehensive surveillance and control program to combat the spread of WNV. Since 2004, Chicago health officials have been laying and testing mosquito traps so as to designate pesticide spraying efforts to control mosquito numbers. However, in spite of these steps, WNV continues to be present in Chicago.

To better formulate action strategies and to prevent a possible WNV outbreak, Chicago city officials have tasked us to develop a model to that will better help them predict the presence of WNV, and to let them effectively allocate resources towards preventing transmission of this potentially deadly virus. Using the provided NOAA weather data, trap location, testing, and spraying data, our model's efficacy will be assessed through a Kaggle submission (evaluation by AUC), as well as a project report (Jupyter Notebook) and presentation to the CDC and Chicago City's health officials about our key findings are recommendations.


## Key Findings
#### On top of the train and test datasets, there were weather and spray datasets. So one of the key steps was combining all the datasets and evaluatin the relationships across the data.

- The effect of weather on the presence ov WNV across the years is inconclusive.
- Only certain species of mosquitoes (Culex Restuans/Culex Pipiens/ crossbreed of both types) are the dominant species contributing towards WNV presence.
- Certain geographical locations (streets/trapIDs) have a higher or lower prevalence of WNV.
- Mosquito spraying efforts in 2011 and 2013 have largely failed to eradicate the key WNV hotspot regions effectively.


## Model Evaluation
Our best model for predicting WNV is using the XGBClassifier. As we're dealing with an imbalanced dataset, we would using the SMOTE transformer in our pipeline to re-balance our minority class.

|Model||Kaggle Public
|:-------|------------|
|**RandomForestClassifier + SMOTE**|0.668|
|**XGBClassifier + SMOTE**|0.xxx|
|**AdaBoostClassifier + SMOTE**|0.xxx|



## Recommendations
**1) The study of seasonal weather patterns on mosquito behaviour**
As observed in our EDA section, the relationship between the weather features is still unclear. On top of this, it can be observed that the presence of WNV peaks around the approximately same few months YOY, regardless of weather patterns. This could also indicate that there could be other influencing factors, for example dense human population in certain areas.
 
**2) Understanding how WNV is transmitted by mosquitos**
As WNV is only transmitted by a crossbred species of mosquitoes (Culex Restauns/Pipiens), from a city management and health perspective, understanding the behaviors and habitats of this mosquito species will enable better modelling of effective mosquito eradication efforts.

**3) Have more training data**
Our model was trained on *10506* observations, but we were making predictions on *116293* observations. Our predictions could have improved tremendously, if we can acquire more data for our model training.

**4) Targeted mosquito spraying and data collection efforts**
To maximise city resources, all mosquito-borne disease statistics should be handled by a dedicated department in the city council. That way appropriate steps can be taken quickly, eliminating administrative lag between testing and reporting. Regular mosquito pre-spraying efforts should also be undertaken in summer months at mosquito hotspots, where identified to have a higher probablity of the presence of the WNV virus.
