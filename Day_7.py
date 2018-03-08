#Day7________ Read a file

# Windows OS
f=open("E:\\path\\file_name.txt","r")
# Mac OS
f=open("//Volumes//[drive name]//file_name.txt","r")

f.close()

# importing/exporting
# https://docs.python.org/3.3/tutorial/inputoutput.html#reading-and-writing-files
# https://docs.python.org/2.7/tutorial/inputoutput.html#reading-and-writing-files
r - reading
w - writing
a - appending

# read eachline
f.readline()

# Write something
A=10
f.write(A)
f.close()



The argument mode points to a string beginning with one of the following
 sequences (Additional characters may follow these sequences.):

 ``r''   Open text file for reading.  The stream is positioned at the
         beginning of the file.

 ``r+''  Open for reading and writing.  The stream is positioned at the
         beginning of the file.

 ``w''   Truncate file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.

 ``w+''  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file.

 ``a''   Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.

 ``a+''  Open for reading and writing.  The file is created if it does not
         exist.  The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar.