import cv2
import numpy as np
import os
import glob
#txtのピアノロールをjpgに変換する
#フォルダ内はピアノロールのtxtが直で入っていることを前提としている
#txtは削除され画像データのみが残る
def main():


    txt_paths=glob.glob(os.path.join("output/",'*.txt'))

    for txt_path in txt_paths:
        music_txt = np.loadtxt(txt_path)*255
        music_txt = music_txt[:,:,np.newaxis]
        tmp_musictxt = np.append(music_txt,music_txt,axis=2)
        tmp_musictxt = np.append(tmp_musictxt,music_txt,axis=2)
        music_txt = tmp_musictxt
        #拡張し無しファイル名を取得
        music_name_path=os.path.splitext(os.path.basename(txt_path))

        cv2.imwrite('output/{}.png'.format(music_name_path[0]), music_txt)
        cv2.imwrite('TEMP/{}.png'.format(music_name_path[0]), music_txt)
if __name__ == "__main__":
    main()
