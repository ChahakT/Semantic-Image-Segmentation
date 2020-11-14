import numpy as np
import co_occurrence as co
from PIL import Image

imageLocation = '/home/chahak/ADEChallengeData2016/images/training/ADE_train_'
annotationLocation = '/home/chahak/ADEChallengeData2016/annotations/training/ADE_train_'

def AngularMoment(matrice) :
	return np.sum(np.square(matrice))
def InverseMoment(matrice) :
	x,y = matrice.shape
	sumi = 0
	for i in range(x) :
		for j in range(y) :
			sumi += float(matrice[i][j])/(1+(i-j)*(i-j))
	return sumi	
def Variance(matrice) :
	x,y = matrice.shape
	mu = np.mean(matrice)
	sumi = 0
	for i in range(x) :
		for j in range(y) :
			sumi += float((i-mu)*(i-mu))*matrice[i][j]
	return sumi
def Correlation(matrice) :
	px = []
	py = []
	x,y = matrice.shape
	for i in range(x) :
		px.append(np.sum(matrice[i,:]))
		py.append(np.sum(matrice[:,i]))
	sigmax = np.std(px)
	sigmay = np.std(py)
	mux = np.mean(px)
	muy = np.mean(py)
	sumi = 0
	for i in range(x) :
		for j in range(y) :
			sumi += (i*j)*matrice[i][j]
	sumi = float(sumi - mux*muy)/(sigmax*sigmay)
	return sumi

def Entropy(matrice) :
	x,y = matrice.shape
	sumi = 0
	for i in range(x) :
		for j in range(y) :
			if matrice[i][j] == 0 :
				sumi += 0
			else :
				sumi += matrice[i][j]*np.log(matrice[i][j])	
	return (-sumi/np.log(2))

#classCount = np.zeros([151])
#classVector = np.zeros([151,20])
classCount = np.genfromtxt('classCount_ch.txt')
classVector = np.genfromtxt('classVectors_ch.txt')
for index in range(9020,10000) :

	filename = str('00000000'+ str(index+1))
	filename = filename[len(filename)-8:]
	img = Image.open(imageLocation+filename+'.jpg').convert('L')

	annotation = Image.open(annotationLocation+filename+'.png') 
	img = img.resize((192,192))
	
	annotation = np.array(annotation.resize( (192,192) ) )
	img = np.array(img)
	x,y = img.shape
	img1 = np.zeros([x+7,y+7])
	img1[3:3+x,3:3+y] = img
	
	if index %10 == 0 :
		print('%d steps reached'%index)

	for i in range(x) :
		for j in range(y) :
			classCount[annotation[i][j]] +=1	
			vec = []
			matrices = co.get_matrices(img1[i:i+7,j:j+7])
			for k in range(4) :
				vec.append(AngularMoment(matrices[k]))
			for k in range(4) :
				vec.append(InverseMoment(matrices[k]))
			for k in range(4) :
				vec.append(Variance(matrices[k]))
			for k in range(4) :
				vec.append(Correlation(matrices[k]))
			for k in range(4) :
				vec.append(Entropy(matrices[k]))
			classVector[annotation[i][j],:] = classVector[annotation[i][j],:] + vec 					
			

	del img,img1,annotation,matrices		

np.savetxt('classVectors_ch.txt',classVector)
np.savetxt('classCount_ch.txt',classCount)	
