# median_unique.py - Median number of unique words
# Insight Data Engineering Coding Challenge, 2015 July
# Katrina Sitkovits, katrina.sitkovits@gmail.com

import bisect
import sys

# Open input and output file streams
input_file = sys.argv[1];
output_file = sys.argv[2];
tweets_input = open(input_file, "r")
stats_output = open(output_file, "w")

# Growing list of total number of unique words as tweets come in
unique_words_list = []

for line in tweets_input:

    # Parse tweet input lines and separate words by whitespace
    # Find number of unique words in each tweet
    unique_words_in_tweet = {} # Dictionary for unique words in each tweet
    for word in line.split():
        if word in unique_words_in_tweet:
            unique_words_in_tweet[word] += 1
        else:
            unique_words_in_tweet[word] = 1
    num_unique_words_in_tweet = len(unique_words_in_tweet)

    # Add unique number of words in current tweet to (ascending) sorted list of total unique word counts
    bisect.insort(unique_words_list, num_unique_words_in_tweet)

    # Update unique word median
    num_tweets = len(unique_words_list)
    if num_tweets == 1: # only one tweet
        median = unique_words_list[0]
    elif (num_tweets % 2) == 1: # odd number of tweets
        median_index = int(num_tweets//2)
        median = unique_words_list[median_index]
    else: # even number of tweets
        index_upper = int(num_tweets//2)
        index_lower = index_upper-1
        median = float(unique_words_list[index_lower]+unique_words_list[index_upper])/float(2)
        #Python version compatibility - cast denominator to floating point to ensure output is also floating point

    # Save updated median to output file (each median has 2 decimal points)
    stats_output.write('%.2f' % median + '\n')
	    
	    
# Close input/output file streams
tweets_input.close()
stats_output.close()






