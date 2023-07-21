#=======================================================================
rosters = {
    'Nur_____': {'team': 'Nur_____',
                 'draft': 1,
                 'QB': 'Jackson, Lamar',
                 'RB': 'RB1',
                 'WR1': 'WR24',
                 'WR2': 'WR25',
                 'WR3': 'Metcalf, DK',
                 'TE': 'TE2'
                 },
    'Front AI': {'team': 'Front AI',
                 'draft': 2,
                 'QB': 'QB1',
                 'RB': 'RB4',
                 'WR1': 'Lamb, CeeDee',
                 'WR2': 'Moore, D.J.',
                 'WR3': 'WR30',
                 'TE': 'TE3'
                 },
    'Kalif___': {'team': 'Kalif___',
                 'draft': 3,
                 'QB': 'QB6',
                 'RB': 'RB2',
                 'WR1': 'WR11',
                 'WR2': 'WR23',
                 'WR3': 'WR26',
                 'TE': 'TE11'
                 },
    'Road way': {'team': 'Road way',
                 'draft': 4,
                 'QB': 'QB10',
                 'RB': 'Cook, Dalvin',
                 'WR1': 'WR1',
                 'WR2': 'WR12',
                 'WR3': 'WR22',
                 'TE': 'Kelce, Travis'
                 },
    'DDD_____': {'team': 'DDD_____',
                 'draft': 5,
                 'QB': 'Herbert, Justin',
                 'RB': 'RB9',
                 'WR1': 'WR13',
                 'WR2': 'WR21',
                 'WR3': 'Johnson, Diontae',
                 'TE': 'TE1'
                 },
    'lUser___': {'team': 'lUser___',
                 'draft': 6,
                 'QB': 'Mahomes, Patrick',
                 'RB': 'RB3',
                 'WR1': 'WR14',
                 'WR2': 'Pittman, Michael',
                 'WR3': 'McLaurin, Terry',
                 'TE': 'TE10'
                 },
    'Fox_____': {'team': 'Fox_____',
                 'draft': 7,
                 'QB': 'QB2',
                 'RB': 'RB7',
                 'WR1': 'WR10',
                 'WR2': 'Hill, Tyreek',
                 'WR3': 'WR29',
                 'TE': 'TE4'
                 },
    'Rex_____': {'team': 'Rex_____',
                 'draft': 8,
                 'QB': 'QB5',
                 'RB': 'McCaffrey, Christian',
                 'WR1': 'WR15',
                 'WR2': 'WR20',
                 'WR3': 'WR27',
                 'TE': 'TE9'
                 },
    'Get lost': {'team': 'Get lost',
                 'draft': 9,
                 'QB': 'Allen, Josh',
                 'RB': 'Mixon, Joe',
                 'WR1': 'Adams, Davante',
                 'WR2': 'Evans, Mike',
                 'WR3': 'Higgins, Tee',
                 'TE': 'Pitts, Kyle'
                 },
    'mimimi__': {'team': 'mimimi__',
                 'draft': 10,
                 'QB': 'QB3',
                 'RB': 'Henry, Derrick',
                 'WR1': 'WR9',
                 'WR2': 'WR16',
                 'WR3': 'WR28',
                 'TE': 'TE8'
                 },
    'Robus___': {'team': 'Robus___',
                 'draft': 11,
                 'QB': 'QB4',
                 'RB': 'RB5',
                 'WR1': 'WR5',
                 'WR2': 'Brown, A.J.',
                 'WR3': 'Waddle, Jaylen',
                 'TE': 'Waller, Darren'
                 },
    'Commi___': {'team': 'Commi___',
                 'draft': 12,
                 'QB': 'QB9',
                 'RB': 'Ekeler, Austin',
                 'WR1': 'WR2',
                 'WR2': 'WR6',
                 'WR3': 'Samuel, Deebo',
                 'TE': 'TE5'
                 },
    'Toroid__': {'team': 'Toroid__',
                 'draft': 13,
                 'QB': 'Murray, Kyler',
                 'RB': 'Taylor, Jonathan',
                 'WR1': 'Jefferson, Justin',
                 'WR2': 'Allen, Keenan',
                 'WR3': 'Sutton, Courtland',
                 'TE': 'Kittle, George'
                 },
    'GHOSH!__': {'team': 'GHOSH!__',
                 'draft': 14,
                 'QB': 'QB8',
                 'RB': 'RB6',
                 'WR1': 'WR3',
                 'WR2': 'WR7',
                 'WR3': 'WR17',
                 'TE': 'TE7'
                 },
    'Blue sky': {'team': 'Blue sky',
                 'draft': 15,
                 'QB': 'Hurts, Jalen',
                 'RB': 'Harris, Najee',
                 'WR1': 'Kupp, Cooper',
                 'WR2': 'Diggs, Stefon',
                 'WR3': 'WR19',
                 'TE': 'Andrews, Mark'
                 },
    'Amirai__': {'team': 'Amirai__',
                 'draft': 16,
                 'QB': 'QB7',
                 'RB': 'RB8',
                 'WR1': 'Chase, Ja\'Marr',
                 'WR2': 'WR4',
                 'WR3': 'WR18',
                 'TE': 'TE6'
                 }
    }
