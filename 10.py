from collections import Counter

with open("input/10.txt") as f:
    jolts = sorted(int(line.rstrip("\n")) for line in f)

c = Counter(b - a for a, b in zip([0, *jolts], jolts))
part1 = c[1] * (c[3] + 1)
print(f"{part1=}")

dp = [1] + [0] * max(jolts)
for i in range(1, len(dp)):
    if i in jolts:
        dp[i] = sum(dp[max(i - 3, 0) : i])
part2 = dp[-1]
print(f"{part2=}")
