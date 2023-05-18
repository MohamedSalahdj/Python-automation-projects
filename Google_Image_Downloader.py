"""
create a python function:
    that takes a url of an image from google and save location , 
    then download the image in the save location

"""
import urllib.request
import os

print(os.getcwd())
def download_image():
    url = input("Enter the image address: ")
    image_name = input("Enter image name with extention such as 'im.jpg' : ")
    urllib.request.urlretrieve(url, image_name)
    
download_image()