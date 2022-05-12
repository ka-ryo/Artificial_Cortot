import subprocess
import os
import glob
import sys
import shutil
from TestDataGenerate import Test_Data_Generate
from DataAdjust import DataAdjustMain
from txt2mid import txt2midmain
from Organize import target_remove

if __name__ == "__main__":
    #input,outputのディレクトリの存在を確認
    if not os.path.exists("input"):
        print("inputフォルダを生成します")
        print("inputフォルダの中にmidiデータを入れて再度このプログラムを実行してください")
        sys.exit()
        os.makedirs("input")
    if not os.path.exists("output"):
        os.makedirs("output")
    else:
        shutil.rmtree("output")
        os.makedirs("output")

    #inputのmidiデータをTestDataでTestデータに
    #input内にmidiが入っているかを確認
    if len(list(glob.glob('input/*.mid')))==0:
       print("inputフォルダの中にmidiデータを入れて再度このプログラムを実行してください")
       sys.exit()
    numrator_list,denominator_list=Test_Data_Generate.main()
    #pix2pixのテストを実行する
    cmd = 'python pix2pixProrams/pix2pix.py --mode test --output_dir TEMP --input_dir output --checkpoint pix2pixProrams/train_result'
    returncode = subprocess.call(cmd,shell=True)

    shutil.rmtree("output")
    os.makedirs("output")

    Png_File_Paths = glob.glob('TEMP/images/*.png')
    File_Count = 0
    for Png_File_Path in Png_File_Paths:
        if File_Count%3 == 0:
            basename_without_ext = os.path.splitext(os.path.basename(Png_File_Path))[0]
            basename_without_ext.replace("_inputs","")
            os.makedirs("output/{}".format(int(File_Count/3)))
        shutil.copyfile(Png_File_Path, "output/{}/{}".format(int(File_Count/3),os.path.basename(Png_File_Path)))
        File_Count+=1
    DataAdjustMain.main()
    txt2midmain.main(denominator_list,numrator_list)

    shutil.rmtree("TEMP")

    target_remove.main()