# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 17:13:32 2026

@author: stanh
"""

"tabulate my results"


import numpy as np
import pandas as pd

p = np.array([3.75, 1.875, 0.625, 0.125, 0.0625])
speed = np.array([300, 150, 50, 10, 5])

aE = 1 
aW = 1 + p
aS = 1 + p
aN = 1 

# Calculate the sum of coefficients for each case
aP = aE + aW + aS + aN 

# Normalize coefficients
aE  = aE  / aP
aW  = aW  / aP
aS  = aS  / aP
aN  = aN  / aP

# Create table
df1 = pd.DataFrame(
    [p, speed, aE, aW, aN, aS, aP],
    index=["Péclet number", "speed", "aE", "aW", "aN", "aS", "aP"],
    columns=[f"Case {i+1}" for i in range(len(p))]
)

print(df1.round(6).to_string())

df1.round(6).to_csv(
    "Upwind_Scheme_Coefficients.csv",
    index=True
)
