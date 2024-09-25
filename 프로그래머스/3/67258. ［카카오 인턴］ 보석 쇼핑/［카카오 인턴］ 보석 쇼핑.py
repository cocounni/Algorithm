def solution(gems):
    gemTypes = len(set(gems))
    gemDict = {}
    
    left = 0
    answer = [0, len(gems) - 1]
    minLength = len(gems)

    for right in range(len(gems)):
        # 딕셔너리에 현재 보석 기록
        gemDict[gems[right]] = gemDict.get(gems[right], 0) + 1

        # 모든 종류의 보석이 포함될 때까지 왼쪽 포인터 이동
        while len(gemDict) == gemTypes:
            if right - left < minLength:
                minLength = right - left
                answer = [left, right]

            # 왼쪽 포인터의 보석을 제거하면서 윈도우 축소
            gemDict[gems[left]] -= 1
            if gemDict[gems[left]] == 0:
                del gemDict[gems[left]]
            left += 1

    return [answer[0] + 1, answer[1] + 1]