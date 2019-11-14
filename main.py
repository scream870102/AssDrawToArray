import random,re
divider = 1.0
counter=0
content='m 0 -22 l -15 0 l 15 0 m -15 0 l 15 0 l 0 22 '
test = 'test'
color=[]
point=[]
x = re.findall(r'(-?\d+) (-?\d+)',content)
for m,k in x:
    point.append('_points[{0}] = point4({1}f, {2}f, 0.0f, 1.0f);'.format(counter,float(m)/divider,float(k)/divider))
    color.append('_colors[{0}] = color4({1}f, {2}f, {3}f, 1.0f);'.format(counter,random.uniform(0.75,1.0),random.uniform(0.75,1.0),random.uniform(0.75,1.0)))
    counter+=1
    pass
for p in point:
    print(p)
    pass
for c in color:
    print(c)
    pass