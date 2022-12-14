import numpy as np


example = np.matrix([list("Sabqponm"),
                     list("abcryxxl"),
                     list("accszExk"),
                     list("acctuvwj"),
                     list("abdefghi")])


def possible(frm: str, to: str) -> bool:
    if frm == "S":
        frm = "a"
    if to == "E":
        to = "z"
    return (ord(to) - ord(frm)) <= 1


def bounds_check(loc: tuple[int, int], N: int, M: int) -> bool:
    return (loc[0] >= 0) and (loc[0] < N) and (loc[1] >= 0) and (loc[1] < M)


def bfs_steps(topo: np.ndarray) -> int:
    N, M = topo.shape
    visited = np.full(topo.shape, fill_value=False, dtype=bool)
    start = (np.where(topo == 'S')[0][0], np.where(topo == 'S')[1][0])
    Q = [start]
    visited[start[0], start[1]] = True
    n_steps = 0
    while Q:
        new_Q = []
        for loc in Q:
            if topo[loc] == "E":
                return n_steps
            for delta in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                new_loc = (loc[0] + delta[0], loc[1] + delta[1])
                if ((bounds_check(new_loc, N, M)) and
                        (not visited[new_loc]) and
                        possible(topo[loc], topo[new_loc])):
                    new_Q.append(new_loc)
                    visited[new_loc] = True
        Q = new_Q
        n_steps += 1
    return 0


print(f"The example topography takes {bfs_steps(example)} steps.")

hills = []
with open("inputs/day12", 'r') as f:
    for line in f:
        hills.append(list(line.strip()))
hills = np.array(hills)

print(f"Our topography takes {bfs_steps(hills)} steps!")


def trail_steps(topo: np.ndarray) -> int:
    N, M = topo.shape
    visited = np.full(topo.shape, fill_value=False, dtype=bool)
    start = (np.where(topo == 'S')[0][0], np.where(topo == 'S')[1][0])
    a = list(zip(np.where(topo == "a")[0], np.where(topo == "a")[1]))
    Q = [start] + a
    visited[start[0], start[1]] = True
    n_steps = 0
    while Q:
        new_Q = []
        for loc in Q:
            if topo[loc] == "E":
                return n_steps
            for delta in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                new_loc = (loc[0] + delta[0], loc[1] + delta[1])
                if ((bounds_check(new_loc, N, M)) and
                        (not visited[new_loc]) and
                        possible(topo[loc], topo[new_loc])):
                    new_Q.append(new_loc)
                    visited[new_loc] = True
        Q = new_Q
        n_steps += 1
    return 0


print(f"Our trail is {trail_steps(hills)} steps long!")