#=======================================================================
def check_draft():
    status = True
    rpos = ["QB","RB","TE","WR1","WR2","WR3"]
    all_lst = []
    for k in rosters.keys():
        for p in rpos:
            if rosters[k][p] in all_lst:
                status = False
                print("Double "+ rosters[k][p])
            all_lst.append(rosters[k][p])
    return status
    
def get_team_by_draft( draft ):
    for k in rosters.keys():
        if rosters[k]["draft"] == draft:
            return rosters[k]
    return None

def get_team_by_name( name ):
    for k in rosters.keys():
        if rosters[k]["team"] == name:
            return rosters[k]
    return None

def get_team( token, key="draft" ):
    if key in ["draft","id","num","order","number"]:
        return get_team_by_draft(token)
    if key in ["name","team"]:
        return get_team_by_name(token)
    return None
#=======================================================================

season = {
    "regular":{
        "week 1":{
            "game 1": {
                "away": 1,
                "home": 5,
                "score":""
                },
            "game 2": {
                "away": 9,
                "home": 13,
                "score":""
                },
            "game 3": {
                "away": 2,
                "home": 6,
                "score":""
                },
            "game 4": {
                "away": 10,
                "home": 14,
                "score":""
                },
            "game 5": {
                "away": 3,
                "home": 7,
                "score":""
                },
            "game 6": {
                "away": 11,
                "home": 15,
                "score":""
                },
            "game 7": {
                "away": 4,
                "home": 8,
                "score":""
                },
            "game 8": {
                "away": 12,
                "home": 16,
                "score":""
                }
            },
        "week 2":{
            "game 1": {
                "away": 1,
                "home": 9,
                "score":""
                },
            "game 2": {
                "away": 5,
                "home": 13,
                "score":""
                },
            "game 3": {
                "away": 2,
                "home": 10,
                "score":""
                },
            "game 4": {
                "away": 6,
                "home": 14,
                "score":""
                },
            "game 5": {
                "away": 3,
                "home": 11,
                "score":""
                },
            "game 6": {
                "away": 7,
                "home": 15,
                "score":""
                },
            "game 7": {
                "away": 4,
                "home": 12,
                "score":""
                },
            "game 8": {
                "away": 8,
                "home": 16,
                "score":""
                }
            },
        "week 3":{
            "game 1": {
                "away": 1,
                "home": 13,
                "score":""
                },
            "game 2": {
                "away": 9,
                "home": 5,
                "score":""
                },
            "game 3": {
                "away": 2,
                "home": 14,
                "score":""
                },
            "game 4": {
                "away": 10,
                "home": 6,
                "score":""
                },
            "game 5": {
                "away": 3,
                "home": 15,
                "score":""
                },
            "game 6": {
                "away": 11,
                "home": 7,
                "score":""
                },
            "game 7": {
                "away": 4,
                "home": 16,
                "score":""
                },
            "game 8": {
                "away": 12,
                "home": 8,
                "score":""
                }
            },
        "week 4":{
            "game 1": {
                "away": 1,
                "home": 2,
                "score":""
                },
            "game 2": {
                "away": 5,
                "home": 6,
                "score":""
                },
            "game 3": {
                "away": 9,
                "home": 10,
                "score":""
                },
            "game 4": {
                "away": 13,
                "home": 14,
                "score":""
                },
            "game 5": {
                "away": 3,
                "home": 4,
                "score":""
                },
            "game 6": {
                "away": 7,
                "home": 8,
                "score":""
                },
            "game 7": {
                "away": 11,
                "home": 12,
                "score":""
                },
            "game 8": {
                "away": 15,
                "home": 16,
                "score":""
                }
            },
        "week 5":{
            "game 1": {
                "away": 1,
                "home": 14,
                "score":""
                },
            "game 2": {
                "away": 5,
                "home": 10,
                "score":""
                },
            "game 3": {
                "away": 9,
                "home": 6,
                "score":""
                },
            "game 4": {
                "away": 13,
                "home": 2,
                "score":""
                },
            "game 5": {
                "away": 3,
                "home": 16,
                "score":""
                },
            "game 6": {
                "away": 7,
                "home": 12,
                "score":""
                },
            "game 7": {
                "away": 11,
                "home": 8,
                "score":""
                },
            "game 8": {
                "away": 15,
                "home": 4,
                "score":""
                }
            },
        "week 6":{
            "game 1": {
                "away": 1,
                "home": 7,
                "score":""
                },
            "game 2": {
                "away": 2,
                "home": 8,
                "score":""
                },
            "game 3": {
                "away": 3,
                "home": 5,
                "score":""
                },
            "game 4": {
                "away": 4,
                "home": 6,
                "score":""
                },
            "game 5": {
                "away": 9,
                "home": 15,
                "score":""
                },
            "game 6": {
                "away": 10,
                "home": 16,
                "score":""
                },
            "game 7": {
                "away": 11,
                "home": 13,
                "score":""
                },
            "game 8": {
                "away": 12,
                "home": 14,
                "score":""
                }
            },
        "week 7":{
            "game 1": {
                "away": 1,
                "home": 3,
                "score":""
                },
            "game 2": {
                "away": 5,
                "home": 7,
                "score":""
                },
            "game 3": {
                "away": 9,
                "home": 11,
                "score":""
                },
            "game 4": {
                "away": 13,
                "home": 15,
                "score":""
                },
            "game 5": {
                "away": 2,
                "home": 4,
                "score":""
                },
            "game 6": {
                "away": 6,
                "home": 8,
                "score":""
                },
            "game 7": {
                "away": 10,
                "home": 12,
                "score":""
                },
            "game 8": {
                "away": 14,
                "home": 16,
                "score":""
                }
            },
        "week 8":{
            "game 1": {
                "away": 1,
                "home": 10,
                "score":""
                },
            "game 2": {
                "away": 5,
                "home": 14,
                "score":""
                },
            "game 3": {
                "away": 9,
                "home": 2,
                "score":""
                },
            "game 4": {
                "away": 13,
                "home": 6,
                "score":""
                },
            "game 5": {
                "away": 3,
                "home": 12,
                "score":""
                },
            "game 6": {
                "away": 7,
                "home": 16,
                "score":""
                },
            "game 7": {
                "away": 11,
                "home": 4,
                "score":""
                },
            "game 8": {
                "away": 15,
                "home": 8,
                "score":""
                }
            },
        "week 9":{
            "game 1": {
                "away": 1,
                "home": 8,
                "score":""
                },
            "game 2": {
                "away": 2,
                "home": 7,
                "score":""
                },
            "game 3": {
                "away": 4,
                "home": 5,
                "score":""
                },
            "game 4": {
                "away": 3,
                "home": 6,
                "score":""
                },
            "game 5": {
                "away": 9,
                "home": 16,
                "score":""
                },
            "game 6": {
                "away": 10,
                "home": 15,
                "score":""
                },
            "game 7": {
                "away": 12,
                "home": 13,
                "score":""
                },
            "game 8": {
                "away": 11,
                "home": 14,
                "score":""
                }
            },
        "week 10":{
            "game 1": {
                "away": 1,
                "home": 4,
                "score":""
                },
            "game 2": {
                "away": 5,
                "home": 8,
                "score":""
                },
            "game 3": {
                "away": 9,
                "home": 12,
                "score":""
                },
            "game 4": {
                "away": 13,
                "home": 16,
                "score":""
                },
            "game 5": {
                "away": 3,
                "home": 2,
                "score":""
                },
            "game 6": {
                "away": 7,
                "home": 6,
                "score":""
                },
            "game 7": {
                "away": 11,
                "home": 10,
                "score":""
                },
            "game 8": {
                "away": 15,
                "home": 14,
                "score":""
                }
            },
        "week 11":{
            "game 1": {
                "away": 1,
                "home": 6,
                "score":""
                },
            "game 2": {
                "away": 5,
                "home": 2,
                "score":""
                },
            "game 3": {
                "away": 9,
                "home": 14,
                "score":""
                },
            "game 4": {
                "away": 13,
                "home": 10,
                "score":""
                },
            "game 5": {
                "away": 3,
                "home": 8,
                "score":""
                },
            "game 6": {
                "away": 7,
                "home": 4,
                "score":""
                },
            "game 7": {
                "away": 11,
                "home": 16,
                "score":""
                },
            "game 8": {
                "away": 15,
                "home": 12,
                "score":""
                }
            },
        "week 12":{
            "game 1": {
                "away": 1,
                "home": 5,
                "score":""
                },
            "game 2": {
                "away": 9,
                "home": 13,
                "score":""
                },
            "game 3": {
                "away": 2,
                "home": 6,
                "score":""
                },
            "game 4": {
                "away": 10,
                "home": 14,
                "score":""
                },
            "game 5": {
                "away": 3,
                "home": 7,
                "score":""
                },
            "game 6": {
                "away": 11,
                "home": 15,
                "score":""
                },
            "game 7": {
                "away": 4,
                "home": 8,
                "score":""
                },
            "game 8": {
                "away": 12,
                "home": 16,
                "score":""
                }
            },
        "week 13":{
            "game 1": {
                "away": 1,
                "home": 9,
                "score":""
                },
            "game 2": {
                "away": 5,
                "home": 13,
                "score":""
                },
            "game 3": {
                "away": 2,
                "home": 10,
                "score":""
                },
            "game 4": {
                "away": 6,
                "home": 14,
                "score":""
                },
            "game 5": {
                "away": 3,
                "home": 11,
                "score":""
                },
            "game 6": {
                "away": 7,
                "home": 15,
                "score":""
                },
            "game 7": {
                "away": 4,
                "home": 12,
                "score":""
                },
            "game 8": {
                "away": 8,
                "home": 16,
                "score":""
                }
            },
        "week 14":{
            "game 1": {
                "away": 1,
                "home": 13,
                "score":""
                },
            "game 2": {
                "away": 9,
                "home": 5,
                "score":""
                },
            "game 3": {
                "away": 2,
                "home": 14,
                "score":""
                },
            "game 4": {
                "away": 10,
                "home": 6,
                "score":""
                },
            "game 5": {
                "away": 3,
                "home": 15,
                "score":""
                },
            "game 6": {
                "away": 11,
                "home": 7,
                "score":""
                },
            "game 7": {
                "away": 4,
                "home": 16,
                "score":""
                },
            "game 8": {
                "away": 12,
                "home": 8,
                "score":""
                }
            }
        },
    "playoff":{
        "quaterfinals":{
            "A1": {
                "away": 0,
                "home": 0,
                "score":""
                },
            "A2": {
                "away": 0,
                "home": 0,
                "score":""
                },
            "B1": {
                "away": 0,
                "home": 0,
                "score":""
                },
            "B2": {
                "away": 0,
                "home": 0,
                "score":""
                }
            },
        "semifinals":{
            "A": {
                "away": 0,
                "home": 0,
                "score":""
                },
            "B": {
                "away": 0,
                "home": 0,
                "score":""
                }
            },
        "finals":{
            "3rd place": {
                "away": 0,
                "home": 0,
                "score":""
                },
            "final": {
                "away": 0,
                "home": 0,
                "score":""
                }
            }
        }
    }
#=======================================================================
def check_regular_season():
    status = True
    good = []
    for i in range(1,17):
        good.append(i)
    for w in range(1,15):
        week = "week "+str(w)
        check = []
        for g in range(1,9):
            game = "game " + str(g)
            check.append(season["regular"][week][game]["away"])
            check.append(season["regular"][week][game]["home"])
        if good != sorted(check):
            status = False
            print("Problem with week "+str(w))
    return status
#=======================================================================
print("Regular season is consistent : " + str(check_regular_season()))
print("Rosters are consistent       : " + str(check_draft()))
#=======================================================================
