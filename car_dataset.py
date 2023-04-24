import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

link="https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"

df_car=pd.read_csv(link)
df_car



choice = st.sidebar.radio("Select the Topic", ('Correlation', 'Distribuition','Distribuition of Cylinders by Region'))
if choice=='Correlation':
    st.header('Correltion cubicinches how long of the years')
    viz1=sns.scatterplot(x="year", y="cubicinches", data=df_car)
    plt.figure(figsize=(12,6))
    st.pyplot(viz1.figure)
    st.write("we found that higher cubicinches (>350) were produced until 1978 and infrequently in this time period.")

if choice=='Distribuition':
    st.header('Distribuition of Cylinders')
    distribution=sns.distplot(df_car['cylinders'], bins=6, hist=True, kde=True, rug=False)
    plt.figure(figsize=(12,6))
    st.pyplot(distribution.figure)

if choice=='Distribuition of Cylinders by Region':
    st.header('Distribuition of Cylinders')
    Regions=st.sidebar.selectbox('Select Region', ('Europe', 'US','Japan'))
    if Regions=='Europe':
        viz3=sns.distplot(df_car['continent'].loc['Europe.'], bins=6, hist=True, kde=True, rug=False)
        viz3.set_title("Distribution of Cylinders by year")
        st.pyplot(viz3.figure)
        
    if Regions=='US':
        viz4=sns.distplot(df_car['continent'].loc['US.'], bins=6, hist=True, kde=True, rug=False)
        viz4.set_title("Distribution of Cylinders by year")
        st.pyplot(viz4.figure)
   
    if Regions=='Japan':
        viz4=sns.distplot(df_car['continent'].loc['Japan.'], bins=6, hist=True, kde=True, rug=False)
        viz4.set_title("Distribution of Cylinders by year")
        st.pyplot(viz4.figure)


      
    #distribution=sns.distplot(df_car['cylinders'], bins=6, hist=True, kde=True, rug=False)
    #plt.figure(figsize=(12,6))
    
       
#Filter Data
#options = list(df_car['continent'].unique())
#options.append("All continents")

#st.selectbox('Select Region', options, index=3)



##distribution = df_car['cylinders'].value_counts()

 #if len(dropdown) > 0:
          #  df=df_car['Continent']==dropdown

#if st.selectbox('Select Region', options, index=3) == "Europe.":
    

#if select == "Europe":
    #years_ms = st.sidebar.radio("Select the Year:", 
    #options=[2021,2022,2023])
    
    
    #fig_hr = drawHr(years_ms)
    #st.pyplot(fig_hr)

        
#def drawCil():
#

#st.write("The preference is the cars with 4 cylinders and than for 8 cylinders")

#st.write("**Note:** Not finished yet.")


