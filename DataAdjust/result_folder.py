import shutil
import os
import glob

def main():
    Folder_names = os.listdir('output/')
    for Folder_name in Folder_names:
        os.makedirs("output/{}/img".format(Folder_name))
        os.makedirs("output/{}/txt".format(Folder_name))
        os.makedirs("output/{}/midi".format(Folder_name))
        img_paths=  glob.glob("output/{}/*png".format(Folder_name))
        txt_paths = glob.glob("output/{}/*.txt".format(Folder_name))
        for img_path in img_paths:
            shutil.copyfile(img_path, "output/{}/img/{}".format(Folder_name,os.path.basename(img_path)))
            os.remove(img_path)

        for txt_path in txt_paths:
            shutil.copyfile(txt_path, "output/{}/txt/{}".format(Folder_name,os.path.basename(txt_path)))
            os.remove(txt_path)

if __name__ == "__main__":
    main()