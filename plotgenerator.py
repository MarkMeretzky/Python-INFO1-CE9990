"""
plotgenerator.py
by the Brothers Heimberg: Jason & Justin

Generate a movie plot.
"""

import sys
import random

subjects = [
    "A cop who doesn't play by the rules",
    "A single mom",
    "Three naughty nurses",
    "An adorable panda cub",
    "A ruthless Mafia kingpin",
    "An ancient and powerful wizard",
    "A fraternity of lovable slobs, misfits, and drunks",
    "Adolph Hitler",
    "From a land where honor and tradition reign, "
        "comes the legend of a Samurai who",
    "A bumbling nerd",
    "Bigfoot",
    "A crackhead",
    "A flamboyantly gay hairdresser",
    "A retarded boy",
    "America's founding fathers",
    "A hockey mask-wearing psychopath",
    "A gangsta rapper",
    "An unrefined but precocious orphan girl",
    "The ultimate crime-fighting indestructible cyborg",
    "The Sesame Street puppets",
    "A small-town girl with big-time dreams",
    "A group of orthodox rabbis",
    "A burned-out hippie",
    "A Catholic priest",
    "A hooker with a heart of gold",
    "A grumpy midget",
    "A group of cantankerous senior citizens",
    "Jesus",
    "A no-nonsense Army drill sergeant",
    "A macho NFL quarterback"
]

predicates = [
    "fight(s) crime",
    "raise(s) a baby",
    "discover(s) the wonders of self pleasure",
    "befriends(s) the creatures of the forest",
    "is/are on the run from the Mob",
    "quest(s) for a dragon's treasure",
    "indulge(s) in beer bashes, toga parties, "
        "and an assortment of ill-advised high junks",
    "invade(s) Poland",
    "take(s) on an army of evil Ninjas",
    "become(s) immersed in hip-hop culture",
    "become(s) a nanny for a conservative aristocratic family",
    "coach(es) a hapless Little League baseball team",
    "hit(s) the Karaoke circuit",
    "grow(s) 50 times in size and go(es) on a destructive rampage",
    "travel(s) through time",
    "hack(s) up coeds with a rusty machete",
    "becomes a pimp (become pimps)",
    "challenge(s) the social mores of upper class society",
    "command(s) a fleet of starships against a horde of insectoid aliens",
    "help(s) children learn to read",
    "get(s) transformed into (a) gorgeous sexpot(s)",
    "compete(s) in gritty inner-city street basketball tournaments",
    "go(es) on an LSD-induced psychedelic adventure",
    "discover(s) a hidden talent for dance",
    "struggle(s) to get off heroin",
    "try (tries) to lose (his/her/their) virginity",
    "battle(s) problem flatulence",
    "rise(s) from the grave",
    "rescue(s) a group of American P.O.W.'s",
    "come(s) out of the closet"
]

modifiers = [
    "with a mischievous orangutan",
    "while juggling work, parenthood, and finding personal fulfillment",
    "in two hours of the raunchiest hardcore porno action ever seen",
    "in this heartwarming animated adventure",
    "in the heart of the Amish country",
    "with a cunning elf, an obese ogre, and a belligerent dwarf",
    "despite being admonished by a crusty old dean",
    "in this documentary narrated by James Earl Jones",
    "in an action-packed epic filled with elaborate, "
        "acrobatic Kung-Fu fight sequences",
    "to win the heart of the high school dreamboat",
    "in the feel-good comedy of the year",
    "in order to pay off a gambling debt",
    "in a beat-up Buick",
    "in the middle of Downtown Tokyo (in Japanese with English subtitles)",
    "with a wise-cracking robot",
    "in a blood-filled teen slasher, deep in the Compton ghetto",   #Los Angeles
    "in 1954 Baltimore (based on the Pulitzer Prize winning novel)",
    "shown in spectacular 3-D Imax",
    "in this powerful after school special",
    "set to an all-star '80's soundtrack "
        "featuring Air Supply, Journey, and Survivor",
    "to save the local synagogue",
    "with a magical talking bong, "
    "in this stoner cult classic",
    "in a rousing adaptation of the Broadway musical",
    "with the help of former tennis great Ivan Lendl (based on a true story)",
    "with the help of the ghost of Elvis",
    "set against the backdrop of a Florida retirement community",
    "in the inspiring story loosely adapted from the Bible",
    "in a Vietnamese prison camp",
    "and in the process learn(s) the true meaning of Christmas"
]

print("Keep pressing return, or control-d to exit.") #control-z enter in Microsoft

while True:
    try:
        input()
    except EOFError:
        sys.exit(0)

    print(f"""\
{random.choice(subjects)}
{random.choice(predicates)}
{random.choice(modifiers)}.""")

