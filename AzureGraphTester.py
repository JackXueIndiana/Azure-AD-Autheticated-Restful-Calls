# Python 3.7
# Example for Azure Graph call
# Jack Xue
# 2020-09-10

import json
import adal
import requests

authority_url = "https://login.windows.net/microsoft.com"
clientId = "your client id from AAD app regisration"
clientSecret = "your client secret from AAD app registration"
RESOURCE = "6f4db35d-5ea2-440e-ade1-c63da3623dea" # This is resource ID for Azure Graph. No touch!!!

context = adal.AuthenticationContext(authority_url, validate_authority=None, cache=None, api_version=None, timeout=None, enable_pii=False)

token = context.acquire_token_with_client_credentials(RESOURCE, clientId, clientSecret)

print('Here is the token:')
print(json.dumps(token, indent=2))

# Use the token on Azure Graph endpoint
ag_url = "https://azuregraph-preview.msftcloudes.com/api/v1/query/PhysicalAsset_DCMTRegions"

headers = {'Authorization': 'Bearer {}'.format(token["accessToken"])
}

response_data = json.loads(requests.get(ag_url, headers=headers).text)

print(json.dumps(response_data))