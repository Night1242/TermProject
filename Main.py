import pypokedex
from cmu_graphics import *
from PIL import Image
import random

#sprites: https://www.spriters-resource.com/game_boy_advance/pokemonemerald/

def onAppStart(app):
    app.width=960
    app.height=640
    app.BattleGrass=CMUImage(Image.open('BattleGrass.png'))
    trainers(app)
    player(app)

def player(app):
    app.player=Player('Night')
    pokemon1=Pokemon('torchic', 5)
    app.player.addPokemon(pokemon1)

def trainers(app):
    fisherman1(app)

def fisherman1(app):
    app.fisherman1=Trainer('Fisherman')
    pokemon1=Pokemon('mudkip', 5)
    app.fisherman1.addPokemon(pokemon1)

def redrawAll(app):
    Background(app)

def Background(app):
    opponent=app.fisherman1
    name=str(app.player.pokemon[0])
    pokemonUs=pypokedex.get(name=name)
    name=str(opponent.pokemon[0])
    pokemonOppo=pypokedex.get(name=name)
    spriteFront=pokemonOppo.sprites.front.get('default')
    spriteBack=pokemonUs.sprites.back.get('default')
    drawImage(app.BattleGrass, 0, 0, width=app.width, height=(app.width/480)*224)
    drawImage(spriteFront, 675, 0, height=250, width=250)
    drawImage(spriteBack,-50, 175, height=400, width=400)
    drawRect(0, 448, app.width, app.height-448, fill='white')

class Pokemon:
    def __init__(self, name, level):
        self.level=level
        self.pokemon=pypokedex.get(name=name)
        self.name=name
        self.basestats=list(self.pokemon.base_stats)
        self.hp=self.basestats[0]

    def __repr__(self):
        return self.name

class Player:
    def __init__(self, name):
        self.name=name
        self.money=0
        self.pokemon=[]

    def addPokemon(self, other):
        self.pokemon.append(other)

class Trainer:
    def __init__(self, name):
        self.name=name
        self.money=0
        self.pokemon=[]
    
    def addPokemon(self, other):
        self.pokemon.append(other)

def main():
    runApp()

main()