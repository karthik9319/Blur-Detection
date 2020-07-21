# Blur-Detection

In this repo blur detection is done in two ways

    > Blur detection with OpenCV

    > OpenCV Fast Fourier Transform (FFT) for Blur Detection

# Blur detection with OpenCV

### Uses Variance of the laplacian

The Laplacian is often used for edge detection. The assumption here is that if an image contains high variance then there is a wide spread of responses, both edge-like and non-edge like, representative of a normal, in-focus image. But if there is very low variance, then there is a tiny spread of responses, indicating there are very little edges in the image. As we know, the more an image is blurred, the less edges there are.