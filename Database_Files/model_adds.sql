DROP TABLE IF EXISTS model_daily_data;
DROP TABLE IF EXISTS model_rmse_data;

CREATE TABLE "model_daily_data" (
    "date" DATE   NOT NULL,
	"fips_code" INT   NOT NULL,
	"lstm_cases_predicted" double precision,
    "lstm_cases_residuals" double precision,
	"lstm_deaths_predicted" double precision,
    "lstm_deaths_residuals" double precision,
	"sarimax_cases_predicted" double precision,
    "sarimax_cases_residuals" double precision,
	"sarimax_cases_forecasted" double precision,
	"sarimax_deaths_predicted" double precision,
    "sarimax_deaths_residuals" double precision,
	"sarimax_deaths_forecasted" double precision,
    CONSTRAINT "pk_model_daily_data" PRIMARY KEY (
        "date","fips_code"
     )
);

CREATE TABLE "model_rmse_data" (
	"fips_code" INT   NOT NULL,
	"lstm_case_rmse" double precision,
	"lstm_death_rmse" double precision,
	"sarimax_case_rmse" double precision,
	"sarimax_death_rmse" double precision,
    CONSTRAINT "pk_model_rmse_data" PRIMARY KEY (
        "fips_code"
     )
);