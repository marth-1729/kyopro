from collections import defaultdict
import math

class Number_Theory:
    def prime_factrization_list(n):
        """
        素因数分解
        引数   :元の自然数
        戻り値 :素因子(全部)
        ex) 12なら[2,2,3]を返す．
        """

        prime_list = Number_Theory.prime_number_list(int(n ** 0.5) + 1)
        m = 0
        ret = []
        while True:
            if n % prime_list[m] == 0:
                n //= prime_list[m]
                ret.append(prime_list[m])
            else:
                m += 1
            if m >= len(prime_list) and n != 1:
                ret.append(n)
                return ret
            elif m >= len(prime_list):
                return ret

    def prime_factrization_dict(n):
        """
        素因数分解
        引数   :元の自然数
        戻り値 :素因子(全部)
        ex) 12なら{2:2,3:1} (<-dict型)を返す．
        """

        prime_list = Number_Theory.prime_number_list(int(n ** 0.5) + 1)
        m = 0
        ret = defaultdict(int)
        while True:
            if n % prime_list[m] == 0:
                n //= prime_list[m]
                ret[prime_list[m]] += 1
            else:
                m += 1
            if m >= len(prime_list) and n != 1:
                ret[n] += 1
                return ret
            elif m >= len(prime_list):
                return ret

    def prime_number_list(n):
        """
        素数リスト
        引数   :2以上の自然数 n
        戻り値 :nまでの素数のリスト
        ex) 12なら[2,3,5,7,11]を返す．
        """
        is_prime = [True] * (n + 1)
        prime_num = []                  #返すlist

        m = 2
        while m ** 2 <= n:
            if is_prime[m]:
                max_cnt = n // m + 1
                for i in range(2, max_cnt):
                    is_prime[i * m] = False
            m += 1
        for i in range(2, n + 1):
            if is_prime[i]:
                prime_num.append(i)

        return prime_num


    def euler_function(n):
        """
        euler関数
        引数  :自然数
        戻り値: n以下の自然数で nと互いに素である値の個数．
        """
        prime_list = Number_Theory.prime_factrization_dict(n)
        ret = n
        for i in prime_list:
            ret *= 1 - (1 / i)
        return int(ret)


    """----------------調整中------------------------------------------------------"""
    def not_comprime(n, m):
        """
        m以下の自然数で，nと互いに素でない値のリストを返す．
        引数  :2以上の2つの整数
        戻り値:nと互いに素でない値のリスト
        ex) n=12,m=7なら[2,3,4,6]を返す．
        """
        prime_list = Number_Theory.prime_number_list(n)
        ret = []
        ret_set = set()
        for i in prime_list:
            if n % i != 0:
                continue
            ret.append(i)
            ret_set |= {i}
        for i in range(len(ret)):
            for j in range(len(prime_list)):
                for k in range(10 ** 10):
                    if ret[i] * (prime_list[j] ** k) > m:
                        break
                    if ret[i] * (prime_list[j] ** k) in ret_set:
                        continue
                    ret.append(ret[i] * (prime_list[j] ** k))
                    ret_set |= {ret[i] * (prime_list[j] ** k)}
        return sorted(ret)

    """----------------調整中------------------------------------------------------"""





n=int(input())
ans=Number_Theory.euler_function(n)
print(ans)
