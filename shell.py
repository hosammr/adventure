import sys

from game import Game


class Shell:
    def __init__(self, game):
        self.game = game

    def __str__(self):
        return 'shell for "%s"' % self.game

    def parse(self, cmd):
        cmd = cmd.split()
        try:
            if cmd[0] == "help":
                print('Elk commando verwacht twee woorden (behalve "help").')
                print("Commando's zijn: ga, pak, leg, bekijk.")
                print("Speciaal command: bekijk spullen")
                print("Je kunt het spel verlaten met Ctrl-C")
            elif cmd[0] == "ga":
                self.game.move(cmd[1])
            elif cmd[0] == "pak":
                self.game.get(cmd[1])
            elif cmd[0] == "leg":
                self.game.drop(cmd[1])
            elif cmd[0] == "bekijk":
                print(self.game.describe(cmd[1]))
            else:
                print('Het commando "%s" wordt niet ondersteund' % cmd[0])
        except KeyError as e:
            print(e)

    def run(self):
        print('Running "%s"' % self)

        while not self.game.is_done():
            print("\nJe bent in de %s." % self.game.location)
            try:
                cmd = input()
                self.parse(cmd)
            except KeyboardInterrupt:
                print('Bedankt voor het spelen van "%s"' % self.game)
                sys.exit(0)
        print("Gefeliciteerd!")


if __name__ == "__main__":
    try:
        game = Game.load(sys.argv[1])
        shell = Shell(game)
        shell.run()
    except IndexError:
        print("Usage: %s <game.json>" % sys.argv[0])
