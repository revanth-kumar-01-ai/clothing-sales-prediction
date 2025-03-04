import streamlit as st
from Streamlit import config

st.set_page_config(layout = 'wide', page_title = config.PROJECT_NAME)

print(config.PROJECT_NAME)

home = st.Page(
    page = "./Streamlit/ViewPage/Home.py", 
    title = "Home", 
    icon = '🏠' 
)

dataExploration = st.Page(
    page = "./Streamlit/ViewPage/Data_Exploration.py", 
    title = "Data Exploration", 
    icon = '📊' 
)

modelTraining = st.Page(
    page = "./Streamlit/ViewPage/Model_Training.py", 
    title = "Model Training", 
    icon = '🤖' 
)

prediction = st.Page(
    page = "./Streamlit/ViewPage/Prediction.py", 
    title = "Prediction", 
    icon = '🎯' 
)

conclusion = st.Page(
    page = "./Streamlit/ViewPage/Conclusion.py", 
    title = "Conclusion", 
    icon = '🔍' 
)

st.logo('./Streamlit/assets/logo.png', size = 'large')

pg = st.navigation({
    config.PROJECT_NAME:[home, dataExploration, modelTraining, prediction, conclusion],

})

pg.run()