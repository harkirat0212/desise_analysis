import streamlit as st
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

with st.sidebar:
    opt=option_menu("Menu",["Home","Graphs","About"],icons=["house","bar-chart","people"],menu_icon="cast",default_index=0)

if opt=="Home":
    with st.container():
        
        st.header("Introduction")
        st.write("Chronic diseases such as diabetes and heart disease are among the leading causes of morbidity and mortality worldwide, presenting significant challenges to public health systems. These conditions are often interrelated and share common risk factors, including unhealthy diets, physical inactivity, and genetic predispositions. Diabetes, characterized by elevated blood glucose levels, can lead to severe complications like kidney failure, blindness, and limb amputations. Heart disease, encompassing conditions such as coronary artery disease, heart attacks, and heart failure, remains the primary cause of death globally. Understanding the epidemiology, risk factors, and outcomes of these diseases is crucial for developing effective prevention and management strategies.")
    
    with st.container():
        st.write("---")
        c1,c2=st.columns(2)
        with c1:
            st.header("Objectives")
        
            st.write(
                """The primary objectives of this study are as follows:

1. *Epidemiological Analysis*:
   - To assess the prevalence and incidence rates of diabetes and heart disease across different populations and regions.
   - To identify temporal trends and variations in disease occurrence over time.

2. *Risk Factor Identification*:
   - To investigate the correlation between various demographic, socioeconomic, and lifestyle factors and the risk of developing diabetes and heart disease.
   - To identify high-risk groups based on age, gender, ethnicity, and other relevant factors.

3. *Data Preprocessing and Cleaning*:
   - To ensure the accuracy and consistency of the datasets through meticulous data cleaning and preprocessing.
   - To handle missing values, outliers, and other data quality issues effectively.
"""
                )

        with c2:
            st.write("##")
            st.write("##")
            
            st.image("images.jpeg")
            
            st.image("img.png")

