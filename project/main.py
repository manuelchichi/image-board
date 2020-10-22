
from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from flask_pymongo import ObjectId
import json 

from project import mongo
import base64

main = Blueprint('main', __name__)

def get_all_images():
    return list(mongo.db.images.find())

def get_image(imageId):
    return mongo.db.images.find_one({"_id": imageId})

@main.route("/")
def index():
    data = get_all_images()
    return render_template('index.html',allImages=data)

@main.route("/menu/", methods=['GET'])
@login_required
def menu():
    userImagesId=current_user.user_json['images']
    userImages = []
    for imageId in userImagesId:
        userImages.append(get_image(imageId))
    return render_template('menu.html', name=current_user.user_json['name'],userImages=userImages)

@main.route("/image/<id>", methods=['GET'])
def show_image(id):
    image = get_image(ObjectId(id))

    return render_template('show.html',image=image)

@main.route("/image/", methods=['POST'])
@login_required
def add_image():
    title = request.form.get('title')
    image = request.files['image']
    
    base64str = base64.b64encode(image.read()).decode()
    
    imageId = mongo.db.images.insert({'title':title,'base64':base64str})
    mongo.db.users.update({"_id": ObjectId(current_user.get_id())},{ '$push': { "images": ObjectId(imageId) } })

    return redirect(url_for('main.menu'))

@main.route("/image/modify", methods=['POST'])
@login_required
def modify_image():
    imageId = request.form.get('imageId')
    newTitle =  request.form.get('title')
    newImage =  request.files['image']

    base64str = base64.b64encode(newImage.read()).decode()

    if ObjectId(imageId) in current_user.user_json['images']:
        mongo.db.images.update({"_id": ObjectId(imageId)},{ '$set': { "title": newTitle, "base64": base64str} } )

    return redirect(url_for('main.menu'))

@main.route("/image/delete", methods=['POST'])
@login_required
def delete_image():
    imageId = request.form.get('imageId')

    if ObjectId(imageId) in current_user.user_json['images']:
        mongo.db.images.delete_one({"_id": ObjectId(imageId)})
        mongo.db.users.update({"_id": ObjectId(current_user.get_id())},{ '$pull': { "images": ObjectId(imageId) } })

    return redirect(url_for('main.menu'))


