from flaskApp.config.mysqlconnection import connectToMySQL # import the function that will return an instance of a connection

class Ninja_cls:
    def __init__( self , data ):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.age = data['age']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
    
    @classmethod 
    def saveNinja(cls, data ):
        q = "INSERT INTO ninja (firstName, lastName, age,  dojo_id, createdAt, updatedAt) VALUES ( %(clr_firstName)s , %(clr_lastName)s, %(clr_age)s, %(clr_dojo_id)s, NOW() , NOW() );"
        return connectToMySQL('dojoNinja_sch').query_db(q, data )







    """ get all dojo records from db"""
    @classmethod 
    def get_allx(cls):
        q = "SELECT * FROM ninja;"
        rez = connectToMySQL('dojoNinja_sch').query_db(q) 
        ninjaList = [] 
        for rec in rez:
            ninjaList.append(cls(rec))
        return ninjaList





    """ !!!!! below class method not employed on ninja_cls, but keeping it for future use"""
    @classmethod
    def getOnex(cls, data):
        q = 'select * from ninja where id = %(clr_id)s;'
        results = connectToMySQL("dojoNinja_sch").query_db(q, data)
        return cls(results[0])

    """ !!!!! below class method not employed on ninja_cls, but keeping it for future use"""
    @classmethod 
    def updatex(cls, data ):
        q = "update dojo set ninja = %(dojoName)s , updatedAt = NOW() where id = %(clr_id)s;"
        return connectToMySQL('dojoNinja_sch').query_db(q, data )
    
    """ !!!!! below class method not employed on ninja_cls, but keeping it for future use"""
    @classmethod 
    def deletex(cls, data ):
        q = "delete from ninja where id = %(clr_id)s;"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojoNinja_sch').query_db(q, data )
