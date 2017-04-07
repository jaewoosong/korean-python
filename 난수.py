import random

# 각 단원 내에서 함수는 가나다순으로 정렬되어 있습니다.

#----------------------
# 9.6.1. 기본 난수 함수
#----------------------

def 난수비트반환(k):
    return random.getrandbits(k)

def 상태반환():
    return random.getstate()

def 상태설정(state):
    return random.setstate(state)

def 초기화(a=None, version=2):
    return random.seed(a, version)


#----------------------
# 9.6.2. 정수 관련 함수
#----------------------

def 난수범위(start, stop=None, step=1):
    return random.randrange(start, stop, step)

def 난수정수(a, b):
    return random.randint(a, b)


#-------------------------------
# 9.6.3. 연속된 순서에 대한 함수
#-------------------------------

def 섞기(x, rand=None):
    # 인자의 random이 모듈명과 똑같아서 rand로 표기하였습니다.
    return random.shuffle(x, random=rand)

def 선택(seq):
    return random.choice(seq)

def 선택들(population, weights=None, *, cum_weights=None, k=1):
    return random.choices(population, weights, cum_weights=cum_weights, k=k)

def 표본(population, k):
    return random.sample(population, k)


#-----------------
# 9.6.4. 실수 분포
#-----------------

'''
9.6.4. Real-valued distributions
The following functions generate specific real-valued distributions. Function parameters are named after the corresponding variables in the distribution’s equation, as used in common mathematical practice; most of these equations can be found in any statistics text.

random.random()
Return the next random floating point number in the range [0.0, 1.0).

random.uniform(a, b)
Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.

The end-point value b may or may not be included in the range depending on floating-point rounding in the equation a + (b-a) * random().

random.triangular(low, high, mode)
Return a random floating point number N such that low <= N <= high and with the specified mode between those bounds. The low and high bounds default to zero and one. The mode argument defaults to the midpoint between the bounds, giving a symmetric distribution.

random.betavariate(alpha, beta)
Beta distribution. Conditions on the parameters are alpha > 0 and beta > 0. Returned values range between 0 and 1.

random.expovariate(lambd)
Exponential distribution. lambd is 1.0 divided by the desired mean. It should be nonzero. (The parameter would be called “lambda”, but that is a reserved word in Python.) Returned values range from 0 to positive infinity if lambd is positive, and from negative infinity to 0 if lambd is negative.

random.gammavariate(alpha, beta)
Gamma distribution. (Not the gamma function!) Conditions on the parameters are alpha > 0 and beta > 0.

The probability distribution function is:

          x ** (alpha - 1) * math.exp(-x / beta)
pdf(x) =  --------------------------------------
            math.gamma(alpha) * beta ** alpha
random.gauss(mu, sigma)
Gaussian distribution. mu is the mean, and sigma is the standard deviation. This is slightly faster than the normalvariate() function defined below.

random.lognormvariate(mu, sigma)
Log normal distribution. If you take the natural logarithm of this distribution, you’ll get a normal distribution with mean mu and standard deviation sigma. mu can have any value, and sigma must be greater than zero.

random.normalvariate(mu, sigma)
Normal distribution. mu is the mean, and sigma is the standard deviation.

random.vonmisesvariate(mu, kappa)
mu is the mean angle, expressed in radians between 0 and 2*pi, and kappa is the concentration parameter, which must be greater than or equal to zero. If kappa is equal to zero, this distribution reduces to a uniform random angle over the range 0 to 2*pi.

random.paretovariate(alpha)
Pareto distribution. alpha is the shape parameter.

random.weibullvariate(alpha, beta)
Weibull distribution. alpha is the scale parameter and beta is the shape parameter.

9.6.5. Alternative Generator
class random.SystemRandom([seed])
Class that uses the os.urandom() function for generating random numbers from sources provided by the operating system. Not available on all systems. Does not rely on software state, and sequences are not reproducible. Accordingly, the seed() method has no effect and is ignored. The getstate() and setstate() methods raise NotImplementedError if called.

'''
