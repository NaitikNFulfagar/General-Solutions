import sympy as sy
wrt=sy.Symbol('x'or 'X')
p=input("Enter P from Equation : ")
q=input("Enter Q from Equation : ")
intg=sy.simplify(sy.integrate(p, wrt))
z= sy.simplify(sy.simplify(q) * sy.exp(intg))
intg2=(sy.integrate(z, wrt))
print("General Solution is Y * ",sy.exp(intg)," = " ,intg2, " ) + A" )
