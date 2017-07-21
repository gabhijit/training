"""
A simple python program that processes Web Log Data.
"""

# with construct - this is very useful when you don't have to worry about
# opening and closing files explicitly. What happens when exceptions occurs
# etc.
with open('weblog.txt', 'r') as f:

    # We traverse through each line.
    # Note: There is also one more function call f.readlines()
    # for applications like this, we should always avoid using that function
    #
    # why? readlines - reads an entire file in a list (memory consumption)
    for line in f:
        tokens = line.split(" ")

        toks = [tokens[0], tokens[5], tokens[6],
                tokens[8], tokens[9], tokens[11]]
        print ",".join(map(lambda x: x.strip().strip('"'), toks))
        # Now let's say we want to count numbers for different error codes.
        # Which data structure we'd use?

        # Hint: We want to have a datastructure which looks like
        # (something : count(something))
