import streamlit as st
import numpy as np
import pandas as pd


html = """
  <style>
    .reportview-container {
      flex-direction: row-reverse;
    }

    header > .toolbar {
      flex-direction: row-reverse;
      left: 1rem;
      right: auto;
    }
    
    body {
    color: #fff;
    background-color: #09ab3b;
    }

    .sidebar .sidebar-collapse-control,
    .sidebar.--collapsed .sidebar-collapse-control {
      left: auto;
      right: 0.5rem;
      background-color: #09ab3b
    }

    .sidebar .sidebar-content {
      transition: margin-right .3s, box-shadow .3s;
      color: #fff;
      background-color: #09ab3b;
    }

    .sidebar.--collapsed .sidebar-content {
      margin-left: auto;
      margin-right: -21rem;
      background-color: #09ab3b;
    }

    @media (max-width: 991.98px) {
      .sidebar .sidebar-content {
        margin-left: auto;
        background-color: #09ab3b
      }
    }
  </style>
"""

st.markdown(html, unsafe_allow_html=True)


add_selectbox = st.sidebar.radio(
    "Select a search method",
    ("Similarity Search", "Facebook AI")
    )

if add_selectbox == 'Similarity Search':
 st.title("**_Recommendations using similarity search_** :camera:")
 st.write("-------------------------------------------------------------------------------------------------")
 def get_data():
     return pd.read_csv('algo1.csv')
 n=1
 df = get_data()
 images = df['0'].unique()
 #images1 = df['second']
 st.subheader("Select an image from below :point_down:")
 pic = st.selectbox('Images:', images)
 st.write("**Image you selected:**")
 st.image(pic,width=None)


 z = st.slider('How many similar products would you like to see?', 1, 10, 5)
 st.write("-------------------------------------------------------------------------------------------------")
 st.subheader("YOU MAY ALSO LIKE:")
 #st.write('**Images similar to the image selected by you:**')
 for index, row in df.iterrows():
     if row['0']==pic:
         while n < z+1:
            
             st.image(row[n], use_column_width=None, caption=row[n])
             n+=1

elif add_selectbox == 'Facebook AI':
 st.title("**_Recommendations using facebook AI_** :computer:")
 st.write("-------------------------------------------------------------------------------------------------")
 def get_data():
     return pd.read_csv('algo2.csv')
 n=1
 df = get_data()
 images = df['0'].unique()
 #images1 = df['second']
 st.subheader("Select an image from below :point_down:")
 pic = st.selectbox('Images:', images)
 st.write("**Image you selected:**")
 st.image(pic,width=None)


 z = st.slider('How many similar products would you like to see?', 1, 10, 5)
 st.write("-------------------------------------------------------------------------------------------------")
 st.subheader("YOU MAY ALSO LIKE:")
 #st.write('**Images similar to the image selected by you:**')
 for index, row in df.iterrows():
     if row['0']==pic:
         while n < z+1:
            
             st.image(row[n], use_column_width=None, caption=row[n])
             n+=1

 st.balloons()




