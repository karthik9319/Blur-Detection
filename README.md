# Blur-Detection

In this repo blur detection is done in two ways

    > Blur detection with OpenCV

    > OpenCV Fast Fourier Transform (FFT) for Blur Detection

# Blur detection with OpenCV

######  Uses Variance of the laplacian

The Laplacian is often used for edge detection. The assumption here is that if an image contains high variance then there is a wide spread of responses, both edge-like and non-edge like, representative of a normal, in-focus image. But if there is very low variance, then there is a tiny spread of responses, indicating there are very little edges in the image. As we know, the more an image is blurred, the less edges there are.

Two input arguments need to be provided

    > --images "folder where images are located"

    > --threshold "default is 100 where if the focus of image is less that the threshold it says its blurry"

# OpenCV Fast Fourier Transform (FFT) for Blur Detection

###### Fast Fourier Transform

The FFT represents the image in both real and imaginary components. By analyzing these values, we can perform image processing routines such as blurring, edge detection, thresholding, texture analysis, and yes, even blur detection.

Input arguments need to be provided

    > --images "folder where images are located"

Optional arguuments

    > --threshold "default is 10 where if the focus of image is less that the threshold it says its blurry"

    > --vis > 0 "whether or not we are visualizing intermediary steps"

    > --test >0 "whether or not we should progressively blur the image"


# For more information regarding this blur methods 

[Blur detection with OpenCV](https://www.pyimagesearch.com/2015/09/07/blur-detection-with-opencv/)

[OpenCV Fast Fourier Transform (FFT) for Blur Detection](https://www.pyimagesearch.com/2020/06/15/opencv-fast-fourier-transform-fft-for-blur-detection-in-images-and-video-streams/)