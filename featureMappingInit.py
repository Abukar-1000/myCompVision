import cv2 
import numpy as np
basePath = "Computer-Vision-py/DATA/"

# this is the brute force attempt to find an image in another given img
reeces = cv2.imread(basePath + 'reeses_puffs.png', 0)

cereal = cv2.imread(basePath + 'many_cereals.jpg', 0)

# cv2.imshow("puff", reeces)
# cv2.imshow("many", cereal)

# using orb detectors, create orb object and train it by passing in the img we are looking for
orb = cv2.ORB_create()
# takes in a mask but will pass none there
keyPoint1, descriptor1 =  orb.detectAndCompute(reeces, None)
keyPoint2, descriptor2 =  orb.detectAndCompute(cereal, None)

# create mating using brute force
bruteForce = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

matches = bruteForce.match(descriptor1, descriptor2)

# sort the matches using .distance of each match object instance

matches = sorted(matches, key= lambda obj: obj.distance)
# view distances, raking is the less distance it has the greater the match
print([x.distance for x in matches]) 

# showing result, grab top 10 matches
topMatches = matches[0:10]

reecesMatches = cv2.drawMatches(
    img1= reeces,
    keypoints1= keyPoint1,
    img2= cereal,
    keypoints2= keyPoint2,
    matches1to2= topMatches,
    matchesMask= None,
    flags= 2,
    outImg= None
)

cv2.imshow("matches", reecesMatches)


cv2.destroyAllWindows() if ( cv2.waitKey(0) & 0xFF == 0x1B ) else None
