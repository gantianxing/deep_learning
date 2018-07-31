import scipy.misc as misc
import numpy as np

pic = misc.imread("test1.jpg")
print(pic.shape)

r,g,b = np.split(pic, 3, 2)

#ru,rs,rv=np.linalg.svd(pic)
r = r.reshape([150,200])
g = g.reshape([150,200])
b = b.reshape([150,200])
print(r.shape)
print(g.shape)
print(b.shape)

ru,rs,rv = np.linalg.svd(r)
gu,gs,gv = np.linalg.svd(g)
bu,bs,bv = np.linalg.svd(b)

k=50

kr = np.dot(ru[:,0:k],np.diag(rs[0:k]))
kr = np.dot(kr,rv[0:k,:])
print("nr",kr)
kg = np.dot(gu[:,0:k],np.diag(gs[0:k])) 
kg = np.dot(kg,gv[0:k,:])
print("ng",kg)
kb = np.dot(bu[:,0:k],np.diag(bs[0:k]))
kb = np.dot(kb,bv[0:k,:])
print("nb",kb)

pk = np.stack([kr,kg,kb], 2)

misc.imsave("%d.jpg"%k,pk)

