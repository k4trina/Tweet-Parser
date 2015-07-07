# Tweet-Parser

### Developer: Katrina Sitkovits
### Email: katrina.sitkovits@gmail.com
### Date: July 6, 2015

Programming Langugage: Python

The tweet parser is comprised of the following two features:
* Calculates total number of times each word appears in tweets
* Calculates median number of unique words per tweet, and maintains rolling median as tweets come in

The tweet parser is executed by running the run.sh script, which reads the tweet input file from the ./tweet_input directory, and outputs the results of each feature to the ./tweet_output directory. 

The run.sh script runs the following commands:

```
$ python ./src/words_tweeted.py ./tweet_input/tweets.txt ./tweet_output/ft1.txt
$ python ./src/median_unique.py ./tweet_input/tweets.txt ./tweet_output/ft2.txt 
```

The two features use standard Python modules (libraries): sys and bisect.
