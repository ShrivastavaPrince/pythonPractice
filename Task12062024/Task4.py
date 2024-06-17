def fibonacci(n):
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series[:n]

n = int(input("Enter the number of terms in the Fibonacci series: "))
print(f"The first {n} terms of the Fibonacci series are: {fibonacci(n)}")
