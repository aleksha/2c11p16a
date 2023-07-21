from config import *


def get_data(week="14"):
    data = {}
    poss = ["RB", "QB", "WR", "TE"]
    for pos in poss:
        lst = []
        with open(pos+week+".txt") as fl:
            for line in fl:
                lst.append( line[:-1].split("\t") )
        data[pos]=lst
    return data

      
def find(player, data):
    poss = ["RB", "QB", "WR", "TE"]
    for pos in poss:
        for rec in data[pos]:
            w = player.split(" ")
            if rec[1].startswith(w[0]+" "+w[1]):
                return rec
    return None

def names(pos, data):
    with open(pos+"_names.txt","w") as fl:
        for rec in data[pos]:
            words = rec[1].split(" ")
            fl.write(words[0]+" " +words[1]+"\n")

def conv_name(s):
    words = s.split(" ")
    return (words[0]+" " +words[1])

def check_float(s):
    if s=="  " or s=="B ":
        return "0.0"
    return s

def name_from_data(who,data):
    pos = who[0:2]
    num = int(who[2:])-1
    s = conv_name(data[pos][num][1]) + " (" + who +")"
    return s
    

def update_rosters(data):
    poss = ["RB", "QB", "WR", "TE"]
    rpos = ["RB", "QB", "TE", "WR1", "WR2", "WR3"]
    for k in rosters.keys():
        for r in rpos:
            for pos in poss:
                if rosters[k][r].startswith(pos):
                    rosters[k][r] = name_from_data(rosters[k][r],data)
        

def add_npt(pl,pts):
    rpos = ["QB","RB", "TE", "WR1","WR2","WR3"]
    for k in rosters.keys():
       for r in rpos:
           if rosters[k][r]==pl:
               rosters[k]["npt"] += pts
               break
    

def player_result(player,week,data):
    if "(" not in player:
        if ")" not in player:
            add_npt(player,float(check_float(find(player,data)[2+week])))
    return check_float(find(player,data)[3+week])

def get_result(away, home, week, game, data):
    """retutn number of team, which won"""
    rpos = ["QB","RB", "TE", "WR1", "WR2", "WR3"]
    aa = 0.; hh = 0.; s=""
    s += "week "+str(week)+"\t"
    s += "game "+str(game)+"\t"
    s += away["team"]+" : "+home["team"] + "\n"
    for p in rpos:
        a=float( player_result( away[p], week, data ) )
        aa+=a
        h=float( player_result( home[p], week, data ) )
        hh+=h
        s += "  " + p + "   "
        s += away[p] + " " + str(a) + " : "
        s += home[p] + " " + str(h) + "\n"
    s += "-------------------------------------\n"
    s += "{:.2f}".format(aa) + " : " + "{:.2f}".format(hh) + "\n"
    season["regular"]["week " + str(week)]["game "+str(game)]["score"] = "{:.2f}".format(aa) + " : " + "{:.2f}".format(hh)
    win = 0
    if aa>hh:
        win = away["draft"]
    elif aa==hh:
        if away["draft"]>home["draft"]:
            win = away["draft"]
    else:
        win = home["draft"]
    s += "WINNER : " + get_team(win,"draft")["team"]+"\n"
    season["regular"]["week " + str(week)]["game "+str(game)]["log"] = s
    print(s)
    return win

dat = get_data()
divs = { "I":[1,5,9,13], "II":[2,6,10,14], "III":[3,7,11,15], "IV":[4,8,12,16]}

for k in rosters.keys():
    rosters[k]["res"] = []
    rosters[k]["npt"] = 0.
    rosters[k]["status"] = ""
    rosters[k]["playoff"] = ""
    for dk in divs.keys():
        if rosters[k]["draft"] in divs[dk]:
            rosters[k]["div"] = dk


update_rosters(dat)

