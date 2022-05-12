from DataAdjust import result_adjust
from DataAdjust import noise_remove
from DataAdjust import txt2png
from DataAdjust import result_folder
from DataAdjust import line0_remove
def main():
    result_adjust.main()
    noise_remove.main()#
    line0_remove.main()#
    txt2png.main()
    result_folder.main()    

if __name__ == '__main__':
    main()
        