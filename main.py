import argparse
from game import solve_maze
from enum import Enum

class Algorithm(Enum):
    dfs = 'dfs'
    bfs = 'bfs'
    ids = 'ids'
    a_star = 'a_star'

    def __str__(self):
        return self.value


def main():
    parser = argparse.ArgumentParser(prog='Maze Solver',
                                     description='Utilizing artificial intelligence algorithms to solve mazes')
    parser.add_argument('-a', '--algorithm', type=Algorithm, default='dfs', choices=list(Algorithm), help='Algorithm must be: [dfs, bfs, ids, a_star]')
    parser.add_argument('-m', '--map', default=0, type=int, help='0, and 1 are the available maps')
    
    args = parser.parse_args()
    if args.algorithm:
        solve_maze(map_address=f"mazes/maze_{args.map}.csv", algorithm=str(args.algorithm).upper())
    else:
        parser.print_help()
        exit(1)



if __name__ == '__main__':
    main()