winners = []
for w in range(1,15):
    winners_week = []
    week = "week " + str(w)
    for g in range(1,9):
        game = "game " + str(g)
        away_team = get_team(season["regular"][week][game]["away"],"draft")
        home_team = get_team(season["regular"][week][game]["home"],"draft")
        win = get_result(away_team, home_team, w, g, dat)
        winners_week.append(win)
    winners.append(winners_week)

for ww in winners:
    for k in rosters.keys():
        if rosters[k]["draft"] in ww:
            rosters[k]["res"].append(1)
        else:
            rosters[k]["res"].append(0)

for k in rosters.keys():
    print(k + "  " + str(rosters[k]["draft"])
          + "\t" + str(rosters[k]["res"])
          + "  " + str(sum(rosters[k]["res"]))
          + "  " + "{:.2f}".format(rosters[k]["npt"]))

def status_div(div, wins_div, wins_tot):
    m = max(wins_div)
    for i in range(3,-1,-1):
        if m==wins_div[i]:
            for k in rosters.keys():
                if rosters[k]["draft"]==div[i]:
                    rosters[k]["status"]="D1"
            break
    m = max(wins_tot)
    cont = True
    for i in range(3,-1,-1):
        if m==wins_tot[i] and rosters[get_team(div[i],"draft")["team"]]["status"]!="D1":
            rosters[ get_team(div[i],"draft")["team"] ]["status"]="D2"
            cont = False
            break
    if cont:
        sml = []
        for w in wins_tot:
            sml.append(w)
        sm = sorted(sml,reverse=True)[1]
        for i in range(3,-1,-1):
            if sm==wins_tot[i]:
                rosters[ get_team(div[i],"draft")["team"] ]["status"]="D2"
                break
   

for dk in divs.keys():
    div = divs[dk]
    wins_div = []
    wins_tot = []
    for d in div:
        k = get_team(d,"draft")["team"]
        wins_div.append( sum(rosters[k]["res"][0:3]) + sum(rosters[k]["res"][11:]) )
        wins_tot.append( sum(rosters[k]["res"]) )
    status_div(div, wins_div,wins_tot)

print("\n\n Divisions:\n")
for dk in divs.keys():
    div = divs[dk]
    print("  Div. "+dk)
    print("-----------")
    for d in div:
        k = get_team(d,"draft")["team"]
        print( k + "  " + str(d) + "\t" + str(rosters[k]["res"]) + "  "
               + str( sum(rosters[k]["res"][0:3]) + sum(rosters[k]["res"][11:]) )
               + "  " + str(sum(rosters[k]["res"]))
               + "  " + rosters[k]["status"])
    print("\n")



def find_div_winner(d,s):
    for k in rosters.keys():
        if rosters[k]["div"]==d and rosters[k]["status"]==s:
            return rosters[k]["draft"]

season["playoff"]["quaterfinals"]["A1"]["away"] = find_div_winner("I" ,"D1")
season["playoff"]["quaterfinals"]["A1"]["home"] = find_div_winner("II","D2")
season["playoff"]["quaterfinals"]["A2"]["away"] = find_div_winner("I" ,"D2")
season["playoff"]["quaterfinals"]["A2"]["home"] = find_div_winner("II","D1")
season["playoff"]["quaterfinals"]["B1"]["away"] = find_div_winner("III","D1")
season["playoff"]["quaterfinals"]["B1"]["home"] = find_div_winner("IV" ,"D2")
season["playoff"]["quaterfinals"]["B2"]["away"] = find_div_winner("III","D2")
season["playoff"]["quaterfinals"]["B2"]["home"] = find_div_winner("IV" ,"D1")

playoff_data = get_data("17")

def player_result_playoff(player,week,data):
    return check_float(find(player,data)[3+week])

