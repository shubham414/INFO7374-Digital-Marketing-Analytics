# Core Pkg
import uvicorn
from fastapi import FastAPI,Query
import pandas as pd

# ML Aspect
import joblib,os




result = pd.read_pickle('xdeepfmfinalimage.pkl')



# init app
app = FastAPI()


# Routes
@app.get('/')
async def index():
	return {"text":"Hello API2 Cuties"}

@app.get('/items/{name}')
async def get_items(name):
	return {"name":name}

# ML Aspect
@app.get('/predict2/{user}')
async def predict2(user):
	temp = result[result['userId'] == user]
	values = temp.copy()
	values = values.astype(str)
	for ind in values.index:
		print(values['userId'][ind], values['productId'][ind], values['Like Probability'][ind], values['Product Name'][ind], values['Price'][ind], values['img'][ind])	

#
	return {"Prediction for user ":user,"Like Prob":values}


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
	uvicorn.run(app,host="127.0.0.1",port=8081)