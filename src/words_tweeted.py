# words_tweeted.py - Unique word counter
# Insight Data Engineering Coding Challenge, 2015 July
# Katrina Sitkovits, katrina.sitkovits@gmail.com

import sys

# Open input and output file streams
input_file = sys.argv[1];
output_file = sys.argv[2];
tweets_input = open(input_file, "r")
stats_output = open(output_file, "w")

# Instantiate dictionary
data = {}

# Parse tweet.txt lines and separate words by whitespace
for line in tweets_input:
    for word in line.split():
        if word in data:
            data[word] += 1
        else:
            data[word] = 1

# Save values to output file in alphabetical order
for key, value in sorted(data.items()):
    stats_output.write("%s %s\n" % (key,value))

# Close input/output file streams
tweets_input.close()
stats_output.close()
