import pyshorteners
link=input("Enter The Link")
short=pyshorteners.Shortener()
x=short.tinyurl.short(link)
print(x)
