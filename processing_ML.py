# this module imports NYT data and Google mobility data, pre-processes and joins them into a dataframe in preparation to feed into an ML Model

# Install Dependencies
# Install Dependencies
import statsmodels.api as sm
import pandas as pd
from patsy import dmatrix
from statsmodels.tsa.api import VAR
import plotly.express as px
import plotly as py
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.preprocessing import StandardScaler
import statsmodels.tsa.vector_ar

#  datasets filepaths
NYT_file="Potential Data Sources/NYT- Cty Cases Deaths Thru Oct2/us-counties.csv"
Mob_file="Potential Data Sources/Google US Mobility/2020_US_Region_Mobility_Report.csv"
Urban_Rural_file="Potential Data Sources/Rural_or_Urban_Designations/ruralurbancodes2013.csv"
insurance_filepath = "Potential Data Sources/US Census-Health Insurance/sahie_2018.csv"

# read datasets
NYT=pd.read_csv(NYT_file, parse_dates=['date'])
Mob=pd.read_csv(Mob_file, parse_dates=['date'])
Urban_Rural=pd.read_csv(Urban_Rural_file)
insurance_df = pd.read_csv(insurance_filepath, skiprows=79)

# RURAL URBAN CLASSIFICATION DATA
# ------------------------------------
# Return only wanted columns for rural table
rural_columns = ['FIPS', 'State', 'County_Name', 'RUCC_2013', 'Description']
new_rural_df = Urban_Rural[rural_columns]

## filter to texas only
TX_rural=new_rural_df.loc[new_rural_df['State']=='TX']

# CENSUS INSURANCE DATA
#------------------------------------
new_insurance_df = insurance_df.loc[(insurance_df['geocat'] == 50) & (insurance_df['agecat'] == 0) & (insurance_df['racecat'] == 0)
                      & (insurance_df['sexcat'] == 0) & (insurance_df['iprcat'] == 0)]
## strip whitespace:
cols = new_insurance_df.select_dtypes(['object']).columns
new_insurance_df[cols] = new_insurance_df[cols].apply(lambda x: x.str.strip())

## filter to texas
TX_ins=new_insurance_df.loc[new_insurance_df['state_name']=='Texas']                                       

## return only wanted columns
insurance_columns = ['statefips', 'countyfips', 'PCTUI', 'PCTIC', 'state_name', 'county_name']
TX_ins = TX_ins[insurance_columns].copy()

## convert the 'PCTUI' and 'PCTIC' column to float format
TX_ins = TX_ins.astype({"PCTUI":'float', "PCTIC":'float'})

## Rename the column headers
TX_ins = TX_ins.rename(columns={'PCTUI': '% Uninsured',
                                'PCTIC': '% Insured',
                                'state_name': 'state',
                                'county_name': 'county'})
TX_ins=TX_ins.dropna(axis=0, how='any')

#NYT Data
#------------------------------------
# Limit to Texas
Texas=NYT.loc[NYT['state']=='Texas']
Texas=Texas.dropna(how='any', axis=0)
TX_county_fips=Texas[['county', 'fips']].drop_duplicates()

# add suffix to counties
Texas['county']=Texas['county'].map(str)+' County'

## drop state and fips
Texas2=Texas.drop(['fips', 'state'], axis=1)

## pivot on cases and clean
TX_Cases=Texas2.pivot(index= 'date',columns='county', values='cases')
TX_Cases=TX_Cases.fillna(0)

# repeat for deaths
Texas3=Texas
Texas3=Texas3.drop(['fips', 'state'], axis=1)

## pivot on deaths and clean
TX_Deaths=Texas3.pivot(index= 'date',columns='county', values='deaths')
TX_Deaths=TX_Deaths.fillna(0)

# create figure plot cases in all counties
fig = px.line(TX_Cases)
# TODO: SAVE FIGURE for use on website, make interactive

# create figure to show all deaths
fig2 = px.line(TX_Deaths)
# TODO: SAVE FIGURE for use on website, make interactive

# calcate daily cases and deaths:
TX_Cases_Differenced=TX_Cases.diff().fillna(0)
TX_Deaths_Differenced=TX_Deaths.diff().fillna(0)

# Create plots of daily cases and deaths
fig3 = px.scatter(TX_Cases_Differenced)
# TODO: SAVE FIGURE for use on website, make interactive
fig4 = px.scatter(TX_Deaths_Differenced)
# TODO: SAVE FIGURE for use on website, make interactive

# clip outliars:
TX_Cases_Differenced= TX_Cases_Differenced.clip(lower=0)
TX_Cases_Differenced=TX_Cases_Differenced.clip(upper=4000)
TX_Deaths_Differenced= TX_Deaths_Differenced.clip(lower=0)
TX_Deaths_Differenced=TX_Deaths_Differenced.clip(upper=70)

