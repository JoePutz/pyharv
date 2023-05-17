import requests
import json
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("http://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]) 
print(json.dump(response.json(), indent=2))