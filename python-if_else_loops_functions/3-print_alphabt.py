#!/usr/bin/python3
for i in range(26):
    if chr(97 + i) not in ('q', 'e'):
        print(f"{chr(97 + i)}", end="")
