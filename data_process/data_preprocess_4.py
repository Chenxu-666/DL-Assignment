import SimpleITK as sitk
import numpy as np
import cv2
import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'


def convert_from_dicom_to_jpg(img, low_window, high_window, save_path):
    toothwin = np.array([low_window * 1., high_window * 1.])
    newimg = (img - toothwin[0]) / (toothwin[1] - toothwin[0])
    newimg = (newimg * 255).astype('uint8')
    cv2.imwrite(save_path, newimg, [int(cv2.IMWRITE_JPEG_QUALITY), 100])


path = r'D:\datasets\dataset_1\姜子拓@\姜子拓CT'
filename = os.listdir(path)
print(filename)
count = 1

for i in filename:
    document = os.path.join(path, i)
    save_path = r"D:\datasets\dataset_unlabeled_and_labeled\jiangzituoAT/img_" + str(count).rjust(4, '0') + ".jpg"

    if __name__ == '__main__':
        ds_array = sitk.ReadImage(document)
        img_array = sitk.GetArrayFromImage(ds_array)
        shape = img_array.shape  # name.shape
        img_array = np.reshape(img_array, (shape[1], shape[2]))
        high = np.max(img_array)
        low = np.min(img_array)
        convert_from_dicom_to_jpg(img_array, low, high, save_path)
        print('FINISHED')
    count = count + 1
