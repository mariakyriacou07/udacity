lines = ["Haiku frogs in snow",
         "A limerick came from Nantucket",
         "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]

def breakify(strings):
    return "<br>".join(strings)

print(breakify(lines))