from collections import defaultdict


class MpNumberVariant:
    """storing the base_10 and power_representation of an integer"""

    # NOTE: We do not check the accuracy of the power_tuple
    def __init__(self, integer, power_tuple):
        self.base_10 = integer
        self.power_tuple = power_tuple
        self.two_power = power_tuple[0]
        self.three_power = power_tuple[1]
        self.five_power = power_tuple[2]
        self.seven_power = power_tuple[3]
        self.power_notation = str(self)
        self.digit_count = self.digit_count(integer)

    def __str__(self):
        return f"2^{self.two_power} * 3^{self.three_power} * 5^{self.five_power} * 7^{self.seven_power}"

    def __repr__(self):
        return str(self)

    def to_list(self):
        return [self.base_10, self.power_tuple]

    @classmethod
    def prime_factor(self, n=None, collapse=False):
        """given n, return prime factorization under 10 (2, 3, 5, 7)"""

        l = []
        primes = [2, 3, 5, 7]
        for p in primes:
            while (n % p == 0) and (n != 1):
                n /= p
                l.append(p)

        return_list = l if n == 1 else []
        if collapse:
            return self._collapse_prime_factor(return_list)
        else:
            return return_list

    @classmethod
    def _collapse_prime_factor(self, prime_factor_l):
        d = defaultdict(int)
        for prime in prime_factor_l:
            d[prime] += 1
        return [d[2], d[3], d[5], d[7]]

    @classmethod
    def digit_count(self, integer):
        """Create a condensed string that counts all digits from 2 to 9 (the digits important to MP analysis"""
        l = [0] * 10

        if type(integer) == int:
            s = str(integer)
            for c in s:
                l[int(c)] += 1
        if type(integer) == list:
            for c in integer:
                l[c] += 1

        return ",".join([str(i) for i in l[2:]])
