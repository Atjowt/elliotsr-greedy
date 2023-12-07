def entertainment_box(shows, n, k):

    shows.sort(key=lambda x: (x[1], x[0]))

    recorded = 0
    slots = [0] * k

    for start, end in shows:

        i = slots.floor(start)
        if i is None:
            recorded += 1
            slots.remove()
            slots[i] = end

        # find the slot with the latest end time still <= start; ideally O(log k) with a balanced binary tree but O(k) here
        try: i = max((slot for slot in enumerate(slots) if slot[1] <= start), key=lambda slot: slot[1])[0]
        except ValueError: continue
        recorded += 1
        slots[i] = end

    return recorded

n, k = [int(s) for s in input().split()]
shows = [[int(s) for s in input().split()] for _ in range(n)]
result = entertainment_box(shows, n, k)
print(result)