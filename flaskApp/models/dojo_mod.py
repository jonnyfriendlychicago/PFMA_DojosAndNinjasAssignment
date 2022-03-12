from sqlite3 import connect
from flaskApp.config.mysqlconnection import connectToMySQL # import the function that will return an instance of a connection
from flaskApp.models import ninja_mod

class Dojo_cls:
    def __init__( self , data ):
        self.id = data['id']
        self.dojoName = data['dojoName']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.dojoNinjaList = []
    
    """ get all dojo records from db"""
    @classmethod 
    def get_all(cls):
        q = "SELECT * FROM dojo;"
        rez = connectToMySQL('dojoNinja_sch').query_db(q) 
        dojoList = [] 
        for rec in rez:
            dojoList.append(cls(rec))
        print(dojoList)
        return dojoList

    @classmethod 
    def save(cls, data ):
        q = "INSERT INTO dojo (dojoName, createdAt, updatedAt) VALUES ( %(clr_dojoName)s , NOW() , NOW() );"
        return connectToMySQL('dojoNinja_sch').query_db(q, data )


    """ get one, JUST ONE, dojo records from db"""
    @classmethod
    def getOne(cls, data):
        q = 'select * from dojo where id = %(clr_id)s;'
        results = connectToMySQL("dojoNinja_sch").query_db(q, data)
        return cls(results[0])

    @classmethod
    def getDojoWithStudents(cls, data):
        q = "select * from dojo d left join ninja n on d.id = n.dojo_id where d.id = %(clr_id)s;"
        rez = connectToMySQL('dojoNinja_sch').query_db(q, data)
        print (rez)
        dojo = cls (rez[0]) 
        for row in rez:
            ninja_data = {
                "id" : row['n.id'], 
                "firstName" : row['firstName'], 
                "lastName" : row['lastName'], 
                "age" : row['age'], 
                "createdAt" : row['n.createdAt'], 
                "updatedAt" : row['n.updatedAt']
            }
            dojo.dojoNinjaList.append(ninja_mod.Ninja_cls(ninja_data))
            # return dojo.dojoNinjaList
        return dojo







    """ !!!!! below class method not employed on Dojo_cls, but keeping it for future use"""
    @classmethod 
    def update(cls, data ):
        q = "update dojo set dojoName = %(dojoName)s , updatedAt = NOW() where id = %(clr_id)s;"
        return connectToMySQL('dojoNinja_sch').query_db(q, data )
    
    """ !!!!! below class method not employed on Dojo_cls, but keeping it for future use"""
    @classmethod 
    def delete(cls, data ):
        q = "delete from dojo where id = %(clr_id)s;"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojoNinja_sch').query_db(q, data )
