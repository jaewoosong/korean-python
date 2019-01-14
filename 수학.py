# -*- coding: UTF-8 -*-

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

def 천장(x):
    u"""천장 함수"""
    if isinstance(x, int):
        return x
    else:
        결과 = int(x) # int()는 0에 가까워지는 쪽으로 소수점 버림
        return 결과 if 결과 <= 0 else 결과 + 1

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