def get_result_playoff(away_team, home_team, stage, game, data):
    """retutn number of team, which wonat playoff stage"""
    rpos = ["QB","RB", "TE", "WR1", "WR2", "WR3"]
    if stage=="quaterfinals":
        week=15
    if stage=="semifinals":
        week=16
    if stage=="finals":
        week=17
    aa = 0.; hh = 0.; s=""
    away = get_team(away_team,"draft")
    home = get_team(home_team,"draft")

    s += stage +" week "+str(week)+"\t"
    s += "game "+str(game)+"\t"
    s += away["team"]+" : "+home["team"] + "\n"
    for p in rpos:
        a=float( player_result_playoff( away[p], week, data ) )
        aa+=a
        h=float( player_result_playoff( home[p], week, data ) )
        hh+=h
        s += "  " + p + "   "
        s += away[p] + " " + str(a) + " : "
        s += home[p] + " " + str(h) + "\n"
    s += "-------------------------------------\n"
    s += "{:.2f}".format(aa) + " : " + "{:.2f}".format(hh) + "\n"
    win = 0
    if aa>hh:
        win = away["draft"]
    elif aa==hh:
        if away["draft"]>home["draft"]:
            win = away["draft"]
    else:
        win = home["draft"]
    s += "WINNER : " + get_team(win,"draft")["team"]+"\n"
    season["playoff"][stage][game]["score"] = "{:.2f}".format(aa) + " : " + "{:.2f}".format(hh)
    season["playoff"][stage][game]["log"] = s
    print(s)
    return win


A1 = get_result_playoff(season["playoff"]["quaterfinals"]["A1"]["away"],
                        season["playoff"]["quaterfinals"]["A1"]["home"],
                        "quaterfinals", "A1", playoff_data)
A2 = get_result_playoff(season["playoff"]["quaterfinals"]["A2"]["away"],
                        season["playoff"]["quaterfinals"]["A2"]["home"],
                        "quaterfinals", "A2", playoff_data)
B1 = get_result_playoff(season["playoff"]["quaterfinals"]["B1"]["away"],
                        season["playoff"]["quaterfinals"]["B1"]["home"],
                        "quaterfinals", "B1", playoff_data)
B2 = get_result_playoff(season["playoff"]["quaterfinals"]["B2"]["away"],
                        season["playoff"]["quaterfinals"]["B2"]["home"],
                        "quaterfinals", "B2", playoff_data)

season["playoff"]["semifinals"]["A"]["home"] = A2
season["playoff"]["semifinals"]["A"]["away"] = A1
season["playoff"]["semifinals"]["B"]["home"] = B2
season["playoff"]["semifinals"]["B"]["away"] = B1

A = get_result_playoff(season["playoff"]["semifinals"]["A"]["away"],
                        season["playoff"]["semifinals"]["A"]["home"],
                        "semifinals", "A", playoff_data)
B = get_result_playoff(season["playoff"]["semifinals"]["B"]["away"],
                        season["playoff"]["semifinals"]["B"]["home"],
                        "semifinals", "B", playoff_data)

def find_looser(G1,G2,G):
    if G1==G:
        return G2
    return G1



season["playoff"]["finals"]["3rd place"]["home"] = find_looser(B1,B2,B)
season["playoff"]["finals"]["3rd place"]["away"] = find_looser(A1,A2,A)
season["playoff"]["finals"]["final"]["home"] = B
season["playoff"]["finals"]["final"]["away"] = A

T = get_result_playoff(season["playoff"]["finals"]["3rd place"]["away"],
                        season["playoff"]["finals"]["3rd place"]["home"],
                        "finals", "3rd place", playoff_data)
F = get_result_playoff(season["playoff"]["finals"]["final"]["away"],
                        season["playoff"]["finals"]["final"]["home"],
                        "finals", "final", playoff_data)


for k in rosters.keys():
    print("Team: " + str(rosters[k]["draft"]) + "  "+ k + "  Div.: "+rosters[k]["div"] )
    rpos = ["QB","RB", "TE", "WR1", "WR2", "WR3"]
    for r in rpos:
        print("  " + r + " : "+rosters[k][r])
    print("\n")

    
