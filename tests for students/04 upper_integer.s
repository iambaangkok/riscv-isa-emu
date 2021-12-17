# load 10,000 into X1
addi   x1,x0, 0x710
lui    x1, 2

addi   x2, x0, 0

# increase X2 by 10 until it is 10,000
addi   x2, x2, 10
blt    x2, x1, -4

# after execution x1,x2 should contain
# 10,000




