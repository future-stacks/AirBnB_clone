'''user.py
'''

from models.base_model import BaseModel


class User(BaseModel):
    ''' Class for User'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""