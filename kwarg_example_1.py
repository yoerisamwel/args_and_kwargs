class DatabaseConnection:
    def __init__(self, **kwargs):
        self.host = kwargs.get('host', 'localhost')
        self.port = kwargs.get('port',5432)
        self.username = kwargs.get('username', 'root')
        self.password = kwargs.get('password','')
        self.database = kwargs.get('database','mydb')
        self.ssl_enabled = kwargs.get('ssl_enabled', False)
        self.connection_timeout = kwargs.get('connection_timeout',30)

    def connect(self):
        #simulate connecting to the databse
        print(f"Connecting to database at {self.host}:{self.port} as {self.username}...")
        print(f"Using database: {self.database}")
        if self.ssl_enabled:
            print("SSL is enabled")
        print(f"Connection timeout set to {self.connection_timeout} seconds.")
        print("Connected succesfully!\n")

if __name__=="__main__":
    #Create a Databaseconnection object with various kwargs
    db1 = DatabaseConnection(
    host='db.example.com',
    port=5433,
    username="admin",
    password="secretpassword",
    database="production_db",
    ssl_enabled=True,
    connection_timeout=45
    )
    db2 = DatabaseConnection(
        host='localhost',
        username='dev_user',
        password='devpassword',
        connection_timeout=15
    )
#Connect to the database
    db1.connect()
    db2.connect()
