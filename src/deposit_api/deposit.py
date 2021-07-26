import os
import webbrowser

KEY_FILE = '~/.onedep.jwt'
AUTH_URL = 'http://pdbe-worker-1.ebi.ac.uk:12000/deposition/auth/authenticate'

class Deposit:
    def __init__(self):
        pass
    
    def new(self):
        self.authenticate()
    
    def authenticate(self):
        if os.access(KEY_FILE, os.R_OK):
            with open(KEY_FILE, encoding='utf-8'):
                self._api_key = f.read()

            return True
        
        webbrowser.open_new_tab(AUTH_URL)
        
        try:
            self._api_key = input('Enter your API key: ')
            return True
        except:
            print('Error getting an API key')
        
        return False