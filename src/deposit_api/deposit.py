import os
import requests
import webbrowser
from pathlib import Path

KEY_FILE = os.path.join(Path.home(), '.onedep_api.jwt')
AUTH_URL = 'http://pdbe-worker-1.ebi.ac.uk:12000/deposition/auth/authenticate'
NEW_DEP_URL = 'http://pdbe-worker-1.ebi.ac.uk:12000/deposition/api/new'

class Deposit:
    def __init__(self):
        pass
    
    def new(self):
        self.authenticate()
        self.create_deposition()
    
    def authenticate(self):
        if os.access(KEY_FILE, os.R_OK):
            with open(KEY_FILE, encoding='utf-8'):
                self._api_key = f.read()

            return True
        
        webbrowser.open_new_tab(AUTH_URL)

        print('If a browser does not open, copy this link and open it in a working browser: %s' % AUTH_URL)
        
        try:
            self._api_key = input('Enter your API key: ')
            
            with open(KEY_FILE, 'w', encoding='utf-8') as fp:
                fp.write(self._api_key)
        except Exception as e:
            print('Error getting an API key, %s', e)
        
        return False
    
    def create_deposition(self):
        r = requests.post(NEW_DEP_URL, headers={
            'Authorization': 'Bearer %s' % self._api_key
        }, data={
            'location': 'United Kingdom',
            'email': 'w3_pdb05@localhost',
            'password': 'notNeededAnymore',
            'experiments': [{'method': 'xray'}]
        })
