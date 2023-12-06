#!/usr/bin/python3
print("{}".format("".join([chr(i).upper() if i % 2 == 1 else chr(i).lower() for i in range(ord('z'), ord('a') - 1, -1)])))
