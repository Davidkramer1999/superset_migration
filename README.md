# Superset Dashboard Migration Tool

This tool automates the process of migrating a dashboard from a development (dev) environment to a production (prod) environment within Apache Superset. It streamlines the workflow by using environment variables for configuration and requires a `.env` file to store sensitive information securely.

## Features

- Authenticate against both dev and prod Superset instances.
- Export a dashboard from the dev instance.
- Import the exported dashboard into the prod instance.

## Requirements

- Python 3.x
- `python-dotenv` package for loading environment variables.
- Access to both dev and prod Superset instances.

## Setup Instructions

1. **Clone the repository or download the source code.**

2. **Ensure Python 3.x is installed on your system.** You can verify this by running `python --version` in your terminal.

3. **Install the required Python packages.** Run the following command in your terminal:

   ```sh
   pip install python-dotenv requests
   ```

4. **Create a `.env` file in the root directory of the project** with the following content:

   ```makefile
   SUP_RESET_URL_DEV=<Your Dev Superset URL>
   SUP_RESET_URL_PROD=<Your Prod Superset URL>
   DEV_USERNAME=<Your Dev Username>
   DEV_PASSWORD=<Your Dev Password>
   DEV_AUTH_METHOD=<Your Dev Auth Method>
   PROD_USERNAME=<Your Prod Username>
   PROD_PASSWORD=<Your Prod Password>
   PROD_AUTH_METHOD=<Your Prod Auth Method>
   ```

   Replace the placeholder values with your actual Superset credentials and URLs.

## Usage

To run the script from the command line, execute:

```sh
python main.py
```

## Config
I have included the configuration file used for deploying Superset v3! with Docker. Please note that certain flags are enabled or disabled, which may affect the migration process