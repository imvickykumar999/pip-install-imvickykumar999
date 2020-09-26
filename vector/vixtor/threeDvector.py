
import numpy as np, math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def mod(vector=[2,1,2]):
	return np.sqrt(sum(pow(element, 2) for element in vector))


def showplane(n=[1, 1, 2]):

	point  = np.array([1, 2, 3])
	normal = np.array(n)

	d = -point.dot(normal)
	xx, yy = np.meshgrid(range(10), range(10))
	z = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2]

	plt3d = plt.figure().gca(projection='3d')
	plt3d.plot_surface(xx, yy, z)
	plt.show()


def showline(a=[-1,0,2], b=[4,4,4], u=1):

    a = np.array(a)
    b = np.array(b)
    r = a + u*b # different value of 'u' give different 'r' points on line
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(xs=[a[0], r[0]], ys=[a[1], r[1]], zs=[a[2], r[2]])
    plt.show()
    # Axes3D.plot()

# showline(a=[-1,0,2], b=[4,4,4], u=10)


def line(a=[1,2,-4], b=[2,3,6], two_points = False, sno=''):

	r = np.array([a, b])
	a = np.array(r[0])
	b = np.array(r[1])

	if two_points == True:
		b = b-a

	print('''
>>> Line{}...

	Vector Form :
		r = [ ({})i + ({})j + ({})k ] + u*[ ({})i + ({})j + ({})k ]

	Cartesian form :

		[x- ({})] / ({}) = [y- ({})] / ({}) = [z- ({})] / ({})
	'''.format(sno, a[0], a[1], a[2], b[0], b[1], b[2], a[0], a[1], a[2],
	b[0], b[1], b[2]))
	
	showline(a, b, u=10)

	return a, b

# line(a=[-1,0,2], b=[3,4,6], two_points = True)
# line(a=[2,1,-1], b=[3,-5,2], two_points = False)
# print(line(a=[1,1,0], b=[2,-1,1]))


# ...couldn't solve question 20, pg- 486 in class 11 NCERT book !!!

def plane(a=[2,5,-3], n=[-2,-3,5], p=[5,3,-3], dis=34, nd = False, three_points = False, sno=''):

	r = np.array([a, n])
	a = np.array(r[0])
	n = np.array(r[1])
	p = np.array(p)

	if three_points == True:
		n = np.cross(n-a, p-a)

	d = n[0]*a[0] + n[1]*a[1] + n[2]*a[2]

	if nd == True:
		d = dis

	if d<0:
		n, d = -n, -d

	print('''
>>> Plane...

	Vector Form :
		[ r - ( ({})i + ({})j + ({})k ) ].[ ({}) i+ ({}) j+ ({})k ] = 0

		r.[ ({}) i+ ({}) j+ ({})k ] = {}

	Cartesian form :
		({})(x- ({})) + ({})(y- ({})) + ({})(z- ({})) = 0

		({})x + ({})y + ({})z = {}

	Intercept form :
		   x/({:.3f}) + y/({:.3f}) + z/({:.3f}) = 1
	'''.format(
	a[0], a[1], a[2], n[0], n[1], n[2], n[0], n[1], n[2], d,
	n[0], a[0], n[1], a[1], n[2], a[2], n[0], n[1], n[2], d,
	d/n[0], d/n[1], d/n[2]))

	showplane(n=n)
	
	return a, n, d

# print(plane(a=[1,1,1], n=[1,2,0], p = [-1,2,1], three_points = True))
# plane(a=[5,2,-4], n=[2,3,-1])
# print(plane(n=[2,3,4], dis = -5, nd = True))
# plane(three_points = True)


def comp_hcf(x=15, y=80):

	x, y = int(x), int(y)
	if x > y:
		s = y
	else:
	    s = x

	for i in range(1, s+1):
	    if((x % i == 0) and (y % i == 0)):
	        hcf = i

	print(hcf)
	return hcf

# comp_hcf(40,12)


# def cos(b1, b2):
# 	return abs(np.dot(b1, b2)/(mod(b1)*mod(b2)))


def distbw2line(a1=[1,2,-4], b1=[2,3,6], a2=[3,3,-5], b2=[2,3,6]):

	a1, b1 = line(a1, b1, sno=1)
	a2, b2 = line(a2, b2, sno=2)

	r2 = np.array([a2, b2])
	a2 = np.array(r2[0])
	b2 = np.array(r2[1])

	c = np.cross(b1, b2)

	if (b1 == b2).all():
		c = b1
		e = mod(np.cross(c, a2-a1))
		print("\n>>> Lines are Parallel...")
	else:
		e = np.dot(c, a2-a1)
		print("\n>>> Lines are [ NOT ] Parallel...")

	e = abs(e)
	c = mod(c)

	print('''
	Distance between Lines...

	r = ({})i+({})j+({})k + l(({})i+({})j+({})k) and
	r = ({})i+({})j+({})k + u(({})i+({})j+({})k) is...
	'''.format(a1[0], a1[1], a1[2], b1[0], b1[1], b1[2], a2[0], a2[1], a2[2], b2[0], b2[1], b2[2]))
	
	print('''
	distance = sqrt( {} ) / sqrt( {} )
	= {}/{}
	= {} units.'''.format(e*e,c*c,e,c,e/c))

	return e/c

