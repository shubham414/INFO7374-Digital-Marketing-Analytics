# import pandas as pd
import plotly.graph_objs as go
# import dash_daq as daq
import pandas as pd
import numpy as np
# from sklearn.preprocessing import LabelEncoder, MinMaxScaler
# from sklearn.model_selection import train_test_split
# import pickle
# import plotly.express as px
# import json
# import plotly.figure_factory as ff
# import time
import base64
import dash
import dash_html_components as html
import dash_core_components as dcc
# import glob
# #from IPython.display import display, HTML
# from tqdm import tqdm_notebook as tqdm
# from sklearn import preprocessing
# import seaborn as sns
# import matplotlib.pyplot as plt
# # from IPython.core.interactiveshell import InteractiveShell
# # InteractiveShell.ast_node_interactivity = "all"
from dash.dependencies import Input, Output
# plot wtih holoviews + datashader - bokeh with map background


# def configure_plotly_browser_state():
#     import IPython
#     display(IPython.core.display.HTML('''
#         <script src="/static/components/requirejs/require.js"></script>
#         <script>
#           requirejs.config({
#             paths: {
#               base: '/static/base',
#               plotly: 'https://cdn.plot.ly/plotly-latest.min.js?noext',
#             },
#           });
#         </script>
#         '''))

# app = dash.Dash(__name__,)#meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],)
# app.config["suppress_callback_exceptions"] = True




fig = go.Figure()

fig.add_trace(go.Bar(
    x=["Apples", "Oranges", "Watermelon", "Pears"],
    y=[3, 2, 1, 4]
))

fig.update_layout(
    autosize=False,
    width=500,
    height=500,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor= "rgba(0,0,0,0)",
    font_color= "white",

    yaxis=dict(
        title_text="Y-axis Title",
        ticktext=["Very long label", "long label", "3", "label"],
        tickvals=[1, 2, 3, 4],
        tickmode="array",
        titlefont=dict(size=30),
    )
)

fig.update_yaxes(automargin=True)

rfm_level_ag = pd.read_csv('data/csvfordash/CustomerSeg1.csv')
rfm_level_ag['Customer Segmentation'] = 'Customer Segmentation'

rfm_cseg = go.Figure(go.Treemap(
    labels=rfm_level_ag['Customer Segment'],
    parents=['Customer Segmentation', 'Customer Segmentation', 'Customer Segmentation', 'Customer Segmentation',
             'Customer Segmentation', 'Customer Segmentation', 'Customer Segmentation'],
    # rfm_level_ag[('Marketing Action', 'unique')].tolist(),
    values=rfm_level_ag['%ofTotalCustomers']
))
rfm_cseg.update_layout(
        title="Customer Segmentation using RFM",
        autosize=False,
        width=700,
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",

        font=dict(
            family="Courier New, monospace",
            size=15,
            #color="#7f7f7f"
        )
   )




import plotly.express as px
rfm =  pd.read_csv('data/csvfordash/rfm.csv')
rfmrf = px.scatter(rfm, x="Recency", y="Frequency", color="Customer Segment", size = "Frequency")
rfmrf.update_layout(
        title="Customer Segments by Recency & Frequency",
        #autosize=False,
        # width=500,
        # height=450,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        xaxis =  { 'showgrid': False,'zeroline': True },
        yaxis = { 'showgrid': False,'zeroline': True},

        font=dict(
            family="Courier New, monospace",
        )
    )

rfmfm = px.scatter(rfm, x="Frequency", y="Monetary", color="Customer Segment", size = "Monetary")
rfmfm.update_layout(
        title="Customer Segments by Frequency & Monetary",
        #autosize=False,
        # width=500,
        # height=450,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        xaxis =  { 'showgrid': False,'zeroline': True },
        yaxis = { 'showgrid': False,'zeroline': True},

        font=dict(
            family="Courier New, monospace",
        )
    )

