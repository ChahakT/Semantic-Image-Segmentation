# Semantic Image Segmentation

**Scene Parsing Using Image Segmentation and Semantic Labelling**

Our objective is to segment and parse an image into different image regions associated with
semantic categories, such as sky, road, person, and bed. The data for this challenge comes
from ADE20K Dataset which contains more than 20K scene-centric images exhaustively
annotated with objects and object parts. Specifically, the problem data is divided into 20K
images for training, 2K images for validation, and another batch of held-out images for testing.

There are a total of 150 semantic categories included in the challenge for evaluation, which
include stuffs like sky, road, grass, and discrete objects like person, car,bed. Note that there
are non-uniform distribution of objects occurring in the images, mimicking a more natural
object occurrence in daily scene.

To evaluate the segmentation algorithms, we will take the mean of the pixel-wise accuracy as
the final score. Pixel-wise accuracy indicates the ratio of pixels which are correctly predicted,
averaged over all the 150 semantic categories.

**Methodology**

We implemented 4 models:
1. Naive Bayes
2. Feature Based Classification
3. 2D Bi-Directional RNN architecture
4. Ensemble averaging of state-of-art networks

>Naive Bayes

● 3*3 neighbourhood of each pixel ( RGB image)

● Data point of length 27 was mapped to one of 150 Classes

● Prior and likelihood probabilities learned from 20,000 images

>Feature Based Classification

● 9*9 neighbourhood of each pixel ( gray image) was analysed and five(5) Haralick features from co-occurrence matrices were computed, namely:
  Angular Second Moment, Variance, Entropy, Correlation and Inverse Difference Moment
  
>2D Bi-Directional RNN architecture

● Images are passed through 2 CNN layers with stride of 2 and 3 respectively. Then these images of
dimensions, 64 x 64 x 16, are row wise scanned pixel by pixel and column wise scanning of resulted
image pixel by pixel which results in a image of dimension 64 x 64 x128

>Ensemble averaging

● Intuition: FCN model is more responsive to certain images, similar is the case with Segnet model. For a
test image, we find its correlation with training images to find which model is best suited. Our own
model learns this correlation and gives a corresponding weightage to FCN or Segnet.

To get a probability of 1 for class c1,

a* x1 + (1-α)*x2 =1

 x1: Segnet output
 
 x2: FCN output
 
We learned a model which will predict a weight given to a pre-trained image segmentation model if
image was provided as an input to the ensemble of the two models as shown in the ensemble
architecture.

Training loss: (1-(α*x1 +(1-α)*x2))^2


  
  


