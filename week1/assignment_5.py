'''
5. 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y 좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램
    -> 2차원 리스트 / input().split()
'''
arr = []
n = int(input("점의 개수: "))

# map을 이용해 공백을 기준으로 입력된 값을 x, y 형태로 변환 -> 배열에 입력
for _ in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])

arr.sort()

print("--- 출력 ---")
for x, y in arr:
    print(x, y)

'''
TODO 조건)점의 개수 조건(1 <= N <= 100000)
TODO 조건)점의 위치 조건(-100000 <= x, y <= 100,000)
TODO 조건) 위치가 같은 두 점은 존재 안 함
'''