import netCDF4 as nc;import numpy as np;import matplotlib.pyplot as plt
d=nc.Dataset('era_interim_monthly_197901_201512_upscaled_annual.nc','r')
r=d.variables['t2m'][:]
a=5;b=50;c=10;d=100;e=0;f=10
A,B=[],[]
for t in range(len(r)): 
    if ((t < e) | (t >= f)):continue
    count = 0
    val = 0
    for y in range(len(r[0])):
        lr=[]
        if ((y<a) | (y>=b)):continue
        for x in range(len(r[0][0])):
            if ((x<c) | (x>=d)):continue
            count = count + 1
            val = val + r[t][y][x]
    A.append(val/count)
for t in range(len(r)):
 if ((t < e) | (t >= f)):continue
 count = 0
 val = 0
 for y in range(len(r[0])):
    lr=[]
    if ((y<a) | (y>=b)):continue
    for x in range(len(r[0][0])):
            if ((x<c) | (x>=d)):continue
            count = count + 1
            val = val + (r[t][y][x] - A[t])**2
 B.append(val/count)
A=np.array(A)
B=np.array(B)
plt.plot(A);plt.plot(B)
plt.show()
o=nc.Dataset('out.nc','w')
o.createDimension('t',10)
v=o.createVariable('B','f4',('t',));v[:]=A
v=o.createVariable('A','f4',('t',));v[:]=B
o.close()
