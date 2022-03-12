# def fuc(P):
#     return (P**2*(2.4216*P**(1/3)+2.8663*P**(2/3)+2.3415*P**(3/3)))
#     # return (P**2*(2.4216*P**(1/3)+2.8663*P**(2/3)+2.3415*P**(3/3)))

# import  numpy as np
# a= np.array([-9.298797480115046e+154+4.878698398254467e+149j])
# print(fuc(a))

# a={1,2}
# b={5}
# if a&b:
#     print('yes')


# def _diff(set1,set2):
#     '''return the diffent ele of set2 with set1'''
#     res=set()
#     for i in set2:
#         tmp=0
#         for j in set1:
#             if j==i:
#                 tmp=1
#         if tmp==0:
#             res.add(i)
#     return res       
# from sympy.abc import i,j,a,b,k,l,c,d
# def findEquivalentIndices(indexSets):
#     equi=[]
#     selectedSet=set()
#     for beingSelectedSet in indexSets:
#         diffset=_diff(selectedSet,beingSelectedSet)
#         if diffset!=set():
#             equi.append(diffset)
#             selectedSet.update(diffset)
#     return equi
# print(findEquivalentIndices( [{a,b},{k,l},{a,b},{k,l},{a,b},{a,b},{a,c},{a},{a,k}]))


from sympy import IndexedBase

# from sympy import symbols
from sympy.abc import *
G=IndexedBase('G')
H=IndexedBase('H')
A=IndexedBase('A')
a=symbols('a')
b=symbols('b')
c=symbols('c')
d=symbols('d')
e=symbols('e')
f=symbols('f')
if str(q) > str(p):
    print('yes')
print({a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z})
print({a,b,c,d,e,f})
print({1,2,3,4,5,6,})

# #DO NOT import this module later than declare IndexBase varible ,
# #because it will cover IndexedBase varible.

exp=A[(1,),(2,)]*H[(3,5),(7,9)]*H[(),(5,)]
print(exp)
print(exp.args[0].args)
print(len((1,)))
print(tuple([a,b,c,d,e,f]))
print(set([a,b,c,d,e,f]))

x={a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z}
y={c,a}
print(x & y==y)

    # inputcase=-A[(a, p), (r, s)]*G[(a,), (b,)]*H[(p, q), (r, s)]*delta[(q,), (b,)] + A[(a, q), (r, s)]*G[(a,), (b,)]*H[(p, q), (r, s)]*delta[(p,), (b,)] + A[(p, q), (b, r)]*G[(a,), (b,)]*H[(p, q), (r, s)]*delta[(a,), (s,)] - A[(p, q), (b, s)]*G[(a,), (b,)]*H[(p, q), (r, s)]*delta[(a,), (r,)] + A[(p,), (r,)]*G[(a,), (b,)]*H[(p, q), (r, s)]*n[(), (a,)]*delta[(a,), (s,)]*delta[(q,), (b,)] - A[(p,), (r,)]*G[(a,), (b,)]*H[(p, q), (r, s)]*n[(), (q,)]*delta[(a,), (s,)]*delta[(q,), (b,)] - A[(p,), (s,)]*G[(a,), (b,)]*H[(p, q), (r, s)]*n[(), (a,)]*delta[(a,), (r,)]*delta[(q,), (b,)] + A[(p,), (s,)]*G[(a,), (b,)]*H[(p, q), (r, s)]*n[(), (q,)]*delta[(a,), (r,)]*delta[(q,), (b,)] - A[(q,), (r,)]*G[(a,), (b,)]*H[(p, q), (r, s)]*n[(), (a,)]*delta[(a,), (s,)]*delta[(p,), (b,)] + A[(q,), (r,)]*G[(a,), (b,)]*H[(p, q), (r, s)]*n[(), (p,)]*delta[(a,), (s,)]*delta[(p,), (b,)] + A[(q,), (s,)]*G[(a,), (b,)]*H[(p, q), (r, s)]*n[(), (a,)]*delta[(a,), (r,)]*delta[(p,), (b,)] - A[(q,), (s,)]*G[(a,), (b,)]*H[(p, q), (r, s)]*n[(), (p,)]*delta[(a,), (r,)]*delta[(p,), (b,)] - G[(a,), (b,)]*H[(p, q), (r, s)]*delta[(a,), (r,)]*lamda[(p, q), (b, s)] + G[(a,), (b,)]*H[(p, q), (r, s)]*delta[(a,), (s,)]*lamda[(p, q), (b, r)] + G[(a,), (b,)]*H[(p, q), (r, s)]*delta[(p,), (b,)]*lamda[(a, q), (r, s)] - G[(a,), (b,)]*H[(p, q), (r, s)]*delta[(q,), (b,)]*lamda[(a, p), (r, s)]


# for i in exp.args:
#     if type(i)!=type(A[{},{}]):
#         print(i)

#     # print(i.args)


# for i in [1,2]:
#     for j in [3,4]:
#         print(j)
#         break
#     print(i)