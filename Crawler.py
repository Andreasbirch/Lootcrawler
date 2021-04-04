
file = open('WowChatLog.txt', 'r')

def contentIsNotEmpty(ls):
    if(ls == []):
        return False
    
    for elem in ls:
        if elem == '':
            return False
    return True

output = []

for cnt, line in enumerate(file):
    outputline = []


    if '-STARTED-' in line:
        currLine = next(file)
        words = currLine.split(' ')
        
        date = (' '.join(words[0:2]))
        
        strBuilder = []
            
        for word in words[::-1]:
            if word == 'item:':
                break
            else:
                if word != '\n':    
                    strBuilder.append(word)
        currItem = strBuilder.reverse()
        
        item = (' '.join(strBuilder))[:-1]
        
        #Should be more robust, but might work
        nextLine = next(file).split(' ')
        awardedTo = ''
        if nextLine[6] == 'awarded':    
            awardedTo = nextLine[5]
    
    
        outputline.append(date)
        outputline.append(item)
        outputline.append(awardedTo)
        
    
    if contentIsNotEmpty(outputline):
        output.append(outputline)

file.close()




outFile = open('Lootlog.csv','w')

for line in output:
    outFile.write(', '.join(line))
    outFile.write('\n')
outFile.close()
#Write to out file
