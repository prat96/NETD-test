# NETD-test
Python implementation of NETD test script for uncooled microbolometers.

Tools required:
- Numpy
- Inquirer
  >  pip install inquirer

This script allows for evaluating the NETD performance of any LWIR microbolometer.


Capture the following 3 datasets - 60 frames of images from the unit - pointing at a blackbody.

1) blackbody @20C
2) blackbody @25C
3) blackbody @30C

Convert these files to pgm using the swap.c file and place them in the 'datasets' folder, in each respective temperature folder.

Make sure no other files exist in the path.
NETD result is displayed in mK(miliKelvin)
