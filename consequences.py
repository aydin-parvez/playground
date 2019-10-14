

woman = ["A shop keeper", "A queen", "A Waitress", "A Gardener"]

man  = ["a ninja", "a stunt guy", "an actor", "a teacher"]
place = ["on Pluto", "at the supermarket", "in a spooky, bat-filled cave"]
sheWore = ["a service dress", "a royal dress", "a white dress", "garden clothes"]
heWore = ["a ninja suit", "a stunt dress", "a costume", "a suit"]

womanSays = ["Who are you?", "How many beans make five?", "Why?"]
manSays = ["Beep boop!", "Don't eat frogs!", "What time do you call this?"]
consequence = ["world peace", "chaos", "a giant foot squashed them"]
worldSaid = ["Errant nonsense!", "Cheese is trending now.", "I'm melting!"]
import fun
while True:
    print(fun.choice(woman), "met", fun.choice(man), "in", fun.choice(place))
    print("She was wearing", fun.choice(sheWore))
    print("He was wearing", fun.choice(heWore))
    print("She said", fun.choice(womanSays))
    print("He said", fun.choice(manSays))
    print("The consequense was", fun.choice(consequence))
    print("The world said", fun.choice(worldSaid))
    print()
    input("Press enter to read again.")
    print()
