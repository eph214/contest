# contest
concurrency tester in python

This is a simple script that allows concurrency testing on a url (including https). I used httplib2 as I was able to ignore invalid ssl certs during testing. Just replace the top two variables with the correct url and number of concurrent processes and run it:
python ./concall.py
