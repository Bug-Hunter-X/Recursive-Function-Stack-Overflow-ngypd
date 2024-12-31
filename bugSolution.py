def function_with_uncommon_error_solution(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = function_with_uncommon_error_solution(n-1, memo) + function_with_uncommon_error_solution(n-2, memo)
        memo[n] = result
        return result