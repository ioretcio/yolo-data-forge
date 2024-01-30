import os
import sqlite3
from sqlite3 import Error
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

    parser.add_argument('--first_db', "-f", help="source database (sqlite) directory 1")
    parser.add_argument('--second_db', "-s", help="source database (sqlite) directory 2")
    print("Caution! This action will create a 'need_to_delete.txt' listing file!")
    args = parser.parse_args()

    databasePath1 = args.first_db
    databasePath2 = args.second_db
    
    c1 = create_connection(databasePath1).cursor()
    c1.execute(f""" update files set hashcode = replace(hashcode,'\n',''); """)


    c2 =  create_connection(databasePath2).cursor()
    if(databasePath1!=databasePath2):
        c2.execute(f""" update files set hashcode = replace(hashcode,'\n',''); """)
    
    count = 0
    count2 = 0


    c1.execute(f""" SELECT * from files""")
    first_data = c1.fetchall()
    allcount = len(first_data)
    


    with open('need_to_delete.txt', 'w') as f:
        for pair in first_data:
            try:
                c2.execute(f""" SELECT filename from files WHERE hashcode='{pair[1]}'; """)
                result = c2.fetchall()
                count +=1 
                if(len(result)) >0 :
                    count2+=1
                    f.write(f'{pair[0]}\n')
                    print(f'processed: [{round((count/allcount)*100,5)}%] has copy {count2} from {allcount}')
                    pass
                else:
                    if(count%720==0):
                        print(f'processed: [{round((count/allcount)*100,5)}%] has copy {count2} from {allcount}')
                    pass
                
            except Exception as e:
                print(e)
    print(f"Intersected {count2/count}")
    

