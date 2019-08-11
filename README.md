# 360 Video Derotator

## Introduction 
This repo presents a method for removing rotational motion from an omnidirectional video captured from the viewpoint of a spinning object. This agorithm can be used to recover stable footage from spherical video captured from a spinning 360 camera. 
The algorithm has been successfully tested with various styles of footage which can be viewed [here](https://www.youtube.com/playlist?list=PL9XiBq5tluqSOiY56WZ51r66WDUoJMMfZ). Below is a 

![alt text](https://drive.google.com/file/d/1TX3w71j0n_sSTf0AUQnef9MzKbw2tYmy/view?usp=sharing)

-TODO Insert image or gif showing the before and after. 
-Link to demo video showing the before and after. 

## Package Requirments
Note that the following packages are required/reccomended in order to use the directory:
- Anaconda2 4.2.0 (Python 2.7.12)
- OpenCV 2.4.13
- Numpy 
- Matplot Lib
- PIL 

## Hot to use
In order to use the package first download the repo. Assuming you have installed the required packages into your environment. 

TODO
- Instructional video on how use the repo on your video.  

### Tuning
It is possible to experiment with the results of the video by varying the number of features which are used to track the motion between frames. 

## Methodology
The methodology uses a rotationally-invariant algorithm to obtain feature points and descriptors for pairs of successive frames. This information is then abstracted into three-dimensional point clouds, from which the Kabsch algorithm can infer the rotational motion between frames. The resulting rotational matrices are used to remap each equirectangular frame to a reference frame, and thereby offset the effect of frame-to-frame camera rotations.

For more comprehensive details about the methodology please refer to the following:  
- IEEECON 2019 Publication ( Link pending presentation )
- Maters Thesis ([link](https://drive.google.com/file/d/1C_PAVe0sNiquvzk1Aolnvb1vl0BBU330/view?usp=sharing))

## Future Works
-A TODO section at the end so that if anyone wants to use the code they can. Improvements to methodology, porting to C#/C++.

### TODO:
- o
