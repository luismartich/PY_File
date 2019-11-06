
"""
Luis Martich
CS 100 2019F Section 107
HW 09, Oct 31, 2019
"""

#PROBLEM 1 
def file_copy(in_file, out_file):
  A = open(in_file, 'r')
  in_file = A.read()
  A.close()
  B = open(out_file, 'w')
  for line in in_file:
    B.write(line)
  B.close()

file_copy('filea.txt', 'out_file.txt')



#PROBLEM 2
def file_stats(in_file):
  import string
  A = open(in_file, 'r')
  in_file2 = A.readlines()
  print("Lines: " + str(len(in_file2)))
  count = 0
  count2 = 0
  for i in in_file2:
    count = count + len(i.split())
    count2 = count2 + len(i)
  print("Words: " + str(count))
  print("Characters: " + str(count2))

file_stats('filea.txt')


#PROBLEM 3
def repeat_words(in_file, out_file):
  infile = open(in_file, 'r')
  outfile = open(out_file, 'w') 
  for item in infile:
    list = []
    for word in item.strip().split():
      word = word.strip().lower()
      if word not in list:
        list.append(word )
      else:
        outfile.write(word+' ')
    if len(list) > 0:
      outfile.write('\n')
    
repeat_words('filea.txt', 'out_file2.txt')
