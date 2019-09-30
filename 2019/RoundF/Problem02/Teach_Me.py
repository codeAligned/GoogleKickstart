"""
2
4 100
4 80 90 100 5
1 90
1 80
3 80 90 100
3 30
4 10 11 12 13
4 10 11 12 13
5 25 26 27 28 29

"""

T = int(input())

for case_num in range(0, T):
    N, S = map(int, input().split())

    emp = []

    for i in range(0, N):
        emp.append(list(map(int, input().split())))

    cases = 0

    for i in range(0, N):
        for j in range(0, N):
            if i == j:
                pass
            elif emp[i][0] > emp[j][0]:
                cases += 1
            else:
                for k in range(1, len(emp[i])):
                    if emp[i][k] not in emp[j]:
                        cases += 1
                        break

    print("Case #{}: {}".format(case_num + 1, cases))

