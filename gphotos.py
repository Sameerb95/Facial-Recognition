import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/photoslibrary.readonly']

# Load client secrets from a file
CLIENT_SECRETS_FILE = 'client_secret_138968007521-skhnq3qov9gcspk3ialid0pc1g4cgf4v.apps.googleusercontent.com.json'

# Create the flow using the client secrets file
flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    CLIENT_SECRETS_FILE, scopes=SCOPES)

# Set the redirect URI
flow.redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'

# Generate the authorization URL
auth_url, _ = flow.authorization_url(prompt='consent')

# Print the authorization URL and ask the user to open it
print('Please go to this URL: {}'.format(auth_url))

# Get the authorization code from the user
code = input('Enter the authorization code: ')

# Fetch the access token using the authorization code
flow.fetch_token(code=code)

# Get the credentials
credentials = flow.credentials

# Create a service object for the Google Photos API
service = googleapiclient.discovery.build('photoslibrary', 'v1', credentials=credentials)

# List albums (example API call)
results = service.albums().list(pageSize=10).execute()
items = results.get('albums', [])

if not items:
    print('No albums found.')
else:
    print('Albums:')
    for item in items:
        print('{0} ({1})'.format(item['title'], item['id']))
