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
            "apiKey": env('apiKey'),
            "authDomain": env('authDomain'),
            "databaseURL": "https://checkouttest-c5528-default-rtdb.firebaseio.com",
            "projectId": env('projectId'),
            "storageBucket": "checkouttest-c5528.appspot.com",
            "messagingSenderId": env('messagingSenderId'),
            "appId": env('appId'),
        }
        return config
    
    
    def firebaseAuth(self):
        firebase=pyrebase.initialize_app(ConnectionToDb.defaultFirebaseConnection)
        auth=firebase.auth()
        return auth
        