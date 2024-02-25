from _helpers import Node, Stack, Queue, PriorityQueue



class DFS_Algorithm:
    def __init__(self, start_pos, goal_pos, grid_dim):
        self.start_pos = start_pos
        self.goal_pos = goal_pos
        self.grid_dim = grid_dim
        self.stack = Stack()
        self.stack.push(Node(pos=start_pos, parent=None))
        self.visited = set()
        self.solution_path = []

    def get_successors(self, x, y):
        return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    def is_valid_cell(self, pos):
        return 0 <= pos[0] <= self.grid_dim[0] and 0 <= pos[1] <= self.grid_dim[1]

    def backtrack_solution(self, curr_node):
        if curr_node is None:
            return []
        return self.backtrack_solution(curr_node.parent) + [curr_node.position()]

    def update(self, grid):
        while not self.stack.isEmpty():
            curr_state = self.stack.pop()
            x, y = curr_state.position()

            if curr_state.position() in self.visited:
                continue

            self.visited.add(curr_state.position())

            if curr_state.position() == self.goal_pos:
                self.solution_path = self.backtrack_solution(curr_state)
                return self.solution_path, True, grid

            for step in self.get_successors(x, y):
                if self.is_valid_cell(step) and grid[step[0]][step[1]] in [1, 3]:
                    self.stack.push(Node(pos=step, parent=curr_state))

            grid[x][y] = 4  # Mark as visited

        return self.solution_path, False, grid


class BFS_Algorithm:
    def __init__(self, start_pos, goal_pos, grid_dim):
        pass

    def update(self, grid):
        """
        Input: grid (2D array)
        Output:
            solution_path (List of tuples, empty if no solution found)
            done (Boolean, True if the goal is reached, False otherwise)
            grid (Updated 2D array)
        """
        pass


class IDS_Algorithm:
    def __init__(self, start_pos, goal_pos, grid_dim):
        pass

    def update(self, grid):
        """
        Input: grid (2D array)
        Output:
            solution_path (List of tuples, empty if no solution found)
            done (Boolean, True if the goal is reached, False otherwise)
            grid (Updated 2D array)
        """
        pass


class A_Star_Algorithm:
    def __init__(self, start_pos, goal_pos, grid_dim):
        pass

    def update(self, grid):
        """
        Input: grid (2D array)
        Output:
            solution_path (List of tuples, empty if no solution found)
            done (Boolean, True if the goal is reached, False otherwise)
            grid (Updated 2D array)
        """
        pass
