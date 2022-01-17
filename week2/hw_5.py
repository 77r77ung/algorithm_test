import sys
input = sys.stdin.readline
deque = [0] * 10000
f,r = 0,0
for i in range(int(input())):
    a = input().split()
    if a[0] == "push_front":
        deque[f] = a[1]
        f+=1
    elif a[0] == "push_back":
        r -= 1
        deque[r] = a[1]
    elif a[0] == "pop_front":
        if f-r:
            f -= 1
            print(deque[f])
        else:
            print(-1)
    elif a[0] == "pop_back":
        if f-r:
            print(deque[r])
            r += 1
        else:
            print(-1)
    elif a[0] == "size":
        print(f-r)
    elif a[0] == "empty":
        print(1 if f-r == 0 else 0)
    elif a[0] == "front":
        print(deque[f-1] if f-r else -1)
    elif a[0] == "back":
        print(deque[r] if f-r else -1)