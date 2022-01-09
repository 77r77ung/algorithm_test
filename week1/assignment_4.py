'''
4. 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램
    a) 길이가 짧은 것부터
    b) 길이가 같으면 사전 순으로
'''
arr = []

num = int(input("단어의 개수: "))
for i in range(num):
    arr.append(input("소문자로 구성된 단어를 입력하세요.: "))

new = list(set(arr))
new.sort(key = lambda x : (len(x), x))
print(new)

'''
TODO 조건)문자열의 길이는 50을 넘지 않는다.
for j in arr:
    if int(len(arr[j])) > 50:
        del(arr[i])
TODO 조건)대문자가 입력되었을 때
TODO 조건)단어의 개수에 대한 조건 (1 <= N <= 20000)

arr.sort(): 알파벳 순서로 정렬
'''