# CIS 6930 Spring 2024 Assignment 0

## Project Overview

This project is the implementation of Assignment 0 for CIS 6930 - Spring 2024. The goal of this assignment is to create a Python program that downloads incident data from a given URL, extracts information from a PDF file, creates an SQLite database, populates it with the extracted data, and prints a status report.

## Getting Started

### Prerequisites

- Python 3.x
- Pipenv

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/cis6930sp24-assignment0.git

 ## Run Code
 
 1. cd cis6930sp24-assignment0

 2. pipenv install

 3. pipenv lock

 4. pipenv run python assignment0/main.py --incidents <url>

    Replace <url> with the actual URL from which incident data needs to be fetched.

    ## sample command with working url
    
    pipenv run python assignment0/main.py --incidents https://www.normanok.gov/sites/default/files/documents/2024-01/2024-01-25_daily_incident_summary.pdf

###

    Project Structure

    assignment0/: Contains the main code.
    tests/: Contains test files.
    resources/: Directory to store the SQLite database.

    Command Line Options
    --incidents <url>: Required flag to specify the URL for incident data.
    
    Functions

    1. Download Data

        Function: fetchincidents(url)
        Description: Downloads incident data from the given URL using the urllib.request library.

    2. Extract Data

        Function: extractincidents(incident_data)
        Description: Extracts incident details from a PDF file using the pypdf2 library.
    
    3. Create Database

        Function: createdb()
        Description: Creates an SQLite database file named normanpd.db with a specified schema.
    
    4. Insert Data

        Function: populatedb(db, incidents)
        Description: Inserts incident data into the SQLite database.
    
    5. Status Print

        Function: status(db)
        Description: Prints incident counts sorted by total occurrences and alphabetically.

###