import os

DB_URL = os.getenv("DB_URL", "mysql+pymysql://user:password@localhost:3306/testdb")