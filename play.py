from desk import Desk
from player import PlayerHuman, PlayerAI
from game import Game
# initialization
player_1 = PlayerHuman()
player_2 = PlayerAI()
desk_1 = Desk()
desk_2 = Desk()
player_1.init_desk(desk_1)
player_2.init_desk(desk_2)
play = Game(player_1, desk_1, player_2, desk_2)
play.game_cycle()
if desk_1.get_list_of_ships():
    print("You win!")
elif desk_2.get_list_of_ships():
    print("AI win...")
print("Final look at the state of desk:")
desk_1.print_field(1)
print("Final look at the state of AI desk")
desk_2.print_field(1)
