

##### DEPRECATEDDDDDDD ########## Update Xpaths, Dota2 patch 6.86 introduced major changes in to the game and stattrack websites
###


### DOTA MATCH STAT SCRAPER v0.31, using data from Dota2statistic.com
### still to impliment:
# find out how to scrape what hero each player was on
# scrape game date, duration and additional info if wanted (server location, match start time, whatever else you want/can find
# look at some stat websites for some inspiration and some additional stats to look at
# consider ranking players from 1 to 10, based on ingame metrics, can help rank players' performance relative to others in that game without using benchmark values for
# arbitrary rankings of good gpm, bad gpm, etc, every game is different therefore a 1 - 10 ranking SEEMS better than trying to slot performances in to ceratain levels
# of quality?
# I think you can scrape data from multiple pages by giving "requests.get" multiple variables, from multiple website sources
### Impliment named tuples, call the apprpriate return from radDireTeams() in to all of the stat defs
### NATHAN ROANE 2016

###print len(data) gives length of entire data collection, helps with index calculations

from lxml import html
import requests       ### Not a standard python library, download from here https://bootstrap.pypa.io/get-pip.py  or with pip installed 'pip install requests'

def radDireTeams():

    page = requests.get("http://dota2statistic.com/index.php/matches/981781457")

    tree = html.fromstring(page.text)
    players = tree.xpath('//a[@class="profile"]/text()')     #This will create a list of all 10 players in the match, in the colour order


    data = tree.xpath('//td[@class="stat"]/text()') #creates a list of every stat found in the table, one after the other all together. Finding the correct indices and incrimenting by 12 yields the same stat for the next player    

    

    radiantPlayers = players[:5] #creates list of radiant players using first 5 indices of "players"
    direPlayers = players[5:]    #creates list of dire players

    radiantTeam = tree.xpath('//a[@href="/index.php/teams/1883502"]/text()')   ### checks to see which team is playing on the Radiant side
    direTeam = tree.xpath('//a[@href="/index.php/teams/1333179"]/text()')

    winningTeam = tree.xpath('//h1[@style="text-align: center;"]/text()')       #this grabs either "Radiant Victory" or "Dire Victory"


    print ("Radiant players are " + str(radiantTeam) + ' '), radiantPlayers
    print ("Dire players are " + str(direTeam) + ' '), direPlayers
    print ("\n")



    if radiantTeam == winningTeam:
        print winningTeam[0] + ", ", radiantTeam
        print ("\n")
        
    else:
        print winningTeam[0] + ", ", direTeam
        print ("\n")

    return (tree, page, data)
    
def rLevelsOut():

    data = radDireTeams()
    radLevelStart = 12
    radLevels = []

    for i in range (0,5):
                                                ### loop that incriments every starting point (index) by 12, resulting in retrieving the same stat for the next player
        radLevels.append(data[radLevelStart])
        radLevelStart += 12

    return radLevels


def dLevelsOut():

    data = radDireTeams()
    direLevelStart    = 96
    direLevels = []

    for i in range (0,5):
        direLevels.append(data[direLevelStart])
        direLevelStart += 12

    return direLevels


def rKillsOut():
    data = radDireTeams()
    radKillsStart = 13 #each new stat's beginning index is just +1 from the previous stat's index, respective of teams. 
    radKills = []

    for i in range (0,5):
        radKills.append(data[radKillsStart])   ###Kills
        radKillsStart += 12

    return radKills


def dKillsOut():
    data = radDireTeams()
    direKillsStart = 97
    direKills = []

    for i in range (0,5):
        direKills.append(data[direKillsStart])
        direKillsStart += 12

    return direKills

def rDeathsOut():
    data = radDireTeams()
    radDeathsStart = 14
    radDeaths = []

    for i in range (0,5):
        radDeaths.append(data[radDeathsStart])   ###Deaths
        radDeathsStart += 12

    return radDeaths


def dDeathsOut():
    data = radDireTeams()
    direDeathsStart = 98
    direDeaths = []
        
    for i in range (0,5):
        direDeaths.append(data[direDeathsStart])
        direDeathsStart += 12

    return direDeaths


def rAssistsOut():
    data = radDireTeams()
    radAssistsStart = 15
    radAssists = []
    
    for i in range (0,5):
        radAssists.append(data[radAssistsStart])   ###Assists
        radAssistsStart += 12

    return radAssists


def dAssistsOut():
    data = radDireTeams()
    direAssistsStart = 99
    direAssists = []

    
    for i in range (0,5):
        direAssists.append(data[direAssistsStart])
        direAssistsStart += 12

    return direAssists


def rGoldOut():
    data = radDireTeams()
    radGoldStart = 16
    radGold = []
        
    for i in range (0,5):
        radGold.append(data[radGoldStart])   ###Ending Gold
        radGoldStart += 12

    return radGold


def dGoldOut():
    data = radDireTeams() 
    direGoldStart = 100
    direGold = []

    for i in range (0,5):
        direGold.append(data[direGoldStart])
        direGoldStart += 12

    return direGold


def rLasthitsOut():
    data = radDireTeams()
    radLasthitsStart = 17
    radLasthits = []

    for i in range (0,5):
        radLasthits.append(data[radLasthitsStart])   ###Lasthits
        radLasthitsStart += 12

    return radLasthits


def dLasthitsOut():
    data = radDireTeams()
    direLasthitsStart = 101
    direLasthits = []
        
    for i in range (0,5):
        direLasthits.append(data[direLasthitsStart])
        direLasthitsStart += 12

    return direLasthits


