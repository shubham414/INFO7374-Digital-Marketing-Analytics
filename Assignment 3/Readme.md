# Implementing Visual Search

## Team Information
| Name | NEU ID |
| --- | --- |
| Shubham Mahajan | 001314273 |
| Gauri Verma | 001306996 |
| Anurag Rachcha | 001375637 |


## Claat Link: 
https://codelabs-preview.appspot.com/?file_id=1s2TD3Hrc1xRaptC6GOS7QoZSNMhPvtcofi07SycDlJE#0

## Streamlit app - Hosted on Heroku platform


![streamlitapp-herokuhost](https://user-images.githubusercontent.com/59700753/87215750-99c17000-c307-11ea-965d-67a4aa6c868d.png)


## About the dataset: 

We will be using the Cdiscount dataset for our image similarity search. Cdiscount.com is France's largest non-food e-commerce company. While the company already sells everything from TVs to trampolines, the list of products is still rapidly growing. Cdiscount.com has over 30 million products up for sale. Below is a brief overview of the data used in our analysis-

train.bson - (Size: 58.2 GB) Contains a list of 7,069,896 dictionaries, one per product. Each dictionary contains a product id (key: _id), the category id of the product (key: category_id), and between 1-4 images, stored in a list (key: imgs). Each image list contains a single dictionary per image, which uses the format: {'picture': b'...binary string...'}. The binary string corresponds to a binary representation of the image in JPEG format.
Data Source :- https://www.kaggle.com/c/cdiscount-image-classification-challenge

Here is a brief description of the folder contains :- 

Cosine Similarity and FAISS: Contains python files and images used for the respective search algorithms

Spotify: Contains python files, images, and the json files created using Spotify Annoy method

Streamlit: Contains the images, .py code for the application, files for heroku deployment, and the csv files used for the application.

| --- | --- |

For both algorithms, cosine similarity search and FAISS . Run .ipynb files.

To run the Streamlit app :-

Execute following commands on terminal and run : pip install streamlit
then, Go to path -  streamlit folder from git repository and run
streamlit run streamlitApp.py

The app will be running or mentioned localhost port.

| --- | --- |

To host an app on Heroku follow steps given below :- 

Create account on heroku.
Go to path - streamlit folder of git repo. ( Delete requirements.txt from folder )
Open terminal and login to heroku using command:  heroku login
this will redirect to browser. Close it and get back on terminal window
then run following commands one by one:-
heroku create [give app name] - App wil be created on heroku account. You can check it on your heroku dashboard
pip freeze -> requirements.txt - This will generate requirements.txt in the streamlit folder
git init
git commit -m "message"
git push heroku master

Url will be given on terminal. Run url in browser. The app is successfully hosted on hiroku
If you get an error, remove respective error files from requirements.txt

Note :- Make sure all images you want to work on, .py file, requirements.txt, procfile, setup.sh are in the same folder ( For given repo, All files are in the folder "streamlit" )

| --- | --- |
For Sopitfy Annoy Method :- 
run spotifyPart1.py 
then run spotifyPart2.py - This will generate nearest_neighbors.json

From terminal - install elastic search and kibana
Run elastic search and kibana through terminal
In kibana, Go to developer mode, Create index and insert each document from nearest_neighbors.json
Query on kibana developer window and get result

Note :- If you change images from the "images" folder. You will need to update image_data.json accordingly.

| --- | --- |

To deploy flask app, install flask through terminal - pip install flask
Go to path - Flask folder from the repository
Run:  python spotifysearchapp.py

Flask application will be running on localhost url mentioned on the terminal.

| --- | --- |












