# -*- coding: UTF-8 -*-

# 상수값 얻어온 곳
# https://github.com/python/cpython/blob/master/Modules/mathmodule.c

파이 = 3.141592653589793238462643383279502884197

def 바닥(x):
    u"""바닥 함수"""
    if isinstance(x, int):
        return x
    else:
        결과 = int(x)
        return 결과 if 결과 >= 0 else 결과 - 1

def 절댓값(x):
    u"""절댓값 함수"""
    return x if x >= 0 else -x

def 사인(x):
    u"""사인 함수 (멱급수 사용)"""
    x = x % (2*파이) # 계산 단순화
    def 일반항(n):
        분자 = ((-1)**n) * (x**(2*n+1))
        분모 = 팩토리얼(2*n+1)
        return 분자/분모
    n = 0
    현재항 = 일반항(n)
    총합 = 0
    오차범위 = 1.0e-6
    while(절댓값(현재항) > 오차범위):
        총합 += 현재항
        n += 1
        현재항 = 일반항(n)
    return 총합

def 천장(x):
    u"""천장 함수"""
    if isinstance(x, int):
        return x
    else:
        결과 = int(x) # int()는 0에 가까워지는 쪽으로 소수점 버림
        return 결과 if 결과 <= 0 else 결과 + 1

def 최대공약수(ㄱ, ㄴ):
    u"""최대공약수 함수: 유클리드 호제법 사용"""
    큰 = ㄱ if ㄱ >= 0 else -ㄱ
    작은 = ㄴ if ㄴ >= 0 else -ㄴ
    if 큰 < 작은:
        큰, 작은 = 작은, 큰
    if 작은 == 0:
        return 큰
    나머지 = 큰 % 작은
    return 작은 if 나머지 == 0 else 최대공약수(나머지, 작은)

def 팩토리얼(x):
    u"""팩토리얼 함수"""
    if x < 0:
        raise ValueError()
    elif x == 0:
        return 1
    else:
        결과 = 1
        while x > 1:
            결과 *= x
            x -= 1
        return 결과

