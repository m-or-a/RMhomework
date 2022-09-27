bracket_op = ['(', '[', '{']
bracket_cl = [')', ']', '}']

f = True
b_op = []
s = input()
for i in range(len(s)):
    if s[i] in bracket_op:
        b_op.append(s[i])
    elif s[i] in bracket_cl:
        if len(b_op) != 0 and (b_op[-1] == '(' and s[i] == ')' or
            b_op[-1] == '[' and s[i] == ']' or
            b_op[-1] == '{' and s[i] == '}'):
            b_op.pop()
        else:
            f = False
            break

if f and len(b_op) == 0:
    print(True)
else:
    print(False)
