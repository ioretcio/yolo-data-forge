import argparse
import os

def translit(text):
    cyrillic_to_latin = {
        'а': 'a',         'б': 'b',        'в': 'v',        'г': 'h',        'ґ': 'g',
        'д': 'd',        'е': 'e',        'є': 'ie',        'ж': 'zh',        'з': 'z',
        'и': 'y',        'і': 'i',        'ї': 'i',        'й': 'i',        'к': 'k',
        'л': 'l',        'м': 'm',        'н': 'n',        'о': 'o',        'п': 'p',
        'р': 'r',        'с': 's',        'т': 't',        'у': 'u',        'ф': 'f',
        'х': 'kh',        'ц': 'ts',        'ч': 'ch',        'ш': 'sh',        'щ': 'shch',
        'ь': '_',        'ъ': '_',        'ю': 'iu',        'я': 'ia',        'А': 'A',
        'Б': 'B',        'В': 'V',        'Г': 'H',        'Ґ': 'G',        'Д': 'D',
        'Е': 'E',        'Є': 'Ie',        'Ж': 'Zh',        'З': 'Z',        'И': 'Y',
        'І': 'I',        'Ї': 'I',        'Й': 'I',        'К': 'K',        'Л': 'L',
        'М': 'M',        'Н': 'N',        'О': 'O',        'П': 'P',        'Р': 'R',
        'С': 'S',        'Т': 'T',        'У': 'U',        'Ф': 'F',        'Х': 'Kh',
        'Ц': 'Ts',        'Ч': 'Ch',        'Ш': 'Sh',        'Щ': 'Shch',        'Ь': '_',
        'Ъ': '_',        'Ю': 'Iu',        'Я': 'Ia', 'Ñ':'N' , ' ':'_', '«':'_', '»':'_',
        '"':'_'
    }
    for key in cyrillic_to_latin.keys():
        text = text.replace(key, cyrillic_to_latin[key])
    to_remove = ['\u0096', '\u0094', '\u0306', '\x80', '\x81', '\x8f', '\u044b', '\uff5c'] #it will grow...
    translation_table = str.maketrans("", "", "".join(to_remove))
    text = text.translate(translation_table)
    return text

def recursively_translit():
    parser = argparse.ArgumentParser(
        description='This program recursively translits filenames from cyrrilic to latin (and wipes strange unicode symbols).')
    parser.add_argument('--root_dir', "-d", help="Root directory of deleting")
    parser.add_argument('--force','-f',action='store_true', help="Force renaming without questions")
    args = parser.parse_args()
    directory_path = args.root_dir
    force_rename = args.force
    count = 0
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            new_name = translit(file)
            if os.path.join(root, file)== os.path.join(root, new_name): continue
            if not force_rename:
                print(f"{force_rename} not True")
                if input(f"(y/n) Do you want to rename {os.path.join(root, file)} to {os.path.join(root, new_name)}?").lower() in ['y', 'yes']:
                    os.rename(os.path.join(root, file), os.path.join(root, new_name))
                    count+=1
            else:
                os.rename(os.path.join(root, file), os.path.join(root, new_name))
                count+=1
    print(f"Renamed {count} files")
                
recursively_translit()
