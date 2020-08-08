
import string
import random
import datetime
import subprocess
import os
import uuid
import about
import pandas_profiling
from pandas import DataFrame
import streamlit as st
from sklearn import datasets
import numpy as np
import requests
import pandas as pd
import plotly.graph_objects as go
from plotly.colors import n_colors
import PIL.Image
from plotly.graph_objs import *
from IPython.core.display import HTML
import matplotlib.pyplot as plt
from metakernel.display import display

# Get JMETER_HOME environment variable

os.environ['JMETER_HOME'] = '/usr/local/Cellar/jmeter/5.3'
JMETER_PATH = os.environ['JMETER_HOME']


def main_about():
    st.title('About')
    st.markdown('---')
    #Display About section

def pd_profile(filename):
    df = pd.read_csv(JMETER_PATH + '/libexec/bin/' + filename)
    report = pandas_profiling.ProfileReport(df)
    #st.write(pandas_profiling.__version__)
    random_filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 24)) 
    random_filename = random_filename + ".html"
    st.write('Report file name is `%s`' % random_filename + ' . Report is located at ' + JMETER_PATH + '/libexec/bin/')
    #st.write('You selected `%s`' % selected_filename + '. To execute this test plan, click on Run button as shown below.')
    report.to_file(output_file=random_filename)
    #st.markdown(report)
    return 

def jmeter_execute_load():
    global JMETER_PATH
    #Changing Directory to Root
    #os.chdir('.')
    os.chdir(JMETER_PATH + '/libexec/bin')
    jmeterFileNames = []
    
    # Find only JMeter test plans
    for f in os.listdir("."):
        if f.endswith('.jmx'):
            jmeterFileNames.append(f)
    selected_filename = st.selectbox('Select a file to execute',jmeterFileNames)
    st.write('You selected `%s`' % selected_filename + '. To execute this test plan, click on Run button as shown below.')
    st.info('JMeter Path is ' + JMETER_PATH)
    if st.button('Run'):
        st.info('Execution has been started, you can monitor the stats in the command prompt.')
        jmeter_execute(selected_filename)
    #jmeterfilename = jmeter_execute()
    #st.write('You selected `%s`' % jmeterfilename)

def jmeter_execute(selected_filename):
    global JMETER_PATH
    
    logFileName = str(uuid.uuid1())
    logFileName = logFileName + ".csv"
    
    st.text('Results file is ' + logFileName)

    os.chdir(JMETER_PATH + '/libexec/bin')
    st.text('Your curret directory is ' + os.getcwd())
    cmd = "jmeter -n -t " + selected_filename + " -l " + logFileName
    st.text('Executing ' + cmd)
    #os.chdir(".")
    returned_value = os.system(cmd)


def jmeter_analyze():
    jmeterResults = []
    os.chdir(JMETER_PATH + '/libexec/bin')
    filenames = os.listdir(".")
    # Find only JMeter test results
    for f in os.listdir("."):
        if f.endswith('.csv'):
            jmeterResults.append(f)
    selected_filename = st.selectbox('Select a file to analyze (supports only CSV extension)', jmeterResults)
    return os.path.join(selected_filename)
# icon("search")
# selected = st.text_input("", "Search...")
# button_clicked = st.button("OK")



def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

#local_css("style.css")
#remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

layout = Layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

def path_to_image_html(path):
    return '<img src="'+ path + '" width="60" >'

def get_dataset(user_id):
    server_url = "http://127.0.0.1:8000/predict/" + user_id
    r = requests.get(server_url)

    return r.json()

def get_dataset1(user_id):
    server_url = "http://127.0.0.1:8081/predict2/" + user_id
    r = requests.get(server_url)

    return r.json()


pd.set_option('display.max_colwidth', -1)



