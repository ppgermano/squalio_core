import os
from dynaconf import settings

class Config:
    SECRET_KEY = os.urandom(24)
    # GOOGLE_APPLICATION_CREDENTIALS = settings('PATH_AUTH_GOOGLE')
    
