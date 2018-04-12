"""
Data Visualization using matlabplot
import CSV file ( from an excel file) and convert to JSON.
Convert JSON data into graphs.


"""

import csv


def parser(csv_file, delimiter):
    """Parses a raw CSV file to a JSON-like object"""

    # Open CSV input file
    with open(csv_file) as f:
        # Read the CSV data
        csv_data = csv.reader(f, delimiter=delimiter)

        parsed_data = []

        # Skip over the first line -- headers
        fields = next(csv_data)
       
        # Iterate over each row of the csv file, zip together field -> value
        for row in csv_data:
            parsed_data.append(dict(zip(fields, row)))

    return parsed_data


def main():
    # Call parser and give needed parameters.
    new_data = parser(MY_FILE, ",")
    print(new_data)


# sample data to inject into application.

MY_FILE = r'data/sample_sfpd_incident_all.csv'

if __name__ == "__main__":
    main()
