# Voice-Based-Music-Playlist-Generator
This project was done as a sample project for proof of concept. 

## INTRODUCTION:
Voice Based Mood Analyzed System is named as such as it is a service which takes in user voice tone and analyses this for the mood of the user. The user says something along the lines of “Play a song” and just this line is used to detect the mood of user. This mood is then used to find the tracks suitable for the mood of the listener. This service employs the application of Natural Language Processing, a domain of Artificial Intelligence and Machine Learning.
This project is based on implementing a database of music playlist which would be created from a database of songs by using Spotify API and analyzing the lyrics and music of the song, tags provided by the users and the artist. It will use Watson Tone Analyzer AI and NLP for processing the voice and lyrics of the songs. 


## Use of Machine Learning:
For our project, we have used the concept of natural language processing. The ML model powering our project is SVM. When we run the project, an audio is recorded which is stored in form of waveforms. This waveform is then passed to the IBM cloud-based Tone analyser, which analyses and provides us with mood of the user. 
The service uses linguistic analysis and the correlation between the linguistic features of written text and emotional and language tones to develop scores for each of these tone dimensions
### SVM: 
The objective of the support vector machine algorithm is to find a hyperplane in an N-dimensional space (N — the number of features) that distinctly classifies the data points. The data points are generated from the waveform provided.
Hyperplanes are decision boundaries that help classify the data points. Data points falling on either side of the hyperplane can be attributed to different classes.
Support vectors are data points that are closer to the hyperplane and influence the position and orientation of the hyperplane. Using these support vectors, we maximize the margin of the classifier. Deleting the support vectors will change the position of the hyperplane. These are the points that help us build our SVM.
For the machine-learning model, This model leveraged several categories of features:
*	N-gram features
*	Lexical features from various dictionaries
*	The existence of second-person references in the conversation
*	Some dialogue-specific features such as saying thank you or apologizing
The reason for using SVM as compared to other algorithms like Naïve Bayes Algorithm and kNN Algorithm stems from the fact that SVM is used to analyse datasets in hyperplane. As our waveform is plotted in hyperplane, this increases the accuracy to determine the different highs and lows of the waveform. The data points collected from this hyperplane are used to determine the mood of the user. This model provides best accuracy at present as compared to other models, with accuracy over 80 percent as compared to other state of the art models’ 60 percent.

## FLOWCHART

![Process flowchart](/Images/Flowchart.jpg "FLOWCHART")

## ER Diagram

![ER Diagram](/Images/ER_Diagram.png "ERD")

## Output

![Output](/Images/Output.png "Output")