rfmrm = px.scatter(rfm, x="Recency", y="Monetary", color="Customer Segment", size = "Monetary")
rfmrm.update_layout(
        title="Customer Segments by Recency & Monetary",
        #autosize=False,
        # width=500,
        # height=450,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        xaxis =  { 'showgrid': False,'zeroline': True },
        yaxis = { 'showgrid': False,'zeroline': True},

        font=dict(
            family="Courier New, monospace",
        )
    )

ak=pd.read_csv('data/csvfordash/cltv.csv')
cltv = px.bar(ak, x='customer_id', y='value')
cltv.update_layout(
        title="Conditional expected average profit",
        #autosize=False,
        # width=500,
        # height=450,
        xaxis_title="Customer_id",
        yaxis_title="CLTV",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        xaxis =  { 'showgrid': False,'zeroline': True,'showticklabels':False},
        yaxis = { 'showgrid': False,'zeroline': True},

        font=dict(
            family="Courier New, monospace",
        )
    )

monthly_active_users = pd.read_csv('data/csvfordash/monthly_active_users.csv')

aptry = px.bar(monthly_active_users, x='month_year', y='usercount',color='usercount')
aptry.update_layout(
        title="Monthly Active Customers",
        #autosize=False,
        # width=500,
        # height=450,
        xaxis_title="Months",
        yaxis_title="User Count",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        xaxis =  { 'showgrid': False,'zeroline': True,'showticklabels':False},
        yaxis = { 'showgrid': False,'zeroline': True},

        font=dict(
            family="Courier New, monospace",
        )
    )

df_user_type_revenue = pd.read_csv('data/csvfordash/df_user_type_revenue.csv')
urev = px.line(df_user_type_revenue, x="month_year", y="payment_value", color='usertype')
urev.update_layout(
        title="Monthly Revenue",
        #autosize=False,
        # width=500,
        # height=450,
        xaxis_title="Month",
        yaxis_title="Revenue",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        xaxis =  { 'showgrid': False,'zeroline': True,'showticklabels':False},
        yaxis = { 'showgrid': False,'zeroline': True},

        font=dict(
            family="Courier New, monospace",
        )
    )

image_filename = 'data/csvfordash/kmeans.png' # replace with your own image
kmeans1 = base64.b64encode(open(image_filename, 'rb').read())


image_filename = 'data/csvfordash/palive.png' # replace with your own image
palive = base64.b64encode(open(image_filename, 'rb').read())


Olist= pd.read_csv('data/OLIST_ALL_DATA.csv')
date_columns = ['shipping_limit_date', 'review_creation_date', 'review_answer_timestamp', 'order_purchase_timestamp', 'order_estimated_delivery_date']
for col in date_columns:
    Olist[col] = pd.to_datetime(Olist[col], format='%Y-%m-%d %H:%M:%S')
    # creating a purchase day feature
sales_per_purchase_month = Olist.groupby(['order_purchase_month', 'order_purchase_mon', 'order_purchase_day'],
                                             as_index=False).payment_value.sum()
sales_per_purchase_month = sales_per_purchase_month.sort_values(by=['order_purchase_month'], ascending=True)

df = sales_per_purchase_month
fig1 = px.line(df, x="order_purchase_mon", y="payment_value", color='order_purchase_day',
                  title='Sales Each Month & Each DayofWeek')

fig1.update_layout(
        title="Sales Each Month & Each DayofWeek",
        xaxis_title="Months",
        yaxis_title="Sales(in $$)",
        # autosize=False,
        # width=700,
        # height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        xaxis =  { 'showgrid': False,'zeroline': True },
        yaxis = { 'showgrid': False,'zeroline': True},

        font=dict(
            family="Courier New, monospace",
            size=15,
            #color="#7f7f7f"
        )
    )
fig1.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1,
            y0=0,
            x1=1,
            y1=2,
            line=dict(
                color="RoyalBlue",
                width=3
            )
))

fig1.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=0,
            y0=0,
            x1=0,
            y1=500000,
            line=dict(
                color="white",
                width=2
            )
))


