def solution(n):
    answer = [n]
    for i in range(1, n//2+1):
        if n%i == 0:
            answer.append(i)
    return sum(answer)