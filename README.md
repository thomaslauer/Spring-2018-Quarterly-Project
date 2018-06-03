# Spring-2018-Quarterly-Project: IoT Laundry Monitor

## Introduction

The concept behind this project came from the realization of a common dilemma that we all faced living in residence halls—we shared laundry rooms with limited numbers of laundry machines. This meant that often times, people would have to walk to the laundry room initially without laundry to check if a laundry machine was available. If a laundry machine was available, then people would have to walk back to their rooms and make a second trip back to the laundry room this time actually with laundry, sometimes only to find that the laundry machines had been occupied again between the time they made the two trips to the laundry room.

Through this problem, we decided to create a device that would allow people living with shared laundry rooms to monitor the on-or-off status of laundry machines remotely, without having to make trips to the laundry room to find a conflict of interest in wait time to use the machines.

Our project aims to minimize the number of trips that people have to take to check the laundry room, the occurrences of forced laundry removal for people who don’t want to wait for others to take out their finished laundry, and overall, the efficiency of laundry machine use in shared laundry rooms. With our product that we’ve created through this project, we hope to increase the satisfaction of the residence hall living experience for students living on campus or people living with shared laundry machines for years to come.

## Materials

* Raspberry Pi
* Power supply
* Microphone to detect the sound on the Pi
* WiFi connection

## Instructions

### Connect Microphone to Raspberry PI:

Any standard microphone should work, as long as it works with Linux without drivers. We used a cheap $5 microphone off Amazon, so pretty much anything should be fine. 


### Installing Python and Packages:

Our code needs to have many Python packages installed. Currently, we’re using Python’s sounddevice to record our sounds, NumPy to store and manipulate the data, SciPy to run a Fourier transform that helps with filtering frequencies, matplotlib to display the data locally, and Adafruit IO to display the data online

To install all the pure Python dependencies, all you should need to do is run the commands:

`< sudo pip3 install cffi >` and
`< sudo pip3 install numpy scipy matplotlib adafruit-io >`

This assumes that the correct versions of the packages are available from the package servers. We had an issue where the highest available version of Python was 3.5, but we NumPy was requiring 3.6. To solve this, we manually compiled Python 3.6 and side installed it. This just changes the commands from “python3” and “pip3” to “python3.6” and “pip3.6”. 


### Get the Code:

To get our code, just clone our Github repo:
https://github.com/thomaslauer/Spring-2018-Quarterly-Project



### Test installation:

To test that everything is installed correctly, run `<python3 fftTest.py>`

This should make two plots, one of the raw sound sample, and another of a Fourier transform from the sound.

### Here are some example images:

![Frequency Plot](https://github.com/thomaslauer/Spring-2018-Quarterly-Project/blob/master/screenshots/Frequency%20Plot.png)

![Sound Plot](https://github.com/thomaslauer/Spring-2018-Quarterly-Project/blob/master/screenshots/Sound%20Plot.png)

The plot on the left is the raw sound sample, and the one on the right is the Fourier transform. We can see that the fourier transform picks out the frequencies.

### Install Raspberry Pi:

The next step is to mount the Pi in the washing machine room. We just used double-sided foam tape, any mounting system really works. If it can be mounted closer to the washing machines it will work better because they are the most quiet.

### Pick a configure code:

There are two things that need to be edited in the Python code, the Adafruit IO key and the sound threshold. To connect your Adafruit account, replace our key in main.py with your own. To set up the threshold, run main.py with Python 3 (or Python 3.6, if you needed to install it). This will start printing out values of our sound. This is the average value for the intensity of the sound between 250 Hz and 3000 Hz. There’s no surefire way to pick a good threshold. We recommend looking at the volume when nothing is running, and then see how much sound it makes when the washing machines are. Put a number somewhere between the two in the variable THRESHOLD in the code. 


### Use it!

After you set up the correct data feeds on Adafruit IO, the code should start sending data! We recommend creating a dashboard so you can more easily monitor how available the machines are. 

### Here’s what our dashboard looks like:

![Frequency Plot](https://github.com/thomaslauer/Spring-2018-Quarterly-Project/blob/master/screenshots/Dashboard.png)

You can see that we are displaying line graphs of the volume level in the laundry room as well as if the machines are available.

## Conclusion

With more time, energy, funding, and resources, we recognize that we could have added more features to our product. One feature that we could have added was a display of the information that analyzes the data about when and how busy the washing machines are at different times, similar to how Google Maps’ Popular Times feature displays the busiest hours for restaurants and stores. This information could encourage students to do laundry during the less busy hours to smooth out the laundry room traffic.

We also could have improved the way the information was displayed by deleting data that was irrelevant for the visual information. The greatest obstacle was working with the Python language and all the intricacies of adafruit’s functions.

A different solution to this problem would have involved altering the machine students use to swipe their triton card to start the washing machine or dryer. Since this device is already connected to the internet to deduct the laundry balance for each student, we could have kept track of any changes to the account as an indication of the washer or dryer being turned on.

Another thing we would have changed is the interface of the entire product and put the user interactions on an app instead of a website so that it is more personalized. The user can see which individual washer and dryer is open or not, and the user can also label a machine to indicate that they are using it currently so a reminder or notification can come up on their phone when the machine stops producing sounds, thus indicating that the washing machine cycle has ended.

Overall, our project provided a great learning opportunity, as we used open-source libraries such as ones for adafruit.io and SciPy to obtain a more well-rounded grasp of how these resources can be applied to practical applications. Through our exploration of these resources, our greatest obstacle within this project came from connecting various tools to make a refined and consolidated product. At the same time, our greatest obstacle became our greatest success, as we were ultimately able to create a functioning product that fulfilled the purpose and brought to life the idea of what we set out to make.


## References

### Adafruit IO Basics Overview
https://learn.adafruit.com/adafruit-io-basics-feeds/overview

Explained how to create dashboards, feeds, and displays on adafruit to display the information from the Pi.



### Adafruit IO Python Client Library
https://github.com/adafruit/io-client-python

Helped us figure out how to process and send data to an online display for our product to be monitored from a remote source.



### But what is the Fourier Transform? A visual introduction.
https://www.youtube.com/watch?v=spUNpyF58BY

Guided our understanding of the applications of the Fourier Transform with an animated introduction to the concept.



### Elegant SciPy by Harriet Dashnow, Stéfan van der Walt, Juan Nunez-Iglesias
https://www.safaribooksonline.com/library/view/elegant-scipy/9781491922927/ch04.html

Provided templates and guidance for us to understand the applications of using SciPy to analyze sound.



### Installing Python 3.6 on Raspberry Pi
https://gist.github.com/dschep/24aa61672a2092246eaca2824400d37f

Guided us through figuring out how to connect our written code onto a Raspberry Pi.



### SciPy.org
https://scipy.org/

Equipped us with libraries, documentation, and tutorials for processing scientific data through open-source software.

