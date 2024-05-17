# Load the reticulate package
library(reticulate)

# Set the path to your Python script
py_script <- "path/to/sample_python_load.py"

# Source the Python script
source_python(py_script)

# Call the Python functions
config_path <- "path/to/data_bridges_api_config.yaml"
survey_id <- 3329
access_type <- "full"
country_iso3 <- "AFG"
survey_date <- "2022-01-01"

# Get survey data
survey_data <- get_survey_data(config_path, survey_id, access_type)

# Get price data
price_data <- get_price_data(config_path, country_iso3, survey_date)
