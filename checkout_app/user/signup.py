import email
from checkout_app.models import Users
from backend_core.models import CustomUserManager,User
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
        if (User.objects.filter(username=username).exists()):
            CommonUser.createUserName(email)
        else:
            return username
    
    
    def userSignup(email_or_mobile,password):
        '''SignsUp user through django and their data to sql'''
        
        #django user signup
        username=CommonUser.createUserName(email_or_mobile)
        
        if(User.objects.filter(email_or_mobile=email_or_mobile).exists()):
            return False
        
        else:
            #Django user signup
            user = User.objects.create_user(email_or_mobile,password=password,username=username)
            user.save();
            
            #data to sql
            newUser=Users.objects.create(
            username=username,
            email_or_mobile=email_or_mobile
        )
            return True
        
        
        
        #google signup
        #facebook signup