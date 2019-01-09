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

def 가우스분포(mu, sigma):
    return random.gauss(mu, sigma)

def 감마분포(alpha, beta):
    return random.gammavariate(alpha, beta)

def 균등분포(a, b):
    return random.uniform(a, b)

def 난수():
    return random.random()

def 로그정규분포(mu, sigma):
    return random.lognormvariate(mu, sigma)

def 베이불분포(alpha, beta):
    return random.weibullvariate(alpha, beta)

def 베타분포(alpha, beta):
    return random.betavariate(alpha, beta)

def 삼각분포(low, high, mode):
    return random.triangular(low, high, mode)

def 정규분포(mu, sigma):
    return random.normalvariate(mu, sigma)

def 지수분포(lambd):
    return random.expovariate(lambd)

def 파레토분포(alpha):
    return random.paretovariate(alpha)

def 폰미세스분포(mu, kappa):
    return random.vonmisesvariate(mu, kappa)


#-------------------
# 9.6.5. 다른 클래스
#-------------------

#class 시스템난수([seed])
#class random.SystemRandom([seed])

