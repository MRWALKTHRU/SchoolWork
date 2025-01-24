# 2-statae busy-beaver
# state A
# if you read 0 then print 1 and go right and B
# if you read 1 then print 1 and go left and B
# state B
# if you read 0 then print 1 and go left to A
# if you read 1 then go right and halt

a0 = { 'print':1, 'move':'R', 'next_state': 'b'}
a1 = {'print':1, 'move':'R', 'next_state': 'c' }

b0 = {'print':1, 'move':'R', 'next_state': 'c'}
b1 = {'current_state':'b1', 'print':1, 'move':'L', 'next_state': 'a'}

c0= {'print':1, 'move':'L', 'next_state': 'b'}
c1 = {'print':1, 'move':'L', 'next_state': 'd'}

d0 = { 'print':1, 'move':'L', 'next_state': 'b'}
d1 = { 'print':1, 'move':'L', 'next_state': 'HALT'}

current_machine = {'current_state': a0,}
tape = ["0"]
def machine_input():
    tape[]

for x in tape:
    if x == 0:
        rule = current_machine
    if x == 1:
        rule = current_machine









