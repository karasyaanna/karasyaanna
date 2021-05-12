# coding: utf-8
# Your code here!
import random
import math
import statistics
def norm(xy):
  return math.sqrt(xy[0]*xy[0]+xy[1]*xy[1])
def arg(xy):
  return (2*(xy[0]>=0)-1)*(xy[1]+100)
while True:
  print("Input n: ",)
  ns=input()
  try:
    n=int(ns)
    break
  except Exception:
      pass
pts=[]
for i in range(n):
  pts.append([random.randint(-100,100),random.randint(-100,100)])
dst=[]
pts.sort(key=arg)
last=pts.pop()
pts.insert(0,last)
for i in range(n):
  dst.append(norm(pts[i]))
print(pts)
print("Minimum distance from origin: "+str(min(dst)))
print("Maximum distance from origin: "+str(max(dst)))
print("Average distance from origin: "+str(statistics.mean(dst)))
