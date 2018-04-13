from sys import argv

script, filename = argv

txt = open(filename)

print " The file read here is %r" %filename
print txt.read()

txt.close()

print "Type the filename again"
file_again = raw_input( ">" )

txt_again = open(file_again)

print txt_again.read(3)

txt_again.close()

