from pip._vendor import requests
import sys, pyperclip

sys.argv # ['imgd', 'https://image.com', 'name']

if len(sys.argv) > 1:
    link = sys.argv[1]
    print(link)
    name = sys.argv[2]
    url_name = True
else:
    link = pyperclip.paste()
    url_name = False

image = requests.get(link)
image.raise_for_status()

if url_name:
    imgFile = open('C:\\Users\\manth\\Downloads\\' + name + '.png', 'wb')
else:
    imgFile = open('C:\\Users\\manth\\Downloads\\image.png', 'wb')

for chunk in image.iter_content(100000):
    imgFile.write(chunk)
imgFile.close()

# if url_name:
#     imgFile = 'C:\\Users\\manth\\Downloads\\' + name + '.png'
# else:
#     imgFile = 'C:\\Users\\manth\\Downloads\\image.png'

# with open(imgFile, 'wb') as output:
#     output.write(image.content)