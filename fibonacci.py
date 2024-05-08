def fibonacci(n):
    if n <= 1:
        return n
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] =  fibonacci(n - 1) + fibonacci(n - 2)
    return dp[n]

if __name__ == '__main__':
    number = int(input("Enter the nth term of the Fibonacci series: "))
    dp = [-1] * (number + 1)
    result = fibonacci(number)
    print("The", number, "th Fibonacci number is:", result)
