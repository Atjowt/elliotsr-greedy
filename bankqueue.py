# TC = O(T*N)

def parse(s: str) -> (int, int):
    return [int(ss) for ss in s.split(' ')][:2]

N, T = parse(input())

queue = []
for _ in range(N):
    queue.append(parse(input()))

total = 0
pool = []

for time in reversed(range(T+1)):

    for (balance, patience) in queue:
        if patience == time:
            pool.append(balance)

    if not pool:
        continue

    i_best = 0
    for i in range(len(pool)):
        if pool[i] > pool[i_best]:
            i_best = i
    
    total += pool.pop(i_best)

print(total)