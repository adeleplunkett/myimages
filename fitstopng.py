##
## Run: python ../Scripts/fitstopng.py
## Then: ./cmapcommands.txt
## Then: 
import glob
import os
from astropy.io import fits
import numpy as np
from spectral_cube import SpectralCube
from astropy import units as u


run=False
move=False
calc = True

dirname = '/lustre/cv/users/aplunket/Combo/DC2020/ModbComp'
file_regexp = "*fits"

os.chdir(dirname)
filelist = glob.glob(file_regexp)

filelist=['skymodel_b.WSM.int_pb.TCLEAN.pbcor.fits',
'skymodel_b.WSM.int_pb_multi.TCLEAN.pbcor.fits',
'skymodel_b.WSM.int_auto.TCLEAN.pbcor.fits',
'skymodel_b.WSM.int_auto_multi.TCLEAN.pbcor.fits',
'skymodel_b.WSMpb.TCLEAN.pbcor.fits',
'skymodel_b.WSMpb.combined.image.pbcor.fits',
'skymodel_b.WSMpb_multi.TCLEAN.pbcor.fits',
'skymodel_b.WSMpb_multi.combined.image.pbcor.fits',
'skymodel_b.WSMauto.TCLEAN.pbcor.fits',
'skymodel_b.WSMauto.combined.image.pbcor.fits',
'skymodel_b.WSMauto_multi.TCLEAN.pbcor.fits',
'skymodel_b.WSMauto_multi.combined.image.pbcor.fits']

if run:
    f = open('cmapcommands.txt','w')
    for file in filelist:
        runstr = 'python3 /lustre/cv/users/aplunket/Combo/dc2019/scripts/fitscmap ' + file+' cmr.rainforest'
        f.write(runstr+'\n')
    f.close()

if move:
    for file in filelist:
        os.system('mv '+file+'.cmr.rainforest.png FitsToPng/.')


if calc:
    for file in filelist:
        #print(file)
        hdu = fits.open(file)
        data = hdu[0].data
        header = hdu[0].header
        hdu.close()
        min = np.nanmin(data)
        max = np.nanmax(data)
        summed_pixels = np.nansum(data)
        delta = np.abs(header['CDELT1'])
        beam_area = np.pi*header['BMAJ']*header['BMIN']/(delta**2*4.*np.log(2.)) #units of pixels
        summed_flux = summed_pixels/beam_area
        #print('sum: {0:.2f}, flux: {1:.2f}, min: {2:.2f}, max:{3:.2f}'.format(summed_pixels,summed_flux,min,max))
        print('{0}| {1:.1f}|{2:.3f}|{3:.3f}'.format(file,summed_flux,min,max))
        
## in CASA:
'''
filelist=['skymodel_b.WSM.int_pb.TCLEAN.pbcor.fits',
'skymodel_b.WSM.int_pb_multi.TCLEAN.pbcor.fits',
'skymodel_b.WSM.int_auto.TCLEAN.pbcor.fits',
'skymodel_b.WSM.int_auto_multi.TCLEAN.pbcor.fits',
'skymodel_b.WSMpb.TCLEAN.pbcor.fits',
'skymodel_b.WSMpb.combined.image.pbcor.fits',
'skymodel_b.WSMpb_multi.TCLEAN.pbcor.fits',
'skymodel_b.WSMpb_multi.combined.image.pbcor.fits',
'skymodel_b.WSMauto.TCLEAN.pbcor.fits',
'skymodel_b.WSMauto.combined.image.pbcor.fits',
'skymodel_b.WSMauto_multi.TCLEAN.pbcor.fits',
'skymodel_b.WSMauto_multi.combined.image.pbcor.fits']

for file in filelist:
   min = float(imstat(file)['min'])
   max = float(imstat(file)['max'])
   flux = float(imstat(file)['flux'])
   print('{0}| {1:.1f}|{2:.3f}|{3:.3f}'.format(file,flux,min,max))

'''

'''
FIGURES:
skymodel_b.WSM.int_pb.TCLEAN.pbcor.fits.cmr.rainforest.png
skymodel_b.WSM.int_pb_multi.TCLEAN.pbcor.fits.cmr.rainforest.png
skymodel_b.WSM.int_auto.TCLEAN.pbcor.fits.cmr.rainforest.png
skymodel_b.WSM.int_auto_multi.TCLEAN.pbcor.fits.cmr.rainforest.png

skymodel_b.WSMpb.TCLEAN.pbcor.fits.cmr.rainforest.png
skymodel_b.WSMpb.combined.image.pbcor.fits.cmr.rainforest.png
skymodel_b.WSMpb_multi.TCLEAN.pbcor.fits.cmr.rainforest.png
skymodel_b.WSMpb_multi.combined.image.pbcor.fits.cmr.rainforest.png

skymodel_b.WSMauto.TCLEAN.pbcor.fits.cmr.rainforest.png
skymodel_b.WSMauto.combined.image.pbcor.fits.cmr.rainforest.png
skymodel_b.WSMauto_multi.TCLEAN.pbcor.fits.cmr.rainforest.png
skymodel_b.WSMauto_multi.combined.image.pbcor.fits.cmr.rainforest.png
'''

