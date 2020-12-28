
def b_m_m(a,b):
    if a%b==0:
        return b
    return b_m_m(b,a%b)

number = input().split()
a = int(number[0])
b = int(number[1])
x=b_m_m(a,b)
print(x, a*b//x)

