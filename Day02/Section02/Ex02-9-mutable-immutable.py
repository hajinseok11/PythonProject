'''
Ex02-9-mutable-immutable.py
mutable - 메모리 값을 변경 가능 객체
    리스트(list), 세트(set), 딕셔너리(dict)
'''
me = [1,2,3]
print(id(me)) # 2944849018240
me.append(4)
print(id(me)) # 2944849018240

'''
immutable - 메모리 값 변경 불가
    정수(int), 실수(float), 문자열(str), 튜플(tuple)
'''
me = 10
print(id(me))
me +=1 # me = me+1
print(id(me))
