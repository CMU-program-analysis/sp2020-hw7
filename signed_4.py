from z3 import *

x0 = Int('x0')
y0 = Int('y0')
y1 = Int('y1')

def signed_4(x,y):
  # set up the solver
  s = Solver()
  current_VC = (x0 == x0)

  ##### PROGRAM START #####

  # FIXME: Use your constraints from signed_3.py
  if y < 0:
    y = y * y
  else:
    y = y

  if x == 4:
    # FIXME: add sound constraints to make the test pass
    i = 0
    while (i < x):
      i = i + 1
      y = y + i
      previous_y = Int('y'+str(i))
      fresh_y = Int('y'+str(i+1))
      # FIXME: add sound constraints using previous_y and fresh_y to make the test pass
  else:
    # FIXME: add sound constraints to make the test pass
    y = y

  ##### PROGRAM END   #####

  # y must be nonnegative
  current_VC = And(current_VC, Int('y4') < 0)

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
         , 'UNSAT: PATH IS SAFE'
         , 'UNSAT: PATH IS SAFE'
         ]


########## PRETTY PRINT FUNCTION ##########

# print Z3 constraints in Python in SMT-LIB format
def pp(f, status="unknown", name="benchmark", logic=""):
    v = (Ast * 0)()
    return Z3_benchmark_to_smtlib_string(f.ctx_ref(), name, logic, status, "", 0, v, f.as_ast())
