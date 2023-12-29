from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from sqlalchemy import create_engine
import pymongo
import mysql.connector

#=======================GOOGLE API KEY=================================
api_key = 'AIzaSyB8QccKYXYdlnVZxhPHJ6sQ3aeJYVih-Do'
youtube = build('youtube', 'v3', developerKey=api_key)


#======================MONGODB CONNECTION==============================
client = pymongo.MongoClient('mongodb+srv://priyanka25:alohomora25@mongo.ebmvyp6.mongodb.net/?retryWrites=true&w=majority')
database = client["youtube"]
collection = database["channel_information"]

#=====================SQLALCHEMY FOR SEND AS DATAFRAME================
engine = create_engine('mysql+mysqlconnector://root:alohomora25@localhost/youtube_db', echo=False)


#=====================MYSQL - PYTHON CONNECTION=======================

mydb = mysql.connector.connect(host="localhost", user="root",password="alohomora25", auth_plugin = 'mysql_native_password')

mycursor = mydb.cursor()