def main():
    st.markdown('<style>  body {background-color: white; color: black}</style>', unsafe_allow_html=True)
    st.markdown('<style> h1 {color: sandybrown; text-align: center }</style>', unsafe_allow_html=True)
    #st.sidebar.header("sidebar")
    st.sidebar.title('Select a recommendation method ')
    # add_selectbox = st.sidebar.radio(
    #     "->",
    #     ("FastAI", "xDeepFM")
    #     )

  
    add_selectbox = st.sidebar.selectbox('',('','FastAI', 'xDeepFM'))
    st.sidebar.text(" \n")
    st.sidebar.text(" \n")
    st.sidebar.markdown('---')
    st.sidebar.text(" \n")
    st.sidebar.text(" \n")
  
    if add_selectbox == 'FastAI':
        st.title ("FastAI")
        st.text(" \n")
        st.text(" \n")
        st.header("*The recommendations for this user are : * :arrow_forward:")
        user_input = st.sidebar.number_input("Please Enter User ID",min_value = 0,max_value=1000,value = 0,step = 1)
        user_in = str(user_input)
        print(type(user_in))
        if st.sidebar.button('Get Recommeded Products'):
            result = get_dataset(user_in)
            # print(result['predictions ']['productId'])
            pred = result['predictions ']
            out = list(zip(pred['productId'].values(),pred['Product Name'].values(),pred['Price'].values(), pred['Prediction'].values(), pred['img'].values()))
            productIds = list(pred['productId'].values())
            productNames = list(pred['Product Name'].values())
            productPrice = list(pred['Price'].values())
            preds = list(pred['Prediction'].values())
            image = list(pred['img'].values())
            print(len(productIds))
            print(len(preds))
            df = pd.DataFrame({'ProductID': productIds, 'ProductName': productNames, 'Productprice':productPrice, 'Predictions': preds, 'image': image})
            df = df.sort_values(['Predictions'], ascending=False)
            dfcheck = df.loc[0:4,['ProductID' , 'ProductName','Productprice','Predictions','image']]#.assign( Table ='').set_index('Table')
            dfcheck = dfcheck.reset_index(drop =True)
            dfcheck2 = dfcheck.loc[0:4,:]
            dfcheck2.set_index("ProductID", inplace = True)
            st.write(dfcheck2.to_html(escape=False ,formatters=dict(image=path_to_image_html)), unsafe_allow_html=True)
            #st.write(dfcheck.ProductID)
            #st.write(dfcheck.image

            # colors = ['rgb(255,218,185)', 'rgb(255,228,181)', 'rgb(255,239,213)',
            # 'rgb(250,250,210)', 'rgb(255,250,205)']
            # dfn = pd.DataFrame({'ProductID': productIds, 'ProductName': productNames, 'Productprice':productPrice, 'Predictions': preds, 'image': image})
            # dfn = dfn.sort_values(['Predictions'], ascending=False)
            # dfnn2= dfn.loc[0:4,['ProductID' , 'ProductName','Productprice','Predictions','image']].assign( hack ='').set_index('hack')
            # dfnn2['Color'] = colors
            # dfnn3 = st.write(dfnn2.to_html(escape=False ,formatters=dict(image=path_to_image_html)), unsafe_allow_html=True)
            # print(dfnn3.ProductID)
            # fig = go.Figure(data=[go.Table(header=dict(
        	   #  values=["<b>Product ID<b>", "<b>Product Name</b>", "<b>Product Price</b>","<b>Predicted Rating</b>","<b>Product Image</b>"],
        	   #  line_color='white', fill_color='olive',
        	   #  align='center',font=dict(color='white', size=16),height=50
        	   #  ),
            # cells=dict(
        	   #  values=[dfnn3.ProductID, dfnn3.ProductName, dfnn3.Productprice, dfnn3.Predictions, dfnn3.image],
        	   #  line_color=[dfnn2.Color], fill_color=[dfnn2.Color],
        	   #  align='center',font=dict(color='saddlebrown', size=20),height=50
        	   #  ))
            # ],layout=layout)
            # #fig.show()python -m pip install -r .\requirements.txt
            # image = PIL.Image.open('my_table3.png')
            # st.image(image, use_column_width=True)
        
    
    if add_selectbox == 'xDeepFM':
        st.title ("xDeepFM")
        st.text(" \n")
        st.text(" \n")
        st.header("*The recommendations for this user are : * :arrow_forward:")
        user_input2 = st.sidebar.number_input("Please Enter User ID",min_value = 0,max_value=1000,value = 0,step = 1)
        user_in2 = str(user_input2)
        if st.sidebar.button('Get Recommeded Products'):
            result2 = get_dataset1(user_in2)
            # print(result['predictions ']['productId'])
            pred = result2['Like Prob']
            out = list(zip(pred['productId'].values(),pred['Product Name'].values(),pred['Price'].values(), pred['Like Probability'].values(), pred['img'].values()))
            productIds = list(pred['productId'].values())
            productNames = list(pred['Product Name'].values())
            productPrice = list(pred['Price'].values())
            preds = list(pred['Like Probability'].values())
            image = list(pred['img'].values())
            df = pd.DataFrame({'Product ID': productIds,'Product Name': productNames, 'Product price':productPrice, 'Like Probability': preds, 'image': image})
           
            dfcheck = df.loc[0:4,['Product ID' , 'Product Name', 'Product price', 'Like Probability', 'image']]#.assign( Table ='').set_index('Table')
            dfcheck.set_index("Product ID", inplace = True)
            st.write(dfcheck.to_html(escape=False ,formatters=dict(image=path_to_image_html)), unsafe_allow_html=True)
            

            # colors = ['rgb(255,218,185)', 'rgb(255,228,181)', 'rgb(255,239,213)',
            # 'rgb(250,250,210)', 'rgb(255,250,205)']

            # dfn = pd.DataFrame({'ProductID': productIds, 'Predictions': preds})
            # dfnn2= dfn.loc[0:4,['ProductID' , 'Predictions']].assign( hack ='').set_index('hack')
            # dfnn2['Color'] = colors
            # fig = go.Figure(data=[go.Table(header=dict(
        	   #  values=["<b>Product ID<b>", "<b>Like Probability</b>"],
        	   #  line_color='white', fill_color='olive',
        	   #  align='center',font=dict(color='white', size=16),height=50
        	   #  ),
            # cells=dict(
            #     values=[dfnn2.ProductID, dfnn2.Predictions],
        	   #  line_color=[dfnn2.Color], fill_color=[dfnn2.Color],
        	   #  align='center',font=dict(color='saddlebrown', size=20),height=50
            #     ))
            # ],layout=layout)
            # #fig.show()
            # fig.write_image("my_table3.png")
            # image = PIL.Image.open('my_table3.png')
            # st.image(image, caption='Sunrise by the mountains', use_column_width=True)
           


    menu_list = ['Execute JMeter Test Plan','Analyze JMeter Test Results', 'Home']
    # Display options in Sidebar
    st.sidebar.title('Load Testing Using Jmeter')
    menu_sel = st.sidebar.radio('', menu_list, index=2, key=None)

    # Display text in Sidebar
    about.display_sidebar()

    # Selecting About Menu
    if menu_sel == 'Home':
        about.display_about()

    # Selecting Execute Menu
    if menu_sel == 'Execute JMeter Test Plan':
    #jmeter_run = st.radio('Select',('Default','Execute','Analyze'))
    #if jmeter_run == 'Execute':
        st.title('Execute JMeter Test Plan')
        jmeter_execute_load()


    #if jmeter_run == 'Analyze':
    if menu_sel == 'Analyze JMeter Test Results':
        st.title('Analyze JMeter Test Results')

        filename = jmeter_analyze()
        st.write('You selected `%s`' % filename)
        #DATA_URL = ('C:\\Users\\Navee\\OneDrive\\Documents\\Tools\\apache-jmeter-5.2\\bin\\Run2.csv')
        DATA_URL = filename

        st.markdown('')
        # Show Graphs Checkbox
        show_graphs = st.checkbox('Show Graphs')

        # Show Profiling Report
        profile_report = st.button('Generate Profiling Report')
       
        # Generate Profiling Report

        if profile_report:
            st.write('Generating Report for ', filename)
            pd_profile(filename)


        st.title('Apache JMeter Load Test Results')
        data = pd.read_csv(DATA_URL)
        
        #Display Start Time
        startTime = data['timeStamp'].iloc[0]/1000
        startTime = datetime.datetime.fromtimestamp(startTime).strftime('%Y-%m-%d %H:%M:%S')
        st.write('Start Time ', startTime)

        endTime = data['timeStamp'].iloc[-1]/1000
        endTime = datetime.datetime.fromtimestamp(endTime).strftime('%Y-%m-%d %H:%M:%S')
        st.write('End Time ', endTime)

        FMT = '%Y-%m-%d %H:%M:%S'
        delta = datetime.datetime.strptime(endTime, FMT) - datetime.datetime.strptime(startTime, FMT)

        st.write('Total duration of the test (HH:MM:SS) is ', delta)

        st.subheader('Summary Report - Response Time')
        st.write(data.groupby('label')['elapsed'].describe(percentiles=[0.75,0.95,0.99]))

        st.subheader('Error Count')
        errCount = data.groupby(['label','responseCode'])['responseCode'].count()
        st.write(errCount)

        if show_graphs:
            chart_data = pd.DataFrame(data,columns=['timeStamp','Latency','label','responseCode','elapsed','Connect','bytes'])

            st.subheader("Graph between Timestamp and Latency")
                
            st.vega_lite_chart(chart_data, {
                "mark": {"type": "bar", "color": "maroon"},    
                "selection": {
                    "grid": {
                    "type": "interval", "bind": "scales"
                    }
                }, 
                'encoding': {
                    "tooltip": [
                {"field": "timeStamp", "type": "temporal"},
                {"field": "label", "type": "nominal"},
                {"field": "Latency", "type": "quantitative"}
                ],
                'x': {'field': 'timeStamp', 'type': 'temporal'},
                'y': {'field': 'Latency', 'type': 'quantitative'},
                },
                })

            st.subheader("Graph between Timestamp and Response Code")
            st.vega_lite_chart(chart_data, {
                "mark": {"type": "bar", "color": "aqua"},    
                "selection": {
                    "grid": {
                    "type": "interval", "bind": "scales"
                    }
                }, 
                'encoding': {
                    "tooltip": [
                {"field": "timeStamp", "type": "temporal"},
                {"field": "label", "type": "nominal"},
                {"field": "responseCode", "type": "quantitative"}
                ],
                'x': {'field': 'timeStamp', 'type': 'temporal'},
                'y': {'field': 'responseCode', 'type': 'quantitative'},
                },
                })

            st.subheader("Graph between Timestamp and Response Time")
            st.vega_lite_chart(chart_data, {
                "mark": {"type": "bar", "color": "orange"},    
                "selection": {
                    "grid": {
                    "type": "interval", "bind": "scales"
                    }
                }, 
                'encoding': {
                    "tooltip": [
                {"field": "timeStamp", "type": "temporal"},
                {"field": "label", "type": "nominal"},
                {"field": "elapsed", "type": "quantitative"}
                ],
                'x': {'field': 'timeStamp', 'type': 'temporal'},
                'y': {'field': 'elapsed', 'type': 'quantitative'},
                },
                })

            st.subheader("Graph between Timestamp and Connect Time")
            st.vega_lite_chart(chart_data, {
                "mark": {"type": "bar", "color": "darkgreen"},    
                "selection": {
                    "grid": {
                    "type": "interval", "bind": "scales"
                    }
                }, 
                'encoding': {
                    "tooltip": [
                {"field": "timeStamp", "type": "temporal"},
                {"field": "label", "type": "nominal"},
                {"field": "Connect", "type": "quantitative"}
                ],
                'x': {'field': 'timeStamp', 'type': 'temporal'},
                'y': {'field': 'Connect', 'type': 'quantitative'},
                },
                })

            st.subheader("Graph between Timestamp and bytes")
            st.vega_lite_chart(chart_data, {
                "mark": {"type": "bar", "color": "darkblue"},    
                "selection": {
                    "grid": {
                    "type": "interval", "bind": "scales"
                    }
                }, 
                'encoding': {
                    "tooltip": [
                {"field": "timeStamp", "type": "temporal"},
                {"field": "label", "type": "nominal"},
                {"field": "bytes", "type": "quantitative"}
                ],
                'x': {'field': 'timeStamp', 'type': 'temporal'},
                'y': {'field': 'bytes', 'type': 'quantitative'},
                },
                })

            st.subheader("Graph between Timestamp and Response Time - Line Chart")
            st.vega_lite_chart(chart_data, {
            "mark": "line",
        "encoding": {
            "tooltip": [
                {"field": "timeStamp", "type": "temporal"},
                {"field": "label", "type": "nominal"},
                {"field": "elapsed", "type": "quantitative"}
                ],
            "x": {"field": "timeStamp", "type": "temporal"},
            "y": {"field": "elapsed", "type": "quantitative"},
            "color": {"field": "label", "type": "nominal"}
        },
                })
        
            st.subheader("Graph between Timestamp and Response Time - Bar Chart")
            st.vega_lite_chart(chart_data, {
            "mark": "bar",
        "encoding": {
            "tooltip": [
                {"field": "timeStamp", "type": "temporal"},
                {"field": "label", "type": "nominal"},
                {"field": "elapsed", "type": "quantitative"}
                ],
            "x": {"field": "timeStamp", "type": "temporal"},
            "y": {"field": "elapsed", "type": "quantitative"},
            "color": {"field": "label", "type": "nominal"}
        },
                })

            st.subheader("Histogram")
            st.vega_lite_chart(chart_data, {
                "transform": [{
                "filter": {"and": [
                {"field": "timeStamp", "valid": True},
                {"field": "elapsed", "valid": True}
                ]}
            }],
            "mark": "rect",
            "width": 300,
            "height": 200,
            "encoding": {
                "x": {
                "field": "timeStamp",
                "type": "temporal"
                },
                "y": {
                "field": "elapsed",
                "type": "quantitative"
                },
                "color": {
                "aggregate": "count",
                "type": "quantitative"
                }
            },
            "config": {
                "view": {
                "stroke": "transparent"
                }
            }
                    })

            st.subheader("Histogram")
            st.vega_lite_chart(chart_data, {
                "transform": [{
                "filter": {"and": [
                {"field": "timeStamp", "valid": True},
                {"field": "Connect", "valid": True}
                ]}
            }],
            "mark": "rect",
            "width": 300,
            "height": 200,
            "encoding": {
                "x": {
                "field": "timeStamp",
                "type": "temporal"
                },
                "y": {
                "field": "Connect",
                "type": "quantitative"
                },
                "color": {
                "aggregate": "count",
                "type": "quantitative"
                }
            },
            "config": {
                "view": {
                "stroke": "transparent"
                }
            }
                    })

            st.subheader("Scatter Plot between Timestamp and Response Time")
            st.vega_lite_chart(chart_data, {
                    
                "selection": {
                "grid": {
                "type": "interval", "bind": "scales"
                }
            },
            "mark": "circle",
            "encoding": {
                "tooltip": [
                    {"field": "timeStamp", "type": "temporal"},
                    {"field": "label", "type": "nominal"},
                    {"field": "elapsed", "type": "quantitative"}
                    ],
                "x": {
                "field": "timeStamp", "type": "temporal"    },
                "y": {
                "field": "elapsed", "type": "quantitative"    },
                "size": {"field": "label", "type": "nominal"}
            },
                    })

if __name__== "__main__":
    main()