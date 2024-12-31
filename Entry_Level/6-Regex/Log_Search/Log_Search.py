#this script is configred ot detect all instances of failed login attempts. 

result = []

def search(filename, text):
    with open(filename) as f:
        for line in f:
            if text in line:
                print(line)
                result.append(line)
search('Secure.log', 'failed') #we changed failed to nobody
