# -*- coding: UTF-8 -*-
from statistics import StatisticsError

def 평균(자료):
    u"""산술 평균"""
    if len(자료) == 0:
        raise StatisticsError
    else:
        총합 = 0
        for ㅈ in 자료:
            총합 += ㅈ
        return 총합 / len(자료)
