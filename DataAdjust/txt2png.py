import cv2
import numpy as np
import os 
import glob
#txtのピアノロールをjpgに変換する
def main():
    Folder_names = os.listdir('output/')
    for Folder_name in Folder_names:        
        txt_paths=glob.glob(os.path.join('output/{}/'.format(Folder_name),'*.txt'))
        for txt_path in txt_paths:
            music_txt = np.loadtxt(txt_path)*255
            #music_txt = music_txt[:,:,np.newaxis]
            #拡張し無しファイル名を取得
            music_name_path=os.path.splitext(os.path.basename(txt_path))[0]

            cv2.imwrite('output/{}/{}.png'.format(Folder_name,music_name_path), music_txt)

if __name__ == "__main__":
    main()
            