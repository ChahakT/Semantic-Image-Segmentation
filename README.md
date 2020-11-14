# Semantic-Image-Segmentation

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
