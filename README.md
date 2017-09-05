# Peer-Review-Analysis


Download the Chromium database from ' www.dropbox.com/s/0p7f7ye0mff0no8/chromium.zip?dl=0 'and save to the directory Peer-Reciew-Analysis. Unzip the file.

1.Required python packges 
  igraph and pandas.

2.On executing 'queries.sql' in mysql 'result.csv' is created
3.The file 'personreview.csv' is geneated by executing the code

  use chromium;
  select issue,sender,date,approval from comment;

4The folder Netowrk analysis contains two files 
  1.HeadTailCount.py - 
  Takes input from personreview.csv
    - Find out the number of reviews in the data-set, each of which has been commented upon by at least:
    - One person (R1)
		- Two persons (R2)
		- Three persons (R3)
	- The number of persons in the data-set, each of whom have commented on at least:
		- One review (P1)
		- Two reviews (P2)
		- Three reviews (R3)
  2.analyze.py - 
  Takes input from personreview.csv and result.csv
  Divides the data into 50 culmulative time intervals and finds: 
		- Number of unique reviews commented on 
		- Number of comments
		- Number of approvals
		- Average number of comments per person
		- Average number of approvals per person 
		- Average closure time across all unique reviews commented on (closure time = the time period in days between the review creation date and the date it is last modified)

5.The folder Network generation contains two files
  1.networkgenertator.py - generates a network of developers where the edges represent a common review that is commented on by both developers
  2.code.py - Generates 50 networks of developers (pajek files) over 50 culmulative time intervals 

6.The folder Rcode contains: 
  1.rcode.R - generate histograms, boxplots, and descriptive statistics for the following fields: comments,	NoOfCommenters,approval,created,modified,no_of_days,owners.
  2.Network_family_metrics_calculator.R 

