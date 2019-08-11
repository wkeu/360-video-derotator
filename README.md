# 360 Video Derotator

# Introduction 
This presents a method for removing ro-tational motion from an omnidirectional video captured from the viewpoint of a spinning object. For instance, the technique
could be used to recover stable footage from spherical video captured from within a football used for competitive sports. The methodology uses a rotationally-invariant algorithm to obtain
feature points and descriptors for pairs of successive frames. This information is then abstracted into three-dimensional point clouds, from which the Kabsch algorithm can infer the rotational
motion between frames. The resulting rotational matrices are used to remap each equirectangular frame to a reference frame, and thereby offset the effect of frame-to-frame camera rotations.
The algorithm has been successfully tested with various styles of footage

-Link to demo video showing the before and after. 


# Installation
( Required packages, python version used, opencv version used)

# Hot to use
-Instructions on how use the repo on your video.  

# Methodology
-Short details about the methodology. Link to my thesis paper for further reading. 
-Link to paper
-Link to thesis

# Future Works
-A TODO section at the end so that if anyone wants to use the code they can. Improvements to methodology, porting to C#/C++.
