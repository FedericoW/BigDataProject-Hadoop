# BigDataProject-Hadoop

This project was composed of 2 programs that implemented Hadoop Streaming Framework and were able to run big amounts of data due to XSEDE. Each program consisted of 2 mappers and 2 reducers and used the Yelp dataset (Source:https://www.kaggle.com/yelp-dataset/yelp-dataset/version/4). Program 1 found the most popular buisness, while Program 2 found the highest rated buisness.

Program 1 - Mapper1A-Reducer1A Execution Time: 32930
	  - Mapper1B-Reducer1B Execution Time: 2410

Program 2 - Mapper2A-Reducer2A Execution Time: 34120
	  - Mapper2B-Reducer2B Execution Time: 2440

Instructions on how to use Hadoop
1. Login in to bridges using login and password.
2. To start hadoop use the following commands
    interact -N 4 -t 01:00:00
	module load hadoop
	start-hadoop.sh
3. Create a directory to store input files in the HDFS
   hadoop fs -mkdir -p in 
4. Load file to the HDFS
	hadoop fs -put <file path> in
5. Execute the program
	hadoop jar /opt/packages/hadoop-testing/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -input in/<name of input file> -output out/<name of output file> -mapper <Mapper.py file> -reducer <Reducer.py file>
6. Merge file produced by reducer (If multiple reducers outputted multiple partitions of a result i.e part-00000, part-00001, etc) 
   hadoop fs -getmerge <output file directory> /desired/local/output/file.txt
  

WARNING: Occasionally Hadoop will bug out and give you an error. Just type:
1. stop-all.sh
2. module load hadoop
   start-hadoop.sh
  
