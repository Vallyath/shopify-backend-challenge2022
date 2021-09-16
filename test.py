import requests

'''
In order to test the backend, to ensure that it is working I have included a couple of requests that encompass the following:

Testing to see that the pictures are being added to the database, and saved in the local folder.
Testing to see that if the two pictures have the same filename that the picture will not be added.
Testing to see that if I send the filename to be deleted from the db and server, that it will do so.

For each test, you will have to uncomment each one and comment the other test individually since my backend
only accepts one picture submission at a time.

'''

#UPLOAD pictures test
upload_url = "http://172.20.65.241:5000/upload"

"""
#adds first picture to the database.
file = {'image': open('redpanda.jpg','rb')}
tags = {'tags': 'red_panda, cute, animal, red, panda'}

r = requests.post(upload_url, files=files, data=tags)
print(r.text)
"""

"""
#adds a second picture to the database.
file = {'image': open('redpanda2.jpg','rb')}
tags = {'tags': 'red_panda, cute, animal, red, panda, adorable'}

r = requests.post(upload_url, files=file, data=tags)
print(r.text)
"""

"""
#This test case will fail because redpanda.jpg already exists in the db and uploads folder.
files = {'image': open('random_bad_folder/redpanda.jpg','rb')}
tags = {'tags': 'red_panda, cute, animal, red, panda'}

r = requests.post(upload_url, files=file, data=tags)
print(r.text)
"""

"""
del_url = "http://172.20.65.241:5000/delete"

#this test case should successfully delete the row redpanda.jpg from the database and uploads folder.
del_name = {"name": "redpanda.jpg"}
r = requests.post(del_url, data=del_name)
print(r.text)
"""

"""
#this testcase should fail because there is nothing in the empty string.
del_name = {"name": ""}
r = requests.post(del_url, data=del_name)
print(r.text)
"""

