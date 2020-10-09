# Covid-19 HotSpots 
# Machine Learning Predictive Model- U.S. County Level

## Team:
Beth Emborsky, Brodie Armstrong, Ellen Rud Gentile

## Intent: 
Currently most covid-19 predictive models are graphical and at the state level. County level, geographical data is available, but only with historical data. This does not allow state and local governments to take proactive measures. 

The purpose of this project is to create a cloud-based web application with county-level geographical visualization of predictive models of the spread of the disease.  This predictive visualization will allow government officials and individuals to take a more pro-active approach as they decide what measures are appropriate for mitigating covid-19 risks.

## Summary:
The web application includes interactive & insightful visualizations demonstrating the geographic, temporal, demographic & human-behavioral factors contributing to covid-19 spread such as:
  - County population & populations density
  - Mobility
  - County Average Age
  - County % Gender breakdown
  - Median Income
  - Access to healthcare
  - Number of tests administered
  - Positivity rate of tests
  - Restraurant & bar activity
  - School opening status
  - Number of cases, deaths
  - Per capita cases, deaths
  - Daily/weekly/monthly change in number of cases, deaths
  - Daily/weekly/monthly change in per capita cases, deaths
  - Estimated mask usage
  - County Poverty Level
  - County Education Level
  etc.
  
The application allows users to visualize a county-level predictive model of where future hotspots might occur over time. 

A back-end PostGres database is created using data from several sources.  SQL queries pull the data which is called by a Flask application. Machine Learning algorithms rank the importance of several factors in the development of Covid-19 hotspots. 

## Sources:
  - New York Times Covid-19 Data: https://github.com/nytimes/covid-19-data  files: counties.csv, colleges.csv, mask-use-by-county.csv
  - USDA 2013 Rural-urban Continuum Codes: https://www.ers.usda.gov/data-products/rural-urban-continuum-codes/
  TODO ADD ALL SOURCES
  -
 Based on these factors and historical data, a model was created to determine which counties might become the next hotspots. A full stack, interactive, web application was created and deployed in the cloud to allow users to understand how these factors vary across counties and over time and to visualize at risk areas.  National, State and Local govenrments may use this data to create pro-active policy measures.
