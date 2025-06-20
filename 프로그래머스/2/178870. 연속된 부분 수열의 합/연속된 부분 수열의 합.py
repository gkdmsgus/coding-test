def solution(sequence, k):
    l = len(sequence)
    sum = 0  
    end = 0  
    anwser= []

    for i in range(l):
        while sum < k and end < l:
            sum += sequence[end]
            end += 1

        if sum == k:
            anwser.append([i, end-1, end-1-i])
        sum -= sequence[i]

    anwser = sorted(anwser, key=lambda x: x[2])  
    return anwser[0][:2]