![](data/title.jpg) 
# Project 1: Analysis of SAT & ACT scores across US states


## Problem Statement
Analyze trends in SAT & ACT data from 2017 - 2018 and make recommendations to increase participation in the most appropriate test in at least one state.

<br>

## Executive Summary
This study examines the state scores and other external data to determine the various factors that influence the participation rates across states.

<u>Here are some key findings:</u>

1) A 100% participation rate can only be acheived by the state making either test mandatory and providing the necessary funding to make it affordable for students.
    -  For example, Ohio state had made either ACT or SAT compulsory for high school students. This resulted both test participation rates to increase.

2) Overall SAT scores improved in year 2018 despite the higher participation rate comparing to previous year, while ACT score remains relatively stable.

3) The cost of SAT test is relatively high comparing to ACT test which might affect which tests states would sponsor.

<br>

## Data Dictionary for Final Dataset
(Datasets can be found in data directory)	

|Feature|Type|Description|
|-------|----|------------|
|state| object | States that participated in the ACT/SAT
|sat2017_participation | int64  | State participation rates (%)
|sat2017_rw          |   int64  | Average Evidence-Based Reading and Writing Score which ranges between 200 and 800
|sat2017_math         |   int64  | Average Math Score which ranges between 200 and 800
|sat2017_total        |   int64  | Average Total Score that aggregates Reading and Writing and Math Scores, ranges between 400 and 1600|
|act2017_participation |  int64  | State participation rates (%)
|act2017_english      |   float64| Average English Score which ranges between 1 and 36
|act2017_math        |    float64| Average Math Score which ranges between 1 and 36
|act2017_reading     |    float64| Average Reading Score which ranges between 1 and 36
|act2017_science    |    float64| Average Science Score which ranges between 1 and 36
|act2017_composite  |     float64| Average Composite Score which ranges between 1 and 36
|act2018_participation|   int64  | State participation rates (%)
|act2018_composite   |   float64| Average Composite Score which ranges between 1 and 36
|act2018_english     |   float64| Average English Score which ranges between 1 and 36
|act2018_math         |  float64| Average Math Score which ranges between 1 and 36
|act2018_reading      |  float64| Average Reading Score which ranges between 1 and 36
|act2018_science      |  float64| Average Science Score which ranges between 1 and 36
|sat2018_participation | int64  | State participation rates (%)
|sat2018_rw           |  int64  | Average Evidence-Based Reading and Writing Score which ranges between 200 and 800
|sat2018_math         |  int64  | Average Math Score which ranges between 200 and 800
|sat2018_total   | int64 | Average Total Score that aggregates Reading and Writing and Math Scores, ranges between 400 and 1600|



## Process flow:
- 2017 Data Import & Cleaning
- 2018 Data Import and Cleaning
- Exploratory Data Analysis
- Data Visualization
- Descriptive and Inferential Statistics
- Outside Research
- Conclusions and Recommendations
<br>
<br>
## Recommendation:
The state of Oregon has ACT and SAT participation rates between 40-50% consistently across both 2017 and 2018. 
The state currently neither has a requirement for either test nor does it fund students to take up any of the tests. This gives a clear indication that students are impartial to either test and might be more inclined to take one test over the other with the possiblity of funding.

<u>I would recommend the following actions:</u>

1) Comparing the costs between SAT & ACT, the ACT is fiscally more sound for the state of Oregon to sponsor for all high school students.

2) Create digital prep workshops or seminars to increase the student interest in the ACT and hear sucess stories.

3) Encouraging Oregon colleges to offer ACT sponsorships.

<br>
<br>

### ≈≈≈≈≈  Further investigation required: ≈≈≈≈≈
More details are required on college preferences of Oregon students to confirm if students would tend to enrol in colleges within Oregon, or at other colleges of the mid-west, before endorsing the ACT campaign.

