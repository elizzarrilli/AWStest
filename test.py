import os
import json

print("hi")

text = "hello"

if not os.path.exists("test_files"):
	os.mkdir("test_files")

f = open("test_files/test1.json.tmp", "w")
f.write(json.dumps(text))
f.close()
