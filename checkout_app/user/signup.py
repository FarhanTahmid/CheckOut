import email
from checkout_app.models import Users


class User:
    user=''
    def __init__(self,user):
        pass
    
    
    def userSignup(email_or_mobile,password):
        #django user signup
        
        
        
        #data to sql
        newUser=Users.objects.create(
            username=email_or_mobile,
            email_or_mobile=email_or_mobile
        )
        
        #google signup
        #facebook signup