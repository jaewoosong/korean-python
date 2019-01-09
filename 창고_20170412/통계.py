import statistics

# 각 단원 내에서 함수는 가나다순으로 정렬되어 있습니다.

#-----------------
# 9.7.1. 평균 관련
#-----------------

def 그룹중앙값(data, interval=1):
    return statistics.median_grouped(data, interval)

def 낮은중앙값(data):
    return statistics.median_low(data)

def 높은중앙값(data):
    return statistics.median_high(data)

def 조화평균(data):
    return statistics.harmonic_mean(data)

def 중앙값(data):
    return statistics.median(data)

def 최빈값(data):
    return statistics.mode()

def 평균(data):
    return statistics.mean(data)

#-----------------------
# 9.7.2. 분산과 표준편차
#-----------------------

def 모집단분산(data, mu=None):
    return statistics.pvariance(data, mu)

def 모집단표준편차(data, mu=None):
    return statistics.pstdev(data, mu)

def 분산(data, xbar=None): # 표본에 대한 분산
    return statistics.variance(data, xbar)

def 표준편차(data, xbar=None): # 표본에 대한 표준편차
    return statistics.stdev(data, xbar)

