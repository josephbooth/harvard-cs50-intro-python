# Third Example - json library comes with python
import json
import requests
import sys

# this is protecting from errors if arguments are not correct
if len(sys.argv) != 2:
    sys.exit()

# modified the item limit to 50 at this point in demo
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json() # o is for object in this example
for result in o["results"]:
    print(result["trackName"])

# % python3 itunes.py weezer

# Second Example - json library comes with python
# import json
# import requests
# import sys
# 
# # this is protecting from errors if arguments are not correct
# if len(sys.argv) != 2:
#     sys.exit()
# 
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))
# 
# # json.dumps is a prettify function for console output
# # use indent to adjust output


# First Example - import package requests

# import requests
# import sys
# 
# # this is protecting from errors if arguments are not correct
# if len(sys.argv) != 2:
#     sys.exit()
# 
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(response.json())
# 
# # .json transforms the response into a json object
# 
# 
# # this demo required
# # % python3 -m pip install --break-system-packages requests
# # Collecting requests
# #   Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
# # Collecting charset_normalizer<4,>=2 (from requests)
# #   Downloading charset_normalizer-3.4.7-cp314-cp314-macosx_10_15_universal2.whl.metadata (40 kB)
# # Collecting idna<4,>=2.5 (from requests)
# #   Downloading idna-3.18-py3-none-any.whl.metadata (6.1 kB)
# # Collecting urllib3<3,>=1.26 (from requests)
# #   Downloading urllib3-2.7.0-py3-none-any.whl.metadata (6.9 kB)
# # Collecting certifi>=2023.5.7 (from requests)
# #   Downloading certifi-2026.6.17-py3-none-any.whl.metadata (2.5 kB)
# # Downloading requests-2.34.2-py3-none-any.whl (73 kB)
# # Downloading charset_normalizer-3.4.7-cp314-cp314-macosx_10_15_universal2.whl (309 kB)
# # Downloading idna-3.18-py3-none-any.whl (65 kB)
# # Downloading urllib3-2.7.0-py3-none-any.whl (131 kB)
# # Downloading certifi-2026.6.17-py3-none-any.whl (133 kB)
# # Installing collected packages: urllib3, idna, charset_normalizer, certifi, requests
# # Successfully installed certifi-2026.6.17 charset_normalizer-3.4.7 idna-3.18 requests-2.34.2 urllib3-2.7.0