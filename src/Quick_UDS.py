# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:32:46 2026

@author: stanh
"""
"Assumptions made for the problem "
"-uniform mesh  hx=hy=h "
"-Diffusion coefficient k cst "
"- V vector is diagonal to the cartesian plane :u=v "
"Density of the fluid rho is cst"
"Note that this code uses vertex centered FVM because we already know the boundary temperatures as they were given as Dirichlet boundary conditions"
"This python code uses first order upwind differencing scheme (UDS1) and Quick scheme  for the FVM "
import numpy as np 
import matplotlib.pyplot as plt

#parameters
L=1
k=5.0 #thermal conductivity
rho=1.25 #density of fluid
#velocity compo.
u=100.0
v=100.0

#Number of nodes in x = Number of nodes in y = N 
N=21 
#grid spacing 
h=L/(N-1)
D=k/h
Fx=rho*u
Fy=rho*v

#Grid peclet number , dont calculate for D = 0 
Pe_x = Fx/D
Pe_y = Fy/D
print(f"Pe in x = {Pe_x} , Pe in y= {Pe_y}")

#iteration Number 
iteration =0 
#initialize temperature 
T=np.zeros((N,N))
T[1:,0]=4
T[0,1:]=1
T[0,0]=1.5
#initialise iterated temperature 
T_new=T.copy()
#error variables:
epsilon = 1.E-8
numerical_error=1
#Iterative process , error verfication 
while numerical_error > epsilon :
    for i in range(1,N-1):
        for j in range(1,N-1):
            if (i == 1 or i == N-2) or (j == 1 or j == N-2): # NN boundary nodes calculation treatment: UDS1
               a_E2= 1
               a_W2= 1+Pe_x
               a_N2= 1
               a_S2= 1 +Pe_y
               a_P2= a_E2 + a_W2 + a_N2 + a_S2 
               T_new[i,j]=(a_E2*T[i,j+1] +a_W2*T[i,j-1] + a_N2*T[i-1,j] + a_S2*T[i+1,j])/a_P2
            else: # Interior nodes calculation treatment : QUICK 
               a_E1= 1 - (3/8)*Pe_x
               a_W1= 1+(7/8)*Pe_x
               a_N1= 1-(3/8)*Pe_y
               a_S1= 1 +(7/8)*Pe_y
               a_WW1= (-1/8)*Pe_x
               a_SS1= (-1/8)*Pe_y
               a_P1= a_E1 + a_W1 + a_N1 + a_S1 + a_WW1 + a_SS1 
               T_new[i,j]=(a_E1*T[i,j+1] +a_W1*T[i,j-1]+ a_N1*T[i-1,j] + a_S1*T[i+1,j] + a_WW1*T[i,j-2] + a_SS1*T[i+2,j])/a_P1
    #resetting the numerical error and recalculate
    numerical_error=0
    for i in range(1,N-1):
        for j in range(1,N-1):
            numerical_error=numerical_error+abs(T[i,j]-T_new[i,j])  
    iteration =iteration + 1
    T=T_new.copy()             
print(f'Temperature distribution obtained after {iteration} iterations  ')     
# --- Grid Generation ---
x_dom = np.arange(N)*h
y_dom = L - np.arange(N)*h #very important otherwise domain will be inverted
[X, Y]= np.meshgrid(x_dom, y_dom)
# --- Plot temperature field ---       
plt.figure(figsize=(8, 4))

contour = plt.contourf(X, Y, T, levels=100)
plt.colorbar(orientation= 'vertical' , label="Temperature")


#diagonal line to check for false diffusion
diag = np.linspace(0, L, 1000)
plt.plot(
    diag, diag,
    color='black',
    linewidth=1.0,
    linestyle='-',
    zorder=100
)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Temperature distribution 2D")
plt.show()                     