# 16236번 아기상어
"""
N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 물고기가 최대 1마리 존재한다.

아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다. 가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.

아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다. 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.
따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.

아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.

더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면,
이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은 빈 칸이 된다.

아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.

공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.
"""

from collections import deque

dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]


def bfs(x, y):
    q, visited = deque([(x, y)]), set([(x, y)])
    time = 0
    shark = 2  # 현재 아기 상어의 크기다.
    eat = 0  # 현재 크기에서, 지금까지 먹은 물고기 수다.
    eat_flag = False  # 현재 상태에서 물고기를 먹은 경우, for _ in range(size) 구문을 진행하지 않기 위한 플래그다.
    answer = 0

    while q:
        size = len(q)

        # 위, 그리고 왼쪽을 더 우선시해서 가야하기 때문에, BFS queue를 소팅해준다.
        q = deque(sorted(q))
        for _ in range(size):
            x, y = q.popleft()

            # 현재 위치에 아기 상어보다 작은 물고기가 있어서, 이를 먹은 경우.
            if board[x][y] != 0 and board[x][y] < shark:
                board[x][y] = 0
                eat += 1

                # 아기 상어의 크기 만큼 먹었다면, 아기 상어의 크기를 +1 해줘야한다.
                if eat == shark:
                    shark += 1
                    eat = 0

                    # 먹고 난 뒤, 현재 위치를 기준으로 다시 근처를 탐색해야 하기 때문에,
                # BFS queue 와 visited 를 초기화 해준다.
                q, visited = deque(), set([(x, y)])
                eat_flag = True

                # 먹었을 때의 시간을 저장해둔다.
                answer = time

            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < n and ny >= 0 and ny < n and (nx, ny) not in visited:
                    if board[nx][ny] <= shark:
                        q.append((nx, ny))
                        visited.add((nx, ny))

            # 현재 위치에서 먹었다면, 더 이상 위 반복문을 돌 필요가 없다.
            if eat_flag:
                eat_flag = False
                break

        time += 1
    return answer


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 1. 초기 상어(자신)의 위치를 파악하고, 해당 자리는 판에서 비워둔다.
s_x, s_y = None, None
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            s_x, s_y = i, j
            board[i][j] = 0

# 2. 시작점에서 BFS 진행
print(bfs(s_x, s_y))


