import os
from mixpeek import Mixpeek

api_key = ""
folder_dir = ""

def upload_entire_folder(folder_path):
    # class init
    mix = Mixpeek(api_key=api_key)
    #
    for filename in os.listdir(folder_path):
        #
        r = mix.upload(
            file_name=filename,
            file_path=f'{folder_path}/{filename}'
        )

        print(r)

if __name__ == '__main__':
    upload_entire_folder(folder_dir)
