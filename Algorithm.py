from _helpers import Node, Stack, Queue, PriorityQueue



class DFS_Algorithm:
    def __init__(self, start_pos, goal_pos, grid_dim):
        self.start_pos = start_pos
        self.goal_pos = goal_pos
        self.grid_dim = grid_dim
        self.stack = Stack()
        self.stack.push(Node(pos=start_pos, parent=None))

    def get_successors(self, x, y):
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

    def is_valid_cell(self, pos):
        return 0 <= pos[0] <= self.grid_dim[0] and 0 <= pos[1] <= self.grid_dim[1]

    def backtrack_solution(self, curr_node):
        return self._backtrack(curr_node)

    def _backtrack(self, curr_node):
        return [] if curr_node.parent is None else self._backtrack(curr_node.parent) + [curr_node.position()]

    def update(self, grid):
        curr_state = self.stack.pop()
        x, y = curr_state.position()
        done = False
        solution_path = []

        for step in self.get_successors(x, y):
            if self.is_valid_cell(step) and grid[step[0], step[1]] in [1, 3]: # 1: empty cell has not explored yet, 3: goal cell
                self.stack.push(Node(pos=step, parent=curr_state))

                if step == self.goal_pos:
                    done = True
                    solution_path = self.backtrack_solution(curr_state)
                    break
            
            grid[x, y] = 4 # visited

        return solution_path, done, grid


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
