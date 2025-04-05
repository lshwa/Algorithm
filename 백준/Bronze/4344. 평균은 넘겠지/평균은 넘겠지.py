c = int(input())

for i in range(c):
    average = 0 
    student = 0
    scores = list(map(int,input().split()))
    for j in range(1,len(scores)):
        average += scores[j]
    average /= scores[0]
    for j in range(1,len(scores)):
        if scores[j] > average:
            student += 1
    print("{:.3f}%".format((student/scores[0])*100))