Olist['review_dayofweek'] = Olist.review_answer_timestamp.apply(lambda x: x.dayofweek)
Olist['review_day'] = Olist['review_dayofweek'].map({0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'})
Olist['review_month'] = Olist.review_answer_timestamp.apply(lambda x: x.month).map({1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'})
review_score_per_month = Olist.groupby(['review_month', 'review_day'], as_index=False).review_score.mean()
#review_score_per_month = review_score_per_month.sort_values(by=['review_day'], ascending=True)
review_score_per_month
df4 = review_score_per_month
rscore = px.line(df4, x="review_month", y="review_score", color='review_day', title='Sales Each Month & Each DayofWeek')
rscore.update_layout(
        title="Ratings Each Month & DayofWeek",
        xaxis_title="Months",
        yaxis_title="Review Ratings",
        # autosize=False,
        # width=700,
        # height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        xaxis =  { 'showgrid': False,'zeroline': True },
        yaxis = { 'showgrid': False,'zeroline': True},

        font=dict(
            family="Courier New, monospace",
            size=15,
            #color="#7f7f7f"
        )
    )



avg_score_per_category = Olist.groupby('product_category_name_english', as_index=False).agg({'review_score': ['count', 'mean']})
avg_score_per_category.columns = ['Product Category', 'Number of Reviews', 'Average Review Ratings']
avg_score_per_category = avg_score_per_category[avg_score_per_category['Number of Reviews'] > 100]
avg_score_per_category = avg_score_per_category.sort_values(by='Number of Reviews', ascending=False)
avg_ratings = avg_score_per_category[:20]
arscore = px.bar(avg_ratings, x='Product Category', y='Number of Reviews',
             hover_data=['Average Review Ratings'], color='Average Review Ratings',
             height=500)
arscore.update_layout(
        title="Average review ratings per category",

        # autosize=False,
        # width=700,
        # height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        xaxis =  { 'showgrid': False,'zeroline': True },
        yaxis = { 'showgrid': False,'zeroline': True},

        font=dict(
            family="Courier New, monospace",
            size=15,
            #color="#7f7f7f"
        )
    )
arscore.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1,
            y0=0,
            x1=1,
            y1=2,
            line=dict(
                color="RoyalBlue",
                width=3
            )
))

arscore.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=0,
            y0=0,
            x1=0,
            y1=5.0,
            line=dict(
                color="white",
                width=2
            )
))

total_rev_month = Olist.groupby(['order_purchase_year', 'order_purchase_mon', 'product_category_name_english'], as_index=False).payment_value.sum()
#total_rev_month = total_rev_month.sort_values(by=['order_purchase_year'], ascending=True)
total_rev_month.columns = ['Sales Year','Sales Month','Product Category' , 'Sales Revenue']
df = total_rev_month
YearlySales = px.sunburst(df, path=['Sales Year', 'Product Category'], values='Sales Revenue',
                  color='Sales Revenue', hover_data=['Sales Revenue'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['Sales Revenue'], weights=df['Sales Revenue']))

YearlySales.update_layout(
        title="Product Category Sales across Years",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        font=dict(
            family="Courier New, monospace",
            size=15,
            #color="#7f7f7f"
        )
    )

total_rev_hour = Olist[Olist['order_purchase_year'] == 2018].groupby(['order_purchase_hour', 'product_category_name_english'], as_index=False).payment_value.sum()
#total_rev_month = total_rev_month.sort_values(by=['order_purchase_year'], ascending=True)
total_rev_hour.columns = ['Sales Hour','Product Category' , 'Sales Revenue']
df = total_rev_hour
HourlyCategorySales = px.sunburst(df, path=['Sales Hour', 'Product Category'], values='Sales Revenue',
                  color='Sales Revenue', hover_data=['Product Category'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['Sales Revenue'], weights=df['Sales Revenue']))
#HourlyCategorySales.show()

HourlyCategorySales.update_layout(
        title="Product Category Sales by Hour",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        font=dict(
            family="Courier New, monospace",
            size=15,
            #color="#7f7f7f"
        )
    )




total_rev_day = Olist[Olist['order_purchase_year'] == 2018].groupby(['order_purchase_day', 'product_category_name_english'], as_index=False).payment_value.sum()
total_rev_day.columns = ['Sales DayofWeek','Product Category' , 'Sales Revenue']
total_rev_day

