def minimize_loss(prices):
    n = len(prices)
    min_loss = float('inf')

    for i in range(n):
        for j in range(i+1, n):
            if prices[i] > prices[j]:
                loss = prices[i] - prices[j]
                if loss < min_loss:
                    min_loss = loss

    return min_loss if min_loss != float('inf') else 0

print(minimize_loss([20, 15, 8, 2, 12]))  # Output: 3 (from 15 -> 12)
