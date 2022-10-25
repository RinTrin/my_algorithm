
import re

string = r"https://ai-inter1.com/python-regex/"
pattern = "https?://[^/]*"
result = re.match(pattern, string)
print(result.group())