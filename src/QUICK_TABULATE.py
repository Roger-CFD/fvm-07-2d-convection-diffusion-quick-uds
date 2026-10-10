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

aE = 1 - (3/8)*p
aW = 1 + (7/8)*p
aS = 1 + (7/8)*p
aN = 1 - (3/8)*p
aWW = (-1/8)*p
aSS = (-1/8)*p

# Calculate the sum of coefficients for each case
aP = aE + aW + aS + aN + aWW + aSS

# Normalize coefficients
aE  = aE  / aP
aW  = aW  / aP
aS  = aS  / aP
aN  = aN  / aP
aWW = aWW / aP
aSS = aSS / aP

# Create table
df1 = pd.DataFrame(
    [p, speed, aE, aW, aN, aS, aWW, aSS, aP],
    index=["Péclet number", "speed", "aE", "aW", "aN", "aS", "aWW", "aSS", "aP"],
    columns=[f"Case {i+1}" for i in range(len(p))]
)

print(df1.round(6).to_string())

df1.round(6).to_csv(
    "Quick_Scheme_Coefficients.csv",
    index=True
   
)
