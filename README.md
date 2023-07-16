# Tennis Data Extraction Script
This repository contains a Python script that extracts data from the website https://www.tennisabstract.com/ based on a given player list. The extracted data is then saved in an Excel file with specific formatting.

## Prerequisites
To run the script, make sure you have the following installed:

Python (version 3.7 or above)
Libraries: selenium, pandas, openpyxl

## Usage
1. Clone this repository to your local machine or download the script files: main.py, scraping_men.py, scraping_women.py, column_header_men.py, column_header_women.py, and write_data_xlsx.py.

2. Place the input player list file (Players_List_Tennis.xlsx) in the source folder.

3. Run the main.py script by executing the following command:
   python main.py
   The script will prompt you to choose either men or women's data extraction by entering 'M' or 'W', respectively.

4. The script will read the player list from the provided input file (source/Players_List_Tennis.xlsx), extract the data from the website for the corresponding gender, and save it in a new Excel file with the desired formatting (output.xlsx).

5. If any errors occur during the data extraction process or a player's page cannot be found, an error output file will be created (error_output.xlsx). You can manually update the master list with the correct link in this file.

6. Additionally, a master list (men.xlsx and women.xlsx) will be created, which includes the players' names and links to their corresponding pages on tennisabstract.com. This list can be used to confirm matching pages for the players.


## File Descriptions
1. main.py: The main script that prompts the user for the gender selection and calls the appropriate scraping script based on the input.

2. scraping_men.py: Contains functions to scrape data from tennisabstract.com for men's players.
   
3.scraping_women.py: Contains functions to scrape data from tennisabstract.com for women's players.

4. column_header_men.py: Defines the column headers for men's data in the output Excel file.
   
6. column_header_women.py: Defines the column headers for women's data in the output Excel file.

7. write_data_xlsx.py: Writes the extracted data into an Excel file with the desired formatting.

8. source/Players_List_Tennis.xlsx: Input file containing the list of players (separated by gender) for data extraction.

9. ss3_template.xlsx: Example file showing the desired output formatting for the script.

10. output.xlsx: Output file where the extracted data is saved with the desired formatting.

11. error_output.xlsx: Error output file where any errors or missing player pages are recorded.

12. master_list.xlsx: Master list file containing the players' names and links to their corresponding pages on tennisabstract.com.

## Note
Please note that this script relies on web scraping, and the structure of the target website (tennisabstract.com) may change over time. In case of any changes to the website's structure, the script may need to be updated accordingly.
