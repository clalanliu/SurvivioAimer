import numpy as np
from PIL import ImageGrab
import math
from skimage import data, color
from skimage.transform import hough_circle, hough_circle_peaks, resize
from skimage.feature import canny
from skimage.draw import circle_perimeter
from skimage.util import img_as_ubyte


def calculateDistance(x1,y1,x2,y2):  
     return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)    

def getScreenShot():
    return np.asarray(ImageGrab.grab())


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

def getEmimiesPosition(cursor_pos, people_radii, min_radii, max_radii):
    numpyIm = getScreenShot()
    numpyIm = getPlayerPatch(numpyIm, cursor_pos, max_radii)
    numpyIm = rgb2gray(numpyIm)
    edges = canny(numpyIm, sigma=3, low_threshold=10, high_threshold=50)
    hough_radii = [people_radii + 1, people_radii, people_radii - 1]
    hough_res = hough_circle(edges, hough_radii)
    _accums, cx, cy, _ = hough_circle_peaks(hough_res, hough_radii, total_num_peaks=1, threshold=0.4)
    cx = np.clip(cursor_pos[0] - max_radii + cx, 0, 1920)
    cy = np.clip(cursor_pos[1] - max_radii + cy, 0, 1080)
    if cx.size==1 and cy.size==1 and calculateDistance(cx, cy, 960, 540) > min_radii:
        return cx, cy
    else:
        return None, None 

def getPlayerPatch(numpyIm, cursor_pos, radii):
    xmin = np.max([cursor_pos[0]-radii, 0])
    ymin = np.max([cursor_pos[1]-radii, 0])
    xmax = np.min([cursor_pos[0]+radii, 1920])
    ymax = np.min([cursor_pos[1]+radii, 1080])
    return numpyIm[ymin:ymax,xmin:xmax,:]

def evalulateRedRegion(numpyIm):
    red_mean = np.mean(np.mean(numpyIm[:,:,0]))
    if red_mean > 170:
        return 4*(red_mean - 170)
    return 0

def getPeopleRadii():
    numpyIm = getScreenShot()
    numpyIm = numpyIm[500:580,920:1000,:]
    numpyIm = rgb2gray(numpyIm)
    edges = canny(numpyIm, sigma=3, low_threshold=10, high_threshold=50)
    hough_radii = [37,36,27,26,19,18,13,12]
    hough_res = hough_circle(edges, hough_radii)
    _, _, _, rad = hough_circle_peaks(hough_res, hough_radii, total_num_peaks=1, threshold=0.4)
    if rad.size == 1:
        return rad.item()
    else:
        return None 