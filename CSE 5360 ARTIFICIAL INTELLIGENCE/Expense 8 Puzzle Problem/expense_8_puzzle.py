import distutils.util
import sys
from FinalSearch import Search
from datetime import datetime


def read_file(fileName):
    with open(fileName, 'r') as file:
        content_list = [list(map(int, line.split())) for line in file if line.strip() != "END OF FILE"]
    return content_list


def make_dump_file():
    filename = 'trace-' + str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + '.txt'
    with open(filename, 'w') as f:
        f.write(f'Command-Line Arguments :{sys.argv} \n')
        f.write(f'Method :{sys.argv[3]}\n')
        f.write(f'Running :{sys.argv[3]}\n')
    return filename


def main():
    list_of_arguments = sys.argv
    start_file = list_of_arguments[1]
    goal_file = list_of_arguments[2]
    start_state = read_file(fileName=start_file)
    goal_state = read_file(fileName=goal_file)
    if len(list_of_arguments) < 5:
        dump_flag = False
        search = Search(start_state, goal_state, dump_flag)
        if len(list_of_arguments) < 4:
            fName = ''
            search.aStarSearch(fName)
    else:
        dump_flag = distutils.util.strtobool(list_of_arguments[4])
    if len(list_of_arguments) > 3:
        search = Search(start_state, goal_state, dump_flag)
        method = list_of_arguments[3]
        fName = ''
        if dump_flag:
            fName = make_dump_file()
        if method == 'ucs':
            search.uniformCostSearch(fName)
        if method == 'bfs':
            search.breadthFirstSearch(fName)
        if method == 'ids':
            search.iteratingDeepeningSearch(fName)
        if method == 'dfs':
            search.depthFirstSearch(fName)
        if method == 'dls':
            search.depthLimitedSearch(fName)
        if method == 'greedy':
            search.greedySearch(fName)
        if method == 'a*':
            search.aStarSearch(fName)


if __name__ == "__main__":
    main()
