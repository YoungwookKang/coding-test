def move(x, y, next_point_x, next_point_y):
    if x != next_point_x:
        if next_point_x > x:
            x += 1
        else:
            x -= 1
    else:
        if next_point_y > y:
            y += 1
        else:
            y -= 1
    return x, y


def solution(points, routes):
    path = []
    for i in range(len(routes)):
        start_x, start_y = points[routes[i][0] - 1]
        depth = len(routes[i])
        path.append((start_x, start_y, 0, depth - 1))

    position = {}
    for i in range(len(routes)):
        robot = routes[i][0] - 1
        x, y = points[robot]
        if (x, y) in position:
            position[(x, y)] += 1
        else:
            position[(x, y)] = 1

    cnt = 0
    t = 0
    for p in position:
        if position[p] >= 2:
            cnt += 1
    print(f'path = {path}')
    print(f'routes = {routes}')
    print(f'points = {points}')
    print(f'충돌 수 = {cnt}')
    while len(path) > 0:

        temp = {}
        temp_path = []
        temp_route = []
        # len(path) == len(route)
        for i in range(len(path)):
            x, y, curr_depth, dest_depth = path[i]
            next_point = routes[i][curr_depth + 1]
            next_point_x, next_point_y = points[next_point - 1]
            nx, ny = move(x, y, next_point_x, next_point_y)
            complete = False
            if (nx, ny) in temp:
                temp[(nx, ny)] += 1
            else:
                temp[(nx, ny)] = 1
            if nx == next_point_x and ny == next_point_y:
                curr_depth += 1
                # 도착 리스트 말소
                if curr_depth == dest_depth:
                    complete = True
            if not complete:
                temp_path.append((nx, ny, curr_depth, dest_depth))
                temp_route.append(routes[i])

        for p in temp:
            if temp[p] >= 2:
                cnt += 1
        path = temp_path
        routes = temp_route
        position = temp

        t += 1
        print(f'{t} 초 후')
        print(f'path = {path}')
        print(f'routes = {routes}')
        print(f'points = {points}')
        print(f'충돌 수 = {cnt}')

    answer = cnt
    return answer