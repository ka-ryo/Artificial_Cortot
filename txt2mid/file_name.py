import os.path
import pathlib
import glob
import subprocess

def main(numerator_list,denominator_list):
    Folder_names = os.listdir('output/')
    for Folder_name in Folder_names:
        #データのフォルダーパス
        Input_Path = pathlib.Path('output/{}/txt/'.format(Folder_name))
        #データを取得
        txt_name_paths =pathlib.Path(Input_Path).glob('*.txt')
        for txt_name_path in txt_name_paths:
            print(txt_name_path)
            cmd = 'txt2mid/txt2mid.exe {} {} {} {} {}'.format(txt_name_path,os.path.splitext(os.path.basename(txt_name_path))[0],numerator_list[int(Folder_name)],denominator_list[int(Folder_name)],os.path.basename(Folder_name))
            returncode = subprocess.call(cmd)


if __name__ == "__main__":
    main()