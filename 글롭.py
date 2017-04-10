import glob

# 각 단원 내에서 함수는 가나다순으로 정렬되어 있습니다.

def 글롭(pathname, *, recursive=False):
    return glob.glob(pathname, recursive=recursive)

def 반환자글롭(pathname, recursive=False):
    return glob.iglob(pathname, recursive=recursive)

def 제어문자(pathname):
    return glob.escape(pathname)

