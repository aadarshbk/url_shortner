import pyshortners
url= input('Enter the url:')
def shortenurl(url):
    s=pyshortners.Shortners()
    print(s.tinyurl.short(url))
    shortenurl(url)
