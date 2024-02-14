import sqlite3
from sqlite3 import Error
import os
import argparse

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        return conn

def merge():
    parser = argparse.ArgumentParser(
        description='This program merges all .dbs in the directory.')
    parser.add_argument('--root_dir', "-d", help="Root directory with dbs")
    parser.add_argument('--file_destination','-f', help="Destination file")
    args = parser.parse_args()
    directory_path = args.root_dir
    target_file = args.file_destination
    if not target_file.endswith('.db'): target_file+='.db'
    
    conn_target = create_connection(target_file)
    cursor_target = conn_target.cursor()
    cursor_target.execute( """ CREATE TABLE IF NOT EXISTS files (filename text UNIQUE NOT NULL,hashcode text NOT NULL); """)
    for file in os.listdir(directory_path):
        if file.endswith('.db') and file!=target_file:
            print(f"merging {file}")
            tmp_cursor = create_connection(file).cursor()
            tmp_cursor.execute(f""" SELECT * from files; """)
            result = tmp_cursor.fetchall()
            for image in result:
                querry = f"INSERT or REPLACE INTO files (filename, hashcode) values\
                        ('{image[0]}','{image[1]}');"
                cursor_target.execute(querry)
        conn_target.commit()