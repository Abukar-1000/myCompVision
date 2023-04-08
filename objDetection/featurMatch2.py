import cv2 
import numpy as np
basePath = "Computer-Vision-py/DATA/"

reeces = cv2.imread(basePath + 'reeses_puffs.png', 0)
cereal = cv2.imread(basePath + 'many_cereals.jpg', 0)

"""
Apply feature matching using SIFT ( Scale Invariant Feature Transform )
Does really well grabbing features off images that are of different sizes

"""

# create sift obj
SIFT = cv2.SIFT_create()
keyPoints1, descriptor1 = SIFT.detectAndCompute(reeces, None)
keyPoints2, descriptor2 = SIFT.detectAndCompute(cereal, None)

# calculate matches
bruteForce = cv2.BFMatcher()
# find k best matches from 2 descriptor sets => returns top 2 match results 
matches = bruteForce.knnMatch(descriptor1, descriptor2, k = 2)

"""
1) SIFT MATCHER 
the matches are in the form 
    [ matchObj1, matchObj2 ]
    [ matchObj3, matchObj4 ]
    [ matchObj5, matchObj6 ]
    ...

once we have the k matches, we apply a ratio test on each pair of matches to 
see how far apart they are. 

Matches that are closer to each other are better
""" 

# ratio test, i'm using a 75% distance metric
goodMatches = []

for match1, match2 in matches:

    if match1.distance < 0.75 * match2.distance:
        goodMatches.append([match1])

# draw SIFT matches from ratio test
siftMatches = cv2.drawMatchesKnn(reeces, keyPoints1, cereal, keyPoints2, goodMatches, None, flags= 2)

cv2.imshow("Sift matches", siftMatches)

"""
2) FLANN ( Fast Library For Approcimate Nearest Neighbors ) BASED MATCHER

Much faster than the brute force approach but not as accurate
you can play with the perameters, but this reduces the speed of the search


""" 

SIFT = cv2.SIFT_create()
keyPoints1, descriptor1 = SIFT.detectAndCompute(reeces, None)
keyPoints2, descriptor2 = SIFT.detectAndCompute(cereal, None)

FLANN_INDEX_KDTREE = 0

indexParams = {
    "algorithm": FLANN_INDEX_KDTREE,
    "trees": 5
}

searchParams = {
    "checks": 50
}

FLANN = cv2.FlannBasedMatcher(indexParams, searchParams)
matches = FLANN.knnMatch(descriptor1, descriptor2, k = 2)

# apply ratio test
goodMatches = []

# train idx points are the corrisponding points in the second image
# upper left and bottom right points for drawing a rectangle on second image

upperLeft = (0xFFFFFFFF, 0xFFFFFFFF)
bottomRight = (-0xFFFFFFFF, -0xFFFFFFFF)

# print(upperLeft, bottomRight)1

meanPoint = None
meanX, meanY = 0, 0
THRESHHOLD = 0.45
for match1, match2 in matches:
    
    if match1.distance < THRESHHOLD * match2.distance:
        goodMatches.append([match1])
        meanX += keyPoints2[match1.trainIdx].pt[0]
        meanY += keyPoints2[match1.trainIdx].pt[1]
try:
    meanX, meanY = int(meanX / len(goodMatches)), int(meanY / len(goodMatches))
except ZeroDivisionError:
    print("No matches found")


flannMatches = cv2.drawMatchesKnn(reeces, keyPoints1, cereal, keyPoints2, goodMatches, None, flags= 2)
reference = cereal.copy()

cv2.circle(
    reference,
    (meanX, meanY),
    40,
    (255,0,255),
    2
)

cv2.imshow("Flann matches", flannMatches)
cv2.imshow("Refference matches", reference)
cv2.destroyAllWindows() if ( cv2.waitKey(0) & 0xFF == 0x1B ) else None

