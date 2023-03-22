import json
import re
import sys

# Load JSON data from file
with open('package-lock.json', 'r') as f:
    data = json.load(f)

# Regular expression pattern to match keys ending with the specified argument
if len(sys.argv) > 1:
    pattern = re.compile(".*" + sys.argv[1] + "$")
else:
    pattern = None

# Remove matching keys from dependencies dictionary
if 'dependencies' in data:
    for key in list(data['dependencies'].keys()):
        if pattern is None or pattern.match(key):
            del data['dependencies'][key]

# Save updated JSON data to file
with open('package-lock.json', 'w') as f:
    json.dump(data, f, indent=4)