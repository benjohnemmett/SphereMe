import cv2
import numpy as np
import random
import math


height = 256
width = 256

class Sphere():

    r = 0.0
    c = 0.0
    radius = 5
    color = (255,255,255)

    def __init__(self, nR, nC, nRadius, nColor):
        self.r = nR
        self.c = nC
        self.radius = nRadius
        self.color = nColor


class RotationalObject():

    def __init__(self):
        self.mySpheres = []

    def addSphere(self, new_sphere):
        self.mySpheres.append(new_sphere)

    def createSphere(self, r, c, radius, color):
        new_sphere = Sphere(r, c, radius, color)

        self.addSphere(new_sphere)

    def getNumSpheres(self):
        return len(self.mySpheres)

    # Create an image of this object centered at zero
    def draw(self, rSize, cSize):

        img = np.zeros((rSize, cSize, 4), dtype=np.uint8) # Color image

        for sph in self.mySpheres:

            # Center is x,y not r,c
            aColor = (sph.color[0], sph.color[1], sph.color[2], 255)

            cv2.circle(img, (sph.c, sph.r), sph.radius, aColor, -1)

        return img


'''
Calculate the sum of squared errors between two images, evalutaed for each channel and summed up to one value

'''
def compareImages(img1, img2):

    B = img1[:,:,0].astype(np.double) - img2[:,:,0].astype(np.double)
    G = img1[:,:,1].astype(np.double) - img2[:,:,1].astype(np.double)
    R = img1[:,:,2].astype(np.double) - img2[:,:,2].astype(np.double)

    sumsqrError = np.sum(B**2 + G**2 + R**2)

    return sumsqrError

'''
Randomly draw N, (x,y) value pairs with values between 0 and the specified max values

Returns as RotationalObject
'''
def smatterSpheres(img, maxRow, maxCol, N=1):

    # Create rotational object
    obj = RotationalObject()

    has_alpha = img.shape[2] == 4

    spheres_done = 0
    # For N times:
    while spheres_done < N:
        # randomly draw x & Y location within bounds
        r = random.randint(0, maxRow-1)
        c = random.randint(0, maxCol-1)

        if(has_alpha and img[r,c,3] == 0):
            continue

        # get color from img
        color = (img[r,c,0].astype(int),img[r,c,1].astype(int),img[r,c,2].astype(int))

        # Set sphere radius
        rad = 3

        # # Convert to polar coordinates
        # rho = math.atan2(y,x)
        # theta = math.sqrt(x**2 + y**2)

        # add to rotational object
        obj.createSphere(r, c, rad, color)

        spheres_done += 1

    # Return rotational object
    return obj


'''
Generate a list of sphere locations, sizes, & colors to reproduce an image similar to the input image.

'''
def genSphereImage(imgIn):
    pass

    ################################################
    # Generate hypothesis

    converged = False
    max_population = 100

    population = []

    # While not converged
    while not converged:

        if(population.count() > 0):
            pass
            # Randomly remove bottom percentile

            # Randomly Cross over top population
                # This fills in some of the missing population, but not all

            # Randomly mutate some

        # genPop = MaxPopulation - Current population
        genPop = max_population - population.count()

        # For genPop number of iterations
        for i in range(0,genPop) :
            # Smatter circles to start
            pass
            # Grab circle colors from closest pixel in input image
            # You now have circle locations & colors

            # Randomize circle sizes as well

        # Evaluated error of each hypothesis in population

    # Return the best hypothesis


def main():
    print("Testing main")

    #makeCircle()

    penguin = cv2.imread('test_images/penguin.png',cv2.IMREAD_UNCHANGED)

    penguin_small = cv2.resize(penguin,None,fx=0.1, fy=0.1, interpolation=cv2.INTER_CUBIC)
    cv2.imwrite("output/penguin_small.png",penguin_small)

    # cv2.namedWindow("penguin", cv2.WINDOW_NORMAL)
    # cv2.imshow("penguin", penguin)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    pObj = smatterSpheres(penguin_small, penguin_small.shape[0], penguin_small.shape[1], N=50)
    pImg = pObj.draw(penguin_small.shape[0], penguin_small.shape[1])


    cv2.imwrite("output/penguin_obj.png",pImg)

    print("Penguin Read")


def makeCircle():
    img = np.zeros((height, width, 3), np.uint8)
    img[:, :] = [255, 255, 255]

    img2 = img.copy()

    rad = 50
    color = (255,0,0)

    cv2.circle(img, (height/2, width/2), rad, color, -1)

    cv2.imwrite('output/Circle.jpg',img)
    #cv2.imshow('Image', img)
    #cv2.waitKey(0)


    error = compareImages(img, img2)

    print("Error ",error)


if __name__ == "__main__":
    main()