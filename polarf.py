import math
import svgwrite


def make_svg(filename, n1,n2,count=100):
    scale_factor = math.log(n2,n1)
    def pycode(x):
        return math.ceil(x*scale_factor-1)

    dim = 1024
    dwg = svgwrite.Drawing(filename, profile='full', size=('{}px'.format(dim),'{}px'.format(dim)))
    dwg.viewbox(width=1,height=1)
    dwg.add(dwg.rect(insert=(0,0), size=('100%','100%'), rx=None,ry=None, fill='rgb(0,0,0)'))

    gg = dwg.g()
    min_radius = 0.8

    circle_radius = 1e-2
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
    for x in range(1,count+1):
        alpha = 1-(x-1) / (count)
        alpha = alpha**2

        y1 = n2**x / n1**pycode(x)
        y2 = n1**(pycode(x)+1) / n2**x

        print(x*2-1,y1)
        print(x*2,y2)

        max_radius = max(max(y1,y2),max_radius)

        p1 = draw_circle(x*2-1, y1-min_radius, svgwrite.rgb(10,20,90,'%'),opacity=alpha)
        p2 = draw_circle(x*2, y2-min_radius, svgwrite.rgb(90,20,10,'%'),opacity=alpha)



        if last is not None:
            l = dwg.line(last[0],p1)
            l.stroke(svgwrite.rgb(30,255,255,'%'), width=1e-3,opacity=alpha)
            gg.add(l)

            l = dwg.line(last[1],p2)
            l.stroke(svgwrite.rgb(30,255,255,'%'), width=1e-3,opacity=alpha)
            gg.add(l)

        last = (p1,p2)

    if min_radius < 1:
        cir = dwg.circle(center=(0,0), r=1-min_radius,fill='none')
        cir.stroke(svgwrite.rgb(0,0,0),width=1e-2)
        #gg.add(cir)

    l = dwg.line((0,0), (1,0))
    l.stroke(svgwrite.rgb(0,0,0),width=1e-2)
    #gg.add(l)

    #gg.scale(dim/2,dim/2)
    gg.scale(1/2,1/2)
    gg.translate(1,1)
    gg.scale(0.8,0.8)
    r = max_radius - min_radius
    gg.scale(1/r,1/r)
    gg.scale(1,-1)

    dwg.add(gg)
    dwg.save()


def main():
    (n1,n2) = (4,5)
    make_svg('fastaro45.svg',n1,n2,count=2000//2)

main()