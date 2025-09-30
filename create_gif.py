import imageio.v3 as iio

filenames = ['emoji1.clockit.jpg', 'emoji2.clockit.jpg']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

  iio.imwrite('clockit.gif', images, duration = 500, loop = 0)