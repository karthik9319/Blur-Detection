import os
import argparse
import cv2

#image should be gray scale
def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()


argparse = argparse.ArgumentParser()

argparse.add_argument("-i", 
                      "--images", 
                      required=True, 
                      help="path to input directory of images")

argparse.add_argument("-t",
                       "--threshold", 
                       type=float, 
                       default=80.00, 
                       help="focus measures that fall below this value will be considered 'blurry'")

args = vars(argparse.parse_args())

data_path = os.path.join(os.getcwd(), "{}" .format(args["images"]))

for root, sub_dirs, files in os.walk(data_path):
    for file in files:
        try:
            image = cv2.imread(os.path.join(root, file))
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            fm = variance_of_laplacian(gray)
            text = "Not Blurry"
            print("fm: ", fm)
            if fm < args["threshold"]:
                text = "Blurry"
                
            cv2.putText(image, "{}: {: .2f}".format(text, fm), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
            cv2.imshow("Image",image)
            cv2.waitKey(0)
        except Exception as e:
            print(e)