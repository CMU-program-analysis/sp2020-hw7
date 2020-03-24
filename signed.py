from z3 import *

x0 = Int('x0')
y0 = Int('y0')

def signed(x):
  # set up the solver
  s = Solver()
  current_VC = (x0 == x0)

  ##### PROGRAM START #####

  if (x < 0):
      current_VC = And(current_VC, x0 < 0)
      y = x
      current_VC = And(current_VC, y0 == x0)
  else:
      # FIXME: add sound constraints to make the test pass
      y = x

  ##### PROGRAM END   #####

  # y must be nonnegative
  current_VC = And(current_VC, y0 < 0)

  # you can print your constraint in SMT-LIB format by uncommenting the following:
  # print(pp(current_VC))
  s.add(current_VC)
  if s.check() == sat:
    result = "SAT: PATH IS UNSAFE"
  else:
    result = "UNSAT: PATH IS SAFE"

  return result

def expected_result():
    return ["SAT: PATH IS UNSAFE", "UNSAT: PATH IS SAFE"]


########## PRETTY PRINT FUNCTION ##########

# print Z3 constraints in Python in SMT-LIB format
def pp(f, status="unknown", name="benchmark", logic=""):
    v = (Ast * 0)()
    return Z3_benchmark_to_smtlib_string(f.ctx_ref(), name, logic, status, "", 0, v, f.as_ast())
