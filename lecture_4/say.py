# Fourth Example

import sys # to access command line arguments

from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])

# Third Example

# import sys # to access command line arguments
# 
# from sayings import hello
# 
# if len(sys.argv) == 2:
#     hello(sys.argv[1])
# 
# # python3 say.py joseph
# 
# # this demo is showing an error with the whole main thing
# # if __name__ == "__main__":
# # look in sayings.py
# 
# # came back to this file towards the end of the lecture
# # to demo the import of a file not part of a public package
# # or part of the standard libraries delivered with python

# Second Example

# import cowsay
# import sys
# 
# if len(sys.argv) == 2:
#     cowsay.trex("hello, " + sys.argv[1])

# First Example

# import cowsay
# import sys
# 
# if len(sys.argv) == 2:
#     cowsay.cow("hello, " + sys.argv[1])

# setup of this demo required
# % python3 -m pip install --break-system-packages cowsay
# Collecting cowsay
#   Downloading cowsay-6.1-py3-none-any.whl.metadata (5.6 kB)
# Downloading cowsay-6.1-py3-none-any.whl (25 kB)
# Installing collected packages: cowsay
# Successfully installed cowsay-6.1
# chatgpt had to walk me through this - I'm using Homebrew which
# I am still very new at using