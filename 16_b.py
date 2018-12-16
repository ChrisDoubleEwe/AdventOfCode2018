import re
import sys
from copy import copy, deepcopy

before = []
after = []
instr = []

all_op_codes = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr' ]

with open("16_a_input.txt") as f:
  line_type = 0
  for line in f:
    line = line.strip()

    if line_type == 0:
      item = []
      x = line.split('[')[1]
      y = x.split(']')[0]
      z = y.split(', ')
      z = map(int, z)
      before.append(z)
    if line_type == 1:
      item = []
      z = line.split(' ')
      z = map(int, z)
      instr.append(z)
    if line_type == 2:
      item = []
      x = line.split('[')[1]
      y = x.split(']')[0]
      z = y.split(', ')
      z = map(int, z)
      after.append(z)
    if line_type == 3:
      dummy = 1
    line_type += 1
    if line_type > 3:
      line_type = 0

def addr(op1, op2, op3, input):
  result = list(input)
  result[op3] = result[op1] + result[op2]
  return result

def addi(op1, op2, op3, input):
  result = list(input)
  result[op3] = result[op1] + op2
  return result

def mulr(op1, op2, op3, input):
  result = list(input)
  result[op3] = result[op1] * result[op2]
  return result

def muli(op1, op2, op3, input):
  result = list(input)
  result[op3] = result[op1] * op2
  return result

def banr(op1, op2, op3, input):
  result = list(input)
  result[op3] = result[op1] & result[op2]
  return result

def bani(op1, op2, op3, input):
  result = list(input)
  result[op3] = result[op1] & op2
  return result

def borr(op1, op2, op3, input):
  result = list(input)
  result[op3] = result[op1] | result[op2]
  return result

def bori(op1, op2, op3, input):
  result = list(input)
  result[op3] = result[op1] | op2
  return result

def setr(op1, op2, op3, input):
  result = list(input)
  result[op3] = result[op1]
  return result

def seti(op1, op2, op3, input):
  result = list(input)
  result[op3] = op1
  return result

def gtir(op1, op2, op3, input):
  result = list(input)
  if op1 > result[op2]:
    result[op3] = 1
  else:
    result[op3] = 0
  return result

def gtri(op1, op2, op3, input):
  result = list(input)
  if result[op1] > op2:
    result[op3] = 1
  else:
    result[op3] = 0
  return result

def gtrr(op1, op2, op3, input):
  result = list(input)
  if result[op1] > result[op2]:
    result[op3] = 1
  else:
    result[op3] = 0
  return result

def eqir(op1, op2, op3, input):
  result = list(input)
  if op1 == result[op2]:
    result[op3] = 1
  else:
    result[op3] = 0
  return result

def eqri(op1, op2, op3, input):
  result = list(input)
  if result[op1] == op2:
    result[op3] = 1
  else:
    result[op3] = 0
  return result

def eqrr(op1, op2, op3, input):
  result = list(input)
  if result[op1] == result[op2]:
    result[op3] = 1
  else:
    result[op3] = 0
  return result


def do_instruction(opcode, op1, op2, op3, input):
  output = []
  if opcode == 0:
    output = addr(op1, op2, op3, input)
  if opcode == 1:
    output = addi(op1, op2, op3, input)
  if opcode == 2:
    output = mulr(op1, op2, op3, input)
  if opcode == 3:
    output = muli(op1, op2, op3, input)
  if opcode == 4:
    output = banr(op1, op2, op3, input)
  if opcode == 5:
    output = bani(op1, op2, op3, input)
  if opcode == 6:
    output = borr(op1, op2, op3, input)
  if opcode == 7:
    output = bori(op1, op2, op3, input)
  if opcode == 8:
    output = setr(op1, op2, op3, input)
  if opcode == 9:
    output = seti(op1, op2, op3, input)
  if opcode == 10:
    output = gtir(op1, op2, op3, input)
  if opcode == 11:
    output = gtri(op1, op2, op3, input)
  if opcode == 12:
    output = gtrr(op1, op2, op3, input)
  if opcode == 13:
    output = eqir(op1, op2, op3, input)
  if opcode == 14:
    output = eqri(op1, op2, op3, input)
  if opcode == 15:
    output = eqrr(op1, op2, op3, input)
  return output

    
def check_equal(l1, l2):
  equal = 1
  for i in range(0, len(l1)):
    if l1[i] != l2[i]:
      equal = 0
  if equal == 1:
    return True
  return False
    
    
def options_for_opcode(pre, instr, post):
  potential = 0
  op = instr[0]
  op1 = instr[1]
  op2 = instr[2]
  op3 = instr[3]

  for i in unknown_opcodes:
    if check_equal(do_instruction(i, op1, op2, op3, pre), post):
      potential += 1

  return potential

def get_single_opcode(pre, instr, post):
  potential = 0
  opcode = -1
  op = instr[0]
  op1 = instr[1]
  op2 = instr[2]
  op3 = instr[3]

  for i in unknown_opcodes:
    if check_equal(do_instruction(i, op1, op2, op3, pre), post):
      potential += 1
      opcode = i

  return opcode

# Store pairs of INPUT OPCODE / ACTUAL OPCODE
decoder = []
unknown_opcodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
unknown_input_opcodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Get all opcodes from test input
seen = []
for i in instr:
  if i[0] not in seen:
    seen.append(i[0])
seen = sorted(set(seen))
  
prev_len = 20
while len(unknown_opcodes) > 0:
  if len(unknown_opcodes) == prev_len:
    print "Stalled"
    exit() 
  prev_len = len(unknown_opcodes)
  for i in range(0, len(before)):
    if instr[i][0] in unknown_input_opcodes:
      num_opts = options_for_opcode(before[i], instr[i], after[i])
      if num_opts == 1:
        opcode = get_single_opcode(before[i], instr[i], after[i])
        pair = []
        pair.append(instr[i][0])
        pair.append(opcode)
        decoder.append(pair)
        unknown_opcodes.remove(opcode)
        unknown_input_opcodes.remove(instr[i][0])
        break

with open("16_b_input.txt") as f:
    prog = f.readlines()


regs = [0, 0, 0, 0]

for line in prog:

  inst = line.split(' ')
  in_op = int(inst[0])
  op1 = int(inst[1])
  op2 = int(inst[2])
  op3 = int(inst[3])

  real_op = -1
  for pair in decoder:
    if pair[0] == in_op:
      real_op = pair[1]

  if real_op == 0:
    regs = addr(op1, op2, op3, regs)
  if real_op == 1:
    regs = addi(op1, op2, op3, regs)
  if real_op == 2:
    regs = mulr(op1, op2, op3, regs)
  if real_op == 3:
    regs = muli(op1, op2, op3, regs)
  if real_op == 4:
    regs = banr(op1, op2, op3, regs)
  if real_op == 5:
    regs = bani(op1, op2, op3, regs)
  if real_op == 6:
    regs = borr(op1, op2, op3, regs)
  if real_op == 7:
    regs = bori(op1, op2, op3, regs)
  if real_op == 8:
    regs = setr(op1, op2, op3, regs)
  if real_op == 9:
    regs = seti(op1, op2, op3, regs)
  if real_op == 10:
    regs = gtir(op1, op2, op3, regs)
  if real_op == 11:
    regs = gtri(op1, op2, op3, regs)
  if real_op == 12:
    regs = gtrr(op1, op2, op3, regs)
  if real_op == 13:
    regs = eqir(op1, op2, op3, regs)
  if real_op == 14:
    regs = eqri(op1, op2, op3, regs)
  if real_op == 15:
    regs = eqrr(op1, op2, op3, regs)

print regs[0]
