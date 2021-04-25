file = open('C:/Users/Andreas/Documents/Loot logs/WowChatLog.txt', 'r')

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

    if 'Officer' and 'awarded' in line:
        words = line.split(' ')
        strBuilder = []
        itemString = ''
        
        try:
            date = (' '.join(words[0:2]))
            awardedTo = words[5]
            item = words[7:]
            itemString = ' '.join(item)

            outputline.append(date)
            outputline.append(awardedTo)
            outputline.append(itemString)
            
        except IndexError:
            pass
            
        if contentIsNotEmpty(outputline):
            output.append(outputline)

file.close()



outFile = open('C:/Users/Andreas/Documents/Loot logs/Log.csv','w')

for line in output:
    outFile.write(', '.join(line))
outFile.close()
#Write to out file
