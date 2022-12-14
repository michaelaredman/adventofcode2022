import numpy as np

treeHeightsRaw = ["30373",
                  "25512",
                  "65332",
                  "33549",
                  "35390"]


def rawToArray(rawHeights):
    heightArray = []
    for x in rawHeights:
        temp = []
        for c in x:
            temp.append(int(c))
        heightArray.append(temp)
    return heightArray


def findVisible(heightArray):
    heights = np.array(heightArray)
    visible = np.full(heights.shape, False, dtype=bool)
    for i in range(0, heights.shape[0]):
        maxHeight = heights[i][0]
        visible[i][0] = True
        for j in range(1, heights.shape[1]):
            if (heights[i][j] > maxHeight):
                visible[i][j] = True
            maxHeight = max(maxHeight, heights[i][j])
        maxHeight = heights[i][-1]
        visible[i][-1] = True
        for j in reversed(range(0, heights.shape[1]-1)):
            if (heights[i][j] > maxHeight):
                visible[i][j] = True
            maxHeight = max(maxHeight, heights[i][j])

    for j in range(0, heights.shape[1]):
        maxHeight = heights[0, j]
        visible[0, j] = True
        for i in range(1, heights.shape[0]):
            if (heights[i][j] > maxHeight):
                visible[i][j] = True
            maxHeight = max(maxHeight, heights[i][j])
        maxHeight = heights[-1][j]
        visible[-1][j] = True
        for i in reversed(range(0, heights.shape[0]-1)):
            if (heights[i][j] > maxHeight):
                visible[i][j] = True
            maxHeight = max(maxHeight, heights[i][j])

    return visible


# print(findVisible(rawToArray(treeHeightsRaw)))
print(
    f"Number of visible trees: {sum(map(sum, findVisible(rawToArray(treeHeightsRaw))))}")

with open("inputs/day8", "r") as f:
    largeRawInput = [line.rstrip() for line in f]

largeHeights = rawToArray(largeRawInput)

print(f"Number of visible trees: {sum(map(sum, findVisible(largeHeights)))}")

# Use a monostack with (height, index) for ech of up down left right

# for each (wlog) row:
# pop from the top of the stack if the top of the stack is strictly smaller than the
# current height
# the numtreesleft is the difference between my index and the index of the top of the stack
# if the stack is empty then its just my index


def findScenicScore(heights: np.ndarray) -> int:
    N, M = heights.shape
    leftVisible = np.empty((N, M), dtype=int)
    for i in range(0, N):
        monostack = []
        for j in range(0, M):
            while (monostack and heights[i][j] > monostack[-1][0]):
                monostack.pop()
            if (monostack):
                leftVisible[i][j] = j - monostack[-1][1]
            else:
                leftVisible[i][j] = j
            monostack.append((heights[i][j], j))
    rightVisible = np.empty((N, M), dtype=int)
    for i in range(0, N):
        monostack = []
        for j in reversed(range(0, M)):
            while (monostack and heights[i][j] > monostack[-1][0]):
                monostack.pop()
            if (monostack):
                rightVisible[i][j] = monostack[-1][1] - j
            else:
                rightVisible[i][j] = (M - 1) - j
            monostack.append((heights[i][j], j))
    topVisible = np.empty((N, M), dtype=int)
    for j in range(0, M):
        monostack = []
        for i in range(0, N):
            while (monostack and heights[i][j] > monostack[-1][0]):
                monostack.pop()
            if (monostack):
                topVisible[i][j] = i - monostack[-1][1]
            else:
                topVisible[i][j] = i
            monostack.append((heights[i][j], i))
    downVisible = np.empty((N, M), dtype=int)
    for j in range(0, M):
        monostack = []
        for i in reversed(range(0, N)):
            while (monostack and heights[i][j] > monostack[-1][0]):
                monostack.pop()
            if (monostack):
                downVisible[i][j] = monostack[-1][1] - i
            else:
                downVisible[i][j] = (N - 1) - i
            monostack.append((heights[i][j], i))

    maxScenicScore = 0
    for i in range(0, N):
        for j in range(0, M):
            maxScenicScore = max(
                maxScenicScore,
                topVisible[i][j] * downVisible[i][j] * leftVisible[i][j] * rightVisible[i][j])

    return maxScenicScore


print(
    f"The maximum scenic score is: {findScenicScore(np.array(rawToArray(treeHeightsRaw)))}")

print(
    f"The maximum scenic score is: {findScenicScore(np.array(largeHeights))}")