# unpivot/melt data:
TX_Cases_unpivoted=TX_Cases_Differenced.reset_index().melt(id_vars=['date'],var_name='county', value_name='Daily Cases')
TX_Deaths_unpivoted=TX_Deaths_Differenced.reset_index().melt(id_vars=['date'],var_name='county', value_name='Daily Deaths')


# GOOGLE MOBILITY DATA:
#------------------------------------
# filter to texas
TX_mob=Mob.loc[Mob['sub_region_1']=='Texas']
# rename columns
TX_mob.rename(columns={'sub_region_2':'county','census_fips_code':'fips'}, inplace=True)
# drop unnecessary columns and rename columns to standardize with NYT data
TX_mob=TX_mob.drop(['country_region_code','country_region','metro_area','iso_3166_2_code','sub_region_1', 'fips'], axis=1)

# DF for each mobilty indicator so can remove NAs without deleting other indicators for that date
## Retail and Recreation Mobility Index
Retail_Rec_Mob=TX_mob.pivot(index= 'date',columns='county', values='retail_and_recreation_percent_change_from_baseline')

# drop columns/ counties with na in data
Retail_Rec_Mob=Retail_Rec_Mob.dropna(axis=1).reset_index()

# unpivot dataframe to prep for merge
Retail_Rec_Mob_unpivoted = Retail_Rec_Mob.melt(id_vars=['date'],var_name='county', value_name='Retail Rec Pct Change from Baseline')

# drop row with no county name or no value
Retail_Rec_Mob_unpivoted=Retail_Rec_Mob_unpivoted.dropna(axis=0)

## Grocery and Pharmacy Mobility Index
Groc_Pharm_Mob=TX_mob.pivot(index= 'date',columns='county', values='grocery_and_pharmacy_percent_change_from_baseline')

# drop columns/ counties with na in data
Groc_Pharm_Mob=Groc_Pharm_Mob.dropna(axis=1).reset_index()

# unpivot dataframe to prep for merge
Groc_Pharm_Mob_unpivoted = Groc_Pharm_Mob.melt(id_vars=['date'],var_name='county', value_name='Grocery Pharm Pct Change from Baseline')

# drop row with no county name or no value
Groc_Pharm_Mob_unpivoted=Groc_Pharm_Mob_unpivoted.dropna(axis=0)

## Parks Mobility Index
Parks_Mob=TX_mob.pivot(index= 'date',columns='county', values='parks_percent_change_from_baseline')

# drop columns/ counties with na in data
Parks_Mob=Parks_Mob.dropna(axis=1).reset_index()

# unpivot dataframe to prep for merge
Parks_Mob_unpivoted = Parks_Mob.melt(id_vars=['date'],var_name='county', value_name='Parks Pct Change from Baseline')

# drop row with no county name or no value
Parks_Mob_unpivoted=Parks_Mob_unpivoted.dropna(axis=0)

## Transit Stations Mobility Index
Transit_Mob=TX_mob.pivot(index= 'date',columns='county', values='transit_stations_percent_change_from_baseline')

# drop columns/ counties with na in data
Transit_Mob=Transit_Mob.dropna(axis=1).reset_index()

# unpivot dataframe to prep for merge
Transit_Mob_unpivoted = Transit_Mob.melt(id_vars=['date'],var_name='county', value_name='Transit Pct Change from Baseline')

# drop row with no county name or no value
Transit_Mob_unpivoted=Transit_Mob_unpivoted.dropna(axis=0)

## Workplaces Mobility Index
Workplaces_Mob=TX_mob.pivot(index= 'date',columns='county', values='workplaces_percent_change_from_baseline')

# drop columns/ counties with na in data
Workplaces_Mob=Workplaces_Mob.dropna(axis=1).reset_index()

# unpivot dataframe to prep for merge
Workplaces_Mob_unpivoted = Workplaces_Mob.melt(id_vars=['date'],var_name='county', value_name='Workplaces Pct Change from Baseline')

# drop row with no county name or no value
Workplaces_Mob_unpivoted=Workplaces_Mob_unpivoted.dropna(axis=0)

## Workplaces Mobility Index
Residential_Mob=TX_mob.pivot(index= 'date',columns='county', values='residential_percent_change_from_baseline')

# drop columns/ counties with na in data
Residential_Mob=Residential_Mob.dropna(axis=1).reset_index()

# unpivot dataframe to prep for merge
Residential_Mob_unpivoted = Residential_Mob.melt(id_vars=['date'],var_name='county', value_name='Residential Pct Change from Baseline')