def rDeniesOut():
    data = radDireTeams()
    radDeniesStart = 18
    radDenies = []
        
    for i in range (0,5):
        radDenies.append(data[radDeniesStart])  ###Denies
        radDeniesStart += 12

    return radDenies


def dDeniesOut():
    data = radDireTeams()
    direDeniesStart = 102
    direDenies = []

    for i in range (0,5):
        direDenies.append(data[direDeniesStart])
        direDeniesStart += 12

    return direDenies


def rGPMOut():
    data = radDireTeams()
    radGPMStart = 19
    radGPM = []
    
    for i in range (0,5):
        radGPM.append(data[radGPMStart])   ####GPM
        radGPMStart += 12

    return radGPM


def dGPMOut():
    data = radDireTeams()
    direGPMStart = 103
    direGPM = []
    
    for i in range (0,5):
        direGPM.append(data[direGPMStart])
        direGPMStart += 12

    return direGPM


def rXPMOut():
    data = radDireTeams()
    radXPMStart = 20
    radXPM = []
        
    for i in range (0,5):
        radXPM.append(data[radXPMStart])   ###XPM
        radXPMStart += 12

    return radXPM


def dXPMOut():
    data = radDireTeams()
    direXPMStart = 104
    direXPM = []

    for i in range (0,5):
        direXPM.append(data[direXPMStart])
        direXPMStart += 12

    return direXPM


def rTowerDmgOut():
    data = radDireTeams()
    radTowerDamageStart = 21
    radTowerDamage = []

    for i in range (0,5):
        radTowerDamage.append(data[radTowerDamageStart])
        radTowerDamageStart += 12

    return radTowerDamage


def dTowerDmgOut():
    data = radDireTeams()
    direTowerDamageStart = 105
    direTowerDamage = []

    for i in range (0,5):
        direTowerDamage.append(data[direTowerDamageStart])
        direTowerDamageStart += 12

    return direTowerDamage


def rHeroDmgOut():
    data = radDireTeams()
    radHeroDamageStart = 22
    radHeroDamage = []

    for i in range (0,5):
        radHeroDamage.append(data[radHeroDamageStart])
        radHeroDamageStart += 12

    return radHeroDamage


def dHeroDmgOut():
    data = radDireTeams()
    direHeroDamageStart = 106
    direHeroDamage = []

    for i in range (0,5):
        direHeroDamage.append(data[direHeroDamageStart])
        direHeroDamageStart += 12

    return direHeroDamage    


def rHealingOut():
    data = radDireTeams()
    radHealingStart = 23
    radHealing = []
    
    for i in range (0,5):
        radHealing.append(data[radHealingStart])
        radHealingStart += 12

    return radHealing


def dHealingOut():
    data = radDireTeams()  
    direHealingStart = 107
    direHealing = []
    
    for i in range (0,5):
        direHealing.append(data[direHealingStart])
        direHealingStart += 12

    return direHealing

    
def statReadout():

    radLevelsOut = rLevelsOut()
    direLevelsOut = dLevelsOut()
    radKillsOut = rKillsOut()
    direKillsOut = dKillsOut()
    radDeathsOut = rDeathsOut()
    direDeathsOut = dDeathsOut()
    radAssistsOut = rAssistsOut()
    direAssistsOut = dAssistsOut()
    radGoldOut = rGoldOut()
    direGoldOut = dGoldOut()
    radLasthitsOut = rLasthitsOut() 
    direLasthitsOut = dLasthitsOut() 
    radDeniesOut = rDeniesOut()
    direDeniesOut = dDeniesOut() 
    radGPMOut = rGPMOut()
    direGPMOut = dGPMOut()
    radXPMOut = rXPMOut()
    direXPMOut = dXPMOut()
    radTowerDamageOut = rTowerDmgOut()
    direTowerDamageOut = dTowerDmgOut()
    radHeroDamageOut = rHeroDmgOut()
    direHeroDamageOut = dHeroDmgOut()
    radHealingOut = rHealingOut()
    direHealingOut = dHealingOut()
    
    

    print "Radiant hero levels     : ", radLevelsOut
    print "Dire hero levels        : ", direLevelsOut
    print ("\n")
    print "Radiant hero kills      : ", radKillsOut
    print "Dire hero kills         : ", direKillsOut
    print("\n")
    print "Radiant hero deaths     : ", radDeathsOut
    print "Dire hero deaths        : ", direDeathsOut
    print("\n")
    print "Radiant hero assists    : ", radAssistsOut
    print "Dire hero assists       : ", direAssistsOut
    print("\n")
    print "Radiant hero gold       : ", radGoldOut
    print "Dire hero gold          : ", direGoldOut
    print("\n")
    print "Radiant hero last hits  : ", radLasthitsOut
    print "Dire hero last hits     : ", direLasthitsOut
    print("\n")  
    print "Radiant hero denies     : ", radDeniesOut
    print "Dire hero denies        : ", direDeniesOut
    print("\n")
    print "Radiant hero GPM        : ", radGPMOut
    print "Dire hero GPM           : ", direGPMOut
    print("\n")
    print "Radiant hero XPM        : ", radXPMOut
    print "Dire hero XPM           : ", direXPMOut
    print("\n")
    print "Radiant hero tower dmg  : ", radTowerDamageOut
    print "Dire hero tower dmg     : ", direTowerDamageOut
    print("\n")
    print "Radiant hero damage     : ", radHeroDamageOut
    print "Dire hero damage        : ", direHeroDamageOut
    print("\n")
    print "Radiant hero healing    : ", radHealingOut
    print "Dire hero healing       : ", direHealingOut


radDireTeams()

statReadout()
