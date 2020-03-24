from z3 import *

x0 = Int('x0')
y0 = Int('y0')
y1 = Int('y1')

def signed_3(y):
  # set up the solver
  s = Solver()
  current_VC = (x0 == x0)

  ##### PROGRAM START #####

  if y < 0:
    # FIXME: add sound constraints to make the test pass
    y = y * y
  else:
    # FIXME: add sound constraints to make the test pass
    y = y

  ##### PROGRAM END   #####

  # y must be nonnegative
  current_VC = And(current_VC, y1 < 0)

  # you can print your constraint in SMT-LIB format by uncommenting the following:
  print(pp(current_VC))
  s.add(current_VC)
  if s.check() == sat:
    print(s.model())
    result = "SAT: PATH IS UNSAFE"
  else:
    result = "UNSAT: PATH IS SAFE"

  return result

def expected_result():
  return ['UNSAT: PATH IS SAFE', 'UNSAT: PATH IS SAFE']


########## PRETTY PRINT FUNCTION ##########

# print Z3 constraints in Python in SMT-LIB format
def pp(f, status="unknown", name="benchmark", logic=""):
    v = (Ast * 0)()
    return Z3_benchmark_to_smtlib_string(f.ctx_ref(), name, logic, status, "", 0, v, f.as_ast())
