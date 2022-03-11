from flaskApp import app
from flask import render_template,redirect,request,session,flash
# from flaskApp.models.user_mod import user


# all of below copy/pasted from original server.py file

from flaskApp.models.user_mod import User_cls

""" HOME PAGE / INDEX """
@app.route('/')
def index():
    allUsers = User_cls.get_all()
    return render_template("index.html", display_allUsers = allUsers)

""" ADD NEW USER """
@app.route('/addNewUser')
def addNewUser():
    return render_template("addNewUser.html") 

""" Route invoked on the Add New User page """
@app.route('/createUser', methods=["POST"])
def createUser():
    data = { # this creates cleared variables, containing cleansed incoming data from the form
        "clr_firstName": request.form["frm_firstName"],
        "clr_lastName" : request.form["frm_lastName"],
        "clr_email" : request.form["frm_email"]
        }
    id = User_cls.save(data) # creates variable... 'id' ... = that we'll use in next line (represents the ID of newly created record.... oh, and runs the "save" method from server.py)
    return redirect('/userProfile/' + str(id)) 

"""route invoked by the redirect immediately above"""
@app.route('/userProfile/<int:id>')
def userProfile(id):
    data = {
        "clr_id": id
    }
    userProfile = User_cls.getOne(data)
    """ ABOVE absolutely essential; below will not work on it's own """
    # userProfile = User_cls.getOne(id)
    return render_template("userProfile.html", display_userProfile = userProfile)

""" route engaged by the 'edit' button on the userProfile.html page"""
@app.route('/userProfile/<int:id>/edit')
def editUserProfile(id):
    data = {
        "clr_id": id
    }
    userProfile = User_cls.getOne(data)
    """ ABOVE absolutely essential; below will not work on it's own """
    # userProfile = User_cls.getOne(id)
    return render_template("editUserProfile.html", display_userProfile = userProfile)

""" Route invoked by clicking the 'update friend' button on the edit user profile page """
@app.route('/userProfile/<int:id>/update', methods=["POST"])
def updateUserProfile(id):
    data = { # this creates cleared variables, containing cleansed incoming data from the form
        "clr_id": id, 
        "clr_firstName": request.form["frm_firstName"],
        "clr_lastName" : request.form["frm_lastName"],
        "clr_email" : request.form["frm_email"]
        }
    User_cls.update(data) # this line is just "run this update!" this  is getting a whole array of data, not just a single integer/ID
    return redirect(f"/userProfile/{id}")

    """ below should be working, no idea why it's not!"""
    # dataX = {
    #     "clr_id": id
    # }
    # sid = dataX
    # User_cls.update(data) # this line is just "run this update!" this  is getting a whole array of data, not just a single integer/ID
    # return redirect('/userProfile/' + str(sid)) 
    """ i don't understand why line above won't work"""
    
@app.route('/userProfile/<int:id>/delete')
def deleteUserProfile(id): 
    data = {
        "clr_id": id
    }
    User_cls.delete(data) # this line is just "run this update!" this  is getting a whole array of data, not just a single integer/ID
    return redirect('/')    

"""DON'T TOUCH BELOW :-) below always needs to be at the bottom of the script, yes!"""
# below is stuff you oughta have, per TA Cameron Smith, from Coding Dojo: 

@app.route('/', defaults={'cookies': ''})
@app.route('/<path:cookies>')
def catch_all(cookies):
    return 'Sorry! No response here. Try url again.'


