def 천장(x):
    u"""천장 함수 구현

    2019/01/01: 버전 1.0
    """
    if isinstance(x, int):
        return x
    else:
        결과 = int(x) # int()는 0에 가까워지는 쪽으로 소수점 버림
        if 결과 > 0:
            결과 += 1
        return 결과

