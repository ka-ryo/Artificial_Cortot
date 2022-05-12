
import pretty_midi
import numpy as np
import os.path
import pathlib
import glob
import re

def scan(midi_file_name):
    hight = 128
    width = 512
    np.set_printoptions(threshold=np.inf)
    #midiデータを読み込む
    midi_file = pretty_midi.PrettyMIDI(str(midi_file_name))
    #拍子を取得
    A=midi_file.time_signature_changes
    A = str(A[0])
    A = re.findall('[0-9]+',A)
    denominator=A[0]
    numrator=A[1]
    #midiデータ（ピアノ）をNumpyで保存
    midi_numpy = midi_file.get_piano_roll()

    if midi_numpy.shape[1] != width:
        zero_array = np.zeros((hight,width-midi_numpy.shape[1]))
        midi_numpy=np.hstack((midi_numpy,zero_array))


    #intへ変更
    int64_midi_numpy = midi_numpy.astype(np.int64)
    bool_midi_file = (midi_numpy > 0)
    one_hot_vector_midi = bool_midi_file.astype(np.int)
    #正方形に変形
    #追加する奴生成
    add_array = np.zeros([1,width])
    for i in range(width-hight):
        one_hot_vector_midi = np.concatenate([one_hot_vector_midi,add_array])
    #txt保存
    np.savetxt('output/{}.txt'.format((os.path.splitext(os.path.basename(midi_file_name))[0])),one_hot_vector_midi,fmt="%2d")
    return numrator,denominator

def main():
    #originalとpracticeのパスを取得する
    first_dir = os.getcwd()
    #データのフォルダーパス
    Result_Path = pathlib.Path('input')
    #mid取得
    Music_name_paths =pathlib.Path(Result_Path).glob('*')
    #拍子を保存するlist
    numrator_list=[]
    denominator_list=[]
    #midiを読み込んで拍子を受け取る
    for Music_name_path in Music_name_paths:
        numrator,denominator=scan(Music_name_path)
        numrator_list.append(numrator)
        denominator_list.append(denominator)


    return  numrator_list,denominator_list

if __name__ == '__main__':
    main()