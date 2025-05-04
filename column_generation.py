"""
Column Generation
1. Relaxation으로 초기해를 만든다.
2. 초기해를 가지고 Sub Problem을 푼다.
3. 1-목적함수 < 0 이면 그 해를 추가한다.
4. 다시 master problem을 푼다.

If no variable has a negative reduced cost, then the current solution of the master problem is optimal.
"""

"""
해결해야할 것
"master problem의 dual만 받아와도 된다" --> 해결
model 돌렸을 때 해를 리스트로 받아오는 법 --> 해결

"""
import random
import time

import gurobipy as gp
from gurobipy import GRB
import itertools

lengths = [1380, 1520, 1560, 1710, 1820, 1880, 1930, 2000, 2050, 2100, 2140, 2150, 2200]
demands = [22, 25, 12, 14, 18, 18, 20, 10, 12, 14, 16, 18, 20]
num_items = len(demands)
L = 5600

def master(A):
    global dual_var
    global opt_val
    model = gp.Model("master")
    x = model.addVars(range(len(A)), vtype=GRB.CONTINUOUS, name="x") #INTEGER -> CONTINOUS
    model.addConstrs(gp.quicksum(A[j][i]*x[j] for j in range(len(A))) >= demands[i] for i in range(num_items))
    model.setObjective(gp.quicksum(x[i] for i in range(len(A))), GRB.MINIMIZE)
    model.optimize()
    if model.status == GRB.OPTIMAL:
        dual_var = [x.Pi for x in model.getConstrs()]
        opt_val = model.ObjVal

def sub(dual_var):
    global L
    global lengths
    global sub_sol
    global sub_val
    model = gp.Model("sub")
    y = model.addVars(range(num_items), vtype=GRB.INTEGER, name="y")
    model.addConstr(gp.quicksum(lengths[i]*y[i] for i in range(num_items)) <= L)
    model.setObjective(gp.quicksum(dual_var[i]*y[i] for i in range(num_items)), GRB.MAXIMIZE)
    model.optimize()
    if model.status == GRB.OPTIMAL:
        sub_sol = [x.X for x in model.getVars()]
        sub_val = model.ObjVal

A = []
for i in range(num_items):
    arr = [0]*num_items
    arr[i] = L//lengths[i]
    A.append(arr)

while True :
    master(A)
    sub(dual_var)
    if 1 - sub_val < -0.000000001 :
        A.append(sub_sol)
        continue
    else: break

print(opt_val)
