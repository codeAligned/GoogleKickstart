"""
1
11 1 2
8
2 3
"""

T = int(input())

for case_num in range(0, T):

	N, M, Q = map(int, input().split())
	P = list(map(int, input().split()))
	R = list(map(int, input().split()))

	pages_read = 0

	for r in R:
		pages_read += N // r
		for p in P:
			if p % r == 0:
				pages_read -= 1

	print("Case #{}: {}".format(case_num + 1, pages_read))
