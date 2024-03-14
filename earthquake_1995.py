
import plotly.express as px
import pandas as pd
import streamlit as st

dff = pd.read_csv('cleaned_dff.csv')
mon_highest = dff.groupby('Month_Name')['Year'].count().sort_values( ascending=False).reset_index().head(10)
df_time = dff.groupby(['Year','tsunami'])['sig'].sum().reset_index().sort_values(by= 'sig')
occu_avg = dff.groupby(['net','tsunami'])['sig'].size().sort_values(ascending= False).reset_index()
impact = dff.groupby(['location','nst'])['sig'].size().sort_values(ascending= False).reset_index().head(500)
algorithms = dff.groupby(['magtype','tsunami'])['sig'].mean().sort_values(ascending= False).reset_index()
earthquakes_avg = dff.groupby(['location','magnitude'])['title'].count().sort_values(ascending= False).reset_index().head(100)
affected = dff.groupby(['alert','mmi'])['sig'].count().sort_values(ascending= False).reset_index()
#earthquakes_avg = dff.groupby(['location','magnitude'])['alert'].count().sort_values(ascending= False).reset_index().head(100)



st.title('earthquake from 1995 to 2023')

page =  st.sidebar.radio('Select page', ['About','Univariate Analysis', 'Bivariate Analysis', 'Multivariate Analysis'])


if page == 'About':
    
    def main():
        
        st.title('About Suberstore Project')
        st.write(dff)
        
    if __name__ == '__main__':

        main()
        
if page == 'Univariate Analysis':

    def main():
    
        # create tabs of numerical and categorical features
        tab1, tab2 = st.tabs(['Numerical Features', 'Categorical Features'])
        
        # Numerical Features
        num_cols = dff.select_dtypes(exclude= 'object').columns
        
        for col in num_cols:
            tab1.plotly_chart(px.histogram(dff, x = col))
            
        # Categorical features
        cat_cols = dff.select_dtypes(include= 'object').columns
        
        for col in cat_cols:
            tab2.plotly_chart(px.histogram(dff, x = col))
            
            
    if __name__ == '__main__':

        main()
    
elif page == 'Bivariate Analysis':
    
    def main():
        
        st.write('# Numerical features VS Target Variable')
        
        # Create selection box for features and plots
        select_col = st.selectbox('Select Feature', ['magnitude', 'mmi', 'tsunami', 'sig', 'nst',
         'latitude', 'longitude','Year'])
        
        select_plot = st.selectbox('Select Plot Type', ['Box plot', 'Violin Plot', 'Bar Chart Plot'])
        
        if select_plot == 'Box plot':
            
            st.plotly_chart(px.box(dff, x= 'title', y= select_col))
            
        elif select_plot == 'Violin Plot':
            
            st.plotly_chart(px.violin(dff, x= 'title', y= select_col))

        else:
            
            st.plotly_chart(px.bar(dff, x= 'title', y= select_col))
        
    if __name__ == '__main__':

        main()
        
else:
    
    def main():
        
        st.header('1- The most common alert and its impact on the event?') 
        
        st.plotly_chart(px.scatter(dff, x='alert' , y='sig',  color='tsunami',title='Relation Ship btn cdi  vs mmi'))
        
        st.header('Which months witness the highest seismic activity during the year?')
        
        st.plotly_chart(px.pie(mon_highest, names='Month_Name', values='Year',color='Month_Name'))   
        
        st.header('Is there a change in the intensity of earthquakes over time? Is there any effect of a tsunami?')
        
        st.plotly_chart( px.line(df_time, x= 'sig', y= ['Year'],  color= 'tsunami', title= 'Total earthquakes & tsunami over Time Period (1995-2023)'))
        
        st.header(' What is the most media coverage of the event?')
        
        st.plotly_chart(px.bar(occu_avg, x= 'net', y= 'sig',color='tsunami'))
        
        st.header('What is the impact of the presence of stations inside residential areas?')
        
        st.plotly_chart(px.bar(impact, x= 'location', y= 'sig',color='nst'))
        
        st.header('Average impact of algorithms on event importance')
        
        st.plotly_chart(px.bar(algorithms, x= 'magtype', y= 'sig', color= 'tsunami' ))
        
        st.header('How many earthquakes have occurred in certain places and what is the magnitude of the earthquake’s intensity?')
        
        st.plotly_chart(px.bar(earthquakes_avg, x= 'location', y= 'title', color= 'magnitude'))
        
        st.header('What is the alert rate affected by the event?')
        
        st.plotly_chart(px.bar(affected, x= 'alert', y= 'sig',color= 'mmi'))
        
        #st.header('The relationship between all the data')
        
        #st.plotly_chart(px.bar(earthquakes, x= 'location', y= 'title', color= 'magnitude'))

      
    if __name__ == '__main__':
        
        main()    
