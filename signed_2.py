from z3 import *

x0 = Int('x0')
y0 = Int('y0')
z0 = Int('z0')

def signed_2(x,z):
  # set up the solver
  s = Solver()
  current_VC = (x0 == x0)

  ##### PROGRAM START #####

  if (x >= 0 and z < 0):
      y = 100
  elif (x > 0 and z > x):
      t = x * z
      y = t + 30
  else:
      y = x

  ##### PROGRAM END   #####

  # y must be nonnegative
  current_VC = And(current_VC, y0 < 0)

  # you can print your constraint in SMT-LIB format by uncommenting the following:
  # print(pp(current_VC))
  s.add(current_VC)
  if s.check() == sat:
    print(s.model())
    result = "SAT: PATH IS UNSAFE"
  else:
    result = "UNSAT: PATH IS SAFE"

  return result

def expected_result():
  return [ 'UNSAT: PATH IS SAFE'
         , 'UNSAT: PATH IS SAFE'
         , 'SAT: PATH IS UNSAFE'
         , 'SAT: PATH IS UNSAFE'
         , 'SAT: PATH IS UNSAFE'
         ]


########## PRETTY PRINT FUNCTION ##########

# print Z3 constraints in Python in SMT-LIB format
def pp(f, status="unknown", name="benchmark", logic=""):
    v = (Ast * 0)()
    return Z3_benchmark_to_smtlib_string(f.ctx_ref(), name, logic, status, "", 0, v, f.as_ast())
