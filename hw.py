from collections import deque

def getMinDiceThrows(moves, N):
    visited = [False] * N

    queue = deque()

    visited[0] = True

    queue.append((0, 0))

    while queue:
        cell, dist = queue.popleft()

        if cell == N - 1:
            return dist

        for dice in range(1, 7):
            next_cell = cell + dice
            if next_cell < N and not visited[next_cell]:
                visited[next_cell] = True

                if moves[next_cell] != -1:
                    queue.append((moves[next_cell], dist + 1))
                else:
                    queue.append((next_cell, dist + 1))

    return -1


if __name__ == "__main__":
    N = 30
    moves = [-1] * N

    moves[2] = 21
    moves[4] = 7
    moves[10] = 25
    moves[19] = 28

    moves[26] = 0
    moves[20] = 8
    moves[16] = 3
    moves[18] = 6

    print("Min Dice Throws required is:", getMinDiceThrows(moves, N))
