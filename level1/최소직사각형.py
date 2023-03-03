def solution(sizes):
    answer = 0
    rol = []
    cow = []
    for i in sizes:
        if i[1] > i[0]:
            i[0],i[1] = i[1],i[0]
    for i in sizes:
        rol.append(i[0])
        cow.append(i[1])
    answer = max(rol) * max(cow)

    return answer