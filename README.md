# AWS_Projects_2019
Data Engineering Pipeline Assessment
Please complete the below tasks using python. You may use any IDE of your choice, however please mention the IDE you have used.
Please email your solution to:
Chirag.Agrawal@novelis.adityabirla.com and Cynthia.Khan@novelis.adityabirla.com
1. Create a folder named RAW.
2. Create a folder called ADLS.
3. Write code which will:
A) look for any new files that appear in RAW
B) copy new files which appear in RAW to ADLS
C) have a retention clause which checks files in RAW and deletes any file which is more than 6 months old and has been copied to ADLS.
D) log the movement of files at every step.
4. Indicate how your code will ensure that the script is running at all times, including circumstances where the server restarts.