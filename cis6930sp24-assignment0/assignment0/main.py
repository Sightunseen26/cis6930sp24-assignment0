import argparse
from download import fetchincidents
from extract import extractincidents
from database import createdb, populatedb, status

def main(url):
    # Step 5: Download Data
    incident_data = fetchincidents(url)

    # Step 6: Extract Data
    incidents = extractincidents(incident_data)

    # Step 7: Create Database
    db = createdb()

    # Step 8: Insert Data
    populatedb(db, incidents)

    # Step 9: Status Print
    status(db)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process Norman Police Department incident data.")
    parser.add_argument("--incidents", type=str, help="URL to download incident data")

    args = parser.parse_args()

    if args.incidents:
        main(args.incidents)
    else:
        print("Please provide the --incidents flag with the URL.")