# distbw2line(a1=[1,2,-4], b1=[2,3,6], a2=[3,3,-5], b2=[2,3,6])
# distbw2line([1,1,0],[2,-1,1],[2,1,-1],[3,-5,2])


def coplanof2line(a1=[-3, 1,5], b1=[-3,1,5], a2=[-1,2,5], b2=[-1,2,5]):

	a1, b1 = line(a1, b1, sno=1)
	a2, b2 = line(a2, b2, sno=2)

	print('''
>>> Lines...

	r = ({})i+({})j+({})k + l(({})i+({})j+({})k) and
	r = ({})i+({})j+({})k + u(({})i+({})j+({})k) is...
	'''.format(a1[0], a1[1], a1[2], b1[0], b1[1], b1[2], a2[0], a2[1], a2[2], b2[0], b2[1], b2[2]))
	

	if np.dot((a2-a1), np.cross(b1, b2)) == 0:
		print('\t...Coplanar.')
		return True
	else:
		print('\t...[ NOT ] Coplanar.')
		return False

# coplanof2line(a1=[-3, 1,5], b1=[-3,1,5], a2=[-1,2,5], b2=[-1,2,5])


def angbw2plane(n1=[2,1,-2], d1=5, n2=[2,1,-2], d2=7):

	n1 = plane(n=n1, dis = d1, nd = True, sno=1)[1]
	n2 = plane(n=n2, dis = d2, nd = True, sno=2)[1]

	a = np.dot(n1, n2)
	b = mod(n1)*mod(n2)

	cos = abs(a/b)
	arc = np.arccos(cos)
	deg = arc*57.296

	if deg == 0.0:
		print("\n>>> Planes are Parallel...")
	else:
		print("\n>>> Planes are [ NOT ] Parallel...")

	print('''
	Angle between Planes...

	r.(({})i+({})j+({})k) = {} and
	r.(({})i+({})j+({})k) = {} is...
	'''.format(n1[0], n1[1], n1[2], d1, n2[0], n2[1], n2[2], d2))
	
	print('''
	angle = arccos( abs( {}/{} ))
	= arccos( sqrt( {} ) / sqrt( {} ))
	= arccos( {} )
	= {} radian
	= {} degree'''.format(a, b, a*a, b*b, cos, arc, deg))

	return deg

# angbw2plane(n1=[2,1,-2], d1=5, n2=[3,-6,-2], d2=7)
# angbw2plane([2,1,-2], 5, [2,1,-2], 7)


def distbwpointandplane(a=[2,5,-3], n=[6,-3,2], d=4):

	a = np.array(a) # point
	n = plane(n=n, dis = d, nd = True)[1]

	dot = np.dot(a, n)
	h = abs(dot-d)
	k = mod(n)
	dist = h/k

	print('''
>>> Distance between :

	Plane...
	r.(({})i+({})j+({})k) = {}

	and, Point ({},{},{}) is...
	= sqrt( {} ) / sqrt( {} )
	= {} / {}
	= {} units.'''.format(n[0], n[1], n[2], d, a[0], a[1], a[2], h*h, k*k, h, k, dist))
	
	return dist

# distbwpointandplane(a=[0,0,0], n=[2,-3,4], d=6)


def angbwlineandplane(a=[2,5,-3], b=[3,5,1], n=[6,-3,2], d=4):

	a, b = line(a, b)
	n = plane(n=n, dis = d, nd = True)[1]

	h = np.dot(b, n)
	k = mod(b)*mod(n)

	sin = abs(h/k)
	arc = np.arcsin(sin)
	deg = arc*57.296

	print('''
>>> Angle between :

	Line...
	r = ({})i+({})j+({})k + u(({})i+({})j+({})k)

	and, Plane...
	r.(({})i+({})j+({})k) = {} is...
	'''.format(a[0], a[1], a[2], b[0], b[1], b[2], n[0], n[1], n[2], d))
	
	print('''
	angle = arcsin( abs( {}/{} ))
	= arcsin( sqrt( {} ) / sqrt( {} ))
	= arcsin( {} )
	= {} radian
	= {} degree'''.format(h, k, h*h, k*k, sin, arc, deg))

	return deg

# angbwlineandplane(a=[-1,0,3], b=[2,3,6], n=[10,2,-11], d=3)
