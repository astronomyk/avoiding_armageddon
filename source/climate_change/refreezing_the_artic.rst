An extra meter of ice would stop the ice disappearing.
Pumping stations need to only pump water 2-3 meters up.

Arctic Sea ice map
------------------
https://climatedataguide.ucar.edu/climate-data/sea-ice-thickness-data-sets-overview-comparison-table

17361 blocks were between 0m and 1m
Each block is 26km2
Total area to be refrozen: 461350 km2

Water pumping equation
----------------------
https://www.engineeringtoolbox.com/pumps-power-d_505.html
Ph(kW) = q ρ g h / (3.6e6)

where

Ph(kW) = hydraulic power (kW)

q = flow capacity (m3/h)

ρ = density of fluid (kg/m3)

g = acceleration of gravity (9.81 m/s2)

h = differential head (m)

1000 m3/h of salt water needs 2.8kW of energy to be pumped 1 meter upwards.
2m head height --> 5.6kW
Assume a 56% efficiency factor, this makes a round 10kW for 1000m3/hr

polar to cartesian conversion
-----------------------------
import numpy as np

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

Small wind turbine prices
-------------------------
10kW @ $64000
https://www.renewableenergyhub.us/wind-turbines/how-much-does-wind-turbines-cost.html
Large scale Vestas cost around 1 M€ per MW
https://www.windpowermonthly.com/article/1228426/unmasking-turbine-prices

Given the 10W needed for 1000m3/hr
A small scale plant has a capacity of 1000m3/hr, or an area 33x33m per hour up to a level or 1m
A Vesta 1MW plant can do 1e6 m3/hr, or an area 1x1km per hour up to a level of 1m

461350 km2 need to be re-iced

If a wind turbine is turning for 100 days per winter, and 10 hours per day,
that's 1000 hours. For a Vesta 1 MW turbine, thats 1000 km2 per winter per turbine.
Hence we need 461 Vesta turbines to run the project.

Given a sale price of ~1 M€ per 1 MW turbine, the turbine costs are at around
500 M€.

Assuming the same for installation, the project could be realised for 1 G€


