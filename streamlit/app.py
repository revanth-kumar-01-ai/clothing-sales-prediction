import streamlit as st

st.set_page_config(layout = 'wide', page_title = "Cloths ")

home = st.Page(
    page = "./ViewPage/Home.py", 
    title = "Home", 
    icon = '🏠' 
)

dataExploration = st.Page(
    page = "./ViewPage/Data_Exploration.py", 
    title = "Data Exploration", 
    icon = '📊' 
)

modelTraining = st.Page(
    page = "./ViewPage/Model_Training.py", 
    title = "Model Training", 
    icon = '🤖' 
)

prediction = st.Page(
    page = "./ViewPage/Prediction.py", 
    title = "Prediction", 
    icon = '🎯' 
)

conclusion = st.Page(
    page = "./ViewPage/Conclusion.py", 
    title = "Conclusion", 
    icon = '🔍' 
)

st.logo('assets/logo.png', size = 'large')

pg = st.navigation({
    "cloths":[home, dataExploration, modelTraining, prediction, conclusion]
})

pg.run()