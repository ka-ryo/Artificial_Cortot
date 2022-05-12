import os.path
import pathlib
import glob
import subprocess
import os

def main():
    Folder_names = os.listdir('output/')
    for Folder_name in Folder_names:
        #データのフォルダーパス
        Input_Path = pathlib.Path('output/{}'.format(Folder_name))
        #データを取得
        remove_file_paths =pathlib.Path(Input_Path).glob('*/*target*')
        for remove_file_path in remove_file_paths:
            #targetの削除
            os.remove(remove_file_path)

        File_Path=list(pathlib.Path('output/{}/midi'.format(Folder_name)).glob("*"))[0]
        File_Path = os.path.splitext(os.path.basename(File_Path))[0]
        File_Path= str(File_Path).replace("-inputs",'')
        os.chdir("output")
        os.rename("{}".format(Folder_name),File_Path)
        os.chdir("../")


if __name__ == "__main__":
    main()