import requests
import json

'''
Loading Sensitive files from .gitignore and making them into a dict
'''

with open(".gitignore/package.json") as mylittlefile:
    payload = json.load(mylittlefile)

# This URL will be the URL that your login form points to with the "action" tag.
PRE_LOGIN_URL = payload["LOGIN_URL"]

# This URL is the page you actually want to pull down with requests.
# REQUEST_URL = payload["POST_LOGIN_URL"]

# dict that contains login information
credentials = {
    'userid': payload["userid"],
    'passwd': payload["passwd"],
    '__CSRFToken__': payload["__CSRFToken__"],
    'do': payload["do"],
    'submit': payload["submit"]
}