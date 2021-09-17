import requests
import unittest

'''
In order to test the backend, to ensure that it is working I have included a couple of requests that encompass the following:

Testing to see that the pictures are being added to the database, and saved in the local folder.
Testing to see that if the two pictures have the same filename that the picture will not be added.
Testing to see that if I send the filename to be deleted from the db and server, that it will do so.

For each test, you will have to uncomment each one and comment the other test individually since my backend
only accepts one picture submission at a time OR you can use the monolithic unit test I've written to run 
the tests in order. 

Something to note about the test naming is that I had to include the numbers to ensure they ran in order or else the behaviour
wouldn't match what I expected to happen so they had to happen in that order to work. Otherwise some test cases would fail.

REMEMBER TO CHANGE BEFORE RUNNING:

upload_url
del_url

'''

upload_url = "http://CHANGEHERE:5000/upload"
del_url = "http://CHANGEHERE:5000/delete"

#UPLOAD pictures test
"""

#adds first picture to the database.
file = {'image': open('redpanda.jpg','rb')}
tags = {'tags': 'red_panda, cute, animal, red, panda'}

r = requests.post(upload_url, files=file, data=tags)
print(r.text)"""


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

upload_url = "http://CHANGEHERE:5000/upload"
del_url = "http://CHANGEHERE:5000/delete"

class TestRequests(unittest.TestCase):

    #adds first picture to the database.
    def test_1_send_first_image(self):
        file = {'image': open('redpanda.jpg','rb')}
        tags = {'tags': 'red_panda, cute, animal, red, panda'}
        r = requests.post(upload_url, files=file, data=tags)
        self.assertEqual(r.text, "Picture received and stored!")
        self.assertEqual(r.status_code, 200)

    #adds second picture to the database.
    def test_2_send_second_image(self):
        file = {'image': open('redpanda2.jpg','rb')}
        tags = {'tags': 'red_panda, cute, animal, red, panda, adorable'}
        r = requests.post(upload_url, files=file, data=tags)
        self.assertEqual(r.text, "Picture received and stored!")
        self.assertEqual(r.status_code, 200)

    #tests to see if the server will reject a picture already in the server
    def test_3_send_image_same_name(self):
        file = {'image': open('random_bad_folder/redpanda.jpg','rb')}
        tags = {'tags': 'red_panda, cute, animal, red, panda'}
        r = requests.post(upload_url, files=file, data=tags)
        self.assertEqual(r.text, "File with same name exists, please use a different filename!")
        self.assertEqual(r.status_code, 400)
    
    #this test case should successfully delete the row redpanda.jpg from the database and uploads folder.
    def test_4_delete_image(self):
        del_name = {"name": "redpanda.jpg"}
        r = requests.post(del_url, data=del_name)
        self.assertEqual(r.text, "Picture deleted!")
        self.assertEqual(r.status_code, 200)
    
    #this test case should successfully delete the row redpanda.jpg from the database and uploads folder.
    def test_5_delete_image(self):
        del_name = {"name": "redpanda2.jpg"}
        r = requests.post(del_url, data=del_name)
        self.assertEqual(r.text, "Picture deleted!")
        self.assertEqual(r.status_code, 200)

    #this testcase should return status code 400 because there is nothing in the empty string.
    def test_6_delete_empty_string(self):
        del_name = {"name": ""}
        r = requests.post(del_url, data=del_name)
        self.assertEqual(r.text, "Please enter a filename.")
        self.assertEqual(r.status_code, 400)

    #this testcase should return status code 400 because the file does not exist in the server.
    def test_7_delete_non_existent_file(self):
        del_name = {"name": "fluffypanda.jpg"}
        r = requests.post(del_url, data=del_name)
        self.assertEqual(r.text, "Couldn't find the filename.")
        self.assertEqual(r.status_code, 400)

if __name__ == "__main__":
    unittest.main()