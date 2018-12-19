import re
import sys
from copy import copy, deepcopy

all_op_codes = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr' ]

ip_reg = -1
prog = []
regs = [1, 0, 0, 0, 0, 0]

with open("19_a_input.txt") as f:
  for line in f:
    line = line.strip()

    if line.startswith('#ip'):
      ip_reg = int(line.split(' ')[1])
    else:
      instr = line.split(' ')[0]
      op1 = int(line.split(' ')[1])
      op2 = int(line.split(' ')[2])
      op3 = int(line.split(' ')[3])
      row = []
      row.append(instr)
      row.append(op1)
      row.append(op2)
      row.append(op3)
      prog.append(row)

print prog


def addr(op1, op2, op3):
  regs[op3] = regs[op1] + regs[op2]

def addi(op1, op2, op3):
  regs[op3] = regs[op1] + op2

def mulr(op1, op2, op3):
  regs[op3] = regs[op1] * regs[op2]

def muli(op1, op2, op3):
  regs[op3] = regs[op1] * op2

def banr(op1, op2, op3):
  regs[op3] = regs[op1] & regs[op2]

def bani(op1, op2, op3):
  regs[op3] = regs[op1] & op2

def borr(op1, op2, op3):
  regs[op3] = regs[op1] | regs[op2]

def bori(op1, op2, op3):
  regs[op3] = regs[op1] | op2

def setr(op1, op2, op3):
  regs[op3] = regs[op1]

def seti(op1, op2, op3):
  regs[op3] = op1

def gtir(op1, op2, op3):
  if op1 > regs[op2]:
    regs[op3] = 1
  else:
    regs[op3] = 0

def gtri(op1, op2, op3):
  if regs[op1] > op2:
    regs[op3] = 1
  else:
    regs[op3] = 0

def gtrr(op1, op2, op3):
  if regs[op1] > regs[op2]:
    regs[op3] = 1
  else:
    regs[op3] = 0

def eqir(op1, op2, op3):
  if op1 == regs[op2]:
    regs[op3] = 1
  else:
    regs[op3] = 0

def eqri(op1, op2, op3):
  if regs[op1] == op2:
    regs[op3] = 1
  else:
    regs[op3] = 0

def eqrr(op1, op2, op3):
  if regs[op1] == regs[op2]:
    regs[op3] = 1
  else:
    regs[op3] = 0


def do_instruction(opcode, op1, op2, op3):
  output = []
  print "ip=" + str(ip) + '',
  print regs,
  print " " + opcode + " " + str(op1) + " " + str(op2) + " " + str(op3) + " ", 
  if opcode == 'addr':
    addr(op1, op2, op3)
  if opcode == 'addi':
    addi(op1, op2, op3)
  if opcode == 'mulr':
    mulr(op1, op2, op3)
  if opcode == 'muli':
    muli(op1, op2, op3)
  if opcode == 'banr':
    banr(op1, op2, op3)
  if opcode == 'bani':
    bani(op1, op2, op3)
  if opcode == 'borr':
    borr(op1, op2, op3)
  if opcode == 'bori':
    bori(op1, op2, op3)
  if opcode == 'setr':
    setr(op1, op2, op3)
  if opcode == 'seti':
    seti(op1, op2, op3)
  if opcode == 'gtir':
    gtir(op1, op2, op3)
  if opcode == 'gtri':
    gtri(op1, op2, op3)
  if opcode == 'gtrr':
    gtrr(op1, op2, op3)
  if opcode == 'eqir':
    eqir(op1, op2, op3)
  if opcode == 'eqri':
    eqri(op1, op2, op3)
  if opcode == 'eqrr':
    eqrr(op1, op2, op3)
  print regs
   
#run program
ip = regs[ip_reg]
while True:
  if ip > len(prog):
    print "IP overflow"
    exit()
  regs[ip_reg] = ip
  instruction = prog[regs[ip_reg]]
  do_instruction(instruction[0], instruction[1], instruction[2], instruction[3])
  ip = regs[ip_reg]
  ip += 1
 
