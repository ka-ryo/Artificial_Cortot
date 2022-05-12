import numpy as np
import cv2
import os.path
from os.path import join
import pathlib
from glob import glob
import glob
import os

def main():      
    if not (os.path.exists('input')):
        print("ERROR:Don't exist [input Directory]")
    else:
        #生成した結果を調整します
        #画像のパスを取得
        Folder_names = os.listdir('output/')
        for Folder_name in Folder_names:      
            txt_paths=glob.glob(os.path.join('output/{}/'.format(Folder_name),'*.txt'))
            for txt_path in txt_paths:
                #txtを読み込み
                music_txt =  np.loadtxt(txt_path)
                
                music_txt = music_txt.T

                #128*300に
                music_txt = np.delete(music_txt,slice(299,music_txt.shape[0]-1),0)
                
                array_sum = np.sum(music_txt,axis=1)

                #np.savetxt("output/{}/{}SUM.txt".format(Folder_name,os.path.splitext(os.path.basename(txt_path))[0]),array_sum,"%2d")
                under = 0
                while array_sum[music_txt.shape[0]-under-1]==0:
                    under+=1

                music_txt = np.delete(music_txt,slice(music_txt.shape[0]-under-1,music_txt.shape[0]-1),0)
                
                music_txt = music_txt.T
            
                np.savetxt("output/{}/{}.txt".format(Folder_name,os.path.splitext(os.path.basename(txt_path))[0]),music_txt,"%2d")

if __name__ == "__main__":
    main()