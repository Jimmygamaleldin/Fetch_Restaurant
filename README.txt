
# Fetch Restaurant

## Project Overview
`Fetch_Restaurant.py` is a Python script that retrieves restaurant information from an API based on user input regarding location (postcode). This tool helps users quickly find restaurant options that match specific criteria such as cuisine type, dietary preferences, and special offers.

## Getting Started

### Prerequisites
- Python 3.6 or higher
- `requests` library

### Installation
1. Ensure Python 3.6+ is installed on your system.
2. Clone this repository or download `Fetch_Restaurant.py` directly.
3. Install the `requests` library:
   ```bash
   pip install requests
   ```

### Building and Running the Solution
To run `Fetch_Restaurant.py`, follow these steps:
1. Open a terminal or command prompt. Alternatively, you can run this script in any Python compiler or integrated development environment (IDE) such as IDLE, PyCharm, or VS Code.
2. Navigate to the directory containing `Fetch_Restaurant.py`.
3. Execute the script by running:
   ```bash
   python Fetch_Restaurant.py [POSTCODE]
   ```
   Replace `[POSTCODE]` with the actual postcode you wish to query.
   
   In environments like IDLE, you can simply open the script and run it by pressing F5 or using the run command in the menu.

## Usage
Input a postcode when prompted to fetch restaurant data for that area. The script will display restaurants that match the given criteria.

## Assumptions
- **API Availability**: Assumes that the API is always accessible and functional.
- **Postcode Validity**: Assumes that the user inputs a valid UK postcode.

## Clarifications
- **API Data**: The script processes standard JSON responses from the API, focusing on fields such as name, cuisine type, and offers.

## Improvements
- **Error Handling**: Introduce more robust error handling for API connectivity issues and invalid user inputs.
- **User Interface**: Consider implementing a GUI to facilitate easier interaction with the program.
- **Performance**: Optimize the script to handle responses more quickly and efficiently.


