import time
from termcolor import colored
from data import JOURNEY_IN_DAYS, COST_FOOD_HORSE_COPPER_PER_DAY, COST_FOOD_HUMAN_COPPER_PER_DAY, COST_HORSE_SILVER_PER_DAY, COST_TENT_GOLD_PER_WEEK

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
    print(f"{key}: {returnList}")
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
    pass

def getItemsValueInGold(items:list) -> float:
    pass

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

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