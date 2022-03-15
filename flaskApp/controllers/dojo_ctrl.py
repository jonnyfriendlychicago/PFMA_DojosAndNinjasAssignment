# from typing_extensions import dataclass_transform
from flaskApp import app
from flask import render_template,redirect,request,session,flash

from flaskApp.models.dojo_mod import Dojo_cls

""" HOME PAGE / INDEX """
@app.route('/')
def dojoIndex():
    allDojos = Dojo_cls.get_all()
    return render_template("index.html", display_allDojos = allDojos)

""" ADD NEW Dojo """
# @app.route('/addNewDojo')
# def addNewDojo():
#     return render_template("addNewDojo.html") 

""" Route invoked on the Add New Dojo page """
@app.route('/createDojo', methods=["POST"])
def createDojo():
    data = { # this creates cleared variables, containing cleansed incoming data from the form
        "clr_dojoName": request.form["frm_dojoName"]
        }
    id = Dojo_cls.save(data) # creates variable... 'id' ... = that we'll use in next line (represents the ID of newly created record.... oh, and runs the "save" method from server.py)
    # return redirect('/DojoProfile/' + str(id)) 
    return redirect('/') 

@app.route('/dojoProfile/<int:id>')
def dojoProfile(id):
    data = {
        "clr_id": id
    }
    # dojoProfile = Dojo_cls.getOne(data)
    
    # allDojos = Dojo_cls.get_all()
    allDojoNinjas = Dojo_cls.getDojoWithStudents(data) 
    return render_template("DojoProfile.html" , display_allDojoNinjas = allDojoNinjas)

# """ route engaged by the 'edit' button on the DojoProfile.html page"""
# @app.route('/DojoProfile/<int:id>/edit')
# def editDojoProfile(id):
#     data = {
#         "clr_id": id
#     }
#     DojoProfile = Dojo_cls.getOne(data)
#     """ ABOVE absolutely essential; below will not work on it's own """
#     # DojoProfile = Dojo_cls.getOne(id)
#     return render_template("editDojoProfile.html", display_DojoProfile = DojoProfile)

# """ Route invoked by clicking the 'update friend' button on the edit Dojo profile page """
# @app.route('/DojoProfile/<int:id>/update', methods=["POST"])
# def updateDojoProfile(id):
#     data = { # this creates cleared variables, containing cleansed incoming data from the form
#         "clr_id": id, 
#         "clr_firstName": request.form["frm_firstName"],
#         "clr_lastName" : request.form["frm_lastName"],
#         "clr_email" : request.form["frm_email"]
#         }
#     Dojo_cls.update(data) # this line is just "run this update!" this  is getting a whole array of data, not just a single integer/ID
#     return redirect(f"/DojoProfile/{id}")

    
# @app.route('/DojoProfile/<int:id>/delete')
# def deleteDojoProfile(id): 
#     data = {
#         "clr_id": id
#     }
#     Dojo_cls.delete(data) # this line is just "run this update!" this  is getting a whole array of data, not just a single integer/ID
#     return redirect('/')    

"""DON'T TOUCH BELOW :-) below always needs to be at the bottom of the script, yes!"""
# below is stuff you oughta have, per TA Cameron Smith, from Coding Dojo: 

@app.route('/', defaults={'cookies': ''})
@app.route('/<path:cookies>')
def catch_all(cookies):
    return 'Sorry! No response here. Try url again.'


