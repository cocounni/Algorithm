from itertools import permutations

def solution(n, weak, dist):
    weak_len = len(weak)
    weak_expanded = weak + [w + n for w in weak]
    answer = len(dist) + 1

    for start in range(weak_len):
        for friends in permutations(dist):
            count = 1
            position = weak_expanded[start] + friends[count - 1]

            for i in range(start, start + weak_len):
                if position < weak_expanded[i]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak_expanded[i] + friends[count - 1]

            answer = min(answer, count)

    if answer <= len(dist):
        return answer
    else:
        return -1