# drop row with no county name or no value
Residential_Mob_unpivoted=Residential_Mob_unpivoted.dropna(axis=0)

# merge them back together into overall mobility:
mob1=Retail_Rec_Mob_unpivoted.merge(Groc_Pharm_Mob_unpivoted, on=['date','county'])

# dont include parks because it massively limits number of counties in dataset
# mob2=mob1.merge(Parks_Mob_unpivoted, on=['date','county'])

# dont include transit because it massively limits number of counties in dataset
# when not including parks:
# mob3=mob1.merge(Transit_Mob_unpivoted, on=['date','county'])

# # when including parks:
# # mob3=mob2.merge(Transit_Mob_unpivoted, on=['date','county'])

# when not including parks or transit
mob4=mob1.merge(Workplaces_Mob_unpivoted, on=['date','county'])

# when not including  transit
# mob4=mob2.merge(Workplaces_Mob_unpivoted, on=['date','county'])

# when inlcuding transit:
# mob4=mob3.merge(Workplaces_Mob_unpivoted, on=['date','county'])

mobility_indices=mob4.merge(Residential_Mob_unpivoted, on=['date','county'])

# JOIN DATAFRAMES
#----------------------------------------------------------------------
#----------------------------------------------------------------------
## DEMOGRAPHICS & RELATIVELY CONSTANT DATA
#----------------------------------------
### merge rural urban des with insurance
TX_ins_rural=TX_ins.set_index('county').join(TX_rural.set_index('County_Name'))

#  drop redundancies
TX_ins_rural=TX_ins_rural.drop(['statefips', 'countyfips','state', 'State'],axis=1)

#  merge insurance, rural/urban with county_fips
TX_demogs=TX_ins_rural.join(TX_county_fips.set_index('county')).reset_index().drop('fips', axis=1)


##DAILY CHANGING DATA
#--------------------------------------------
# Join mobility data with daily case data:
TX_casesdiff_mob=mobility_indices.set_index(['county','date']).join(TX_Cases_unpivoted.set_index(['county','date']))

#  join daily death data
TX_casesdiff_deathdiff_mob=TX_casesdiff_mob.join(TX_Deaths_unpivoted.set_index(['county','date'])).reset_index()

# CUMULATIVE DAILIES
#----------------------------------------------
# Join mobility data with cumulative case data:
TX_cases_deaths_mob=mobility_indices.set_index(['county','date']).join(Texas2.set_index(['county','date']))
TX_cases_deaths_mob=TX_cases_deaths_mob.dropna(axis=0).reset_index()

#################################################################################################################
################################################################################################################

#USER INPUT COUNTY SELECTION
#TODO: consider putting this in a javascript element

# Make a list of the counties we have in dataset to choose from
county_list=TX_cases_deaths_mob['county'].drop_duplicates().to_list()

# Get user County choice from input
choices = county_list
print("Select a County\n")
for v in choices:
    print(v)
user_input = str(input())
print(user_input)

## CREATE SOURCES FOR ML BASED ON USER CHOICE
#-----------------------------------------------------
chosen_cty_dailies=TX_cases_deaths_mob.loc[TX_cases_deaths_mob['county']== user_input]
chosen_cty_demogs=TX_demogs.loc[TX_demogs['county']==user_input]
# TODO: DEMOGS CAN GO IN A NICELY FORMATTED BOX WHEN PULL DATA

# format/ prep for ML
dailies=chosen_cty_dailies.drop('county', axis=1).set_index('date')

# split test train 
end_train=pd.to_datetime('2020-07-31')
start_test=pd.to_datetime('2020-08-01')
train=dailies[:end_train]
test=dailies[start_test:]

# TRANSFORM DATA FOR VAR MODEL INPUT
#TODO: change from all data to just training data and add in exam of predict against actual
ddata=dailies[['cases', 'deaths']]
ddata.index=dailies.index
data=np.log(ddata+1).diff().dropna()

# train model
model=VAR(data)
results=model.fit(maxlags=15, ic='aic')

#plot results
#------------------------------------------------------
fig5=results.plot()
fig6=results.plot_acorr()
#TODO: get figs into app??? maybe? remember dep on user input

#plot forecast
#-------------------------------------------------------
# forecasting: lag order is number of days to forecast
lag_order = results.k_ar
results.forecast(data.values[-lag_order:], 30)
fig7 =  results.plot_forecast(10)
#TODO: get figs into app??? maybe? remember dep on user input

# #plot imulse responses
# irf = results.irf(10)
# fig8= irf.plot(orth=False)

# # plot cumulative responses
# fig9= irf.plot_cum_effects(orth=False)
