# Core Pkg
import uvicorn
from fastapi import FastAPI,Query
import pandas as pd

# ML Aspect
import joblib,os



# Vectorizer
top_k_scores_pkl = pd.read_pickle('finalfastai1.pkl')
#training_removed = pd.read_pickle('training_removed.pkl')
#top_k_scores = joblib.load(top_k_scores_pkl)


# Models
#gender_nv_model = open("models/gender_nv_model.pkl","rb")
#gender_clf =  joblib.load(gender_nv_model)


# init app
app = FastAPI()

# def score(
#     learner,
#     test_df,
#     user_col=cc.DEFAULT_USER_COL,
#     item_col=cc.DEFAULT_ITEM_COL,
#     prediction_col=cc.DEFAULT_PREDICTION_COL,
#     top_k=None,
# ):

# Routes
@app.get('/')
async def index():
	return {"text":"Hello API Cuties"}

@app.get('/items/{name}')
async def get_items(name):
	return {"name":name}

# ML Aspect
@app.get('/predict/{user}')
async def predict(user):
	temp = top_k_scores_pkl[top_k_scores_pkl['userId'] == user]
	values = temp.copy()
	values = values.astype(str)
	for ind in values.index:
		print(values['userId'][ind], values['productId'][ind], values['Product Name'][ind], values['Price'][ind], values['Prediction'][ind], values['img'][ind])
	#names=['varad','divya']
#	vectorized_name = gender_cv.transform([name]).toarray()
#	prediction = gender_clf.predict(vectorized_name)
#	if prediction[0] == 0:
#		result = "female"
#	else:
#		result = "male"
#
	return {"Prediction for user ":user,"predictions ":values}


# Using Post
# @app.post('/predict/{name}')
# async def predict(name):
# 	vectorized_name = gender_cv.transform([name]).toarray()
# 	prediction = gender_clf.predict(vectorized_name)
# 	if prediction[0] == 0:
# 		result = "female"
# 	else:
# 		result = "male"

# 	return {"orig_name":name,"prediction":result}



if __name__ == '__main__':
	uvicorn.run(app,host="127.0.0.1",port=8000)