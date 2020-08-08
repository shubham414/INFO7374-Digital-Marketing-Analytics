import streamlit as st

def display_about():
    st.write("")


def display_sidebar():
    st.sidebar.markdown('---')
    
    # st.sidebar.title('Contribute')
    # st.sidebar.info('This is an open source project, you are very welcome to contribute something awesome by commenting, \
    #     feature requests, pull requests, and by raising [defects](https://github.com/QAInsights/Streamlit-JMeter/issues).')
    st.sidebar.title('About')

    st.sidebar.info('This app has been developed by [Shubham Mahajan](https://shubhammahajan714.wixsite.com/portfolio), [Gauri Verma](https://github.com/gauriverma19), [Anurag Rachcha](https://github.com/AnuragRachcha) using [Python](https://www.python.org/), \
    [Streamlit](https://streamlit.io/) [Fast API] (https://fastapi.tiangolo.com/), and [Vega Lite](https://vega.github.io/vega-lite/). You can checkout the source code at \[GitHub](https://github.com//Streamlit-JMeter).')