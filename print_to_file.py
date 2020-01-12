from __future__ import print_function
def print_to_file(source,fn):
   ''' print the source to the file fn'''
   output_file = open(fn, 'w')
   print(source,file=output_file)
   output_file.close()

   
