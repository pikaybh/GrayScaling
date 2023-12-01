import cv2 as cv
import matplotlib.pyplot as plt


class Rgb2Gray:
    def __init__(self, file : str, output_file : str = "OUTPUT"):
        self.file_name = file
        self.custom_output_file_name = False if output_file == "OUTPUT" else output_file
        self.BGR = cv.imread(self.file_name)
        self.RGB = cv.cvtColor(self.BGR, cv.COLOR_BGR2RGB)
        self.BW = cv.cvtColor(self.BGR, cv.COLOR_BGR2GRAY)

    def show(self):
        plt.subplot(1, 2, 1)
        plt.imshow(self.RGB)
        plt.subplot(1, 2, 2) # 1행 2열에서 2번째 열
        plt.imshow(self.BW, cmap='gray')
        plt.xticks([]) # x축 좌표 숨김
        plt.yticks([]) # y축 좌표 숨김
        plt.show()

    def save(self, log : bool = False):
        plt.imshow(self.BW, cmap='gray')
        plt.axis("off")
        if not self.custom_output_file_name:
            f_name, ext = self.file_name.split('.')
            self.custom_output_file_name = f"{f_name}_gray.{ext}"
        plt.savefig(self.custom_output_file_name)
        if log: print(f"{self.custom_output_file_name} is saved successfully.")
