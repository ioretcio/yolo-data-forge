import os
import hashlib
from PIL import Image
import sqlite3
from sqlite3 import Error
import argparse
import time


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        return conn

def intersect():
    parser = argparse.ArgumentParser(
        description='Finds intersection of db and folder and creates purge.txt file with to-delete-candidates')

    parser.add_argument('--source_folder', "-i", help="source images directory")
    parser.add_argument('--source_db', "-d" , help="source database (sqlite) directory")

    args = parser.parse_args()
    candidat = args.source_folder
    databasePath = args.source_db
    
    c = create_connection(databasePath).cursor()
    c.execute(f""" update files set hashcode = replace(hashcode,'\n',''); """)

    
    count = 1
    count2 = 0
    allcount = len(os.listdir(candidat))
    with open(f'purge{int(time.time())}.txt', 'w') as f:
        for image in os.listdir(candidat):
            try:
                c.execute(f""" SELECT filename from files WHERE hashcode='{hashlib.md5(Image.open(  os.path.join( candidat, image)).tobytes()).hexdigest()}'; """)
                result = c.fetchall()
                count +=1 
                if(len(result)) >0 :
                    count2+=1
                    f.write(f'{os.path.join( candidat, image)}\n')
                print(f'processed: [{round((count/allcount)*100,5)}%] has copy {count2} from {allcount}', end='\r')
            except Exception as e:
                print(e)
    print(count2/count)
    
intersect()