#search for log entries based on two different keywords. this allows you to create more tailored seaerches that return information that is more of a direct match to what you are looking for. 

result = []

def search(filename, text, text2):
    with open(filename) as f:
        for line in f:
            if text in line and text2 in line:
                print(line)
                result.append(line)

search("Secure.log", "Failed", "3187")