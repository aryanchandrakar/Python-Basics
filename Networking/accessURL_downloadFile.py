# connecting to url accessing them downloading files and socket programming and sending mails

print("------------------ACCESSING URL-------------------")
# ACCESSING URL
import urllib.request

u=input("Enter a URL: ")
try:
    url=urllib.request.urlopen(u)  # opening the url
    content=url.read()
    url.close()  # close the URL connection
    print("[+]URL saved :)")
except urllib.error.HTTPError:
    print("[-] No such URL exists, WOOPS!")
    exit()

# writing the content to file
f=open('file.html','wb')
f.write(content)
f.close()


print("\n\n------------------DOWNLOAD IMAGE-----------------")
# download image
import urllib.request
u = input("Enter a URL: ")
urllib.request.urlretrieve(u,"fotu.png")  # retrieving the image url, name to save it as
