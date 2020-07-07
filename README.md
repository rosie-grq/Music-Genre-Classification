# Music-Genre-Classification

The goal of the project is to use the audio clips of music as input, apply statistical modelling techniques to classify music tracks into eight genres. (Electronic, Experimental, Folk, Hip-Hop, Instrumental, International, Pop and Rock)

## Dataset

The dataset used in this project is the Free Music Archive(FMA) Small dataset. The dataset (8 GB) includes a combination of raw audio files and metadata, has 8 genres and 1000 songs per genre evenly distributed and the audio files length are 30 seconds each. For the scope of the analysis, only the audio files and genre label from the metadata are used.

## Models and Results

Both traditional machine learning models and deep learning models are built for the project. The top performing model is a VGG16 Convolutional Neutral Network with 55.9% accuracy. The second top performing model is the random forest model that achieved 47% accuracy. AWS EC2 Service is used to deploy the CNN models and speed up the training process.

## Repository Contents

1. Processed Data
2. Data Preprocessing .py file
3. Machine Learning and Deep Learning models python Notebooks
4. Project Report


