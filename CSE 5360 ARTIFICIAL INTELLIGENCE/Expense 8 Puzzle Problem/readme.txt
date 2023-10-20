NAME: YASH JITENDRA MODI
UTA ID:-1002086296
Net Id: yxm6296

Python -- Version = Python 3.8.3

run the code with this argument:
python expense_8_puzzle.py start.txt goal.txt methodName True/False
methodName can be [ucs, bfs, dfs, dls, a*, ids, greedy]
code: expense_8_puzzle.py <start-file> <goal-file> <method> <dump-flag>
<start-file> and <goal-file> are required.
 <method> can be
 bfs - Breadth First Search
ucs - Uniform Cost Search
dfs - Depth First Search
dls - Depth Limited Search (Note: Depth Limit will be obtained as a Console Input) [Note: This part is EC for CSE 4308 students]
ids - Iterative Deepening Search [Note: This part is EC for CSE 4308 students]
greedy - Greedy Seach
a* - A* Search (Note: if no <method> is given, this should be the default option)
If <dump-flag>  is given as true, search trace is dumped for analysis in trace-<date>-<time>.txt (Note: if <dump-flag> is not given, assume it is false)
search trace contains: fringe and closed set contents per loop of search(and per iteration for IDS), counts of nodes expanded and nodes
- for DLS you have to enter input depthlimit when prompted
Dump file will be generated in same folder where the code is starting will 'trace.....'

There will be folder in this zip file and in 'AI 1' folder there will be four .py file and start file, goal file and readme.tx :
FinalNode: Its a class file to store Node Object
FinalSearch: This is the important file store all methods for search of all 7 methods
FinalUtilty: Its a python file containing 5 different helper method which is used in every 7 method of Final Search file
expense_8_puzzle : Main File to run the code
readme = explaining code
goal = goal file last row will "END OF FILE" if not then also it may work
start = initial file last row will "END OF FILE" if not then also it may work


Note: Some method are taking much time to generate the output so first check the trace file which is generated to check the fringe and closed list

All the reference and PseudoCode i have taken from here:

https://crystal.uta.edu/~gopikrishnav/classes/common/4308_5360/slides/chapter03.pdf
https://crystal.uta.edu/~gopikrishnav/classes/common/4308_5360/slides/Informed_Search.pdf
https://crystal.uta.edu/~gopikrishnav/classes/common/4308_5360/slides/implNotes.html

