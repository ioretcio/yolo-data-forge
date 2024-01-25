import argparse
import os
import sqlite3
from sqlite3 import Error
from PIL import Image
import hashlib

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        return conn

def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

def fingerprint_creator():
    parser = argparse.ArgumentParser(
        description='Creates sqlite database with md5 fingerprint of media files!')
    parser.add_argument('--root_dir', "-r", type=dir_path, help="root directory")
    parser.add_argument('--database_name', "-d", type=str, help="database name")
    args = parser.parse_args()
    root_dir = args.root_dir
    database_name = args.database_name
    filename = f"{database_name}.db"
    conn =create_connection(filename)
    cursor = conn.cursor()
    cursor.execute( """ CREATE TABLE IF NOT EXISTS files (filename text UNIQUE NOT NULL,hashcode text NOT NULL); """)
    
    for folder, subs, files in os.walk(root_dir):
        print(f">processing {folder}")
        allcount = len(files)
        count = 0
        for filename in files:
            if(filename.lower().endswith(('jpg', 'jpeg', 'png'))):  
                cursor.execute(f"INSERT or REPLACE INTO files (filename, hashcode) values ('{os.path.join(folder, filename)}',\
                    '{hashlib.md5(Image.open(  os.path.join(folder, filename)).tobytes()).hexdigest()}');")
                count+=1
                if(count%100)==0:
                    print(f'processed: {round((count/allcount)*100,5)}%]', end='\r')
        print('\n')
    conn.commit()