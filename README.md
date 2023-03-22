# JSON Property Deletion Script
This Python script allows you to delete properties from a package-lock.json that match a property name ending. The script can be run from the command line and accepts one optional argument, which is the property name ending to use for matching keys.
## Usage
To use this script, follow these steps:
1. Make sure you have Python 3 installed on your system.
2. Download or clone the script to your local machine.
3. Open a terminal or command prompt and navigate to the directory where the script is located.
4. Run the script using python json-delete-field.py <ending>, where <ending> is an optional property name ending to use for matching keys.
5. The updated JSON data will be saved in package-lock.json.
Note that this script only removes top-level properties from the JSON object under "dependencies". If you need to remove nested properties, you will need to modify the code accordingly.
Also, make sure that you have valid JSON syntax in your input file.

### Example usage:
python json-delete-field.py xyz

This will remove all keys that end with "xyz" inside "dependencies".