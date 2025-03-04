import streamlit as st

st.set_page_config(layout = 'wide', page_title = '👕 Cloth Sales prediction 👕')

home = st.Page(
    page = "/Streamlit/ViewPage/Home.py", 
    title = "Home", 
    icon = '🏠' 
)

dataExploration = st.Page(
    page = "../clothing-sales-prediction/Streamlit/ViewPage/Data_Exploration.py", 
    title = "Data Exploration", 
    icon = '📊' 
)

modelTraining = st.Page(
    page = "../clothing-sales-prediction/Streamlit/ViewPage/Model_Training.py", 
    title = "Model Training", 
    icon = '🤖' 
)

prediction = st.Page(
    page = "../clothing-sales-prediction/Streamlit/ViewPage/Prediction.py", 
    title = "Prediction", 
    icon = '🎯' 
)

conclusion = st.Page(
    page = "../clothing-sales-prediction/Streamlit/ViewPage/Conclusion.py", 
    title = "Conclusion", 
    icon = '🔍' 
)

st.logo('./Streamlit/assets/logo.png', size = 'large')

pg = st.navigation({
    '👕 Cloth Sales prediction 👕':[home, dataExploration, modelTraining, prediction, conclusion],
    

})

pg.run()