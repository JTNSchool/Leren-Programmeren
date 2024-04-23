import time
from termcolor import colored
from data import JOURNEY_IN_DAYS, COST_FOOD_HORSE_COPPER_PER_DAY, COST_FOOD_HUMAN_COPPER_PER_DAY, COST_HORSE_SILVER_PER_DAY, COST_TENT_GOLD_PER_WEEK, COST_INN_HUMAN_SILVER_PER_NIGHT, COST_INN_HORSE_COPPER_PER_NIGHT

##################### O03 #####################

def copper2silver(amount:int) -> float:
    return round(amount / 10,2)

def silver2gold(amount:int) -> float:
    return round(amount / 5,2)

def copper2gold(amount:int) -> float:
    return round(amount / 50,2)

def platinum2gold(amount:int) -> float:
    return round(amount * 25,2)

def getPersonCashInGold(personCash:dict) -> float:
    total = 0
    if "copper" in personCash:
        total += copper2gold(personCash['copper'])
    if "silver" in personCash:
        total += silver2gold(personCash['silver'])
    if "platinum" in personCash:
        total += platinum2gold(personCash['platinum'])
    if "gold" in personCash:
        total += personCash['gold']
    return round(total, 2)

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    cost = copper2gold(JOURNEY_IN_DAYS * ((people * COST_FOOD_HUMAN_COPPER_PER_DAY) + (horses * COST_FOOD_HORSE_COPPER_PER_DAY)))
    return round(cost, 2)

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    returnList = []
    for ListLoop in list:
        if key in ListLoop:
            if ListLoop[key] == value:
                returnList.append(ListLoop)
    return returnList

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, "adventuring", True)

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, "shareWith", True)

def getAdventuringFriends(friends:list) -> list:
    adventuringFriends= getAdventuringPeople(friends)
    SharingFriends = getShareWithFriends(adventuringFriends)
    return SharingFriends

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    if people % 2 == 0:
        return int(people / 2)
    else:
        return int(people / 2) + 1

def getNumberOfTentsNeeded(people:int) -> int:
    if people % 3 == 0:
        return int(people / 3)
    else:
        return int(people / 3) + 1

def getTotalRentalCost(horses:int, tents:int) -> float:
    HorseCost = silver2gold(horses * COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS)
    TentCost = tents * COST_TENT_GOLD_PER_WEEK * int(JOURNEY_IN_DAYS / 7 + 1)
    return HorseCost + TentCost

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    string = ""
    loop = 0
    for item in items:
        loop += 1
        string = string + f'{item["amount"]}{item["unit"]} {item["name"]}'
        if len(items)-1 == loop:
            string = string + " & "
        elif len(items) != loop:
            string = string + ", "
    return string

def getItemsValueInGold(items:list) -> float:
    coins = {
        'platinum' : 0,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
    
    for item in items:
        amount = item["price"]["amount"] * item["amount"]
        type = item["price"]["type"]
        #if type in coins:
        coins[type] += amount
    return getPersonCashInGold(coins)

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    total = 0
    for person in people:
        total += getPersonCashInGold(person['cash'])
    return total

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    Intrested = []
    for investor in investors:
        if investor["profitReturn"] < 10:
            Intrested.append(investor)
    return Intrested

def getAdventuringInvestors(investors:list) -> list:
    return getFromListByKeyIs(getInterestingInvestors(investors), "adventuring", True)

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    GoldCost = 0

    if gear  == []:
        return float(GoldCost)
    investors = getAdventuringInvestors(getInterestingInvestors(investors))
    invenstorcount = len(investors)

    GoldCost += getJourneyFoodCostsInGold(invenstorcount, invenstorcount)

    GoldCost += getItemsValueInGold(gear * invenstorcount)

    GoldCost += getTotalRentalCost(invenstorcount, invenstorcount)

    return GoldCost

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    CostPeople = silver2gold(people * COST_INN_HUMAN_SILVER_PER_NIGHT)
    CostHorse = copper2gold(horses * COST_INN_HORSE_COPPER_PER_NIGHT)
    total = CostHorse + CostPeople
    nachten = leftoverGold // total
    return int(nachten)
    

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    CostPeople = silver2gold(people * COST_INN_HUMAN_SILVER_PER_NIGHT)
    CostHorse = copper2gold(horses * COST_INN_HORSE_COPPER_PER_NIGHT)
    total = CostHorse + CostPeople
    return round(nightsInInn * total, 2)

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    investors_cut = []
    investors = (getInterestingInvestors(investors))
    one_percent_of_gold = float(profitGold / 100)
    for investor in investors:
        investors_cut.append(round(one_percent_of_gold * investor['profitReturn'], 2))
    return investors_cut


def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    LeftOver = profitGold
    for cut in investorsCuts:
       LeftOver -= cut
    ret = LeftOver / fellowship
    if ret < 0:
        ret = 0.0
    return round(ret,2)


#####  ################ O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []
    print(profitGold)
    adventuringFriends = getAdventuringFriends(friends)
    interestingInvestors = getInterestingInvestors(investors)
    adventuringInvestors = getAdventuringInvestors(interestingInvestors)
    investorsCuts = getInvestorsCuts(profitGold, investors)
    print(investorsCuts)
    goldCut = getAdventurerCut(profitGold, investorsCuts, len(people))

    for person in people:
        if person in adventuringInvestors:
            reward = ((profitGold / 100) * person['profitReturn']) + getPersonCashInGold(person['cash']) + goldCut
            profitGold -= reward
        elif person in interestingInvestors:
            reward = ((profitGold / 100) * person['profitReturn']) + getPersonCashInGold(person['cash'])
            profitGold -= reward

    for person in people:
        if person in [mainCharacter]:
            reward = goldCut + getPersonCashInGold(person['cash']) + 10 * len(friends)

        elif person in adventuringFriends:
            reward = goldCut + getPersonCashInGold(person['cash']) - 10

        

        earnings.append({
                'name'   : person['name'],
                'start'  : getPersonCashInGold(person['cash']),
                'end'    : reward
            })
    return earnings

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()