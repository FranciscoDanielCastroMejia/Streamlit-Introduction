import streamlit as st
import pandas as pd
from PIL import Image

df = pd.read_csv('StudentPerformanceFactors.csv')
df2 = df.sample(n=1000, random_state=42)
df3 = df2.apply(pd.to_numeric, errors='coerce')


def main():
    st.title("My First app")
    st.divider()#add a divider line
    
    #_______________Styles of text ____________________
    st.markdown('### Styles of text')

    st.header("Header")
    st.subheader("Sub header")
    st.text("Text")
    st.markdown('### Markdown')

    st.success("Victoria")
    st.warning("Esto es una advertencia")
    st.info("Mensaje de informacion")
    st.error('Mensaje de error')
    st.exception("Esto es una excepcion")
    
    st.write()
    
   
    st.divider()#add a divider line
    #_______________DATAFRAME ____________________

    st.markdown('### DATAFRAME')
    st.text('Original Dataframe')
    st.dataframe(df)
    st.text('5 Random Data from the original dataframe')
    st.dataframe(df2.head())
    st.text('1000 Random data with filters')
    st.dataframe(df3.style.highlight_max(axis=0))

    st.divider()#add a divider line
    #_______________JSONFILE ____________________

    st.markdown('### JSON FILE')
    st.json({"link":"valor"})
    
    
    st.divider()#add a divider line
    #_______________CODE ____________________

    st.markdown('### CODE')
    codigo = """
    def saludar():
        print("Hola")
    
    """
    st.code(codigo, language="python")


    

    # 
    st.divider()#add a divider line
    #_______________Selectbox ____________________

    st.markdown('### SELECTBOX')
    
    option = st.selectbox(
        'Select your favorite fruit',
        ['Apple', 'Orange', 'Banana', 'Strawberry']
    )

    st.write(f'Your favorite fruit is: {option}')

    options = st.multiselect(
        'Select your favorite colors',
        ['Red', 'Green', 'Orange', 'Blue', 'Black', 'Yellow']
    )

    st.write('Your favorite Color is: ',options)

    st.divider()#add a divider line
    #_______________SLIDERS____________________

    st.markdown('### SLIDERS')
    age = st.slider(
        'Select your age:',
        min_value=0,
        max_value=100,
        value=25, #initial value
        step=1
    )

    st.write('Your age is', age)

    level = st.select_slider(
        'Select your level of satisfaction:',
        options=['very low', 'low', 'mid', 'high', 'very high'],
        value='mid', #initial value
    )

    st.write('Your level of satisfaction is:', level)
    st.divider()#add a divider line
    #_______________MULTIMEDIA____________________

    st.markdown('### MULTIMEDIA')
    st.markdown('#### Images')

    img = Image.open('tiger.jpg')
    st.image(img, use_column_width=True)

    st.markdown('#### MP3')
    with open('sample-9s.mp3', 'rb') as audio_file:
        st.audio(audio_file.read())

    st.divider()#add a divider line
    #_______________TEXT INPUT____________________

    st.markdown('### TEXT INPUT')
    
    name = st.text_input('Input your name')
    st.write(name)

    message = st.text_area('Input your message', height=100)
    st.write(message)

    st.divider()#add a divider line
    #_______________NUMBER INPUT____________________

    st.markdown('### NUMBER INPUT')

    number = st.number_input('Input a number', 1.0, 25.0, step=1.0)
    st.write(number)

    st.divider()#add a divider line
    #_______________DATE and hour INPUT____________________

    st.markdown('### DATE INPUT')
    date = st.date_input('Select a date')
    st.write(date)
    hour = st.time_input('Select a hour')
    st.write(hour)

    st.divider()#add a divider line
    #_______________SELECT COLOR____________________

    st.markdown('### SELECT COLOR')
    color = st.color_picker('Select a color')
    st.write(color)





    


if __name__== '__main__':
    main()