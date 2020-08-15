# Snack-Recommendation-System

## Team Information
| Name | NEU ID |
| --- | --- |
| Shubham Mahajan | 001314273 |
| Gauri Verma | 001306996 |
| Anurag Rachcha | 001375637 |

### Clatt Link: <br>
https://codelabs-preview.appspot.com/?file_id=1BMZFFzC3effwE2GC5-k_oc_HKe1Sm2feRvvRMoQEEnc#0 <br>

## Getting Started

#### To setup on your local machine:

1. Install Anaconda with Python >= 3.6. [Miniconda](https://conda.io/miniconda.html) is a quick way to get started.

2. Clone the repository

```
git clone https://github.com/shubham414/Snack-Recommendation-System.git
```

3. Run the generate conda file script to create a conda environment: (This is for a basic python environment)

```
cd Snack-Recommendation-System
python tools/generate_conda_file.py
conda env create -f reco_base.yaml  
```

4. Activate the conda environment and register it with Jupyter:

```
conda activate reco_base
python -m ipykernel install --user --name reco_base --display-name "Python (reco)"
```

5. Start the Jupyter notebook server

```
jupyter notebook
```

6. Run the [Fastai Snack Recommendation](examples/00_quick_start/FoodFastai.ipynb) and  [xDeepFM Snack Recommendation](examples/00_quick_start/tryxdeepfm.ipynb) notebook under the `00_quick_start` folder. Make sure to change the kernel to "Python (reco)".



#### To run the Fast API :

1.Execute following command on terminal and run : 
```
pip install fastapi
```
Go to path -  00_quick_start from git repository and run :
```
uvicorn FastAIfastapi:app --reload
```
Note - FastAIfastapi is the .py file for FastAI algorithm's FastAPI. To run FastAPI for xDeepFM put xdeepfmfastapi befor :app in above command and run

The API will be running on localhost port mentioned on the terminal.


#### To run the Streamlit app :

1.Execute following command on terminal and run : 
```
pip install streamlit
```
Go to path -  00_quick_start from git repository and run :
```
streamlit run Streamlitapp.py
```
The app will be running on localhost port mentioned on the terminal.


## Streamlit app 

<img width="1542" alt="Streamlit App" src="https://user-images.githubusercontent.com/59700753/89094268-1b993c00-d390-11ea-9047-739a81cd6772.png">

## Jmeter integration in Streamlit

<img width="1640" alt="Jmeter in Streamlit" src="https://user-images.githubusercontent.com/59700753/89094265-163bf180-d390-11ea-9356-8258caf1a746.png">
















