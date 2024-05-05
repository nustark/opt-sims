
import os
from app import app

# okay to use http (disable for prod)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
# okay to return different oauth token scopes
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

if __name__ == '__main__':
    app.run(debug=True)
