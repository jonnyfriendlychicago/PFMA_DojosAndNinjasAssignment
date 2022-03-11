from flaskApp.config.mysqlconnection import connectToMySQL # import the function that will return an instance of a connection

class User_cls:
    def __init__( self , data ):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
    
    """ get all user records from db"""
    @classmethod 
    def get_all(cls):
        q = "SELECT * FROM user;"
        rez = connectToMySQL('users_sch').query_db(q) 
        userList = [] 
        for rec in rez:
            userList.append(cls(rec))
        return userList

    @classmethod 
    def save(cls, data ):
        q = "INSERT INTO user (firstName , lastName , email , createdAt, updatedAt) VALUES ( %(clr_firstName)s , %(clr_lastName)s , %(clr_email)s , NOW() , NOW() );"
        return connectToMySQL('users_sch').query_db(q, data )

    """ get one, JUST ONE, user records from db"""
    @classmethod
    def getOne(cls, data):
        q = 'select * from user where id = %(clr_id)s;'
        results = connectToMySQL("users_sch").query_db(q, data)
        return cls(results[0])

    @classmethod 
    def update(cls, data ):
        q = "update user set firstName = %(clr_firstName)s , lastName = %(clr_lastName)s, email = %(clr_email)s, updatedAt = NOW() where id = %(clr_id)s;"
        return connectToMySQL('users_sch').query_db(q, data )
    
    @classmethod 
    def delete(cls, data ):
        q = "delete from user where id = %(clr_id)s;"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users_sch').query_db(q, data )
