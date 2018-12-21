# Gale Israel
# TRACE Camp
# 12/17/18

# HackerRank: Challenge #1

N = int(input())

if N%2 != 0:
    print("Weird")
elif 2 <= N <= 5:
    print("Not weird")
elif 6 <= N <= 20:
    print("Weird")
elif 21 <= N <= 100:
    print("Not Weird")

# HackerRank: Challenge #2
if __name__ == '__main__':
    n = int(input())
    for x in range(n):
        print(x**2)

# HackerRank: Challenge #3
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # find number of scores to average
    count = len(scores)
    # print average
    print('%.2f' % (sum(student_marks[query_name]) / count))



