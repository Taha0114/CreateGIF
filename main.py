
import imageio.v2 as iio

image_files = ['image1.jpg', 'image2.jpg']
images = [iio.imread(image) for image in image_files]
iio.mimsave('animated.gif', images, duration=0.5)