df = total_rev_day
DailyCategorySales = px.sunburst(df, path=['Sales DayofWeek', 'Product Category'], values='Sales Revenue',
                  color='Sales Revenue', hover_data=['Product Category'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['Sales Revenue'], weights=df['Sales Revenue']))
#DailyCategorySales.show()
DailyCategorySales.update_layout(
        title="Product Category Sales by Hour",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        font=dict(
            family="Courier New, monospace",
            size=15,
            #color="#7f7f7f"
        )
    )



Xtest = pd.read_csv('data/csvfordash/futurepurchase.csv')
labels = ['Class 0','Class 1','Class 2']
values = Xtest['Result'].value_counts()
fperc = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                             insidetextorientation='radial'
                            )])
fperc.update_layout(
        title="Future Purchase Customer Classes",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        font=dict(
            family="Courier New, monospace",
            size=15,
            #color="#7f7f7f"
        )
    )



app = dash.Dash(__name__)
app.config["suppress_callback_exceptions"] = True
server = app.server

image_filename = 'data/postofeed1.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

image_filename = 'data/negofeed.png' # replace with your own image
encoded_image2 = base64.b64encode(open(image_filename, 'rb').read())

image_filename = 'data/allfeed.png' # replace with your own image
encoded_image3 = base64.b64encode(open(image_filename, 'rb').read())

image_filename = 'data/geo1re.png' # replace with your own image
geo1 = base64.b64encode(open(image_filename, 'rb').read())


image_filename = 'data/zipcodesbrazil.png' # replace with your own image
zipcode = base64.b64encode(open(image_filename, 'rb').read())

image_filename = 'data/ordrevenue.png' # replace with your own image
orrev = base64.b64encode(open(image_filename, 'rb').read())

image_filename = 'data/freighratio.png' # replace with your own image
frratio = base64.b64encode(open(image_filename, 'rb').read())

image_filename = 'data/deliverydaystaken.png' # replace with your own image
delidays = base64.b64encode(open(image_filename, 'rb').read())

image_filename = 'data/olistthumbnail.png' # replace with your own image
thumbnail = base64.b64encode(open(image_filename, 'rb').read())






def build_banner():
    return html.Div(
        id="banner",
        className="banner",
        children=[
            html.Img(src='data:image/png;base64,{}'.format(thumbnail.decode())),
            html.Div(
                id="banner-text",
                children=[
                    html.H5("Digital Marketing"),
                    html.H6("Brazilian Olist-Ecommerce"),
                ],
            ),
            html.Div(
                id="banner-logo",
                children=[
                    html.Button(
                        id="learn-more-button", children="LEARN MORE", n_clicks=0
                    ),
                    html.Img(id="logo", src=app.get_asset_url("dash-logo-new.png")),
                ],
            ),
        ],
    )

def build_tabs():
    return html.Div(
        id="tabs",
        className="tabs",
        children=[
            dcc.Tabs(
                id="tabs-with-classes",
                value='tab1',
                className='custom-tabs',
                children=[
                    dcc.Tab(
                        id="Specs-tab",
                        label="Customer Segmentation and LifeTime Value",
                        value="tab1",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="Control-chart-tab",
                        label="Customer Behavior Analysis and Future Purchases",
                        value="tab2",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                                            id="Specs-tab2",
                                            label="Customer Satisfaction",
                                            value="tab3",
                                            className="custom-tab",
                                            selected_className="custom-tab--selected",
                                        ),
                                        dcc.Tab(
                                            id="Control-chart-tab2",
                                            label="Geospatial analysis",
                                            value="tab4",
                                            className="custom-tab",
                                            selected_className="custom-tab--selected",
                                        ),
                ],
            )
        ],
    )




app.layout = html.Div(
    id="big-app-container",
    children=[
        build_banner(),
        html.Div(
            id="app-container",
            children=[
                build_tabs(),
                # Main app
                html.Div(id='tabs-content-classes'),
            ],
        ),

    ],
)

