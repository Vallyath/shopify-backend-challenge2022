from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

'''
This code here is used to set up the table that is used to query from.
id ->           sequentially increments, can be used to uniquely identify each row.
image_name ->   this is the image name that the user uploaded, it has to be unique because there would be a conflict if the
                user chooses to upload two different pictures with the same name, when you query you would not get the exact
                picture you're looking for.
image ->        this is the image filepath that points to where it exists in the uploads folder
tags ->         this will help with offline analytics, and searching by tags rather than by name.
'''

class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    image_name = db.Column(db.String())
    image = db.Column(db.String())
    tags = db.Column(db.String())

    def __init__(self, name, path, tags):
        self.image_name = name
        self.image = path
        self.tags = tags

    def __repr__(self):
        return f"{self.id}: {self.image_name}, {self.tags}"
    

