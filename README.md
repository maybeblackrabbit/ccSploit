ccSploit
========

The script "ccSploit.py" affects two card shop scripts known as "Vampire" and "Heaven".

This python script exploits two fraudulent "auto-selling" credit card shop sources.  Right now it can detect the source, test for an undiscovered SQL injection that affects all versions of the two sources, searches for vulnerable files, open directories, a backdoored version of the source, the possiblity of a default admin account, and even more that I'm too lazy to list.  The script is in its "pre-beta" stage, so sorry about some sloppy coding.  The main goal is to get it working in good order with lots of handy-dandy features first. 

--Usage--
<br>
python ccSploit.py -u "url here"

If the url is in a /shop/ directory then do:
python ccSploit.py -u "url here" --shop

Please use Python 2.7.  If you're using Python 3 I highly doubt this will work for obvious reasons (view source).