@app.callback(
    Output(component_id='my-output', component_property='children'),
    [Input(component_id='my-input', component_property='value')]
)
def update_output_div(input_value):
    return 'Output: {}'.format(input_value)




classpred = pd.read_csv('data/csvfordash/futurepurchase1.csv')
# classpred.round({'Result': 0})
def ak(value):
    op = classpred.loc[classpred['customer_id'] == value]
    df2 = {'customer_id': 999, 'Result':''}
    p = op.append(df2, ignore_index=True)
    dd = p.at[0, 'Result']
    #dd = round(dd)
    print(dd)
    return dd

def atcl(value):
    op = classpred.loc[classpred['customer_id'] == value]
    df2 = {'customer_id': 999, 'Result':999,'prediction':''}
    p = op.append(df2, ignore_index=True)
    dd = p.at[0, 'prediction']
    print(dd)
    return dd

@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input-box', 'value')])
def update_output(n_clicks,value):
    p = ak(value)
    ki = atcl(value)
    #op = classpred.loc[classpred['customer_id']=='value']['Result'].values[0]
    return html.Div([
         html.Div(style={'font-family': 'Arial', 'margin-top': '30px','margin-left': '30px','font-size': '20px','font-weight': 'bold'},
                    children=['Entered customer id is "{}" and customer belongs to class "{}"'.format(value,p)]),
         html.Div(style={'font-family': 'Arial', 'margin-top': '30px', 'margin-left': '30px', 'font-size': '30px','font-weight': 'bold'},
                      children=['Customer will make next purchase in']),
        html.Div(style={'font-family': 'Lucida Sans Unicode','color':'Red','margin-top': '30px', 'margin-left': '50px', 'font-size': '50px',
                        'font-weight': 'bold'},
                 children=['{}'.format(ki)])

    ])



cussat = pd.read_csv('data/csvfordash/customersat.csv')
def satak(value):
    op = cussat.loc[cussat['customer_unique_id'] == value]
    df2 = {'customer_id': 999, 'Number of Reviews':'','Average Review Ratings':'','satprediction':''}
    p = op.append(df2, ignore_index=True)
    dd = p.at[0, 'satprediction']
    #dd = round(dd)
    print(dd)
    return dd

pp = cussat['satprediction'].value_counts()
s = pd.Series(pp)
a = s.loc['Unsatisfied']
b = s.loc[' Satisfied']
per = (b/(a+b))*100
per

csatlvl = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = per,
    mode = "gauge+number+delta",
    title = {'text': "Customer Satisfication %"},
    delta = {'reference': 70},
    gauge = {'axis': {'range': [None, 100]},
             'steps' : [
                 {'range': [0, 50], 'color': "lightgray"},
                 {'range': [50, 80], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 90}}))
csatlvl.update_layout(
        #title="Overall Customer Satisfaction ",
        #autosize=False,
        # width=700,
        # height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",

        font=dict(
            family="Courier New, monospace",
            size=15,
            #color="#7f7f7f"
        )
    )

@app.callback(
    dash.dependencies.Output('output-container-buttonpp', 'children'),
    [dash.dependencies.Input('buttonpp', 'n_clicks')],
    [dash.dependencies.State('input-boxpp', 'value')])
def update_output(n_clicks,value):
    sat = satak(value)
    #op = classpred.loc[classpred['customer_id']=='value']['Result'].values[0]
    return html.Div([
         html.Div(style={'font-family': 'Arial', 'margin-top': '30px','margin-left': '30px','font-size': '20px','font-weight': 'bold'},
                    children=['Entered customer id is "{}" and customer is'.format(value)]),
        html.Div(style={'font-family': 'Lucida Sans Unicode','color':'Red','margin-top': '30px', 'margin-left': '50px', 'font-size': '50px',
                        'font-weight': 'bold'},
                 children=['{}'.format(sat)])

    ])



@app.callback(Output('tabs-content-classes', 'children'),
              [Input('tabs-with-classes', 'value')])
