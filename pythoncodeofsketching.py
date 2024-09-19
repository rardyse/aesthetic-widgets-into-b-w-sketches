import cv2

image = cv2.imread("hibiscus.jpg")
#here you read the image chosen thanks to OpenCv (replace your file's name instead of "hibiscus.jpg") ;)

grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#here you are going to convert the image to grayscale (black and white) "COLOR_BGR2GRAY", but you can choose other kind of colors/mixes of colors
invert = cv2.bitwise_not(grey_image)
#here we want to make it b&w thanks to cv2 which we imported just at the beginning by...
#...inverting the grayscale image (making dark areas light and light areas dark hihihihi)
blur = cv2.GaussianBlur(invert, (21,21), 0)
#our bff Gaussian is going to help us to soften the image chosen
inverted_blur = cv2.bitwise_not(blur)
#then we blur it with the Gaussian Blur (previous line of code) by inverting it in order to have it more clear 
sketch = cv2.divide(grey_image, inverted_blur, scale=256.0)
#here you are going to create a pencil sketch effect (what I was personally looking for) by dividing the grayscale image by the inverted blurred hibiscus :)
#the "scale =256.0" parameter controls the intensity of the sketch effect!!!!! the effect in my presentation corresponds to 256.0
#because if you reduce the scale parameter in the cv2.divide(....., scale=x) function, the intensity of the sketch effect will decrease making the sketch appear darker
#for instance : scale=124.0 will make the sketch darker, as the division result is scaled down, making the contrast between light and dark areas LESSSSSSSS intense.


cv2.imwrite("hibiscus_sketch.jpg", sketch)
#WELLLLLL THIS IS THE END, WHERRREEEEEEEEEEEEEEE WHEN YOU CLICK ON "Run" THE FILE WILL BE AUTOMATICALLY DOWNLOADED as the original file's name but with "_sketch" at the end
#don't mind changing whatever you want, that's what I will probs do by replacing that sketch effect with filters / stickers added / color grading for my photos!!
#also taking this base to create a desktop app within tkinter could be a great idea
