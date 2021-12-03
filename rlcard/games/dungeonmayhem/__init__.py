from rlcard.games.dungeonmayhem.barbarian import \
    DungeonMayhemBarbarian as Barbarian
from rlcard.games.dungeonmayhem.card import DungeonMayhemCard as Card
from rlcard.games.dungeonmayhem.char import DungeonMayhemCharacter as Character
from rlcard.games.dungeonmayhem.game import DungeonMayhemGame as Game
from rlcard.games.dungeonmayhem.paladin import DungeonMayhemPaladin as Paladin
from rlcard.games.dungeonmayhem.rogue import DungeonMayhemRogue as Rogue
from rlcard.games.dungeonmayhem.wizard import DungeonMayhemWizard as Wizard

DungeonMayhemClasses = {"0": Wizard, "1": Paladin, "2": Rogue, "3": Barbarian}
DungeonMayhemIDWizard = 0
DungeonMayhemIDPaladin = 1
DungeonMayhemIDRogue = 2
DungeonMayhemIDBarbarian = 3
