# coding: utf-8
import sqlite3

class RequetesDB:
    def __init__(self, dbName):
        self.connection = sqlite3.connect(dbName)
        self.cursor = self.connection.cursor()
    
    def executeCommand (self, sqlCmd):
        self.cursor.execute(sqlCmd)
    
    def commit(self):
        self.connection.commit()
    
    def closeConnection(self):
        self.connection.close()