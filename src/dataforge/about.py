def about():
    print(f"\t{'df_pairs'.ljust(15)} Finds and moves pictures without labels and labels without pictures to a 'single' folder")
    print(f"\t{'df_split'.ljust(15)} Splits images and annotations in a selected percentage configuration across training, validation, and test folders")
    print(f"\t{'df_4parts'.ljust(15)} Converts big-sized images to smaller patches (1to4)")
    print(f"\t{'df_decimator'.ljust(15)} Analyzes the structure of the images and discards those that have copies to a separate directory")
    print(f"\t{'df_partmove'.ljust(15)} Moves only specific part of data to another folder(sorted by name). Can be helpful in pack creation.")
    print(f"\t{'df_latin'.ljust(15)} This program recursively translits filenames from cyrrilic to latin (and wipes strange unicode symbols).")
    print(f"\t{'df_partmove'.ljust(15)} Moves only specific part of data to another folder(sorted by name). Can be helpful in pack creation.")
    print(f"\t{'df_bright_sort'.ljust(15)} Sorts(renames with numbers) images by its brightness and returns afterwork.")
    print(f"\t{'df_video_duration'.ljust(15)} This program counts total duration of video in folder.")
    
    print(f"\t{'df_carmerge'.ljust(15)} Carefully merge two dirs, using random to unicalizate names in case of conflict.")
    print(f"\t{'df_extadd'.ljust(15)} This program adds extension to broken files.")
    
    print("\nExact copies cleaner")
    print(f"\t1-{'df_sizes_dump'.ljust(15)} Creates a txt file with recursively found and sorted by size files in selected directory.")
    print(f"\t1-{'df_sizes_dump'.ljust(15)} Creates a txt file with recursively found and sorted by size files in selected directory.")
    print("\nConverts:")
    print(f"\t{'df_yolo2labelimg_obb'.ljust(15)} Converts from yolo_obb label format detect output to labelimg format.")
    print("\nHashes methods")
    print(f"\t{'df_hash_db'.ljust(15)} Creates a database of datasets images hashes (path-MD5hash)")
    print(f"\t{'df_hash_xf'.ljust(15)} Finds the intersection of hashes from database and images in folder")
    print(f"\t{'df_db_intersection'.ljust(15)} Finds the intersection of hashes from two databases and creates need_to_delete.txt file with list of dubles.")
    print(f"\t{'df_merge_db'.ljust(15)} This program merges all .dbs in the directory.")
