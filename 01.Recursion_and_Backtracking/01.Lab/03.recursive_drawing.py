def draw_pattern(n):
    if n == 0:
        return
    print('*' * n)
    draw_pattern(n - 1)
    print("#" * n)


n = int(input())
draw_pattern(n)
