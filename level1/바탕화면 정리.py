def solution(wallpaper):
    answer = []
    top = 50
    left = 50
    right = 0
    bottom = 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                if i < top:
                    top = i
                if j < left:
                    left = j
                if i > right:
                    right = i
                if j > bottom:
                    bottom = j
    answer.append(top)
    answer.append(left)
    answer.append(right+1)
    answer.append(bottom+1)
    return answer