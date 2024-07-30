**SIGN LANGUAGE DETECTION**

Sign language detection is made to understand and provide an effective means of communication for deaf or hard-of-hearing individuals who use sign language as their primary means of communication. 
Here I have collected my own dataset. And if you are wanting to take the help of this code then you need to collect your own dataset. 
So here you can see 2 .py files in which one file is to collect data and other file is main. 

**I have not added data folder as it was having too much data and was not able to upload. Actually there was max 70 -100 images of each sign that's why.**

*So here I have explained data or image collection steps.*

**DATA COLLOCTION STEPS**

To collect data create a folder with name Data and in that folder create different folders with different sign name. 
Then create a file with .py extension ......as you can see hee 
File named as "Compute_image.py" is having the for collecting data in the form of images. 
In the file "Compute_image.py" line no. 13      
           folder = "C:/Users/hp/Desktop/Sign Language Detection/Data/**Thank you**"   
           you have to just change the last file name where ther is **thank you** there you will have to add your own file or sign name that you want. 
          This thank you will collect data for thank you sign and if you will change thank you to hello it will collect images for hello .

**To collect images you have to press **d** , by which images will be saved in your data folder** 

Then train you model and create a main file with name **test.py**.
After that you have the same code as in the compute_images.py But there are some silly changes lik prdictions 
    run the file **test.py**
    if it give error then install tensorflow with the help of the terminal
    And then again run file **test.py**
***Make sure your camera is not disabled.**
it will take 2-3 mins in running and collecting data after running main file. 
 And then a new file will open and then whem you show signs it will predict that which sign it is.  
