from pylab import *

l=306115

print 'the percentage of very well :',(float(180977)/l)*100

print 'the percentage of well:',(float(61963)/l)*100

print 'the percentage of not well:',(float(43918)/l)*100

print 'the percentage of not at all:',(float(19256)/l)*100

#print 'the percentage of hurting words are :',(float(1307558)/l)*100
# make a square figure and axes

figure(1, figsize=(6,6))

ax = axes([0.1, 0.1, 0.8, 0.8])

# The slices will be ordered and plotted counter-clockwise.

labels = 'very well', 'well', 'not well', 'not at all'

fracs = [(float(180977)/l)*100,(float(61963)/l)*100,(float(43918)/l)*100,(float(19256)/l)*100]

explode=(0, 0, 0, 0)

pie(fracs, explode=explode, labels=labels,

                autopct='%1.1f%%', shadow=True, startangle=90)

                # The default startangle is 0, which would start

                # the Frogs slice on the x-axis.  With startangle=90,

                # everything is rotated counter-clockwise by 90 degrees,

                # so the plotting starts on the positive y-axis.

title('statistical data of a given text:!!!', bbox={'facecolor':'0.8', 'pad':6})
show()
f.close()




