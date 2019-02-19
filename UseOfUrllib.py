import urllib.request

fhand = urllib.request.urlopen('https://wiki.python.org/moin/')
for line in fhand:
    print(line.decode().strip())
