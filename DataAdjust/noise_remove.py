#1の数が5以下のものを削除してノイズを消します
import numpy as np
import os 
import glob


def main():
    Folder_names = os.listdir('output/')
    for Folder_name in Folder_names:      
        txt_paths=glob.glob(os.path.join('output/{}/'.format(Folder_name),'*.txt'))
        for txt_path in txt_paths:
            np_txt_pianoroll=np.loadtxt(txt_path)
            #1が発見された座標
            Save_Point=np.array((2,2))
            #1の連続回数
            One_Count = 0
            for i in range(np_txt_pianoroll.shape[0]):
                One_Count=0
                for j in range(np_txt_pianoroll.shape[1]):
                    #1が出たらカウント＆始めは座標も登録
                    if(np_txt_pianoroll[i][j]==1):
                        if(One_Count == 0):
                            Save_Point=[i,j]
                        One_Count+=1
                        if(j==np_txt_pianoroll.shape[1]-1 and One_Count != 0):
                            print(j)
                            for replace_num in range(One_Count):
                                np_txt_pianoroll[Save_Point[0]][Save_Point[1]+replace_num]=0
                            One_Count=0
                    #0が出る＆1がカウントされていた
                    if(np_txt_pianoroll[i][j]==0 and One_Count!=0):
                        #1の登場回数が5以下だった場合
                        if 5>=One_Count:
                            for replace_num in range(One_Count):
                                np_txt_pianoroll[Save_Point[0]][Save_Point[1]+replace_num]=0
                            One_Count=0
                        else:
                            One_Count=0
                    if(One_Count==0):
                        One_Count=0
            np.savetxt("output/{}/{}.txt".format(Folder_name,os.path.splitext(os.path.basename(txt_path))[0]),np_txt_pianoroll,"%2d")

if __name__ == "__main__":
    main()