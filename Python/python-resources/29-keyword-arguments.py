# 1. Keyword arguments in the function call
def comments_info(comments_qty, day):
    print(f'{comments_qty} comments were posted on {day}')


comments_info(comments_qty=50, day='Monday')
comments_info(20, day='Sunday')
# comments_info(day='Sunday', 20)  # Error
comments_info(10, 'Friday')


# 2. Keyword arguments can't be gathered into the args tuple
def comments_info(*args):
    print(f'{args[0]} comments were posted on {args[1]}')


comments_info(50, day='Monday')  # Error
