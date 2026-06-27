# Sixth Example

import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username: ", matches.group(1)) # notice this is now group(1)

# tighten up the code using the walrus operator
# (?:) is the non-capturing symbol this removes it from the group returned from .search

# r"^https?://(?:wwww\.)?twitter\.com/(.+)$"
# Match a Twitter URL that:
# - starts at the beginning of the text,
# - contains "http://" or "https://",
# - may optionally include "www.",
# - is followed by "twitter.com/",
# - captures everything after the slash,
# - and ends at the end of the text.

# | Regex           | English                                                                                        |
# | --------------- | ---------------------------------------------------------------------------------------------- |
# | `r"..."`        | Treat backslashes literally (raw string).                                                      |
# | `^`             | Start at the beginning of the text.                                                            |
# | `https?://`     | Match `http://` or `https://`.                                                                 |
# | `(?:www\.)?`    | Optionally match `www.` (without capturing it).                                                |
# | `twitter\.com/` | Match the literal text `twitter.com/`.                                                         |
# | `(.+)`          | Capture one or more characters (this is typically the username or whatever follows the slash). |
# | `$`             | Require that this is the end of the text.                                                      |


# Sixth Example

# import re
# 
# url = input("URL: ").strip()
# 
# matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE) # (www\.) is group(1) and (.+) is group(2)
# if matches:
#     print(f"Username: ", matches.group(2))
# 
# # needs conditional logic to make sure we getting the URL we're targeting
# # remember the grouping special symbols in RegEx


# Fifth Example - recommended approach is to take small steps while building a RegEx
# # don't try to come up with a full solution in one step
# 
# import re
# 
# url = input("URL: ").strip()
# 
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")
# 
# # Match the beginning of a Twitter URL.
# # The URL may optionally start with "http://" or "https://",
# # may optionally include "www.",
# # and must then contain "twitter.com/".
# 
# # | Regex           | English                                      |
# # | --------------- | -------------------------------------------- |
# # | `r"..."`        | Treat backslashes literally (raw string).    |
# # | `^`             | Start matching at the beginning of the text. |
# # | `(https?://)?`  | Optionally match `http://` or `https://`.    |
# # | `(www\.)?`      | Optionally match `www.`.                     |
# # | `twitter\.com/` | Match the literal text `twitter.com/`.       |



# Fourth Example - introduce .sub() in re library

# import re
# 
# url = input("URL: ").strip()
# 
# username = re.sub(r"https://twitter.com/", "", url) # substitute
# print(f"Username: {username}")
# 
# 
# # https://docs.python.org/3.14/library/re.html
# # re.sub(pattern, repl, string, count=0, flag=0)

# Third Example

# url = input("URL: ").strip()
# 
# username = url.removeprefix("https://twitter.com/") # .removeprefix 
# print(f"Username: {username}")
# 
# # this is illustrating that there are many different functions that can be used
# # to address this problem... but RegEx just do this pattern matching better
# # don't spend all day writing conditionals


# Second Example - introduce the replace function

# url = input("URL: ").strip()
# 
# username = url.replace("https://twitter.com/", "") # first argument is the find second argument is replace
# print(f"Username: {username}")


# First Example

# url = input("URL: ").strip()
# print(url)

# set the table for the demo
