from flask import Flask, request
from werkzeug.utils import secure_filename
from flask_migrate import Migrate
from model import Image, db
import os

'''
FEATURES IMPLEMENTED:
Add (one) image to the repository
Delete (one) image to the repository

ADDITIONAL POSSIBILITIES TO CONSIDER:

To implement private and public permissions, perhaps it could be part of what the user sends in:
For example to make pictures public, the request should include that it is allowed for public access

That would mean that in my image model I could add one more column to account for whether the picture being 
stored is private or public.

To implement users and scale this image repository up, I would create one more table called Users
and add a column to my current table with UserId, so when I'm deleting pictures I can first check to see
that the session user is the same as the user requesting to delete the picture. If they are the picture
is deleted the same way.

'''

app = Flask(__name__)

#setup for folder, database and validating filenames
#'path/to/upload/folder/on/pc'
app.config['UPLOAD'] = 'path/to/upload/folder/on/pc' #CHANGE
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:yourdbpasswordhere@localhost:5432/images_api" #CHANGE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['VALID_FILENAMES'] = ['jpg', 'jpeg', 'png', 'gif']

db.init_app(app)
migrate = Migrate(app, db)

'''

This function uploads the picture to the image repository. It will first check that the picture
is a valid filename, then it will create a standardized filepath (using a save filepath we create).
This is treated as our local server location, it will check to see if the same path exists (with the
filename), if it does then it will reject the picture, otherwise it will save to our database.

'''
@app.route("/upload", methods=["POST"])
def upload():
    tags = request.form.get('tags')
    file = request.files['image']

    #validates the filename to make sure that it's a picture.
    if file.filename.split(".")[1] in app.config['VALID_FILENAMES']:
        #this prevents the user from submitting a file path that would corrupt the system.
        filename = secure_filename(file.filename)
    else:
        return "Please submit a proper picture.", 400

    #creates a save location path so that we can store it in the database and in our local server.
    #use .lower() to standardize the naming, and prevent filenames having the same name but with 
    #different capitalization
    location = os.path.join(app.config['UPLOAD'], filename.lower())
    #this if statement checks to see if the filename exists within our upload location, 
    if os.path.exists(location):
        return "File with same name exists, please use a different filename!", 400
    else:
        file.save(location)
        new_image = Image(filename, location, tags)
        db.session.add(new_image)
        db.session.commit()
        return "Picture received and stored!", 200

"""
This is the delete route for anyone to delete a picture from the repository.
This functions deletes by querying the filename from the db,
if it finds the filename it will delete it.
"""
@app.route("/delete", methods=["POST"])
def delete():
    #gets the filename sent in from the user.
    filename = request.form.get("name")
    #in the case the user enters an empty string into the case.
    if filename == "":
        return "Please enter a filename.", 400
    db.session.query(Image).filter(Image.image_name==f"{filename}").delete()
    db.session.commit()
    location = os.path.join(app.config['UPLOAD'], filename)
    if os.path.exists(location):
        os.remove(location)
        return "Picture deleted!", 200
    else:
        return "Couldn't find the filename.", 400

#when you run the python file, it will automatically run the server.
if __name__ == "__main__":
    app.run(host="0.0.0.0")