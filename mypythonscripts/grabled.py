"""This module extract the following messages -
a) !XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI
b) IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX
(Problem 1.)
"""

# Problem - a
garbled_a = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message_a = (garbled_a[::2])[::-1]
print(message_a)

###########################################################################################
# Problem - b
garbled_b = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

print("".join(filter(lambda message: message.replace("X", ""), garbled_b)))

# Alternative
message_list = (filter(lambda x: x != "X", garbled_b))
print("".join(message_list))
