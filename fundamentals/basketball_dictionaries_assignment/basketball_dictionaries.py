
# class Player:
#     def __init__(self, name, age, position, team):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.team = team

# kevin = {
#     "name": "Kevin Durant", 
#     "age":34, 
#     "position": "small forward", 
#     "team": "Brooklyn Nets"
# }
# jason = {
#     "name": "Jason Tatum", 
#     "age":24, 
#     "position": "small forward", 
#     "team": "Boston Celtics"
# }
# kyrie = {
#     "name": "Kyrie Irving", 
#     "age":32,
#     "position": "Point Guard", 
#     "team": "Brooklyn Nets"
# }
    
# # Create your Player instances here!
# # player_jason = ???

# class Player:
#     def __init__(self,player):
#         self.name = player["name"]
#         self.age = player["age"]
#         self.position = player["position"]
#         self.team = player["team"]

# player_kevin = Player(kevin)
# player_jason = Player(jason)
# player_kyrie = Player(kyrie)

# class Player:
#     def __init__(self, players):
#         self.team_list = []
#         for i in range(0, len(players)):
#             self.name = players[i]["name"]
#             self.age = players[i]["age"]
#             self.position = players[i]["position"]
#             self.team = players[i]["team"]
#             self.team_list.append(self)
#         print(self.team_list)

players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33,
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32,
        "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

class Player:
    team_list = []
    # creator = "Tyler"
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

# class Player:
#     team_list = []
#     def __init__(self, players):
#         # self.team_list = []
#         for i in range(0, len(players)):
#             self.name = players[i]["name"]
#             self.age = players[i]["age"]
#             self.position = players[i]["position"]
#             self.team = players[i]["team"]
#             # self.team_list.append(self)
#             Player.team_list.append(self)
#         print(self.team_list)

    def build_team(self, players):
        for i in range(0, len(players)):
            self.name = players[i]["name"]
            self.age = players[i]["age"]
            self.position = players[i]["position"]
            self.team = players[i]["team"]
            self.team_list.append(self)
            # Player.team_list.append(self)
        print(self.team_list)
        return self
    
    def display_player_info(self):
        print("Name:",self.name)
        print("Age:", self.age)
        print("Position", self.position)
        print("Team", self.team)
        return self

# team=Player(players)
# team=[]
# print(team.team_list)

# class Player:
#     def __init__(self, name, age, position, team):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.team = team

    @classmethod
    def get_team(cls):
        # for player in cls.team_list:
        players.build_team(players)
        players.display_player_info()
            

    # @classmethod
    # def change_creator(cls, new_creator):
    #     cls.creator = new_creator

    # Car.change_creator("Brandon")


# players = [
#     {
#         "name": "Kevin Durant", 
#         "age":34, 
#         "position": "small forward", 
#         "team": "Brooklyn Nets"
#     },
#     {
#         "name": "Jason Tatum", 
#         "age":24, 
#         "position": "small forward", 
#         "team": "Boston Celtics"
#     },
#     {
#         "name": "Kyrie Irving", 
#         "age":32,
#         "position": "Point Guard", 
#         "team": "Brooklyn Nets"
#     },
#     {
#         "name": "Damian Lillard", 
#         "age":33,
#         "position": "Point Guard", 
#         "team": "Portland Trailblazers"
#     },
#     {
#         "name": "Joel Embiid", 
#         "age":32,
#         "position": "Power Foward", 
#         "team": "Philidelphia 76ers"
#     },
#     {
#         "name": "DeMar DeRozan",
#         "age": 32,
#         "position": "Shooting Guard",
#         "team": "Chicago Bulls"
#     }
# ]

Player.get_team()