import math

# 각 단원 내에서 함수는 가나다순으로 정렬되어 있습니다.

#------------------------------
# 9.2.1. 정수론 및 숫자 표현 함수
#------------------------------

def 무한한가(x):
    return math.isinf(x)

def 바닥값(x):
    return math.floor(x)

def 숫자가아닌가(x):
    return math.isnan(x)

def 유한한가(x):
    return math.isfinite(x)

def 절대값(x):
    return math.fabs(x)

def 천장값(x):
    return math.ceil(x)

def 최대공약수(a, b):
    return math.gcd(a, b)

def 팩토리얼(x):
    return math.factorial(x)



'''
#math.copysign(x, y)
#Return a float with the magnitude (absolute value) of x but the sign of y. On platforms that support signed zeros, copysign(1.0, -0.0) returns -1.0.

#math.fmod(x, y)
#Return fmod(x, y), as defined by the platform C library. Note that the Python expression x % y may not return the same result. The intent of the C standard is that fmod(x, y) be exactly (mathematically; to infinite precision) equal to x - n*y for some integer n such that the result has the same sign as x and magnitude less than abs(y). Python’s x % y returns a result with the sign of y instead, and may not be exactly computable for float arguments. For example, fmod(-1e-100, 1e100) is -1e-100, but the result of Python’s -1e-100 % 1e100 is 1e100-1e-100, which cannot be represented exactly as a float, and rounds to the surprising 1e100. For this reason, function fmod() is generally preferred when working with floats, while Python’s x % y is preferred when working with integers.

#math.frexp(x)
#Return the mantissa and exponent of x as the pair (m, e). m is a float and e is an integer such that x == m * 2**e exactly. If x is zero, returns (0.0, 0), otherwise 0.5 <= abs(m) < 1. This is used to “pick apart” the internal representation of a float in a portable way.

#math.fsum(iterable)
#Return an accurate floating point sum of values in the iterable. Avoids loss of precision by tracking multiple intermediate partial sums:
#>>> sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
#0.9999999999999999
#>>> fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
#1.0
#The algorithm’s accuracy depends on IEEE-754 arithmetic guarantees and the typical case where the rounding mode is half-even. On some non-Windows builds, the underlying C library uses extended precision addition and may occasionally double-round an intermediate sum causing it to be off in its least significant bit.

#math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
#Return True if the values a and b are close to each other and False otherwise.
#Whether or not two values are considered close is determined according to given absolute and relative tolerances.
#rel_tol is the relative tolerance – it is the maximum allowed difference between a and b, relative to the larger absolute value of a or b. For example, to set a tolerance of 5%, pass rel_tol=0.05. The default tolerance is 1e-09, which assures that the two values are the same within about 9 decimal digits. rel_tol must be greater than zero.
#abs_tol is the minimum absolute tolerance – useful for comparisons near zero. abs_tol must be at least zero.
#If no errors occur, the result will be: abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol).
#The IEEE 754 special values of NaN, inf, and -inf will be handled according to IEEE rules. Specifically, NaN is not considered close to any other value, including NaN. inf and -inf are only considered close to themselves.

math.ldexp(x, i)
Return x * (2**i). This is essentially the inverse of function frexp().

math.modf(x)
Return the fractional and integer parts of x. Both results carry the sign of x and are floats.

math.trunc(x)
Return the Real value x truncated to an Integral (usually an integer). Delegates to x.__trunc__().

Note that frexp() and modf() have a different call/return pattern than their C equivalents: they take a single argument and return a pair of values, rather than returning their second return value through an ‘output parameter’ (there is no such thing in Python).

For the ceil(), floor(), and modf() functions, note that all floating-point numbers of sufficiently large magnitude are exact integers. Python floats typically carry no more than 53 bits of precision (the same as the platform C double type), in which case any float x with abs(x) >= 2**52 necessarily has no fractional bits.
'''




#------------------------------
# 9.2.2. 지수, 로그 함수
#------------------------------

def 거듭제곱(x, y):
    return math.pow(x, y)

def 로그(x, base=math.exp(1)):
    return math.log(x, base)

def 로그1더하기(x):
    return math.log1p(x)

def 로그2(x):
    return math.log2(x)

def 로그10(x):
    return math.log10(x)

def 제곱근(x):
    return math.sqrt(x)

def 지수함수(x):
    return math.exp(x)

def 지수함수빼기1(x):
    return math.expm1(x)


#------------------------------
# 9.2.3. 삼각함수
#------------------------------

def 역코사인(x):
    return math.acos(x)

def 역사인(x):
    return math.asin(x)

def 역탄젠트(x):
    return math.atan(x)

def 역탄젠트2(y, x):
    return math.atan2(y, x)

def 코사인(x):
    return math.cos(x)

def 유클리드거리(x, y):
    return math.hypot(x, y)

def 사인(x):
    return math.sin(x)

def 탄젠트(x):
    return math.tan(x)


#------------------------------
# 9.2.4. 각 변환
#------------------------------

def 도(x):
    return math.degrees(x)

def 라디안(x):
    return math.radians(x)


#------------------------------
# 9.2.5. 쌍곡선함수
#------------------------------

def 역쌍곡코사인(x):
    return math.acosh(x)

def 역쌍곡사인(x):
    return math.asinh(x)

def 역쌍곡탄젠트(x):
    return math.atanh(x)

def 쌍곡코사인(x):
    return math.cosh(x)

def 쌍곡사인(x):
    return math.sinh(x)

def 쌍곡탄젠트(x):
    return math.tanh(x)


#------------------------------
# 9.2.6. 특수 함수
#------------------------------

def 오차함수(x):
    return math.erf(x)

def 여오차함수(x):
    return math.erfc(x)

def 감마함수(x):
    return math.gamma(x)

def 로그감마함수(x):
    return math.lgamma(x)


#------------------------------
# 9.2.7. 상수
#------------------------------

원주율 = math.pi

자연상수 = math.e

타우 = math.tau

무한대 = math.inf

숫자아님 = math.nan

