# MUSA-6950-final

## Introduction

This github repository will showcase my MUSA 6950, AI for Urban Sustainability Final Project. In this project I attempted to use MaskRCNN to identify images within a series of non-geographic YouTube videos to better understand urban and rural environments in Japan. The choice for pursuing this topic is because many YouTube videos are NOT recorded for identifying urban information. If there is a way to identify some trends between environments through these type of videos, it could possibly contribute to expanding a geographic data base for many people to use. 

This project will poke at this idea of obtaining useful information from data not meant to be geographic datasets by looking at the distribution of common urban environment objects throughout different regions of Japan. The project uses the YouTube playlist [tip-to-tip](https://www.youtube.com/watch?v=SHIkv0XH20A&list=PLLGT0cEMIAzeq_YFR_iHm831-GuOWlwUJ), created by YouTuber Ludwig, which documents him and YouTuber Michaell Reeves' travel from the Southern tip of Japan (Cape Sata) to the Northern tip of Japan (Cape Soya) using no maps and highways on their motorcycles. This playlist was chosen as it covers various locations of Japan through a means in which different landscapes are captured, albeit unintentionally. 

To do this, tools such as labelme and pytorch's MaskRCNN models are used to identify four main classes: Buildings, People, Non-Motorcycle Vehicles, and Motorcycles. By using MaskRCNN, we are able to identify these classes in different frames of a video, and count the occurence of these classes throughout the various different locations they pass. While the video shows some geographical information each video, they only show distance to the final locations. Based on this, we separated the videos based on Southern, Central, and Northern Japan, for our final analysis, to look at the change in the urban environment through the four classes. 


