# Lootcrawler 3.3.5a
This very simple lootcrawler is made to read the contents of a logs file containing items distributed to players through loot council. It can be connected to directly upload
loot council awards to google sheets, or to text files. It is not an addon, just a small script.

## Prerequisites
To utilise the script best, the following must be set up:
* [WowScribe v. 3.3.1](https://www.curseforge.com/wow/addons/wowscribe/files/400551)
* Google API enabled google sheets worksheet
* A loot council addon capable of announcing awards

## Setup
#### WowScribe
* Download the addon and move it to the addons folder
* Type /wowscribe add Officer
* Type /wowscribe start. Make sure wowscribe is active whenever loot counceling is done  
**NB: the lootcrawler currently only works with messages sent to officer chat**

#### Google sheets
*I recommend following John Whatson Ronney's guide [Here] (https://www.youtube.com/watch?v=ct0xvw_Z0tU) on how to set up. Follow this until around 2:31*

#### Loot council addon
##### RCLootCouncil
* Enable "Announce Awards" under Master Looter > Annoncements > Announce Awards. One of the channels must be Officer. The message should follow the pattern 
  
  "&p was awarded with &i for &r!"

#### Setting up the crawler
* Open the ```config.txt``` file
* Setup the full path to the log file. It should always be named ```WowChatLog.txt``` by WowScribe. Note that the log will be saved only after the character has logged out.
* Copy the id of your google docs sheet. For example, for the url:

  docs.google.com/spreadsheets/d/__1h2wZ32bN6mMiwR5m1TM1qd9xCD_Lbgy2eQ5bY-5bvwM__/edit#gid=0

  The bold text is the id.
* Type the name of the sheet, for example, "lootcrawler"


## Running the crawler
You can use either the precompiled .exe file, compile your own from the ```CrawlerV2.py``` file, or just run the python file itself.
The crawler will scrape officer messages matching "PLAYER awarded ITEM", and push that to the sheets along with a timestamp.
