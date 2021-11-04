import cv2
import numpy
from cvlib import multiply_tuple, add_tuples, rgblist_to_cvimg
from lab5a import cvimg_to_list
import random

def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    """ 
    returns a function which given  a pixel determens if given pixel is within a certian hsv value
    """
    def pixel_identifier(pixel):
        try:
            """ 
            If the input is not a number, a value error has ouccured
            """
            (h,s,v) = pixel
            int(pixel[0])
            int(pixel[1])
            int(pixel[2])
        except ValueError:
            raise ValueError
        
        (h,s,v) = pixel
        try:
            if hlow <= h <= hhigh and slow <= s <= shigh and vlow <= v <= vhigh:
                return 1
            else:   
                return 0
        except TypeError:
            raise ValueError

    return pixel_identifier


def generator_from_image(img: list):
    """
    Returns a function which returns the color of a specific pixel given an index
    """
    def color_of_pixel(index: int) -> tuple:
        pixels = img
        try:
            """ 
            Checks if index is in range, otherwise pixel does not exsist
            """
            return pixels[index]
        except IndexError:
            raise IndexError
        
    return color_of_pixel

# Skapa en generator som gör en stjärnhimmel
def generator1(index):
    val = random.random() * 255 if random.random() > 0.99 else 0
    return (val, val, val)

def combine_images(img, condition, gen1, gen2):
    """ 
    combines two images given a condition
    """

    #Make list of 1 and 0, if 1 pixel is part of sky, if 0 pixel is not part of sky
    is_sky_pixels = [condition(pixel) for pixel in img]  
    out_list = list()
    
   
    for i,is_sky in enumerate(is_sky_pixels):
        if is_sky:
            out_list.append(gen1(i))
        else:
            out_list.append(gen2(i))
    
    return out_list        



def gradient_condition(color):
    return color[0]/256
    



def combine_images_2(img, condition, gen1, gen2):
    """ 
    combines two images with a condition (ex gradient) 
    """
    try:
        """ 
        Condition will raise ValueError if failure occurs, catch this and raise another one since a value error has occured
        """
        condition_list = [condition(pixel) for pixel in img]
    except ValueError:
        raise ValueError("Expected number")

    out_list = list()
    for i, value in enumerate(condition_list):
        try:
            """ 
            Checks if generator 1 and 2 has a pixel for given index. Gen1 or Gen2 will throw an indexError, catch it and throw a ValueError
            """
            gen1(i)
            gen2(i)
            first_pixel =  multiply_tuple( gen1(i), value)
            second_pixel = multiply_tuple( gen2(i), (1 - value))
            new_pixel = add_tuples(first_pixel,second_pixel)
            out_list.append(new_pixel)
        except IndexError:
            raise ValueError

    return out_list

#plane_img = cv2.imread("plane.jpg")
#flower_img = cv2.imread("flowers.jpg")
#gradient_img = cv2.imread("gradient.jpg")

#gradient_img_list = cvimg_to_list(gradient_img)
#plane_img_list = cvimg_to_list(plane_img)
#flower_img_list = cvimg_to_list(flower_img)




#generator1 = generator_from_image(plane_img_list)
#generator2 = generator_from_image(flower_img_list)

#result = combine_images_2(gradient_img_list, gradient_condition, generator1, generator2)

#new_img = rgblist_to_cvimg(result, plane_img.shape[0], plane_img.shape[1])
#cv2.imshow('Final image', new_img)
#cv2.waitKey(0)

