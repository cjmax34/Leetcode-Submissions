def canPlaceFlowers(flowerbed, n):
    counter = 0
    for i in range(len(flowerbed)):
        empty_left = (i == 0) or (flowerbed[i-1] == 0)
        empty_right = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)

        if empty_left and empty_right and flowerbed[i] == 0:
            flowerbed[i] = 1
            counter += 1

    return counter >= n