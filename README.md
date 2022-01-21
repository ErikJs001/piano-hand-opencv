# Piano-Hand-OpenCV
A simple piano that can be played by positioning the fingers on the corresponding keys, with a hand tracker using _MediaPipe_ and _OpenCV_.
- OpenCV 🤖
- MediaPipe 👁 
- PyGame 👾
- Piano 🎹

## Project Description
The program draws multiple lines on screen simulating a piano, with a hand tracker using _MediaPipe_, we detected our fingers, then we can positioned our fingers in the keys drawed and play specifics notes or some chords.
I'm an amateur musician who loves piano, I thought it could be entertained code a simple piano using _MediaPipe_ and _OpenCV_.

I have several problems with sounds, but finally, with _pygame_, I was able to combine multiple sounds into one. In each frame, we detect the sounds that could be sound and add to an empty _.wav_ file, and finally after iteraing into each finger, we play the final sound.

The file could be edited to switch from your webcam to your phone's camera, using _IP Webcam_, only uncomments a few lines and that is all.

### Libraries, how to Install and Run
Maybe you will have to install multiple libraries, only copy this lines:
| Libraries | Links |
| ------ | ------ |
| [OpenCV][opencv] | ```pip install opencv-python``` |
| [MediaPipe][mediapipe] | ```pip install mediapipe``` |
| [PyGame][pygame]| ```pip install pygame``` |
| [Pydub][pydub]| ```pip install pydub``` |
| [Request][request] | ```pip install requests```|
| [Numpy][numpy] | ```pip install numpy``` |
| [imutils][imutils] | ```pip install imutils```|

If you already have all libraries, just drop the folder into VSCode and run!
> Note: This project was development with Python 3.10.2

## How to Use 
When you run the file, Python will draw lines in your video, so, try to position your webcam in a clear place and put your hand in front the webcam. When MediaPipe already detects your hands just keep your fingers in the keys and play. 

## Credits
I learned about hand tracker from a video. I will leave you the link [`Gesture Volumen Control`][videoTracker].




## License
MIT License

Copyright (c) [2021] [Erik Js. González]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.




**Free Software, thanks Lord!**

[//]: #
   [opencv]: <https://opencv.org/>
   [mediapipe]: <https://mediapipe.dev/>
   [pygame]: <https://www.pygame.org/>
   [pydub]: <https://github.com/jiaaro/pydub>
   [request]: <https://docs.python-requests.org/en/latest/>
   [numpy]: <https://numpy.org/>
   [imutils]: <https://github.com/PyImageSearch/imutils>
   [videoTracker]: <https://www.youtube.com/watch?v=9iEPzbG-xLE>
