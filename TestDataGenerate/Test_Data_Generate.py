from TestDataGenerate import midi_scan
from TestDataGenerate import txt2img
import subprocess
import shutil
import os

def main():
    os.makedirs("TEMP")
    denominator,numrator=midi_scan.main()
    txt2img.main()
    cmd = "python TestDataGenerate/scripts/combine_A_and_B.py --fold_A TEMP --fold_B TEMP --fold_AB output"
    subprocess.call(cmd,shell=True)
    shutil.rmtree("TEMP")
    return denominator,numrator

if __name__ == "__main__":
    main()