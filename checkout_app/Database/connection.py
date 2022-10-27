import environ
import pyrebase

class ConnectionToDb:
    def __init__(self) -> None:
        pass
    def defaultFirebaseConnection(self):
        
        #Default Firebase connection
        env = environ.Env()
        environ.Env.read_env()
        config={
            'apiKey': 'AIzaSyCfW6Co7nuWsCAanSdfo4yVfjkGw--JtZU',
            'authDomain': "checkout-8e376.firebaseapp.com",
            'databaseURL': "https://checkout-8e376-default-rtdb.firebaseio.com",
            'projectId': "checkout-8e376",
            'storageBucket': "checkout-8e376.appspot.com",
            'messagingSenderId': "1083396425284",
            'appId': "1:1083396425284:web:1f141be9a275db790ede11",
            'measurementId': "G-JMXZ8V02NT" 
        }
        return config
    
    
    def firebaseAuth(self):
        
        firebase=pyrebase.initialize_app(ConnectionToDb.defaultFirebaseConnection(self))
        auth=firebase.auth()
        return auth
        