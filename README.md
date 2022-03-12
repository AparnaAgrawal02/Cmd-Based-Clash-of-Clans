# Game
## Game Specifications:
### Village (20):
    There will be a map of n*m dimensions representing your village level. Each village must have the
    following properties

## Spawning points:
    ○ There should be three predefined spawning points around the village.
    ○ Each spawning point will be controlled by a different key. Pressing the key of a certain
    spawning point will cause a troop to be spawned there.
## Town Hall:
    ○ The Town Hall is the central building of your village.
    ○ There is only one town hall per village.
    ○ Size: 4x3 tiles
## Huts:
    ○ There should be at least five huts in your village
    ○ Size of the hut can be defined by you.
## Walls:
    ○ There should be a sufficient number of walls in your village to protect your town hall
    from troops.
    ○ Size: 1x1 tiles
    At least two cannon
    Cannon:
    ○ There should be at least two cannons in your village.
    ○ Size can be defined by you.
    ○ The cannon will have a range and damage value (can be defined by you). The range
    (must be greater than 5 tiles) would define the area till which it can attack and the
    damage value should be a number telling the amount of damage it yields to a single
    troop in a second.
    ○ At a given point, the cannon can only target a single troop.
    Each building will have a certain amount of hitpoints (basically health) and the remaining
    hitpoints of the building would be denoted by its colour.
    ○ The hitpoints of the building should be split into at least three ranges, each with a
    different colour.
    ■ For example: Green: 50% to 100% hitpoints, Yellow: 20%-50% hitpoints, Red:
    0%-20% hitpoints.
    ○ A building with 0 hit points is considered destroyed and should not be displayed on
    the screen or targeted by troops.
## King (20):
    The king is a user-controlled character capable of attacking and destroying buildings.
    ●
    ●
    Controls and Movements:
    ○ The King is to be controlled with W/A/S/D which correspond to Up/Left/Down?Right.
    ■ The King’s movement speed is left to you to decide
    ○ <SPACE> will be used for attacks
    ■ The King will attack a single location with a sword. This location should be
    specified relative to the location of the king, any building present in that
    location would be damaged by the king’s attack.
    Attributes:
    The values of each of the following attributes can be defined as you wish, the constraints on
    the values are given below.

## Damage: The damage each attack of the king deals to a building
    ■ The damage the king deals should NOT exceed the maximum health of ANY
    building (i.e. the King can’t one-shot anything).
    Health: The king’s health should be displayed as a health bar anywhere on the
    screen.
    ■ The health of the king should be higher than the damage dealt by any
    defensive building.
    ■ When the health of the king drops to 0, the King would be dead and cannot○
    move or attack anymore.
    Movement Speed: The distance that the king moves in each time step.
## Barbarians (15):
    ● Each barbarian will have the following attributes
    ○ Damage - the amount of damage it will yield per attack
    ■ Every troop attacks once per time step
    ○ Health - the hitpoints it has - The health of the troop would be depicted by the colour
    of barbarian … the colour should change from dark to light with a change in health.
    This shift can be discrete.
    ■ Once the health of a barbarian drops to 0, they are considered dead and
    cannot move or attack any longer.
    ○ Movement speed
    ● Movement : The barbarians will always try to attack the nearest non-wall building and will
    always move towards it. The barbarian movement is automated. If there is a wall in its path
    then the barbarian is expected to first destroy the wall and then move forward.
## Spells (5):

    Rage Spell:
    ○ The Rage spell affects every troop alive in the game and the King.
    ○ It doubles damage and movement speed.
    Heal Spell:
    ○ The Heal spell affects every troop alive in the game and the King.
    ○ It increases their health to 150% of the current health (capped at the maximum health)

## Game Endings (5):

    Each game can end in either victory or defeat.
    ○ Victory: All buildings (excluding walls) have been destroyed.
    ○ Defeat: All troops and the King have died without destroying all buildings.
    Once either of these conditions is satisfied, the game would end.
    You are required to display the result of the game once it ends.
## Replay (15):

    Implement a replay feature for all attacks. Any game that has been played should be available
    as a replay.
## Bonus

    King’s leviathan axe: the king instead of attacking a single building with a sword, now uses an
    axe to do an AoE (Area of Effect) attack to all buildings in a specific vicinity. (10 marks )
    ○ For example: The King when using this attack would deal damage to any building in a
    5 tile radius around him.