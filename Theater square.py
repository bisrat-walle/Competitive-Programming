n, m, a = [int(i) for i in input().split()]
#tot = 0
#for i in range(0, n, a):
#    m_copy = m
#    while m_copy >= 0:
#        tot += 1
#        m_copy -= a
print((((n+a-1)//a)*((m+a-1)//a)))
