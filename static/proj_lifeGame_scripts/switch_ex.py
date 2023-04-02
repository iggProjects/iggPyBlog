#!/usr/bin/python3

# https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
# https://data-flair.training/blogs/python-switch-case/ 

def week(i):
	global A
	switcher={
		0:
			'Sunday',
		1:
			'Monday'
		}
	return switcher.get(i,"Invalid day of week")

A=0
print(f"{week(1)}")
