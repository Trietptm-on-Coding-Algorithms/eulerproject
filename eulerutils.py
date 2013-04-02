#! /usr/bin/env python

def memo(func):
    c={}
    def f(*arg):
        if arg not in c:
            c[arg] = func(*arg)
        return c[arg]
    return f

@memo
def isprime(x):
    try:
        from SMALLPRIMES import SMALLPRIMESET
        start = 100000
        if x < start:
            return x in SMALLPRIMESET
    except ImportError:
        pass

    if x % 2 == 0 and x!=2:
        return False
    for i in xrange(3,int(x**.5)+1,2):
        if x % i == 0:
            return False
    return True
        
def genprime():
    try:
        from SMALLPRIMES import SMALLPRIMESET
        n = 100001
        primelist = sorted(SMALLPRIMESET)
    except ImportError:
        yield 2
        n = 3
        primelist = []
    
    for p in primelist:
        yield p
    while True:
        if isprime(n):
            yield n
        n+=2
    
def ispandigital(n):
    s = str(n)
    return sorted((int(i) for i in s)) == sorted(xrange(1,len(s)+1))

def ispermutation(n,m):
    return sorted(str(n)) == sorted(str(m))

def ispalindrome(n):
    s = str(n)
    ln = len(s)
    for i in xrange(ln/2):
        if s[i] != s[ln-i-1]:
            return False
    return True

@memo
def divisors(x):
    if x < 2:
        return []
    half = [n for n in xrange(2,int(x**.5)+1) if x%n == 0]
    half.extend([ x / n for n in half ])
    half.append(1)
    half.sort()
    return half

@memo
def primefactors(x,ct=False):
    res = []
    gp = genprime()
    while x!=1:
        p = gp.next()
        if x%p==0:
            cnt = 0
            while x%p == 0:
                cnt += 1
                x/=p
            if ct:
                res.append((p,cnt))
            else:
                res.append(p)
    return res

@memo
def d(n):
    return sum(divisors(n))

def gcd(a,b):
    while a%b!=0:
        a,b = b,a%b
    return b

def lcm(m,n):
    return m*n/gcd(m,n)

def seqmaker(lower,upper,func,start=0):
    n=start
    seq=[]
    while True:
        n+=1
        tmp = func(n)
        if tmp > upper:
            return seq
        if tmp > lower:
            seq.append(tmp)
    return seq

class PrimesUtils:
    def __init__(self,upper=2000000):
        sieve = [0]*(upper+1)
        sieve[0] = 0
        sieve[1] = 0
        for i in xrange(2,int(upper**.5)+1):
            if sieve[i] == 0:
                s=i+i
                while s<=upper:
                    sieve[s] = 1
                    s+=i
        self.sieve = sieve

    def isPrime(self,n):
        if n<2:
            return False
        return self.sieve[n] == 0

    def genPrime(self):
        i = 2
        while True:
            if self.sieve[i] == 0:
                yield i
            i+=1

    def primefactors(self,x,ct=False):
        res = []
        gp = self.genPrime()
        while x!=1:
            p = gp.next()
            if x%p==0:
                cnt = 0
                while x%p == 0:
                    cnt += 1
                    x/=p
                if ct:
                    res.append((p,cnt))
                else:
                    res.append(p)
                if self.isPrime(x):
                    if ct:
                        res.append((x,1))
                    else:
                        res.append(x)
                    break
        return res

if __name__ == '__main__':
    print 'Isprime: 19,',isprime(19)
    print 'divisors: 220,',divisors(220)
    print 'd(220):',d(220)
    print 'ispalindrome(7337):',ispalindrome(7337)
    print 'gcds',gcd(999,333),gcd(97,13),gcd(88,122),gcd(12,9)
    print 'ispermutation',ispermutation(87109,79180)
    pu = PrimesUtils(20000)
    limit = 10000
    gp = pu.genPrime()
    gp2 = pu.genPrime()
    p = 0
    while p < limit:
        p = gp.next()
        p2 = gp2.next()
        if p!=p2:
            print 'wrong'
            break
    for i in range(2,8888):
        if primefactors(i) != pu.primefactors(i):
            print 'p wrong'
            print i, primefactors(i,True),pu.primefactors(i,True)
            break

