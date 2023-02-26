# https://leetcode.com/problems/tenth-line/description/

# Read from the file file.txt and output the tenth line to stdout.

# Logic: Use `sed`

sed -n '10p' file.txt
