### install libffi-dev first
import math
import svgwrite
import os
import cairosvg
def make_images(n1,n2):
	for count in range(0,150):
		scale_factor = math.log(n2,n1)
		def pycode(x):
			return math.ceil(x*scale_factor-2)
		def draw_circle(theta,r,color,opacity):
			#theta *= 2*math.pi/360
			x = r * math.cos(theta)
			y = r * math.sin(theta)

			cir = dwg.circle(center=(x,y), r=circle_radius)
			cir.fill(color,opacity=opacity)
			#gg.add(cir)
			return (x,y)

		max_radius = 0

		last = None
		dim = 5000
		dwg = svgwrite.Drawing('myimg' + str(count) + '.svg', profile='full', size=('{}px'.format(dim),'{}px'.format(dim)))
		dwg.viewbox(width=4,height=4)
		dwg.add(dwg.rect(insert=(0,0), size=('100%','100%'), rx=None,ry=None, fill='rgb(0,0,0)'))
		for x in range(count,(count*2)):

			gg = dwg.g()
			min_radius = 0.8

			circle_radius = 1e-2
			alpha = 1 - (x-1) / (count)
			alpha = alpha**2

			y1 = n2**x / n1**pycode(x)
			y2 = n1**(pycode(x)+2) / n2**x

			print(x*2-1,y1)
			print(x*2,y2)

			max_radius = max(max(y1,y2),max_radius)

			p1 = draw_circle(x*2-1, y1-min_radius, svgwrite.rgb(10,20,90,'%'),opacity=alpha)
			p2 = draw_circle(x*2, y2-min_radius, svgwrite.rgb(90,20,10,'%'),opacity=alpha)



			if last is not None:
				l = dwg.line(last[0],p1)
				l.stroke(svgwrite.rgb(30,255,255,'%'), width=.001,opacity=alpha)
				gg.add(l)

				l = dwg.line(last[1],p2)
				l.stroke(svgwrite.rgb(30,255,255,'%'), width=.001,opacity=alpha)
				gg.add(l)

			last = (p1,p2)

			if min_radius < 1:
				cir = dwg.circle(center=(0,0), r=1-min_radius,fill='none')
				cir.stroke(svgwrite.rgb(0,0,0),width=0.01)
				#gg.add(cir)

			l = dwg.line((0,0), (1,0))
			l.stroke(svgwrite.rgb(0,0,0),width=0.01)
			#gg.add(l)

			#gg.scale(dim/2,dim/2)
			gg.scale(1,1)
			gg.translate(1,1)
			r = max_radius - min_radius
			dwg.add(gg)
			
		dwg.save()
		cairosvg.svg2png(url='myimg' + str(count) + '.svg', write_to= 'myimg' + str(count) + '.png')
		print(count)
def main():
	(n1,n2) = (4,5)
	make_images(n1,n2)

main()
