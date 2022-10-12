import email
from checkout_app.models import Users
from django.contrib.auth.models import User,auth
import random
import string

class Users:
    
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
            
        return username
    
    
    def userSignup(email_or_mobile,password):
        #django user signup
        
        username=Users.createUserName(email_or_mobile)
        print(username)
        # if(User.objects.filter(email=email_or_mobile).exists):
        #     return False
        # elif User.objects.filter(username=username).exists():
        #     return False
        # else:
        #     user = User.objects.create_user(username=username, email=email, password=password)
        #     user.save();
            
        # #data to sql
        # newUser=Users.objects.create(
        #     username=email_or_mobile,
        #     email_or_mobile=email_or_mobile
        # )
        
        #google signup
        #facebook signup