elif opt=="Graphs":
    
    a=st.sidebar.selectbox("Select Continents",options=["Globe","Asian","African","American","European"])
    
    if a=="Globe": 

        op= st.selectbox("Select Year",options=[1990,2000,2010,2019])
        if op==1990:
            
            data = pd.read_csv("globe.csv")
            year = 1990
            filtered_data = data[data['Year'] == year]

            # Select the columns for causes of death
            causes_of_death = [
                'Meningitis',
                "Alzheimer's Disease and Other Dementias", "Parkinson's Disease",
                'Nutritional Deficiencies', 'Malaria', 'Drowning', 'Maternal Disorders',
                'HIV/AIDS', 'Tuberculosis', 'Cardiovascular Diseases',
                'Lower Respiratory Infections', 'Neonatal Disorders',
                'Diarrheal Diseases', 'Neoplasms', 'Diabetes Mellitus',
                'Chronic Kidney Disease', 'Protein-Energy Malnutrition',
                'Chronic Respiratory Diseases',
                'Cirrhosis and Other Chronic Liver Diseases', 'Digestive Diseases'

            ]

            # Aggregate data for the selected year
            deaths_by_cause = filtered_data[causes_of_death].sum().reset_index()
            deaths_by_cause.columns = ['Cause of Death', 'Number of Deaths']

            # Create a bar chart
            fig = px.bar(deaths_by_cause,
                        x='Cause of Death',
                        y='Number of Deaths',
                        title=f'Number of Deaths by Cause in {year}',
                        labels={'Number of Deaths':'Number of Deaths', 'Cause of Death':'Cause of Death'},
                        text='Number of Deaths')

            # Customize layout for better appearance
            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig)


            # Create a geographical map
            fig = px.choropleth(filtered_data,
                                    locations='Country/Territory',
                                    locationmode='country names',
                                    color='Cardiovascular Diseases',
                                    hover_name='Country/Territory',
                                    color_continuous_scale=px.colors.sequential.Plasma,
                                    title=f'Cardiovascular Diseases Deaths in {year}')

            st.plotly_chart(fig)
            

            # Create a bubble chart
            fig = px.scatter(filtered_data,
                            x='Cardiovascular Diseases',
                            y='Neoplasms',
                            size='Cardiovascular Diseases',
                            color='Country/Territory',
                            hover_name='Country/Territory',
                            size_max=60,
                            title=f'Cardiovascular Diseases vs Neoplasm in {year}')

            # Show the plot
            st.plotly_chart(fig)
   
        elif op==2000:
            data=pd.read_csv("globe.csv")
            year = 2000
            filtered_data = data[data['Year'] == year]

            # Select the columns for causes of death
            causes_of_death = [
                'Meningitis',
                "Alzheimer's Disease and Other Dementias", "Parkinson's Disease",
                'Nutritional Deficiencies', 'Malaria', 'Drowning', 'Maternal Disorders',
                'HIV/AIDS', 'Tuberculosis', 'Cardiovascular Diseases',
                'Lower Respiratory Infections', 'Neonatal Disorders',
                'Diarrheal Diseases', 'Neoplasms', 'Diabetes Mellitus',
                'Chronic Kidney Disease', 'Protein-Energy Malnutrition',
                'Chronic Respiratory Diseases',
                'Cirrhosis and Other Chronic Liver Diseases', 'Digestive Diseases'
            ]

            # Aggregate data for the selected year
            deaths_by_cause = filtered_data[causes_of_death].sum().reset_index()
            deaths_by_cause.columns = ['Cause of Death', 'Number of Deaths']

            # Create a pie chart
            fig = px.pie(deaths_by_cause,
                        names='Cause of Death',
                        values='Number of Deaths',
                        title=f'Proportion of Deaths by Cause in {year}',
                        hole=0.4)  # Optional: add a hole in the center to create a donut chart
            st.plotly_chart(fig)

            fig = px.choropleth(filtered_data,
                                    locations='Country/Territory',
                                    locationmode='country names',
                                    color='Cardiovascular Diseases',
                                    hover_name='Country/Territory',
                                    color_continuous_scale=px.colors.sequential.Plasma,
                                    title=f'Cardiovascular Diseases Deaths in {year}')

            st.plotly_chart(fig)

            fig = px.scatter(filtered_data,
                            x='Cardiovascular Diseases',
                            y='Neoplasms',
                            size='Cardiovascular Diseases',
                            color='Country/Territory',
                            hover_name='Country/Territory',
                            size_max=60,
                            title=f'Cardiovascular Diseases vs Neoplasm in {year}')

            st.plotly_chart(fig)

        elif op==2010:
            
            data = pd.read_csv("globe.csv")
            year = 2010
            filtered_data = data[data['Year'] == year]

            # Select the columns for causes of death
            causes_of_death = [
                'Meningitis',
                "Alzheimer's Disease and Other Dementias", "Parkinson's Disease",
                'Nutritional Deficiencies', 'Malaria', 'Drowning', 'Maternal Disorders',
                'HIV/AIDS', 'Tuberculosis', 'Cardiovascular Diseases',
                'Lower Respiratory Infections', 'Neonatal Disorders',
                'Diarrheal Diseases', 'Neoplasms', 'Diabetes Mellitus',
                'Chronic Kidney Disease', 'Protein-Energy Malnutrition',
                'Chronic Respiratory Diseases',
                'Cirrhosis and Other Chronic Liver Diseases', 'Digestive Diseases'

            ]

            # Aggregate data for the selected year
            deaths_by_cause = filtered_data[causes_of_death].sum().reset_index()
            deaths_by_cause.columns = ['Cause of Death', 'Number of Deaths']

            # Create a bar chart
            fig = px.bar(deaths_by_cause,
                        x='Cause of Death',
                        y='Number of Deaths',
                        title=f'Number of Deaths by Cause in {year}',
                        labels={'Number of Deaths':'Number of Deaths', 'Cause of Death':'Cause of Death'},
                        text='Number of Deaths')

            # Customize layout for better appearance
            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig)


             # Create a geographical map
            fig = px.choropleth(filtered_data,
                                    locations='Country/Territory',
                                    locationmode='country names',
                                    color='Cardiovascular Diseases',
                                    hover_name='Country/Territory',
                                    color_continuous_scale=px.colors.sequential.Plasma,
                                    title=f'Cardiovascular Diseases Deaths in {year}')

            st.plotly_chart(fig)
            

            # Create a bubble chart
            fig = px.scatter(filtered_data,
                            x='Cardiovascular Diseases',
                            y='Neoplasms',
                            size='Cardiovascular Diseases',
                            color='Country/Territory',
                            hover_name='Country/Territory',
                            size_max=60,
                            title=f'Cardiovascular Diseases vs Neoplasm in {year}')

            st.plotly_chart(fig)

        elif op==2019:
            data=pd.read_csv("globe.csv")
            year = 2019
            filtered_data = data[data['Year'] == year]

            # Select the columns for causes of death
            causes_of_death = [
                'Meningitis',
                "Alzheimer's Disease and Other Dementias", "Parkinson's Disease",
                'Nutritional Deficiencies', 'Malaria', 'Drowning', 'Maternal Disorders',
                'HIV/AIDS', 'Tuberculosis', 'Cardiovascular Diseases',
                'Lower Respiratory Infections', 'Neonatal Disorders',
                'Diarrheal Diseases', 'Neoplasms', 'Diabetes Mellitus',
                'Chronic Kidney Disease', 'Protein-Energy Malnutrition',
                'Chronic Respiratory Diseases',
                'Cirrhosis and Other Chronic Liver Diseases', 'Digestive Diseases'
            ]

            # Aggregate data for the selected year
            deaths_by_cause = filtered_data[causes_of_death].sum().reset_index()
            deaths_by_cause.columns = ['Cause of Death', 'Number of Deaths']

            # Create a pie chart
            fig = px.pie(deaths_by_cause,
                        names='Cause of Death',
                        values='Number of Deaths',
                        title=f'Proportion of Deaths by Cause in {year}',
                        hole=0.4)  # Optional: add a hole in the center to create a donut chart
            st.plotly_chart(fig)

            fig = px.choropleth(filtered_data,
                                    locations='Country/Territory',
                                    locationmode='country names',
                                    color='Cardiovascular Diseases',
                                    hover_name='Country/Territory',
                                    color_continuous_scale=px.colors.sequential.Plasma,
                                    title=f'Cardiovascular Diseases Deaths in {year}')

            st.plotly_chart(fig)

            fig = px.scatter(filtered_data,
                            x='Cardiovascular Diseases',
                            y='Neoplasms',
                            size='Cardiovascular Diseases',
                            color='Country/Territory',
                            hover_name='Country/Territory',
                            size_max=60,
                            title=f'Cardiovascular Diseases vs Neoplasm in {year}')

            st.plotly_chart(fig)
            
            
    elif a=="Asian":
        data=pd.read_csv("asia.csv")
        st.title("Dataset of Asia")
        st.dataframe(data)

        data = pd.read_csv("asia.csv")
        
        opt=st.selectbox("Select Year",options=[1990,2000,2010,2019])
        if opt==1990:
            filtered_data=data[data.loc[:,"Year"]==1990]
            causes_of_death = [
                    'Meningitis',
                    "Alzheimer's Disease and Other Dementias", "Parkinson's Disease",
                    'Nutritional Deficiencies', 'Malaria', 'Drowning', 'Maternal Disorders',
                    'HIV/AIDS', 'Tuberculosis', 'Cardiovascular Diseases',
                    'Lower Respiratory Infections', 'Neonatal Disorders',
                    'Diarrheal Diseases', 'Neoplasms', 'Diabetes Mellitus',
                    'Chronic Kidney Disease', 'Protein-Energy Malnutrition',
                    'Chronic Respiratory Diseases',
                    'Cirrhosis and Other Chronic Liver Diseases', 'Digestive Diseases'

                ]

                # Aggregate data for the selected year
            deaths_by_cause = filtered_data[causes_of_death].sum().reset_index()
            deaths_by_cause.columns = ['Cause of Death', 'Number of Deaths']

                # Create a bar chart
            fig = px.bar(deaths_by_cause,
                            x='Cause of Death',
                            y='Number of Deaths',
                            title=f'Number of Deaths by Cause in {1990}',
                            labels={'Number of Deaths':'Number of Deaths', 'Cause of Death':'Cause of Death'},
                            text='Number of Deaths')

                # Customize layout for better appearance
            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig)

           
            year = 1990
            filtered_data = data[data['Year'] == year]

            # Create a bubble chart
            fig = px.scatter(filtered_data,
                            x='Cardiovascular Diseases',
                            y='Neoplasms',
                            size='Cardiovascular Diseases',
                            color='Country/Territory',
                            hover_name='Country/Territory',
                            size_max=60,
                            title=f'Cardiovascular Diseases vs Neoplasms in {year}')

            # Show the plot
            st.plotly_chart(fig)

        elif opt==2000:
            filtered_data=data[data.loc[:,"Year"]==2000]
            causes_of_death = [
                    'Meningitis',
                    "Alzheimer's Disease and Other Dementias", "Parkinson's Disease",
                    'Nutritional Deficiencies', 'Malaria', 'Drowning', 'Maternal Disorders',
                    'HIV/AIDS', 'Tuberculosis', 'Cardiovascular Diseases',
                    'Lower Respiratory Infections', 'Neonatal Disorders',
                    'Diarrheal Diseases', 'Neoplasms', 'Diabetes Mellitus',
                    'Chronic Kidney Disease', 'Protein-Energy Malnutrition',
                    'Chronic Respiratory Diseases',
                    'Cirrhosis and Other Chronic Liver Diseases', 'Digestive Diseases'

                ]

                # Aggregate data for the selected year
            deaths_by_cause = filtered_data[causes_of_death].sum().reset_index()
            deaths_by_cause.columns = ['Cause of Death', 'Number of Deaths']

                # Create a bar chart
            fig = px.bar(deaths_by_cause,
                            x='Cause of Death',
                            y='Number of Deaths',
                            title=f'Number of Deaths by Cause in {2000}',
                            labels={'Number of Deaths':'Number of Deaths', 'Cause of Death':'Cause of Death'},
                            text='Number of Deaths')

                # Customize layout for better appearance
            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig)

         
            fig = px.scatter(filtered_data,
                            x='Cardiovascular Diseases',
                            y='Neoplasms',
                            size='Cardiovascular Diseases',
                            color='Country/Territory',
                            hover_name='Country/Territory',
                            size_max=60,
                            title=f'Cardiovascular Diseases vs Neoplasms in {2000}')

            # Show the plot
            st.plotly_chart(fig)

        elif opt==2010:
            filtered_data=data[data.loc[:,"Year"]==2010]
            causes_of_death = [
                    'Meningitis',
                    "Alzheimer's Disease and Other Dementias", "Parkinson's Disease",
                    'Nutritional Deficiencies', 'Malaria', 'Drowning', 'Maternal Disorders',
                    'HIV/AIDS', 'Tuberculosis', 'Cardiovascular Diseases',
                    'Lower Respiratory Infections', 'Neonatal Disorders',
                    'Diarrheal Diseases', 'Neoplasms', 'Diabetes Mellitus',
                    'Chronic Kidney Disease', 'Protein-Energy Malnutrition',
                    'Chronic Respiratory Diseases',
                    'Cirrhosis and Other Chronic Liver Diseases', 'Digestive Diseases'

                ]

            # Aggregate data for the selected year
            deaths_by_cause = filtered_data[causes_of_death].sum().reset_index()
            deaths_by_cause.columns = ['Cause of Death', 'Number of Deaths']

            # Create a bar chart
            fig = px.bar(deaths_by_cause,
                            x='Cause of Death',
                            y='Number of Deaths',
                            title=f'Number of Deaths by Cause in {2010}',
                            labels={'Number of Deaths':'Number of Deaths', 'Cause of Death':'Cause of Death'},
                            text='Number of Deaths')

             # Customize layout for better appearance
            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig)

           
            fig = px.scatter(filtered_data,
                            x='Cardiovascular Diseases',
                            y='Neoplasms',
                            size='Cardiovascular Diseases',
                            color='Country/Territory',
                            hover_name='Country/Territory',
                            size_max=60,
                            title=f'Cardiovascular Diseases vs Neoplasms in {2010}')

            # Show the plot
            st.plotly_chart(fig)

        else:
            filtered_data=data[data.loc[:,"Year"]==2019]
            causes_of_death = [
                    'Meningitis',
                    "Alzheimer's Disease and Other Dementias", "Parkinson's Disease",
                    'Nutritional Deficiencies', 'Malaria', 'Drowning', 'Maternal Disorders',
                    'HIV/AIDS', 'Tuberculosis', 'Cardiovascular Diseases',
                    'Lower Respiratory Infections', 'Neonatal Disorders',
                    'Diarrheal Diseases', 'Neoplasms', 'Diabetes Mellitus',
                    'Chronic Kidney Disease', 'Protein-Energy Malnutrition',
                    'Chronic Respiratory Diseases',
                    'Cirrhosis and Other Chronic Liver Diseases', 'Digestive Diseases'

                ]

            deaths_by_cause = filtered_data[causes_of_death].sum().reset_index()
            deaths_by_cause.columns = ['Cause of Death', 'Number of Deaths']

            fig = px.bar(deaths_by_cause,
                            x='Cause of Death',
                            y='Number of Deaths',
                            title=f'Number of Deaths by Cause in {2019}',
                            labels={'Number of Deaths':'Number of Deaths', 'Cause of Death':'Cause of Death'},
                            text='Number of Deaths')

            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig)

            fig = px.scatter(filtered_data,
                            x='Cardiovascular Diseases',
                            y='Neoplasms',
                            size='Cardiovascular Diseases',
                            color='Country/Territory',
                            hover_name='Country/Territory',
                            size_max=60,
                            title=f'Cardiovascular Diseases vs neoplasms in {2019}')

            st.plotly_chart(fig)

        oppt=st.selectbox("Select country",options=["India","China","Russia","Indonesia","Afghanistan","Japan"])
        if oppt=="India":
            country = "India"
            country_data = data[data['Country/Territory'] == country]

            # Create a line chart
            fig = px.line(country_data,
                        x='Year',
                        y='Cardiovascular Diseases',
                        title=f'Trend of Cardiovascular Diseases in {country} (1990-2019)',
                        labels={'Cardiovascular Diseases':'Number of Deaths', 'Year':'Year'},
                        markers=True)

            
            fig.add_scatter(x=country_data['Year'], y=country_data['Diabetes Mellitus'], mode='lines+markers', name='Diabetes Mellitus')
            fig.add_scatter(x=country_data['Year'], y=country_data['Malaria'], mode='lines+markers', name='Malaria')
            fig.add_scatter(x=country_data['Year'], y=country_data['Neoplasms'], mode='lines+markers', name='Neoplasms')
            fig.add_scatter(x=country_data['Year'], y=country_data['Digestive Diseases'], mode='lines+markers', name='Digestive Diseases')
            fig.add_scatter(x=country_data['Year'], y=country_data["Chronic Respiratory Diseases"], mode='lines+markers', name="Chronic Respiratory Diseases")
            st.plotly_chart(fig)
        elif oppt=="China":
            country = "China"
            country_data = data[data['Country/Territory'] == country]

            fig = px.line(country_data,
                        x='Year',
                        y='Cardiovascular Diseases',
                        title=f'Trend of Cardiovascular Diseases in {country} (1990-2019)',
                        labels={'Cardiovascular Diseases':'Number of Deaths', 'Year':'Year'},
                        markers=True)

            
            fig.add_scatter(x=country_data['Year'], y=country_data['Diabetes Mellitus'], mode='lines+markers', name='Diabetes Mellitus')
            fig.add_scatter(x=country_data['Year'], y=country_data['Malaria'], mode='lines+markers', name='Malaria')
            fig.add_scatter(x=country_data['Year'], y=country_data['Neoplasms'], mode='lines+markers', name='Neoplasms')
            fig.add_scatter(x=country_data['Year'], y=country_data['Digestive Diseases'], mode='lines+markers', name='Digestive Diseases')
            fig.add_scatter(x=country_data['Year'], y=country_data["Chronic Respiratory Diseases"], mode='lines+markers', name="Chronic Respiratory Diseases")
            st.plotly_chart(fig)

        elif oppt=="Russia":
            country = "Russia"
            country_data = data[data['Country/Territory'] == country]

            fig = px.line(country_data,
                        x='Year',
                        y='Cardiovascular Diseases',
                        title=f'Trend of Cardiovascular Diseases in {country} (1990-2019)',
                        labels={'Cardiovascular Diseases':'Number of Deaths', 'Year':'Year'},
                        markers=True)

            
            fig.add_scatter(x=country_data['Year'], y=country_data['Diabetes Mellitus'], mode='lines+markers', name='Diabetes Mellitus')
            fig.add_scatter(x=country_data['Year'], y=country_data['Malaria'], mode='lines+markers', name='Malaria')
            fig.add_scatter(x=country_data['Year'], y=country_data['Neoplasms'], mode='lines+markers', name='Neoplasms')
            fig.add_scatter(x=country_data['Year'], y=country_data['Digestive Diseases'], mode='lines+markers', name='Digestive Diseases')
            fig.add_scatter(x=country_data['Year'], y=country_data["Chronic Respiratory Diseases"], mode='lines+markers', name="Chronic Respiratory Diseases")
            st.plotly_chart(fig)

        elif oppt=="Indonesia":
            country = "Indonesia"
            country_data = data[data['Country/Territory'] == country]

            fig = px.line(country_data,
                        x='Year',
                        y='Cardiovascular Diseases',
                        title=f'Trend of Cardiovascular Diseases in {country} (1990-2019)',
                        labels={'Cardiovascular Diseases':'Number of Deaths', 'Year':'Year'},
                        markers=True)

            
            fig.add_scatter(x=country_data['Year'], y=country_data['Diabetes Mellitus'], mode='lines+markers', name='Diabetes Mellitus')
            fig.add_scatter(x=country_data['Year'], y=country_data['Malaria'], mode='lines+markers', name='Malaria')
            fig.add_scatter(x=country_data['Year'], y=country_data['Neoplasms'], mode='lines+markers', name='Neoplasms')
            fig.add_scatter(x=country_data['Year'], y=country_data['Digestive Diseases'], mode='lines+markers', name='Digestive Diseases')
            fig.add_scatter(x=country_data['Year'], y=country_data["Chronic Respiratory Diseases"], mode='lines+markers', name="Chronic Respiratory Diseases")
            st.plotly_chart(fig)

        elif oppt=="Afghanistan":
            country = "Afghanistan"
            country_data = data[data['Country/Territory'] == country]

            fig = px.line(country_data,
                        x='Year',
                        y='Cardiovascular Diseases',
                        title=f'Trend of Cardiovascular Diseases in {country} (1990-2019)',
                        labels={'Cardiovascular Diseases':'Number of Deaths', 'Year':'Year'},
                        markers=True)

            
            fig.add_scatter(x=country_data['Year'], y=country_data['Diabetes Mellitus'], mode='lines+markers', name='Diabetes Mellitus')
            fig.add_scatter(x=country_data['Year'], y=country_data['Malaria'], mode='lines+markers', name='Malaria')
            fig.add_scatter(x=country_data['Year'], y=country_data['Neoplasms'], mode='lines+markers', name='Neoplasms')
            fig.add_scatter(x=country_data['Year'], y=country_data['Digestive Diseases'], mode='lines+markers', name='Digestive Diseases')
            fig.add_scatter(x=country_data['Year'], y=country_data["Chronic Respiratory Diseases"], mode='lines+markers', name="Chronic Respiratory Diseases")
            st.plotly_chart(fig)

        elif oppt=="Japan":
            country = "Japan"
            country_data = data[data['Country/Territory'] == country]

            fig = px.line(country_data,
                        x='Year',
                        y='Cardiovascular Diseases',
                        title=f'Trend of Cardiovascular Diseases in {country} (1990-2019)',
                        labels={'Cardiovascular Diseases':'Number of Deaths', 'Year':'Year'},
                        markers=True)

            
            fig.add_scatter(x=country_data['Year'], y=country_data['Diabetes Mellitus'], mode='lines+markers', name='Diabetes Mellitus')
            fig.add_scatter(x=country_data['Year'], y=country_data['Malaria'], mode='lines+markers', name='Malaria')
            fig.add_scatter(x=country_data['Year'], y=country_data['Neoplasms'], mode='lines+markers', name='Neoplasms')
            fig.add_scatter(x=country_data['Year'], y=country_data['Digestive Diseases'], mode='lines+markers', name='Digestive Diseases')
            fig.add_scatter(x=country_data['Year'], y=country_data["Chronic Respiratory Diseases"], mode='lines+markers', name="Chronic Respiratory Diseases")
            st.plotly_chart(fig)
            
            
    elif a =='African':
        data =  pd.read_csv('african.csv')
        data
        # line Chart
        country = st.selectbox('Select Country', data['Country/Territory'].unique())
        filtered_data = data[data['Country/Territory'] == country]
        disease = st.selectbox('Select Disease for Trend Analysis', filtered_data.columns[4:])
        # st.write(filtered_data)
        fig_trend = px.line(filtered_data, x='Year', y=disease, title=f'Trend of {disease} in {country} from 1990 to 2019')
        st.plotly_chart(fig_trend)

        # bar chart
        year = st.selectbox('Select Year for Comparison', filtered_data['Year'].unique())
        st.subheader(f"Disease Comparison in {country} in {year}")
        data_year = filtered_data[filtered_data['Year'] == year].melt(id_vars=['Country/Territory', 'Code', 'Year'], var_name='Disease', value_name='Count')
        # st.write(data_year)
        fig_comparison = px.bar(data_year, x='Disease', y='Count', title=f'Disease Comparison in {country} in {year}')
        st.plotly_chart(fig_comparison)
        
        # Pie Chart
        st.subheader(f'Disease Distribution in {country} in {year}')
        diseases = st.multiselect('Select Diseases for Pie Chart', data_year['Disease'].unique(), default=data_year['Disease'].unique()[:5])
        data_pie = data_year[data_year['Disease'].isin(diseases)]
        fig_distribution = px.pie(data_pie, names='Disease', values='Count', title=f'Disease Distribution in {country} in {year}')
        st.plotly_chart(fig_distribution)
        
        # Heatmap for correlation between diseases
        st.subheader("Heatmap for correlation between diseases")
        corr = filtered_data.iloc[:, 4:].corr()
        plt.figure(figsize=(17, 17))
        heatmap = sns.heatmap(corr, annot=True, cmap='coolwarm')
        st.pyplot(heatmap.figure)
            
            
    elif a == 'American':
        
        data = pd.read_csv("american.csv")
        # print(data.columns)
        data.drop(columns=['Unnamed: 0'],inplace=True)
        # data

        countries = st.sidebar.multiselect('Select Countries', options=data['Country/Territory'].unique(), default=data['Country/Territory'].unique()[:5])
        diseases = st.sidebar.multiselect('Select Diseases', options=data.columns[3:].to_list(),default=data.columns[7:13].to_list())
        # st.write(diseases)
        year = st.sidebar.slider('Select Year', int(data['Year'].min()), int(data['Year'].max()), value=[2001])

        filtered_data = data[data['Country/Territory'].isin(countries)]
        st.write("### Disease Data")
        st.dataframe(filtered_data)

        # Line Chart
        st.write("## Trends Over Time")
        for disease in diseases:
            fig = px.line(filtered_data, x='Year', y=disease, color='Country/Territory', title=f'{disease} Over Time')
            st.plotly_chart(fig)

        # Bar Chart
        st.write("## Comparisons Between Countries")
        bar_chart_data = filtered_data[filtered_data['Year'] == year]
        for disease in diseases:
            fig = px.bar(bar_chart_data, x='Country/Territory', y=disease, color='Country/Territory', title=f'{disease} Comparison in {year}')
            st.plotly_chart(fig)

        # Heatmap for Matrix View of Disease Prevalence
        st.write("## Disease Prevalence Heatmap")
        heatmap_data = bar_chart_data.set_index('Country/Territory')[diseases].transpose()
        # st.write(heatmap_data)
        fig = px.imshow(heatmap_data, labels=dict(x="Country/Territory", y="Disease", color="Prevalence"), title=f'Disease Prevalence in {year}')
        st.plotly_chart(fig)

        # Pie Chart for Distribution of Diseases within a Country for a Specific Year
        st.write("## Disease Distribution Pie Chart")
        country = st.sidebar.selectbox('Select Country for Pie Chart', options=countries)
        pie_chart_data = filtered_data[(filtered_data['Country/Territory'] == country) & (filtered_data['Year'] == year)]
        pie_chart_data = pie_chart_data[diseases].melt(var_name='Disease', value_name='Prevalence')
        fig = px.pie(pie_chart_data, values='Prevalence', names='Disease', title=f'Disease Distribution in {country} for {year}')
        st.plotly_chart(fig)
    
    
    elif a == 'European':
        data = pd.read_csv("europe.csv")
        data
        
        diseases = data.columns.difference(['Year', 'Country/Territory', 'Code'])
        selected_diseases = st.sidebar.multiselect(
            'Select Diseases',
            options=diseases,default=['Diarrheal Diseases','Cirrhosis and Other Chronic Liver Diseases','Drowning',
                                        'HIV/AIDS','Lower Respiratory Infections']
        )
        filtered_data = data[['Year'] + selected_diseases]
        # st.write(filtered_data)
        heatmap_data = filtered_data.set_index('Year')

        st.subheader('Heatmap of Disease Counts Over the Years')
        fig_heatmap = go.Figure(data=go.Heatmap(
            z=heatmap_data.T,
            x=heatmap_data.columns,
            y=heatmap_data.index,
            colorscale='Viridis'
        ))
        fig_heatmap.update_layout(title='Disease Counts Heatmap')
        st.plotly_chart(fig_heatmap)
        
        
        # Pie Chart of Disease Proportions
        st.subheader('Pie Chart of Disease Proportions for Selected Year')
        years = data['Year'].unique()
        selected_year = st.selectbox('Select a year for pie chart', years, index=len(years)-1)
        pie_data = data[data['Year'] == selected_year].drop(columns=['Country/Territory', 'Code', 'Year']).sum().head(10)
        fig_pie = go.Figure(data=go.Pie(labels=pie_data.index, values=pie_data.values, hole=0.3))
        fig_pie.update_layout(title=f'Disease Proportions for {selected_year}')
        st.plotly_chart(fig_pie)

        # # Bar Chart of Disease Counts by Year
        st.subheader('Bar Chart of Disease Counts by Year')
        selected_years = st.multiselect('Select years to display', years, default=[1995,1996,1998,2000])
        selected_diseases = st.multiselect('Select diseases to display', heatmap_data.columns)
        filtered_data = data[data['Year'].isin(selected_years)]
        grouped_data = filtered_data[selected_diseases].groupby(filtered_data['Year']).sum().reset_index()
        fig_bar = px.bar(grouped_data, x='Year', y=selected_diseases, title='Disease Counts by Year', labels={'value': 'Count'})
        st.plotly_chart(fig_bar)

        # # Line Chart of Specific Disease Trends
        selected_diseases_line = st.multiselect('Select diseases for trend analysis', data.columns[3:],default=['Diabetes Mellitus','HIV/AIDS','Lower Respiratory Infections'])
        if selected_diseases_line:
            grouped_data = data.groupby('Year')[selected_diseases_line].sum().reset_index()
            fig_line = go.Figure()
            for disease in selected_diseases_line:
                fig_line.add_trace(go.Scatter(x=grouped_data['Year'], y=grouped_data[disease], mode='lines+markers', name=disease))
            fig_line.update_layout(title='Trend of Selected Diseases', xaxis_title='Year', yaxis_title='Count')
            st.plotly_chart(fig_line)
        else:
            st.warning('Please select at least one disease.')



        # # Area Chart of Disease Counts
        st.subheader('Area Chart of Disease Counts Over the Years')
        fig_area = px.area(data, x='Year', y=heatmap_data.columns, title='Disease Counts Area Chart', labels={'value': 'Count'})
        st.plotly_chart(fig_area)
        
