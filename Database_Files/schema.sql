DROP TABLE IF EXISTS county_daily_data;
DROP TABLE IF EXISTS county_demographics;

-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/D9jGD3
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

CREATE TABLE "county_demographics" (
    "County" VARCHAR(100),
    "Median_Age" double precision,
    "Percent_Age_17_and_Under" double precision,
    "Percent_Age_65_and_Older" double precision,
    "Percent_Age_85_and_Older" double precision,
    "Percent_Hispanic" double precision,
    "Percent_White_Alone" double precision,
    "Percent_African_American_Alone" double precision,
    "Percent_American_Indian_&_Alaska_Native_Alone" double precision,
    "Percent_Asian_Alone" double precision,
    "Percent_Native_Hawaiian_and_Other_Pacific_Islander_Alone" double precision,
    "Percent_Multi_Racial" double precision,
    "Per_Capita_Income" INT,
    "Median_Household_Income" INT,
    "Avg_Annual_Pay" INT,
    "Percent_Population_in_Poverty" double precision,
    "Percent_Population_under_18_in_Poverty" double precision,
    "Percent_Urban" double precision,
    "Percent_Rural" double precision,
    "Percent_HS_Graduate_or_Higher" double precision,
    "Percent_Bachelors_Degree_or_Higher" double precision,
    "Percent_Unemployed" double precision,
    "County_Population" INT,
    "Population_Density_per_Sq_Mile" double precision,
    "Percent_Uninsured" double precision,
    "Percent_Insured" double precision,
    "State" VARCHAR(100),
    "FIPS" INT   NOT NULL,
    "State_Abbr" VARCHAR(10),
    "RUCC_2013" INT,
    "RUCC_Description" VARCHAR(5000),
    CONSTRAINT "pk_county_demographics" PRIMARY KEY (
        "FIPS"
     )
);

CREATE TABLE "county_daily_data" (
    "date" DATE   NOT NULL,
    "FIPS" INT   NOT NULL,
    "retail_and_recreation_percent_change_from_baseline" double precision,
    "grocery_and_pharmacy_percent_change_from_baseline" double precision,
	"parks_percent_change_from_baseline" double precision,
	"transit_stations_percent_change_from_baseline" double precision,
    "workplaces_percent_change_from_baseline" double precision,
    "residential_percent_change_from_baseline" double precision,
    "cases" double precision   NOT NULL,
    "deaths" double precision   NOT NULL,
    CONSTRAINT "pk_county_daily_data" PRIMARY KEY (
        "date","FIPS"
     )
);

ALTER TABLE "county_daily_data" ADD CONSTRAINT "fk_county_daily_data_FIPS" FOREIGN KEY("FIPS")
REFERENCES "county_demographics" ("FIPS");