def render_content(tab):
    if tab == 'tab1':
        return html.Div([
            html.Div(id='cseg1',style={'border':'1px white solid','float' :'left','width':'700px','height':'450px'},children = [dcc.Graph(figure=rfm_cseg)]),
            html.Div(style={'border':'1px white solid','padding-top': '70px','margin-left':'710px', 'width': '740px', 'height': '450px'},
                     children=[html.Img(src='data:image/png;base64,{}'.format(kmeans1.decode()))]),

            html.Div(style={'border': '1px white solid','background-color': '#171a28','float' :'left', 'margin-left': '0px', 'width': '576px', 'height': '450px'},
                     children=[dcc.Graph(figure=rfmrf)]),
            html.Div(style={'border': '1px white solid','background-color': '#171a28','float' :'left', 'width': '576px', 'height': '450px'},
                     children=[dcc.Graph(figure=rfmfm)]),
            html.Div(style={'border': '1px white solid','background-color': '#171a28','float' :'left', 'width': '573px',
                            'height': '450px'},
                     children=[dcc.Graph(figure=rfmrm)]),
            html.Div(style={'border': '1px white solid','background-color': '#171a28' ,'float': 'left', 'width': '1153px',
                            'height': '450px'},
                     children=[dcc.Graph(figure=cltv)]),
            html.Div(style={'border': '1px white solid', 'background-color': '#171a28', 'float': 'left', 'width': '576px',
                            'height': '450px'},
                     children=[dcc.Graph(figure=aptry)]),
            html.Div(style={'border': '1px white solid', 'background-color': '#171a28', 'padding-top':'40px','padding-left':'15px','float': 'left', 'width': '1153px','height': '800px'},
                     children=[html.Img(src='data:image/png;base64,{}'.format(palive.decode()))]),
            html.Div(style={'border': '1px white solid', 'background-color': '#171a28','float': 'left', 'width': '576px',
                            'height': '450px'},
                     children=[dcc.Graph(figure=urev)]),
            ]),

    elif tab == 'tab2':
        return html.Div([
            html.Div(id='cba1',style={'float':'left','background-color': '#171a28','border':'1px white solid','width':'1120px','height':'435px'},
            children=[dcc.Graph(figure=fig1)]),
            html.Div(style={'border': '1px white solid', 'background-color': '#171a28','margin-left': '1120px', 'width': '617px', 'height': '435px'},
            children=[dcc.Graph(figure=YearlySales)]),
            html.Div(style={'float':'left','background-color': '#171a28','margin-top': '0px','border': '1px white solid', 'width': '1120px', 'height': '430px'},
            children=[dcc.Graph(figure=rscore)]),
            html.Div(style={'border': '1px white solid','background-color': '#171a28', 'margin-left': '1120px', 'width': '617px', 'height': '430px'},
            children=[dcc.Graph(figure=HourlyCategorySales)]),
            html.Div(style={'float': 'left','background-color': '#171a28','margin-top': '10px', 'border': '1px white solid', 'width': '1120px', 'height': '500px'},
            children=[dcc.Graph(figure=arscore)]),
            html.Div(style={'border': '1px white solid', 'background-color': '#171a28','margin-top': '10px', 'margin-left': '1120px','width': '617px', 'height': '500px'},
            children=[dcc.Graph(figure=DailyCategorySales)]),
            html.Div(style={'float': 'left', 'background-color': '#171a28', 'margin-top': '10px',
                            'border': '1px white solid', 'width': '617px', 'height': '500px'},
                     children=[dcc.Graph(figure=fperc)]),
            html.Div(style={'border': '1px white solid','padding-top':'30px', 'background-color': '#171a28', 'margin-top': '10px',
                            'margin-left': '618px', 'width': '617px', 'height': '500px'},
                     children=[
                         html.Div(style={'font-family': 'Arial', 'margin-top': '10px','margin-left': '100px','font-size': '40px','font-weight': 'bold'},
                                 children=[
                         dcc.Input(id='input-box',placeholder='Enter Customer ID', type='text')]),
                         html.Div(style={'margin-left': '250px'},
                                  children=[html.Button('Submit', id='button')]),
                         html.Div(id='output-container-button',
                                  children='Enter a value and press submit')
                     ]),

        ])

    elif tab == 'tab3':
        return html.Div([
            html.Div(style={#'border':'1px white solid',
                            'float' :'left','width':'1020px','height':'520px'},children=[html.Img(src='data:image/png;base64,{}'.format(encoded_image3.decode()))]),
            html.Div(style={#'border-left':'1px white solid','border-top':'1px white solid',
                            #'border-right':'1px white solid',
                            'float': 'left', 'width': '710px', 'height': '420px'},children=[html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))]),
            html.Div(style={'float':'left',
                            #'border': '1px #fe2b54 solid',
                            'background-color': '#0f1423',
                            'margin-top': '0px',
                              'width': '700px', 'height': '100px'}),
            html.Div(style={'border': '1px white solid',
                            'float': 'left','background-color': '#0f1423', 'width': '1020px', 'height': '434px'},
                    children= [
                    html.Div(style={'float': 'left','border': '1px Red Solid','margin-top':'40px','margin-left':'40px','width': '600px', 'height':'350px'},
                     children=[
                         html.Div(style={'font-family': 'Arial', 'margin-top': '10px', 'margin-left': '100px',
                                         'font-size': '40px', 'font-weight': 'bold'},
                                  children=[
                                      dcc.Input(id='input-boxpp', placeholder='Enter Customer ID', type='text')]),
                         html.Div(style={'margin-left': '250px'},
                                  children=[html.Button('Submit', id='buttonpp')]),
                         html.Div(html.Div(children=[html.Div(
                             id='output-container-buttonpp', style={'margin-left': '70px'},
                                  children='Enter a value and press submit')]))
                     ]),
                   html.Div(style={'float': 'left','border': '1px Blue Solid','margin-top':'40px'#'margin-left':'700px'
                                    ,'width': '350px', 'height':'350px'},
                            children=[dcc.Graph(figure=csatlvl)]
                            )]
                    ),
            html.Div(id='negfed',children=[html.Div(id='negfed1',style={'float' :'left','width':'100px','height':'434px'}),
                html.Div(id = 'negfed3',style={#'border-bottom':'1px white solid',
                                               'float' :'left','width':'490px','height':'434px'},children=html.Img(src='data:image/png;base64,{}'.format(encoded_image2.decode()))),
                html.Div(id='negfed2',style={
                    #'border-bottom':'1px white solid',
                                           'float':'left','width': '110px', 'height': '434px'})]),

            #html.H3('Tab content 3')
        ])
    elif tab == 'tab4':
        return html.Div([
            html.Div(style={'float' :'left','margin-left':'1px','padding-top':'10px','padding-left':'10px','border':'1px white solid','width': '868px', 'height': '700px'},
                     children=#html.H5("Zip codes in Brazil"
                     html.Img(src='data:image/png;base64,{}'.format(zipcode.decode())) ),
            html.Div(style={'border': '1px white solid','margin-top':'10px','margin-left':'876px','padding-top':'10px','padding-left':'10px','width': '872px', 'height': '700px'},
                     children= #html.H5("Orders Revenue (thousands R$)"
                     html.Img(src='data:image/png;base64,{}'.format(orrev.decode()))   ),
            html.Div(style={'float': 'left', 'margin-top':'10px','margin-left': '1px','padding-top':'10px','padding-left':'10px', 'border': '1px white solid', 'width': '868px','height': '700px'},
                     children=#html.H5("Orders Average Freight Ratio"
                     html.Img(src='data:image/png;base64,{}'.format(frratio.decode()))   ),
            html.Div(style={'border': '1px white solid','margin-top':'10px','margin-left': '876px','padding-top':'10px','padding-left':'10px', 'width': '872px', 'height': '700px'},
                     children=#html.H5("Orders Average Delivery Time (days)"
                     html.Img(src='data:image/png;base64,{}'.format(delidays.decode()))   ),
        ])


if __name__ == '__main__':
    app.run_server(debug=True)