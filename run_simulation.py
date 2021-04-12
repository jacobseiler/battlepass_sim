from player import Player

from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

if __name__ == "__main__":

    N = 1

    players = [Player(persona="agnostic_grinder")]

    start_date = date(2013, 1, 1)
    end_date = date(2013, 2, 1)
    for date in daterange(start_date, end_date):

        for player in players:
            player.play_games_for_day(date)

    print(players[0])
