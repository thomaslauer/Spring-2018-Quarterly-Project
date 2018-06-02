# Spring-2018-Quarterly-Project

## Introduction

The concept behind this project came from the realization of a common dilemma that we all faced living in residence halls—we shared laundry rooms with limited numbers of laundry machines. This meant that often times, people would have to walk to the laundry room initially without laundry to check if a laundry machine was available. If a laundry machine was available, then people would have to walk back to their rooms and make a second trip back to the laundry room this time actually with laundry, sometimes only to find that the laundry machines had been occupied again between the time they made the two trips to the laundry room.

Through this problem, we decided to create a device that would allow people living with shared laundry rooms to monitor the on-or-off status of laundry machines remotely, without having to make trips to the laundry room to find a conflict of interest in wait time to use the machines.

Our project aims to minimize the number of trips that people have to take to check the laundry room, the occurrences of forced laundry removal for people who don’t want to wait for others to take out their finished laundry, and overall, the efficiency of laundry machine use in shared laundry rooms. With our product that we’ve created through this project, we hope to increase the satisfaction of the residence hall living experience for students living on campus or people living with shared laundry machines for years to come.

## Materials

Raspberry Pi
Power supply
Microphone to detect the sound on the Pi
WiFi connection

## Instructions

### Connect Microphone to Raspberry PI:

Any standard microphone should work, as long as it works with linux without drivers. We used a cheap $5 microphone off amazon, so pretty much anything should be fine. 


### Installing Python and Packages:

Our code needs to have many python packages installed. Currently, we’re using sounddevice to record our sounds, numpy to store and manipulate the data, scipy to run a Fourier transform that helps with filtering frequencies, matplotlib to display the data locally, and Adafruit IO to display the data online

### To install all the pure python dependencies, all you should need to do is run the commands

sudo pip3 install cffi
sudo pip3 install numpy scipy matplotlib adafruit-io

This assumes that the correct versions of the packages are available from the package servers. We had an issue where the highest available version of python was 3.5, but we numpy was requiring 3.6. To solve this, we manually compiled python 3.6 and side installed it. This just changes the commands from “python3” and “pip3” to “python3.6” and “pip3.6”. 


### Get the Code:

To get our code, just clone our github repo:
https://github.com/thomaslauer/Spring-2018-Quarterly-Project



### Test installation:

To test that everything is installed correctly, run “python3 fftTest.py.” 

This should make two plots, one of the raw sound sample, and another of a Fourier transform from the sound.


### Install Raspberry Pi:

The next step is to mount the pi in the washing machine room. We just used double sided foam tape, any mounting system really works. If it can be mounted closer to the washing machines it will work better because they are the quietest.

### Pick a configure code:

There are two things that need to be edited in the python code, the Adafruit io key and the sound threshold. To connect your Adafruit account, replace our key in main.py with your own. To set up the threshold, run main.py with python3 (or python3.6, if you needed to install it). This will start printing out values of our sound. This is the average value for the intensity of the sound between 250 Hz and 3000 Hz. There’s no sure fire way to pick a good threshold. We recommend looking at the volume when nothing is running, and then see how much sound it makes 

