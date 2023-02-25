from PIL import Image

myimaage = Image.open("bg-card-front.png")  # open the image
myimaage.show()                          # show the image

mybox = (0, 0, 400, 400)                      # define the bo
mynewimage = myimaage.crop(mybox)          # crop the image
mynewimage.show()                        # show the new image
