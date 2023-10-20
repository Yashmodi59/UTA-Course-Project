Name:- Yash Modi
UTA ID:- 1002086296

Language and Version:- Python 3.11.3

Structure of the code:-
1. Import the required modules - sys for command-line arguments.
2. Define the read_data() function which reads the data from a given file and returns a list of tuples.
3. Define four dictionaries (bdic, cdic, gdic, fdic) to keep track of the frequencies of the values of each variable in the data.
4. Define the count() function which updates the above dictionaries by iterating over the data.
5. Define eight variables to store the probabilities of different combinations of variables.
6. Define the calculate_probabilities() function which calculates the probabilities of each variable and their combinations and prints them out.
7. Define the calculate_jpd() function which takes the values of the variables and calculates the joint probability distribution of all the variables.
8. Define the main() function which takes in the command-line arguments, reads the data, and calls the calculate_jpd() function to calculate the joint probability distribution of the given values.
9. Finally, check if the script was called with the correct number of command-line arguments and call the main() function.

How to run the code:
bnet.py <training_data> <Bt/Bf> <Gt/Gf> <Ct/Cf> <Ft/Ff>
<training_data> text file with training data.
Bt if B is true, Bf if B is false
Gt if G is true, Gf if G is false
Ct if C is true, Cf if C is false
Ft if F is true, Ff if F is false

Sample Invocation: bnet.py training_data.txt Bf Gt Ct Ff 

Sample Output:
P(B=True) = 0.3041 | P(B=False) = 0.6959
P(C=True) = 0.1699 | P(C=False) = 0.8301
P(G=True),P(B=True) = 0.9279  | P(G=False),P(B=True) = 0.0721
P(G=True),P(B=False) = 0.1181 | P(G=False),P(B=False) = 0.8819
P(F=True),P(G=True),P(C=True) = 0.0417 | P(F=False),P(G=True),P(C=True) = 0.9583
P(F=True),P(G=True),P(C=False) = 0.7064 | P(F=False),P(G=True),P(C=False) = 0.2936
P(F=True),P(G=False),P(C=True) = 0.3158 | P(F=False),P(G=False),P(C=True) = 0.6842
P(F=True),P(G=False),P(C=False) = 0.9588 | P(F=False),P(G=False),P(C=False) = 0.0412
P(B=f, G=t, C=t, F=f) = 0.0134

