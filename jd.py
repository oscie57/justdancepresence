import time, sys, pypresence, datetime

clientID2016 = 960250926151663637
clientID2017 = 960237840044793906
clientID2018 = 959239597387284481
clientID2019 = 960251480403755178
clientID2020 = 960251612654362705
clientID2021 = 960251775787614218
clientID2022 = 960251938274959450
clientFALLBACK = 959253107357933639
clientID = 0

game = input("Game being played: ")
if game == '2016':
    RPC = pypresence.Presence(clientID2016)
elif game == '2017':
    RPC = pypresence.Presence(clientID2017)
elif game == '2018':
    RPC = pypresence.Presence(clientID2018)
elif game == '2019':
    RPC = pypresence.Presence(clientID2019)
elif game == '2020':
    RPC = pypresence.Presence(clientID2020)
elif game == '2021':
    RPC = pypresence.Presence(clientID2021)
elif game == '2022':
    RPC = pypresence.Presence(clientID2022)
else:
    RPC = pypresence.Presence(clientFALLBACK)

start = time.time()
end = datetime.datetime(2022, 4, 16, 23, 0, 0).timestamp() # Season ends

RPC.connect()

RPC.update(
        details = "Playing Just Dance",
        state = "Having fun",

        start = start,

        large_image = 'game',
        large_text = f'Made by @oscie#8420',

        small_image = 'connect',
        small_text = 'Ubisoft Connect',

        buttons = [
            {"label": "Ubisoft Connect", "url": "https://ubisoftconnect.com/en-GB/game/just-dance-2018/overview/"},
            {"label": "More Information", "url": "https://justdance.fandom.com/wiki/Just_Dance_2018"},
        ]
    )

people = input("People this season: ")

def justdance(rank):
    RPC.update(
        details = "On the World Dance Floor",
        state = f"Season Ranking: {rank}/{people}",

        start = start,

        large_image = 'game',
        large_text = 'Made by @oscie#8420',

        small_image = 'connect',
        small_text = 'Ubisoft Connect',

        buttons = [
            {"label": "Ubisoft Connect", "url": "https://ubisoftconnect.com/en-GB/game/just-dance-2018/overview/"},
            {"label": "More Information", "url": "https://justdance.fandom.com/wiki/Just_Dance_2018"},
        ]
    )

def main():
    rank = input("Current ranking: ")

    if rank == 'exit':
        RPC.close()
        sys.exit(0)

    justdance(rank = rank)


while True:
    main()
    time.sleep(3)