elif opt=="About":
    with st.container():
        
        st.header("Introduction")
        st.write("Chronic diseases such as diabetes and heart disease are among the leading causes of morbidity and mortality worldwide, presenting significant challenges to public health systems. These conditions are often interrelated and share common risk factors, including unhealthy diets, physical inactivity, and genetic predispositions. Diabetes, characterized by elevated blood glucose levels, can lead to severe complications like kidney failure, blindness, and limb amputations. Heart disease, encompassing conditions such as coronary artery disease, heart attacks, and heart failure, remains the primary cause of death globally. Understanding the epidemiology, risk factors, and outcomes of these diseases is crucial for developing effective prevention and management strategies.")
    
    with st.container():
        st.write("---")
        c1,c2=st.columns(2)
        with c1:
            st.header("Objectives")
        
            st.write(
                """The primary objectives of this study are as follows:

1. *Epidemiological Analysis*:
   - To assess the prevalence and incidence rates of diabetes and heart disease across different populations and regions.
   - To identify temporal trends and variations in disease occurrence over time.

2. *Risk Factor Identification*:
   - To investigate the correlation between various demographic, socioeconomic, and lifestyle factors and the risk of developing diabetes and heart disease.
   - To identify high-risk groups based on age, gender, ethnicity, and other relevant factors.

3. *Data Preprocessing and Cleaning*:
   - To ensure the accuracy and consistency of the datasets through meticulous data cleaning and preprocessing.
   - To handle missing values, outliers, and other data quality issues effectively.
"""
                )

        with c2:
            st.write("##")
            st.write("##")
            
            st.image("images.jpeg")
            
            st.image("img.png")    
