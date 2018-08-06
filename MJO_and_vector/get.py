#!/usr/bin/env python
import numpy as np
import xarray as xr
import os

ifiles = '/home/wenchang/tigress/data/chirps/daily/chirps-v2.0.????.days_p05.nc' 
ofile = 'chirps-v2.0.days_p05.28E36E_02S06N.nc'
data_name = "precip"
xname = 'longitude'
xlim = (28, 36)
yname = 'latitude'
ylim = (-2, 6)

x = xr.open_mfdataset(ifiles)[xname].values
ix = x.argsort()
L = (x>=xlim[0]) & (x<=xlim[1])
ixlim = ix[L][0], ix[L][-1]
print(f'xlim: {xlim}; ixlim: {ixlim}')

y = xr.open_mfdataset(ifiles)[yname].values
iy = y.argsort()
L = (y>=ylim[0]) & (y<=ylim[1])
iylim = iy[L][0], iy[L][-1]
print(f'ylim: {ylim}; iylim: {iylim}')

cmd = f'ncrcat -v {data_name} -d {xname},{ixlim[0]},{ixlim[1]} -d {yname},{iylim[0]},{iylim[1]} {ifiles} {ofile}'
print(cmd, '...')
s = os.system(cmd)
if s==0:
    print('[OK]:', cmd)
