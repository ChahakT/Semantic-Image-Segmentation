import numpy as np

def cooccurence( image, roff, coloff ): 
	cmat = np.zeros((8,8))
	r = image.shape[0]
	c = image.shape[1]
	for i,row in enumerate(image):
		if(i+roff<0):
			continue
		if(i+roff>=r):
			continue
		for j,pix in enumerate(row):
			if(j+coloff>=c):
				continue
			if(j+coloff<0):
				continue
			cmat[pix][image[i+roff][j+coloff]] = cmat[pix][image[i+roff][j+coloff]] + 1
	cmat = cmat / np.sum(cmat)
	return cmat

def quantize(image):
	image = image / 32
	return image

def get_matrices(image):
	image = quantize(image)
	retval = []
	offsets = [(0,1),(1,1),(1,0),(1,-1)]
	for pair in offsets:
		retval.append(cooccurence(image,pair[0],pair[1]))
	return retval


#im = np.random.randint(0,255,(9,9))
#x = get_matrices(im)
#print(x[0])
#print x[2]
