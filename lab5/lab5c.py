import lab5b
import lab5a
import cvlib
import cv2 
import random
import numpy

def test_pixel_constraint():
    """Tests pixel constraint by asserting list of 1's and 0's  """
    test_data = [(255,255,0),(255,255,0),(0,0,255)]
    condition = lab5b.pixel_constraint(200,255,200,255,0,200)
    condition_pixels = [condition(pixel) for pixel in test_data]
    
    assert condition_pixels == [1,1,0]
    print("passed test")

def test_generator_from_image():
    test_data = [(255,255,0),(255,255,0),(0,0,255)]
    generator = lab5b.generator_from_image(test_data)
    assert generator(0) == (255,255,0) and generator(1) == (255,255,0) and generator(2) == (0,0,255)
    print("passed test")


def test_combine_images():
    cond_1 = lambda x:  0.5
    cond_2 = lambda x:  1
    cond_3 = lambda x:  0

    grad = [(128,128,128),(128,128,128),(128,128)]
    gen_1_pixels = [(255,255,0),(255,255,0),(0,0,255)]
    gen_2_pixels = [(0,0,255),(255,128,0),(128,128,128)]
    gen1 = lab5b.generator_from_image(gen_1_pixels)
    gen2 = lab5b.generator_from_image(gen_2_pixels)

    first_image= lab5b.combine_images_2(grad, cond_1, gen1,gen2) 
    second_image= lab5b.combine_images_2(grad, cond_2, gen1,gen2)
    third_image= lab5b.combine_images_2(grad, cond_3, gen1,gen2)
        
    print(first_image)
    print(second_image)
    print(third_image)

test_pixel_constraint()
test_generator_from_image()
test_combine_images()
