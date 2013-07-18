#!/usr/bin/env python2

stars = 100000
arms = 5
radius = 5000


import random
import math

deg2rad = math.pi / 180.0
armangle = (360.0 / arms) % 360.0
angularspread = 250.0 / arms

def hatrandom(range):
	area = 4 * math.atan(6.0)
	p = area * random.random()
	return math.tan(p / 4.0) * range / 6.0

starmap = {}
for i in xrange(stars):
	if (random.randint(0, 1) & 1): 
		extra = 1.0
	else:
		extra = -1.0

	#r = random.uniform(0.0, float(radius))
	r = hatrandom(float(radius))
	#q = random.uniform(0.0, angularspread) * extra
	q = hatrandom(angularspread) * extra
	a = (random.randint(1, arms)) * armangle
	k = 1

	x = int(r * math.cos(deg2rad * (a + r * k + q)))
	y = int(r * math.sin(deg2rad * (a + r * k + q)))

	starmap[(x,y)] = 1

print "stars:", len(starmap)

with open('map', 'w') as f:
	for (x, y) in starmap.iterkeys():
		f.write('%i %i\n' % (x, y))
	

