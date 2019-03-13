class BigNum(object):
    def __init__(self, num):
        self.digits = []
        while num:
            d = num % 10
            self.digits.append(d)
            num /= 10
    def add(self, other):
        carry = 0
        for i in range(len(other.digits)):
            if i >= len(self.digits):
                self.digits.append(0)
                d = carry + other.digits[i]
            else:
                d = carry + self.digits[i] + other.digits[i]
            if d >= 10:
                d -= 10
                carry = 1
            else:
                carry = 0
            self.digits[i] = d
        if carry:
            self.digits.append(carry)
    def to_int(self):
        ret = 0
        for i, d in enumerate(self.digits):
            ret += d * pow(10, i)
        return ret
    def is_palindrome(self):
        r = list(reversed(self.digits))
        for i in range(len(self.digits)):
            if self.digits[i] != r[i]:
                return False
        return True
    def reverse(self):
        ret = BigNum(0)
        ret.digits = list(reversed(self.digits))
        return ret

def add_until_palindrome(n):
    chain = [n]
    n = BigNum(n)
    r = n.reverse()
    n.add(r)
    chain.append(n.to_int())
    while not n.is_palindrome():
        r = n.reverse()
        n.add(r)
        chain.append(n.to_int())
    return chain

if __name__ == '__main__':
    n = 3209
    print add_until_palindrome(n)