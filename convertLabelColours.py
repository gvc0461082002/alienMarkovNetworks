#!/usr/bin/env python
import sys
import amntools
import numpy as np
import matplotlib.pyplot as plt
import pomio
"""
A one-off tool for converting class label colors from mine to MSRC or vice-versa.
Could be generalised to be quite useful.
"""

# usage:
#
#    convertLabelColours.py inputFn.png outputFn.png
#

#
# Colour map, from-to
#
cmap = [\
    ( (  0,255,  0),(  0,128,  0) ), \
    ( (200,100, 20),(128,128,  0) ), \
    ( (255,  0,  0),(128,  0,  0) ), \
    ( (  0,  0,255),( 64,128,  0) ), \
    ( (100,100,100),(128, 64,128) ), \
]

infile = sys.argv[1]
outfile= sys.argv[2]

image = amntools.readImage(infile)

plt.interactive(1)
plt.figure()
pomio.showClassColours()


plt.figure()
plt.imshow(image)
plt.title('input labels')

#plt.waitforbuttonpress()

# Make the output image
newimg = image.copy()
# for each colour make the transfer
nc = 3 # number colour channels

for cpair in cmap:
    clrFrom = cpair[0]
    clrTo   = cpair[1]
    print 'Mapping ', clrFrom, ' to ', clrTo
    # find the from pixels
    msk = np.logical_and( image[:,:,0] == clrFrom[0], np.logical_and( image[:,:,1] == clrFrom[1], \
                              image[:,:,2] == clrFrom[2] ) )
    if 0:
        plt.clf()
        plt.imshow(msk)
        plt.set_cmap( 'gray' )
        plt.waitforbuttonpress()
    for c in range(nc):
        plane = newimg[:,:,c]
        plane[msk] = clrTo[c]

# write the output image
amntools.saveImage(outfile,newimg)

plt.figure()
plt.imshow(newimg)
plt.title('output labels')


plt.waitforbuttonpress()

