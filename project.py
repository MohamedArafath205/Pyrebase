import pyrebase
import os
from getpass import getpass

firebaseConfig = {
  "apiKey": "AIzaSyB90Ka0pHy0SNuSqjt8cM_E81J2dSQ5E2k",
  "authDomain": "pyrebase-ddfca.firebaseapp.com",
  "projectId": "pyrebase-ddfca",
  "storageBucket": "pyrebase-ddfca.appspot.com",
  "messagingSenderId": "747491423505",
  "appId": "1:747491423505:web:03d236a30305c4880e48b0",
  "measurementId": "G-TVBWK7Z3Y1",
  "databaseURL": ""
};

firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()

path = input("Enter location of the file: ")

filename = os.path.basename(path)

add_to_storage = storage.child(filename).put(path)

print(storage.child(filename).get_url(None))

# shorturl.at/pxDMS