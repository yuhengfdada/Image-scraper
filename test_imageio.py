import imageio

buffer = imageio.imread('http://images.metmuseum.org/CRDImages/ep/original/LC-1982_60_23.jpg')
imageio.imwrite('test/test.jpg',buffer)