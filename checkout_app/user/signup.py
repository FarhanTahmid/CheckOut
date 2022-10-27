import email
from multiprocessing import connection
from checkout_app.Database.connection import ConnectionToDb
from checkout_app.models import Users
import random
import string
from checkout_app.user.generate import Generators

class CommonUser:
    
    # def __init__(self):
    #     pass
    
    def createUserName(email_or_mobile):
        """Generates a random username to the userprofile slicing entered email or mobile number"""
        email=email_or_mobile
        username=''
        for x in email:
            if(x=='@' or x=='.'):
                break
            else:
                username+=x
        charCounter=True
        for x in username:
            if(ord(x)>58 and ord(x)<126):
                charCounter=True
                break
            else:
                charCounter=False
                continue
        if(charCounter):
            username=username+str(random.randint(10,10000))
        else:
            s=random.randint(1,5)
            randomchars=''.join(random.choices(string.ascii_uppercase + string.digits, k=s)) #for mobile number signin, system assigns characters to their usernames by itself
            username=username+randomchars
        if (Users.objects.filter(username=username).exists()):
            CommonUser.createUserName(email)
        else:
            return username
    
    
    def userSignup(email_or_mobile,password):
        '''SignsUp user through django and their data to sql'''
        
        username=CommonUser.createUserName(email_or_mobile)
        
        #firebase signup
        if(ord(username[-1])>58 and ord(username[:-1])<126):
            #firebase phone signup
            
            pass
        else:
            
            connections=ConnectionToDb()
            auth=connections.firebaseAuth()
            
            #django user signup
            if(Users.objects.filter(email_or_mobile=email_or_mobile).exists()):
                return False
            
            else:
                
                #firebase email signup
                #try:
                firebaseUser=auth.create_user_with_email_and_password(email=email_or_mobile,password=password)
                    #data='' #have to collect data with googla api
                #except:
                #   print("Some error occured")
                           
                #Django user signup
                try:
                    user = Users.objects.create_user(email_or_mobile,password=password,username=username)
                    user.save();
                except:
                    pass
                #data to sql
                newUser=Users.objects.create(
                username=username,
                email_or_mobile=email_or_mobile
            )
                return True
        #google signup
        #facebook signup