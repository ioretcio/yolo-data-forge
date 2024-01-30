import os
import sys 
import hashlib
from PIL import Image
# import shutil
import sqlite3
from sqlite3 import Error
import sys
from os import listdir, mkdir, makedirs
from os.path import isfile, join, isdir
import argparse


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        return conn

def intersector():
    parser = argparse.ArgumentParser(
        description='Splits images and annotations in a selected percentage configuration across training, validation, and test folders')

    parser.add_argument('--source_folder', "-i", type=dir_path, help="source images directory")
    parser.add_argument('--source_db', "-d", type=dir_path, help="source database (sqlite) directory")

    args = parser.parse_args()
    candidat = args.source_folder
    databasePath = args.source_db
    
    c = create_connection(databasePath).cursor()
    c.execute(f""" update files set hashcode = replace(hashcode,'\n',''); """)

    
    count = 0
    count2 = 0
    allcount = len(os.listdir(candidat))
    
    for image in os.listdir(candidat):
        try:
            c.execute(f""" SELECT filename from files WHERE hashcode='{hashlib.md5(Image.open(  os.path.join( candidat, image)).tobytes()).hexdigest()}'; """)
            result = c.fetchall()
            count +=1 
            if(len(result)) >0 :
                count2+=1
                
                # shutil.move(os.path.join(candidat ,image  ), os.path.join( "C:\\Users\\Gonch\\Desktop\\used_images\\", typeOF, image )  )
                pass
            else:
                # shutil.move(os.path.join(candidat ,image  ), os.path.join("C:\\Users\\Gonch\\Desktop\\unused_images\\", typeOF, image ) )
                pass
            print(f'processed: [{round((count/allcount)*100,5)}%] has copy {count2} from {allcount}', end='\r')
        except Exception as e:
            print(e)
    print(count2/count)
    
    
    
    
    
    




