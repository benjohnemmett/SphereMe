import unittest

import numpy as np
import cv2
from  sphereMe import *



class TestSphereMe(unittest.TestCase):

    def testCreateSphere(self):

        r = 10
        c = 12
        rad = 6
        color = (20, 199, 198)

        new_sphere = Sphere(r, c, rad, color)

        assert new_sphere.r == r
        assert new_sphere.c == c
        assert new_sphere.radius == rad
        assert new_sphere.color == color

    def testRotationalObject_01(self):

        obj = RotationalObject()

        obj.createSphere(1, 2, 3, (3, 4, 5))

        assert obj.getNumSpheres() == 1

        obj.createSphere(10,9,8,(7,6,5))

        assert obj.getNumSpheres() == 2

    def testRotationalObject_02(self):
        obj = RotationalObject()

        sph1 = Sphere(1, 2, 3, (3, 4, 5))

        obj.addSphere(sph1)

        assert obj.getNumSpheres() == 1

        sph2 = Sphere(10, 9, 8, (7, 6, 5))
        obj.addSphere(sph2)

        assert obj.getNumSpheres() == 2

    def testSmatterSpheres(self):

        NUM_SPHERES = 10

        rSize = 480
        cSize = 640

        grad = np.linspace(0, 255, rSize*cSize, dtype=np.uint8).reshape((rSize,cSize))

        bgr_img = cv2.merge((grad, np.zeros_like(grad), np.zeros_like(grad)))

        cv2.imwrite("output/bgr_grad.jpg", bgr_img)

        obj = smatterSpheres(bgr_img, rSize, cSize, N=NUM_SPHERES)

        assert obj.getNumSpheres() == NUM_SPHERES

        for sph in obj.mySpheres:
            #print sph
            assert withinRange(sph.r, 0, rSize)
            assert withinRange(sph.c, 0, cSize)

    def testDraw(self):

        NUM_SPHERES = 100

        rSize = 480
        cSize = 640

        grad = np.linspace(0, 255, rSize*cSize, dtype=np.uint8).reshape((rSize,cSize))

        bgr_img = cv2.merge((grad, np.zeros_like(grad), np.zeros_like(grad)))

        cv2.imwrite("output/bgr_grad.jpg", bgr_img)

        obj = smatterSpheres(bgr_img, rSize, cSize, N=NUM_SPHERES)

        obj_img = obj.draw(rSize,cSize)

        cv2.imwrite("output/obj_img.jpg", obj_img)


def withinRange(val,min,max):
    return (val > min) and (val < max)

if __name__ == 'main':
    unittest.main()
