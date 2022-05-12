import numpy as np
import cv2
import os.path
from os.path import join
import pathlib
from glob import glob
import os

def main():      
    if not (os.path.exists('input')):
        print("ERROR:Don't exist [input Directory]")
    else:
        #生成した結果を調整します
        #画像のパスを取得
        Folder_names = os.listdir('output/')
        for Folder_name in Folder_names:
            input_files = []
            for ext in ('*.png', '*.jpg'):
                input_files.extend(glob(join("output/{}/".format(Folder_name), ext)))

            for Result_Path in input_files: 
                #画像を読み込み
                music_img =  cv2.imread('{}'.format(Result_Path), cv2.IMREAD_GRAYSCALE)
                #0,255だけに変換
                music_img = np.where(music_img<120,0,255)#"4"は適当ここを調整する必要あり
                #cv2.imwrite('B.img', music_img)
                
                #0,1に変換
                music_img_binary = np.where(music_img==255,1,0)
                
                #128*500に戻す
                music_img_binary = np.delete(music_img_binary,slice(127,music_img_binary.shape[0]-1),0)

                music_img_binary = music_img_binary.T

                #128*301に戻す
                music_img_binary = np.delete(music_img_binary,slice(300,music_img_binary.shape[0]-1),0)
                
                array_sum = np.sum(music_img_binary,axis=1)

                #np.savetxt("output/{}/{}SUM.txt".format(Folder_name,os.path.splitext(os.path.basename(Result_Path))[0]),array_sum,"%2d")
                under = 0
                while array_sum[music_img_binary.shape[0]-under-1]==0:
                    under+=1
                
                music_img_binary = np.delete(music_img_binary,slice(music_img_binary.shape[0]-under-1,music_img_binary.shape[0]-1),0)
                
                music_img_binary = music_img_binary.T
            
                np.savetxt("output/{}/{}.txt".format(Folder_name,os.path.splitext(os.path.basename(Result_Path))[0]),music_img_binary,"%2d")

if __name__ == "__main__":
    main()