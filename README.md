# NLP for Twitter Text Data

This repository contains the input files and programs for different assignment questions in relation to keyword extraction, where MongoDB is the database, and the application of MapReduce for word count and sort applications. All code is run with Python 3.9. To run the MapReduce examples, the preprocessed input files and the program must be in the same repository.

## Task 1: [Keyword Extraction](https://github.com/felix-rosenberger/Tweet-Text-NLP-with-MapReduce/blob/main/Keyword%20Extraction/Task1.py)

The program should read the tweet data from MongoDB, and then extract keywords from each tweet. The keywords extracted should then be stored back in a comma-separated format to MongoDB, appended as a new key-value pair. For this, each tweet was tokenized and stopwords were removed. Note that preprocessing has not been exhaustive as it was not required to include e.g. stemming or other options to further featurize/contextualise the text. I am aware that this would need to be done in a real application.

### Libraries used
```
from pymongo import MongoClient 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
```

## Task 2: [MapReduce Word Count](https://github.com/felix-rosenberger/Tweet-Text-NLP-with-MapReduce/tree/main/MapReduce%20Count%20Occurrence%20of%20Words)

The [preprocessing program](https://github.com/felix-rosenberger/Tweet-Text-NLP-with-MapReduce/blob/main/MapReduce%20Count%20Occurrence%20of%20Words/Task2Preprocess.py) connects to MongoDB and reads in the text data which is then saved as a text file which in turn is the [input file](https://github.com/felix-rosenberger/Tweet-Text-NLP-with-MapReduce/blob/main/MapReduce%20Count%20Occurrence%20of%20Words/Task2Input.txt) for the main [MapReduce program](https://github.com/felix-rosenberger/Tweet-Text-NLP-with-MapReduce/blob/main/MapReduce%20Count%20Occurrence%20of%20Words/Task2.py). The MapReduce program outputs a text file that includes each word and the correpsonding number of occurrences across all tweets. As above, the preprocessing step would need to be more sophisticated in a real application and is by no means exhaustive.

### Libraries used
```
import pandas as pd
from pymongo import MongoClient
from mrjob.job import MRJob
import re
```

## Task 3: [MapReduce City Count](https://github.com/felix-rosenberger/Tweet-Text-NLP-with-MapReduce/tree/main/MapReduce%20Count%20Number%20of%20Tweets%20from%20different%20Cities)

The [preprocessing program](https://github.com/felix-rosenberger/Tweet-Text-NLP-with-MapReduce/blob/main/MapReduce%20Count%20Number%20of%20Tweets%20from%20different%20Cities/Task3Preprocess.py) connects to MongoDB and reads in the city data which is then saved as a text file which in turn is the [input file](https://github.com/felix-rosenberger/Tweet-Text-NLP-with-MapReduce/blob/main/MapReduce%20Count%20Number%20of%20Tweets%20from%20different%20Cities/Task3Input.txt) for the main [MapReduce program](https://github.com/felix-rosenberger/Tweet-Text-NLP-with-MapReduce/blob/main/MapReduce%20Count%20Number%20of%20Tweets%20from%20different%20Cities/Task3.py). The MapReduce program outputs a text file that includes each city and the corresponding number of tweets that were posted from that city.

### Libraries used
```
import pandas as pd
from pymongo import MongoClient 
from mrjob.job import MRJob
import re
```

## Task 4: [MapReduce MergeSort by ID](https://github.com/felix-rosenberger/Tweet-Text-NLP-with-MapReduce/tree/main/MapReduce%20Sort%20Tweets%20using%20ID)

The [preprocessing program](https://github.com/felix-rosenberger/Tweet-Text-NLP-with-MapReduce/blob/main/MapReduce%20Sort%20Tweets%20using%20ID/Task4Preprocess.py) connects to MongoDB and extracts the object ID for each tweet which is then saved as a text file which in turn is the [input file](https://github.com/felix-rosenberger/Tweet-Text-NLP-with-MapReduce/blob/main/MapReduce%20Sort%20Tweets%20using%20ID/Task4Input.txt) for the main [MapReduce program](https://github.com/felix-rosenberger/Tweet-Text-NLP-with-MapReduce/blob/main/MapReduce%20Sort%20Tweets%20using%20ID/Task4MergeSort.py). The MapReduce program outputs a text file that contains the sorted tweet IDs.

### Libraries used
```
from pymongo import MongoClient
from mrjob.job import MRJob
```
