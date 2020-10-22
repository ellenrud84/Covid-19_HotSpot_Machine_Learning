# Covid-19 HotSpots 
# Machine Learning Predictive Model- U.S. County Level

## Team:
Beth Emborsky, Brodie Armstrong, Ellen Rud Gentile

## Main Technnologies Used:
Jupyter Notebooks, Python, Pandas, Matplotlib/Pyplot, SQL/PostGres, Flask, HTML, JavaScript, CSS, Bootstrap, Machine Learning: Google Colabs, Keras, SARIMA, LSTM,VECM.

## Intent: 
Currently most Covid-19 predictive models are graphical and at the state level. County level, geographical data is available, but only with historical data. This does not allow state and local governments to take proactive measures. 

The purpose of this project is to create a cloud-based web application with county-level geographical visualization of predictive models of the spread of the disease.  This predictive visualization will allow government officials and individuals to take a more pro-active approach as they decide what measures are appropriate for mitigating covid-19 risks.


## Summary:
The web application includes interactive & insightful visualizations demonstrating the geographic, temporal, demographic & human-behavioral factors contributing to covid-19 spread such as:
  - Population density
  - Mobility
  - County Average Age
  - County % Gender breakdown
  - Median Income
  - Access to healthcare
  - Restraurant & bar activity
  - Number of cases, deaths
  - Poverty Level
  - Education Level
  etc.
  
The application allows users to visualize a county-level predictive model for each county in Texas. 
[![Image from Gyazo](https://i.gyazo.com/d2fb1585068495ee5c9c17971eefa4b1.gif)](https://gyazo.com/d2fb1585068495ee5c9c17971eefa4b1)

A back-end PostGres database is created using data from several sources (see below).   SQL views were created for each county's daily data and for all counties static data (demographics). These views are is called by a Flask application. 

Several machine learning models were fitted to project and forecast each county's cases and deaths. These models include SARIMA and LSTM univariate models and a VECM multivariate model. 

## Sources:
  - New York Times Covid-19 Data: https://github.com/nytimes/covid-19-data  files: counties.csv, colleges.csv, mask-use-by-county.csv
  - Google US Region Covid-19 Mobility Data: https://www.google.com/covid19/mobility/
  - Texas Association of Counties Demographic Data: https://imis.county.org/iMIS/CountyInformationProgram/QueriesCIP.aspx
  
## Methods:
### Data Analysis and Pre-Processing:
Of our data sources, case/ death count and mobility varied daily, while Demographics was considered constant with time.  Therefore, we first made two datasets- one with the daily data and another with the constant data. 

#### Stationarizing the Timeseries Data:
The initial raw data for cases varied by county but overall showed an exponential trend (as expected for a spreading disease):
##### Raw Case Data for all TX counties:
[![Cases Raw Data All Counties](../i.gyazo.com/d2fb1585068495ee5c9c17971eefa4b1.gif)

TODO:Illustrate examples of stationarizing the data.

#### Test Train Split
Test train split was done on a slightly aribtrary date allowing about 75% of the early datapoints to be included in the train data, with the last dates being included in the test data.

### SARIMA MODEL
The SARIMA model can accept non-stationary and seasonal data, because its model algorithm performs these steps internally.  However, the inputs for the SARIMA model can be used to define the steps.  The inputs are as follows: SARIMA((p,d,q)(P,D,Q,m), where (p,d,q,) are trend related terms and (P,D,Q,m) are seasonality related.  
  - p = trend autoregression order,
  - d = trend difference order,
  - q = moving average order,
  - P = seasonal autoregressive order
  - D = seasonal difference order
  - Q = seasonal moving average order
  - m = the number of timesteps in a single seasonal period (e.g. weekly season on daily data =7)
 Since Texas has 253 counties, each needing unique input parameters for their individual models and since we did not have the time in our two week projec to look at these parameters individually, a function called auto-arima from a library called pmdarima was used to automatically determine the best model for each county, by running it in a loop and storing the ouput parameters to a dictionary with the key beign the county name.  

For each of the case and death datasets, we looped through the counties and fit the best model to that data and then ran it. The loop also ran test and train data and assessed model fit and ran projections and forecasts, the model results and forecasts were for each counties cases and deaths models were stored to dictionaries.  These objects were then added to the database so that the results of each model could be easily accessed and compared to the actual cases and deaths.

### LSTM
A similar strategy to the SARIMA model was used to join LSTM model results to the database.   The LSTM results were overall fairly accurate, but the model has not been completely tuned yet.  Accuracy should improve as we optimize the tuning for each county's model.  While the MSE on the LSTM model was frequently higher than that of the SARIMA model, it does appear to be more robust at anticipating changes in trend, whereas the SARIMA models generally seem to smoothen the predicted or forecasted data more (though it depends on the county).

### VECM
The results the VECM model indicate that it needs further tuning before being added to the application.  It is currently not very accurate, but is a goods start at taking on a multivariate analysis of a very complex dataset.


## Conclusion: 
SARIMA, LSTM, and VECM Machine learning models were used to model the change in Covid-19 cases and deaths over time in every Texas County.  A full stack, interactive, web application was created and deployed in the cloud to allow users to visualize at the projections/forecasts from these models at the county level.  National, State and Local govenrments may use this data to create pro-active policy measures. Inidviduals may use this data to gauge the risk in a county they or someone they know may live in or travel to. 


