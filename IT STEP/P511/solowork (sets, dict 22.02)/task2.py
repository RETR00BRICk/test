all_games_sets = []

user_games_input = input("Enter your games: ")
user_games_list = user_games_input.split()
all_games_sets.append(set(user_games_list))

friends_count = int(input("How much friends do you have? "))

for i in range(friends_count):
    friend_games_input = input(f"Enter games of a friend: ")
    friend_games_list = friend_games_input.split()
    all_games_sets.append(set(friend_games_list))

common_games = all_games_sets[0]
for games_set in all_games_sets:
    common_games = common_games.intersection(games_set)

if len(common_games) != 0:
    print("Games which everyone can play:")
    for game in common_games:
        print(game)
else:
    print("Didnt find common games")