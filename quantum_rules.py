import numpy as np
import math

#Identity matrix
I = np.array([[1,0],
              [0,1]])
rootX = np.array([[complex(0.5,0.5),complex(0.5,-0.5)],
               [complex(0.5,-0.5), complex(0.5,0.5)]])

# Hadamard gate
H = np.array([[1/np.sqrt(2),1/np.sqrt(2)],
                  [1/np.sqrt(2),-1/np.sqrt(2)]])
S= np.array([[1,0],
               [0, complex(0,math.sin(math.pi/2))]])

#X gate
X = np.array([[0,1],
               [1,0]])

#Y gate
Y = np.array([[0, -1.j],
               [1.j, 0]])

#Z gate
Z = np.array([[1,0],
               [0,-1]])

def check_identity():
    d=[I,H,X,Y,Z]
    final_identity = []

    for i in range(0,5):
       for j in range(0,5):
           for k in range(0,5):
               for l in range(0,5):
                   for m in range(0,5):
                       for n in range(0,5):
                           for o in range(0,5):
                               for p in range(0,5):
                                   if((np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(d[i],d[j]),d[k]),d[l]),d[m]),d[n]),d[o]),d[p])).round() == I).all():
                                       final_identity.append([i,j,k,l,m,n,o,p])

    for i in range(0,5):
       for j in range(0,5):
           for k in range(0,5):
               for l in range(0,5):
                   for m in range(0,5):
                       for n in range(0,5):
                           for o in range(0,5):
                               if((np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(d[i],d[j]),d[k]),d[l]),d[m]),d[n]),d[o])).round() == I).all():
                                   final_identity.append([i,j,k,l,m,n,o])

    for i in range(0,5):
       for j in range(0,5):
          for k in range(0,5):
               for l in range(0,5):
                   for m in range(0,5):
                       for n in range(0,5):
                           if((np.dot(np.dot(np.dot(np.dot(np.dot(d[i],d[j]),d[k]),d[l]),d[m]),d[n])).round() == I).all():
                               final_identity.append([i,j,k,l,m,n])

    for i in range(0,5):
         for j in range(0,5):
             for k in range(0,5):
                 for l in range(0,5):
                     for m in range(0,5):
                         if((np.dot(np.dot(np.dot(np.dot(d[i],d[j]),d[k]),d[l]),d[m])).round() == I).all():
                             final_identity.append([i,j,k,l,m])

    for i in range(0,5):
        for j in range(0,5):
            for k in range(0,5):
                for l in range(0,5):
                    if((np.dot(np.dot(np.dot(d[i],d[j]),d[k]),d[l])).round() == I).all():
                       final_identity.append([i,j,k,l])

    for i in range(0,5):
        for j in range(0,5):
            for k in range(0,5):
                if((np.dot(np.dot(d[i],d[j]),d[k])) == I).all():
                    final_identity.append([i,j,k])
    
    return final_identity

