"""
The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level 
sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
We are interested in finding the longest (number of characters) absolute path to a file within our file system. 
For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", 
and its length is 32 (not including the double quotes). Given a string representing the file system in the above format, 
return the length of the longest absolute path to a file in the abstracted file system. 
If there is no file in the system, return 0.
Note:
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.
"""
s="dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir34\n\t\tsubsubdir2\n\t\t\tfile2.ext" 

def longestpath(s):
    if s.find("file") == -1:
        return 0

    maxlen = 0
    pathlen = {0: 0}
    for line in s.splitlines():
        depth = line.count("\t")
        nameLength = len(line) - depth
        if '.' in line:
            maxlen = max(maxlen, pathlen[depth] + nameLength)
        else:
            pathlen[depth + 1] = pathlen[depth] + nameLength + 1 # +1 for /
    return maxlen
    
print(longestpath(s))