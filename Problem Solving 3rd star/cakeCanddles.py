candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))
ans = candles.count(max(candles))
print(ans)