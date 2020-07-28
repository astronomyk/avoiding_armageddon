import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii


def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

def get_actic_area():

    # all data points are 5.15km from the next
    # ergo, each data point covers 26.6km2
    data = ascii.read("thk_2018_3.map.complete.txt", format='basic', fast_reader=True)
    mask = (data["latitude"] > 60) * (data["height"] > 0) * (data["height"] < 1)
    print(sum(mask))


get_actic_area()