# Criteo's Digital Marketing Data Analysis

## Team Information
| Name | NEU ID |
| --- | --- |
| Shubham Mahajan | 001314273 |
| Gauri Verma | 001306996 |
| Anurag Rachcha | 001375637 |


## Claat Link: 
https://docs.google.com/document/d/1f3HuWXtxYVvvskPv15PcWPbxiZbUhAX5wXumiBIjiFQ/edit?ts=5ecff4ee#


## Salesforce - Einstein Analytics Dashboard
![Criteo -Einstein Analytics Dashboard](https://user-images.githubusercontent.com/59700753/87963825-58f3f480-ca87-11ea-9f5f-604ce193a79d.jpeg)


## About the dataset: 

The dataset represents a sample of 30 days of Criteo live traffic data. Each line corresponds to one impression (a banner) that was displayed to a user. For each banner we have detailed information about the context, if it was clicked, if it led to a conversion and if it led to a conversion that was attributed to Criteo or not. 


Criteo's product is a form of display advertising. Crieto’s personalized retargeting solution displays interactive banner advertisements, generated based on the online retail browsing preferences and products for each customer. 


Here is a detailed description of the fields (they are tab-separated in the file):

timestamp: timestamp of the impression (starting from 0 for the first impression). The dataset is sorted according to timestamp. <br>
uid a unique user identifier <br>
campaign a unique identifier for the campaign <br>
conversion 1 if there was a conversion in the 30 days after the impression (independently of whether this impression was last click or not) <br>
conversion_timestamp the timestamp of the conversion or -1 if no conversion was observed <br>
conversion_id a unique identifier for each conversion (so that timelines can be reconstructed if needed). -1 if there was no conversion <br>
attribution 1 if the conversion was attributed to Criteo, 0 otherwise <br>
click 1 if the impression was clicked, 0 otherwise <br>
click_pos the position of the click before a conversion (0 for first-click) <br>
click_nb number of clicks. More than 1 if there was several clicks before a conversion <br>
cost the price paid by Criteo for this display (disclaimer: not the real price, only a transformed version of it) <br>
cpo the cost-per-order in case of attributed conversion (disclaimer: not the real price, only a transformed version of it) <br>
time_since_last_click the time since the last click (in s) for the given impression <br>


____________________________________________

Python Notebook contains various data transformations and vizualisations which have been furthur used in Einstein Analytics.

____________________________________________

The .tx dataset file is broken down into smaller folders and is attached.

____________________________________________
