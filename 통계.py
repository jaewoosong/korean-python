# -*- coding: UTF-8 -*-
from statistics import StatisticsError

def 중앙값(자료):
    u"""중앙값"""
    # TODO: 이터레이터 처리 필요
    길이 = len(자료)
    if 길이 == 0:
        raise StatisticsError
    else:
        자료.sort()
        중앙 = int(길이/2)
        if 길이 % 2 == 0:
            return (자료[중앙-1] + 자료[중앙]) / 2
        else:
            return 자료[중앙]

def 평균(자료):
    u"""산술 평균"""
    if len(자료) == 0:
        raise StatisticsError
    else:
        총합 = 0
        for ㅈ in 자료:
            총합 += ㅈ
        return 총합 / len(자료)
