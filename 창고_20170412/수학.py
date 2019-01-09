import math

# 각 단원 내에서 함수는 가나다순으로 정렬되어 있습니다.

#---------------------------------
# 9.2.1. 정수론 및 숫자 표현 함수
#---------------------------------

def 가수지수결합(x, i):
    return math.ldexp(x, i)

def 가수지수분리(x):
    return math.frexp(x)

def 나머지연산(x, y):
    return math.fmod(x, y)

def 무한한가(x):
    return math.isinf(x)

def 바닥값(x):
    return math.floor(x)

def 부호만복사(x, y):
    return math.copysign(x, y)

def 비슷한지(a, b, *, rel_tol=1e-09, abs_tol=0.0):
    return math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)

def 세밀한합계(iterable):
    return math.fsum(iterable)

def 소수정수분리(x):
    return math.modf(x)

def 숫자가아닌가(x):
    return math.isnan(x)

def 유한한가(x):
    return math.isfinite(x)

def 절대값(x):
    return math.fabs(x)

def 정수부분만(x):
    return math.trunc(x)

def 천장값(x):
    return math.ceil(x)

def 최대공약수(a, b):
    return math.gcd(a, b)

def 팩토리얼(x):
    return math.factorial(x)


#------------------------
# 9.2.2. 지수, 로그 함수
#------------------------

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


#-----------------
# 9.2.3. 삼각함수
#-----------------

def 사인(x):
    return math.sin(x)

def 역코사인(x):
    return math.acos(x)

def 역사인(x):
    return math.asin(x)

def 역탄젠트(x):
    return math.atan(x)

def 역탄젠트2(y, x):
    return math.atan2(y, x)

def 유클리드거리(x, y):
    return math.hypot(x, y)

def 코사인(x):
    return math.cos(x)

def 탄젠트(x):
    return math.tan(x)


#----------------
# 9.2.4. 각 변환
#----------------

def 도(x):
    return math.degrees(x)

def 라디안(x):
    return math.radians(x)


#-------------------
# 9.2.5. 쌍곡선함수
#-------------------

def 쌍곡사인(x):
    return math.sinh(x)

def 쌍곡코사인(x):
    return math.cosh(x)

def 쌍곡탄젠트(x):
    return math.tanh(x)

def 역쌍곡사인(x):
    return math.asinh(x)

def 역쌍곡코사인(x):
    return math.acosh(x)

def 역쌍곡탄젠트(x):
    return math.atanh(x)


#------------------
# 9.2.6. 특수 함수
#------------------

def 감마함수(x):
    return math.gamma(x)

def 로그감마함수(x):
    return math.lgamma(x)

def 여오차함수(x):
    return math.erfc(x)

def 오차함수(x):
    return math.erf(x)


#-------------
# 9.2.7. 상수
#-------------

원주율 = math.pi

자연상수 = math.e

타우 = math.tau

무한대 = math.inf

숫자아님 = math.nan

