list_a=[1,2,3]
list_a.extend([4,5,6])
print("[1,2,3].extend([4,5,6]:",list_a)
print()

#리스트를 선언합니다.
list_a=[1,2,3]
#연결 연산자로 리스트를 연결합니다.
output=list_a+list_a
print("#리스트 연결 연산자 사용")
print("원본 리스트:", list_a)
print("연산 결과:", output)
print()
#extend() 함수로 리스트를 연결합니다.
output=list_a.extend([1,2,3])
print("# extend() 함수 사용")
print("원본 리스트:", list_a)
print("연산 결과:", output)