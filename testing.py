import pypokedex
from cmu_graphics import *
from PIL import Image
import random

app.dex='21'
app.pokemon = pypokedex.get(dex=int(app.dex))

print(list(app.pokemon.base_stats))
for stats in app.pokemon.base_stats:
    print(stats)