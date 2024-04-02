def minimumBoxes(apple, capacity):
    apple_sum = sum(apple)
    capacity.sort(reversed=True)
    num_boxes = 0

    while apple_sum > 0:
        apple_sum -= capacity[num_boxes]
        num_boxes += 1

    return num_boxes