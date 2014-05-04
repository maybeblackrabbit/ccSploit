ccSploit
========

The script "ccSploit.py" affects two card shop scripts known as "Vampire" and "Heaven".

Python script to exploit fraudulent "auto-selling" credit card shops.  Right now it can detect the source, tests for an undiscovered SQL injection that affects all versions of the two sources, searches for vulnerable files, searches for open directories, searches for a backdoored version of the source, searches for the possiblity of a default admin account, and tests for even more!  The script is in it's pre-beta stage, so sorry about some sloppy coding. 

Usage:
python ccSploit.py -u "url here"

If the url is in a /shop/ directory then do:
python ccSploit.py -u "url here" --shop
