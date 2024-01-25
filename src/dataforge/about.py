def about():
    print(f"{'df_pairs'.ljust(15)} Finds and moves pictures without labels and labels without pictures to a 'single' folder")
    print(f"{'df_split'.ljust(15)} Splits images and annotations in a selected percentage configuration across training, validation, and test folders")
    print(f"{'df_4parts'.ljust(15)} Converts big-sized images to smaller patches (1to4)")
    print(f"{'df_hash_db'.ljust(15)} Creates a database of datasets images hashes (path-MD5hash)")
    print(f"{'df_decimator'.ljust(15)} Analyzes the structure of the images and discards those that have copies to a separate directory")
    print(f"{'df_hash_xf'.ljust(15)} Finds the intersection of hashes from database and images in folder")