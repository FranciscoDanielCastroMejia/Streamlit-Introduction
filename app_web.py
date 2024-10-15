import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd

logo = Image.open('Wikimedia-logo.png')
#to change the name of the app web
st.set_page_config(page_title='Second APP', page_icon=logo, layout='wide', 
                   initial_sidebar_state='collapsed')



def main():


    st.title('My Second APP')

    
    
    st.sidebar.header("Navegation")

    st.divider()#add a divider line
    #_______________Plot of a dataframe ____________________
    st.markdown('### Plot of a dataframe')
    df = pd.read_csv('StudentPerformanceFactors.csv')
    st.dataframe(df)
    df_count = df.groupby('School_Type').count().reset_index()
    st.dataframe(df_count)
    fig = px.pie(df_count, values="Hours_Studied", names='School_Type', title="Hours studied in Diferent schools")
    st.plotly_chart(fig)

    st.divider()#add a divider line
    st.markdown('#### Second graphic')
    df_avg = df.groupby('Motivation_Level')['Hours_Studied'].mean().reset_index()
    st.dataframe(df_avg)
    fig2 = px.bar(df_avg, "Motivation_Level", 'Hours_Studied', color='Motivation_Level')
    st.plotly_chart(fig2)


if __name__ == '__main__':
    main()
