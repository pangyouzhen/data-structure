from scipy import optimize

# knapsack is a linear programming, the difference of linear programming and dp ?

c = [-1, 4]
A = [[-3, 1], [1, 2]]
b = [6, 4]

x0_bonus = (None, None)
x1_bonus = (-3, None)

res = optimize.linprog(c, A_ub=A, b_ub=b, bounds=[x0_bonus, x1_bonus], method='revised simplex')

print(res)

# the scipy  is not supported integer linear programming, integer linear programing is MLP so we used cvxopt

c = [-3000, -2000, -1500]
A = [[4, 3, 1]]
b = [4]

x0_bonus = (0, 1)
x1_bonus = (0, 1)
x2_bonus = (0, 1)

res = optimize.linprog(c, A_ub=A, b_ub=b, bounds=[x0_bonus, x1_bonus, x2_bonus], method="revised simplex")
print(res)


from cvxopt import glpk