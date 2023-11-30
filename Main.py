import pypokedex
from cmu_graphics import *
from PIL import Image
import random

#sprites: https://www.spriters-resource.com/game_boy_advance/pokemonemerald/

def onAppStart(app):
    app.width=720
    app.height=480
    app.start=True
    app.start1=False
    app.start2=False
    app.battle=False
    app.Truck=False
    app.starter=False
    app.gender=0
    app.name=''
    app.playerx=0
    app.playery=0
    app.mystarter=0
    app.overworld=False
    app.overworldX=-2900
    app.overworldY=-2300
    app.dy=0
    app.dx=0
    app.Overworldplayerx=50
    app.Overworldplayery=app.height/2
    movesList(app)
    trainers(app)
    images(app)

def Start(app):
    introBackground=CMUImage(Image.open('Intro.png'))
    drawImage(introBackground, 0,0, align='center')
    drawLabel('Pokemon 112', app.width/2, 200,align='center',size=75, fill='Green' , font='orbitron')
    drawLabel('Press Enter to Start', app.width/2, 285, align='center',size=30, fill='White' , font='orbitron')

def images(app):
    app.map=CMUImage(Image.open('Map.jpg'))
    app.professor=CMUImage(Image.open('Professor.png'))
    app.girl=CMUImage(Image.open('girl.png'))
    app.boy=CMUImage(Image.open('boy.png'))
    app.truck=CMUImage(Image.open('Truck.jpg'))
    app.wally=CMUImage(Image.open('WallyFront.png'))

def Start1(app):
    if app.gender%2==0:
        drawImage(app.boy, app.width/2,app.height/2,height=app.height, width=app.width+45,align='center')
    if app.gender%2==1:
        drawImage(app.girl, app.width/2,app.height/2,height=app.height, width= app.width+45,align='center')

def Start2(app):
    if app.gender=="Male":
        boy=CMUImage(Image.open('boy1.png'))
        drawImage(boy, app.width/2,app.height/2,height=app.height, width=app.width+45,align='center')
    if app.gender=="Female":
        girl=CMUImage(Image.open('girl1.png'))
        drawImage(girl, app.width/2,app.height/2,height=app.height, width= app.width+45,align='center')
    drawRect(25, 150, 300, 75, fill='white', border='green', borderWidth=10)
    drawLabel(app.name,40, 175, align='top-left', size=30)

def Truck(app):
    
    drawRect(0,0, app.width, app.height, fill='black')
    drawImage(app.truck, app.width/2,app.height/2, width=80*2,height=72*2 ,align='center')
    drawImage(app.direction, app.playerx, app.playery, width=18*2, height=23*2)
    
def Overworld(app):
    drawImage(app.map, app.overworldX, app.overworldY, width=2*2353, height=2*1579)
    if type(app.mystarter)==int:
        drawImage(app.professor, 100, -350+app.dy,width=20*2, height=25*2)
    else:
        drawImage(app.wally,200, -350+app.dy,width=20*2, height=25*2)
    drawImage(app.direction,app.Overworldplayerx, app.Overworldplayery, width=20*2, height=25*2)

def Starter(app):
    mudkip=CMUImage(Image.open('Mudkip.png'))
    torchic=CMUImage(Image.open('Torchic.png'))
    treecko=CMUImage(Image.open('Treecko.png'))
    if app.mystarter%3==0:
        drawImage(torchic, app.width/2,app.height/2,height=app.height, width=app.width+45,align='center')
    if app.mystarter%3==1:
        drawImage(mudkip, app.width/2,app.height/2,height=app.height, width=app.width+45,align='center')
    if app.mystarter%3==2:
        drawImage(treecko, app.width/2,app.height/2,height=app.height, width=app.width+45,align='center')

def Battle(app, opponent):
    player(app)
    app.Win=False
    app.Lose=False
    app.opponent=opponent
    app.battleArrowX=387
    app.battleArrowY=385
    app.movesArrowX=50
    app.movesArrowY=380
    app.BattleGrass=CMUImage(Image.open('BattleGrass.png'))
    app.BattleBar=CMUImage(Image.open('Battle2.jpg'))
    app.BattleMoves=CMUImage(Image.open('BattleMoves.jpg'))
    app.BattleResultBlank=CMUImage(Image.open('BattleResult.jpg'))
    app.battleMoves=False
    app.battleMain=True
    app.battleResults=False

def player(app):
    app.player=Player(app.name)
    app.player.addPokemon(app.mystarter)

def movesList(app):
    app.Tackle=Moves("Tackle", 35, 40, 100, "Normal", True),
    Moves("Thunderbolt", 15, 90, 100, "Electric", True),
    app.WaterGun=Moves("Water Gun", 25, 40, 100, "Water", True),
    app.Ember=Moves("Ember", 25, 40, 100, "Fire", True),
    app.VineWhip=Moves("Vine Whip", 10, 45, 100, "Grass", True),
    Moves("Ice Beam", 10, 90, 100, "Ice", True),
    Moves("Earthquake", 10, 100, 100, "Ground", True),
    Moves("Psychic", 10, 90, 100, "Psychic", True),
    Moves("Shadow Ball", 15, 80, 100, "Ghost", True),
    Moves("Sludge Bomb", 10, 90, 100, "Poison", True),
    app.AerialAce=Moves("Aerial Ace", 20, 60, 100, "Flying", True),
    Moves("Rock Slide", 10, 75, 90, "Rock", True),
    Moves("Dragon Claw", 15, 80, 100, "Dragon", True),
    Moves("Surf", 15, 90, 100, "Water", True),
    Moves("Thunder", 10, 110, 70, "Electric", True),
    Moves("Fire Blast", 5, 110, 85, "Fire", True)

def trainers(app):
    pass

def Rival1(app):
    app.Rival1=Trainer('Rival')
    app.Rival1.addPokemon(app.RivalStarter)


def redrawAll(app):
    if app.battle==True:
        battleBackground(app)
    if app.start==True:
        Start(app)
    if app.start1==True:
        Start1(app)
    if app.start2==True:
        Start2(app)
    if app.Truck==True:
        Truck(app)
    if app.starter==True:
        Starter(app)
    if app.overworld==True:
        Overworld(app)

def battleBackground(app):
    if app.Lose==False and app.Win==False:
        name=str(app.player.pokemon[0])
        pokemonUs=pypokedex.get(name=name)
        name=str(app.opponent.pokemon[0])
        pokemonOppo=pypokedex.get(name=name)
        spriteFront=pokemonOppo.sprites.front.get('default')
        spriteBack=pokemonUs.sprites.back.get('default')
        drawImage(app.BattleGrass, 0, 0, width=app.width, height=(app.width/480)*224)
        drawImage(spriteFront, 535, 25, height=150, width=150)
        drawImage(spriteBack,0, 175, height=250, width=250)
    #OpponentBox
        drawRect(300,50, 200, 50,fill=rgb(255, 250, 205), border='black')
        drawLabel(f'{str(app.opponent.pokemon[0].nickname).upper()}    LV {app.opponent.pokemon[0].level}', 310, 60, size=20, align='top-left', font='orbitron')
        drawRect(310, 80, 175, 15, fill='gray', border='black')
        EnemyPercentage=app.opponent.pokemon[0].hp/app.opponent.pokemon[0].basehp
        if EnemyPercentage < 0.2:
            fill='red'
        elif EnemyPercentage < 0.5:
            fill='orange'
        else:
            fill='green'
        if EnemyPercentage>0:
            drawRect(310, 80, 175*(EnemyPercentage), 15, fill=fill, border='black')
    #PlayerBox
        drawRect(250,250, 200, 75,fill=rgb(255, 250, 205), border='black')
        drawLabel(f'{str(app.player.pokemon[0].nickname).upper()}    LV {app.player.pokemon[0].level}', 260, 260, size=20, align='top-left', )
        PlayerPercentage=app.player.pokemon[0].hp/app.player.pokemon[0].basehp
        drawRect(260, 280, 175, 15, fill='gray', border='black')
        if PlayerPercentage < 0.2:
            fill='red'
        elif PlayerPercentage < 0.5:
            fill='orange'
        else:
            fill='green'
        if PlayerPercentage>0:
            drawRect(260, 280, 175*PlayerPercentage, 15, fill=fill, border='black')
            drawLabel(f'{app.player.pokemon[0].hp}/{app.player.pokemon[0].basehp}', 370, 300, size=20, align='top-left', font='orbitron')
        else:
            drawLabel(f'0/{app.player.pokemon[0].basehp}', 370, 300, size=20, align='top-left', font='orbitron')
        if app.battleMain==True:
            drawImage(app.BattleBar, 0, (app.width/480)*224,width=app.width, height=app.height-(app.width/480)*224 )
            drawRegularPolygon(app.battleArrowX, app.battleArrowY, 13, 3, rotateAngle=90)
            drawLabel('What will', 30, 370, size=35, fill='white', align='top-left', font='orbitron')
            drawLabel(f'{app.player.pokemon[0].nickname.upper()} do?', 30, 415, size=35, fill='white',  align='top-left', font='orbitron')
            drawLabel('FIGHT', 410, 373, size=30,align='top-left', font='orbitron')
            drawLabel('POKéMON', 410, 373+52, size=27, align='top-left', font='orbitron')
            drawLabel('BAG', 410+170, 373, size=30,align='top-left', font='orbitron')
            drawLabel('RUN', 410+170, 373+50, size=30,align='top-left', font='orbitron')

        if app.battleMoves==True:
            drawImage(app.BattleMoves, 0, (app.width/480)*224,width=app.width, height=app.height-(app.width/480)*224 )
            x=75
            y=370
            for moves in app.player.pokemon[0].moves:
                if moves==None:
                    continue
                moves=moves[0].name
                drawLabel(moves, x, y, size=30, align='top-left', font='orbitron')
                if x==75:
                    x+=190
                elif x==190+75:
                    x=75
                    y+=50
            drawRegularPolygon(app.movesArrowX, app.movesArrowY, 13, 3, rotateAngle=90)
            if app.movesSelected!=None:
                drawLabel(f"{app.movesSelected[0].basepp}/{app.movesSelected[0].pp}", 600, 380, size=30, font='orbitron')
                drawLabel(f"TYPE/{app.movesSelected[0].type}", 600, 430, size=30, font='orbitron')
            else:
                drawLabel(f"None", 600, 380, size=30, font='orbitron')
        if app.battleResults==True:
            drawImage(app.BattleResultBlank, 0, (app.width/480)*224,width=app.width, height=app.height-(app.width/480)*224 )
            drawLabel(app.resultList[0], 35, 390, size=35, fill='white',align='top-left')
    if app.Win==True:
        drawRect(0,0, app.width, app.height, fill='black')
        drawLabel(f"{app.name} WON", app.width/2, app.height/2, size=40, fill='White')
    if app.Lose==True:
        drawRect(0,0, app.width, app.height, fill='black')
        drawLabel(f"{app.name} Blackout", app.width/2, app.height/2, size=40, fill='White')


def onKeyPress(app, key):
    if app.battle==True:
        if app.battleMain==True:
            if key=='left':
                if app.battleArrowX != 387:
                    app.battleArrowX-=170
            if key=='right':
                if app.battleArrowX != 557:
                    app.battleArrowX+=170
            if key=='up':
                if app.battleArrowY != 385:
                    app.battleArrowY-=50
            if key=='down':
                if app.battleArrowY != 435:
                    app.battleArrowY+=50
            if key=='x':
                if app.battleArrowX==387 and app.battleArrowY == 385:
                    app.battleMain=False
                    app.battleMoves=True
                    app.movesSelected=None
                    app.movesArrowX = 50
                    app.movesArrowY =380
                
        elif app.battleMoves==True:
            if key=='left':
                if app.movesArrowX != 50:
                    app.movesArrowX-=190
            if key=='right':
                if app.movesArrowX != (50+190):
                    app.movesArrowX+=190
            if key=='up':
                if app.movesArrowY != 380:
                    app.movesArrowY-=50
            if key=='down':
                if app.movesArrowY != 380+50:
                    app.movesArrowY+=50
            if key=='z':
                app.battleMain=True
                app.battleMoves=False
                app.battleArrowX=387
                app.battleArrowY=385
            if key=='x':
                if app.movesSelected!=None:
                    if app.player.pokemon[0].speed >= app.opponent.pokemon[0].speed:
                        app.resultList=[f"{(app.player.pokemon[0].nickname.upper())} used {app.movesSelected[0].name.upper()} "]
                        app.player.pokemon[0].damage(app, app.movesSelected[0], app.opponent.pokemon[0])
                        if app.opponent.pokemon[0].hp>0:
                            app.opponentMove=None
                            app.opponentMovesOptions=[]
                            for moves in app.opponent.pokemon[0].moves:
                                if moves == None:
                                    continue
                                if effective(moves[0], app.player.pokemon[0]) == 2:
                                    app.opponentMove=moves[0]
                                elif effective(moves[0], app.player.pokemon[0]) == 1:
                                    app.opponentMovesOptions.append(moves[0])
                            if app.opponentMove == None and len(app.opponentMovesOptions)!=1:
                                app.opponentMove=app.opponentMovesOptions[random.randrange(0, len(app.opponentMovesOptions)-1)]
                            elif app.opponentMove == None and len(app.opponentMovesOptions) == 1:
                                app.opponentMove=app.opponentMovesOptions[0]
                            app.resultList.append(f"{(app.opponent.pokemon[0].nickname.upper())} used {app.opponentMove.name.upper()} ")
                            app.opponent.pokemon[0].damage(app, app.opponentMove, app.player.pokemon[0])
                        else: 
                            app.resultList.append(f"{(app.opponent.pokemon[0].nickname.upper())} fainted!")
                            if len(app.opponent.pokemon)>1:
                                app.resultList.append(f"Opponent sent out {(app.opponent.pokemon[1].nickname.upper())}")
                    elif app.player.pokemon[0].speed < app.opponent.pokemon[0].speed:
                        if app.opponent.pokemon[0].hp>0:
                            app.opponentMove=None
                            app.opponentMovesOptions=[]
                            for moves in app.opponent.pokemon[0].moves:
                                if moves == None:
                                    continue
                                if effective(moves[0], app.player.pokemon[0]) == 2:
                                    app.opponentMove=moves[0]
                                elif effective(moves[0], app.player.pokemon[0]) == 1:
                                    app.opponentMovesOptions.append(moves[0])
                            if app.opponentMove == None and len(app.opponentMovesOptions)!=1:
                                app.opponentMove=app.opponentMovesOptions[random.randrange(0, len(app.opponentMovesOptions)-1)]
                            elif app.opponentMove == None and len(app.opponentMovesOptions) == 1:
                                app.opponentMove=app.opponentMovesOptions[0]
                            app.resultList=[(f"{(app.opponent.pokemon[0].nickname.upper())} used {app.opponentMove.name.upper()} ")]
                            app.opponent.pokemon[0].damage(app, app.opponentMove, app.player.pokemon[0])
                            if app.player.pokemon[0].hp>0:
                                app.resultList.append(f"{(app.player.pokemon[0].nickname.upper())} used {app.movesSelected[0].name.upper()} ")
                                app.player.pokemon[0].damage(app, app.movesSelected[0], app.opponent.pokemon[0])
                            else:
                                app.resultList.append(f"{(app.player.pokemon[0].nickname.upper())} fainted!")
                    app.battleMain=False
                    app.battleMoves=False
                    app.battleResults=True
        
        elif app.battleResults==True:
            if key=='x' or key=='z':
                app.resultList.pop(0)
                if len(app.resultList)==0:
                    if app.opponent.pokemon[0].hp<=0:
                        app.opponent.pokemon.pop(0)
                    if app.player.pokemon[0].hp<=0:
                        app.player.pokemon.pop(0)
                    if len(app.opponent.pokemon)==0:
                        app.Win=True
                    if len(app.player.pokemon)==0:
                        app.Lose=True
                    app.battleMain=True
                    app.battleMoves=False
                    app.battleResults=False
    elif app.start==True:
        if key=='enter':
            app.start=False
            app.start1=True
    elif app.start1==True:
        if key=='up':
            app.gender+=1
        if key=="down":
            app.gender-=1
        if key=="enter" or key=='x':
            if app.gender%2==0:
                app.gender='Male'
                app.east=CMUImage(Image.open('Right.png'))
                app.west=CMUImage(Image.open('Left.png'))
                app.north=CMUImage(Image.open('Up.png'))
                app.south=CMUImage(Image.open('Down.png'))
                app.walkingeast=CMUImage(Image.open('BoyWalkRight.png'))
                app.walkingwest=CMUImage(Image.open('BoyWalkLeft.png'))
                app.walkingnorth=CMUImage(Image.open('BoyWalkUp.png'))
                app.walkingsouth=CMUImage(Image.open('BoyWalkDown.png'))
                app.direction=app.east
            elif app.gender%2==1:
                app.gender="Female"
                app.east=CMUImage(Image.open('GirlRight.png'))
                app.west=CMUImage(Image.open('GirlLeft.png'))
                app.north=CMUImage(Image.open('GirlUp.png'))
                app.south=CMUImage(Image.open('GirlDown.png'))
                app.direction=app.east
            app.start1=False
            app.start2=True
    elif app.start2==True:
        if (key.isalpha() or key.isdigit() )and len(key)==1 and len(app.name)<=10:
            app.name+=key.upper()
        elif key=='backspace':
            if app.name!='':
                app.name=app.name[:-1]
        elif key=="enter":
            if app.name!='':
                app.start2=False
                app.Truck=True
                app.playerx=325
                app.playery=200
    elif app.Truck==True:
        if key=='left':
            if app.direction!=app.west:
                app.direction=app.west
            else:
                if app.playerx>311:
                    app.playerx-=5
        if key=='right':
            if app.direction!=app.east:
                app.direction=app.east
            else:
                if app.playerx<400:
                    app.playerx+=5
                if app.playerx>=400:
                    app.Truck=False
                    app.overworld=True
    elif app.starter==True:
        print(app.mystarter)
        if key=='right':
            app.mystarter+=1
        if key=='left':
            app.mystarter-=1
        if key=='x':
            if app.mystarter%3==0:
                app.mystarter=Pokemon('torchic', 5, [app.Ember, app.Tackle, None, None])
                app.RivalStarter=Pokemon('mudkip', 5, [None, app.Tackle, None, None])
            elif app.mystarter%3==1:
                app.mystarter=Pokemon('mudkip', 5, [app.WaterGun, app.Tackle, None, None])
                app.RivalStarter=Pokemon('treecko', 5, [None, app.Tackle, None, None])
            elif app.mystarter%3==2:
                app.mystarter=Pokemon('treecko', 5, [app.VineWhip, app.Tackle, None, None])
                app.RivalStarter=Pokemon('torchic', 5, [None, app.Tackle, None, None])
            app.starter=False
            app.overworld=True
    elif app.overworld==True:
        if key=='left':
            if app.direction!=app.west:
                app.direction=app.west
            else:
                app.Overworldplayerx-=5
        elif key=='right':
            if app.direction!=app.east:
                app.direction=app.east
            else:
                app.Overworldplayerx+=5
        elif key=='up':
            if app.direction!=app.north:
                app.direction=app.north
            else:
                app.overworldY-=5
                app.dy-=5
        elif key=='down ':
            if app.direction!=app.south:
                app.direction=app.south
            else:
                app.overworldY+=5
                app.dy+=5

def onMousePress(app, mouseX, mouseY):
    print(mouseX, mouseY)

def onKeyHold(app, keys):
    if app.Truck==True:
        if 'left' in keys:
            app.direction=app.walkingwest
            if app.playerx>311:
                app.playerx-=5
        if 'right' in keys:
            app.direction=app.walkingeast
            if app.playerx<400:
                    app.playerx+=5
            if app.playerx>=400:
                app.Truck=False
                app.overworld=True
    if app.overworld==True:
        if 'up' in keys:
            app.direction=app.walkingnorth
            app.overworldY+=5
            app.dy+=5
        if 'down' in keys:
            app.direction=app.walkingsouth
            app.overworldY-=5
            app.dy-=5
        if 'left' in keys:
            app.direction=app.walkingwest
            app.Overworldplayerx-=5
        if 'right' in keys:
            app.direction=app.walkingeast
            app.Overworldplayerx+=5
        
def onKeyRelease(app, key):
    if app.Truck==True:
        if key=='left':
            app.direction=app.west
        if key=='right':
            app.direction=app.east
    if app.overworld==True:
        if key=='left':
            app.direction=app.west
        if key=='right':
            app.direction=app.east
        if key=='up':
            app.direction=app.north
        if key=='down':
            app.direction=app.south

def onStep(app):
    if app.battle==True:
        if app.battleMoves==True:
            if app.movesArrowX==50 and app.movesArrowY==380:
                app.movesSelected=app.player.pokemon[0].moves[0]
            elif app.movesArrowX==240 and app.movesArrowY==380:
                app.movesSelected=app.player.pokemon[0].moves[1]
            elif app.movesArrowX==50 and app.movesArrowY==430:
                app.movesSelected=app.player.pokemon[0].moves[2]
            elif app.movesArrowX==240 and app.movesArrowY==430:
                app.movesSelected=app.player.pokemon[0].moves[3]
    elif app.overworld==True:
        if 54<=app.Overworldplayerx<=146 and 450<app.dy<600 and type(app.mystarter)==int:
            app.overworld=False
            app.starter=True
        if 150<=app.Overworldplayerx<=250 and 450<app.dy<600 and type(app.mystarter)!=int:
            app.overworld=False
            Rival1(app)
            Battle(app, app.Rival1)
            app.battle=True


class Pokemon:
    def __init__(self, name, level, moves):
        self.level=level
        self.pokemon=pypokedex.get(name=name)
        self.type=self.pokemon.types
        self.name=name
        self.nickname=name
        self.basestats=list(self.pokemon.base_stats)
        self.hp=rounded((self.basestats[0]*2*level)/100+level+10)
        self.basehp=rounded((self.basestats[0]*2*level)/100+level+10)
        self.attack=rounded((self.basestats[1]*2*level)/100+5)
        self.defense=rounded((self.basestats[2]*2*level)/100+5)
        self.spAttack=rounded((self.basestats[3]*2*level)/100+5)
        self.spDefense=rounded((self.basestats[4]*2*level)/100+5)
        self.speed=rounded((self.basestats[5]*2*level)/100+5)
        self.moves=moves

    def __repr__(self):
        return self.name
    
    def damage(self, app, move, other):
        if self.type == move.type:
            STAB=1.5
        else:
            STAB=1
        effectiveness=effective(move, other)
        if effectiveness==2:
            app.resultList.append("It's super effective!")
        elif effectiveness==0.5:
            app.resultList.append("It's not very effective!")
        damage=rounded((((2*self.level/5)+2)*move.power*(self.attack/other.defense))/50)*STAB*effectiveness
        other.hp-=damage

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

class Moves: 
    def __init__(self, name, pp, power, accuracy, type, attack):
        self.name=name
        self.basepp=pp
        self.power=power
        self.accuracy=accuracy
        self.type=type
        self.attack=attack
        self.pp=pp
    
    def __repr__(self):
        return self.name
    
def effective(move, Pokemon):
    effectiveness=1
    offense=move.type.upper()
    defensive=Pokemon.type[0].upper()
    if offense=='WATER':
        if defensive=='FIRE':
            effectiveness*=2
        elif defensive=="WATER":
            effectiveness*=0.5
        elif defensive=='GRASS':
            effectiveness*=0.5
    elif offense=='FIRE':
        if defensive=='FIRE':
            effectiveness*=0.5
        elif defensive=="WATER":
            effectiveness*=0.5
        elif defensive=='GRASS':
            effectiveness*=2
    elif offense=='GRASS':
        if defensive=='FIRE':
            effectiveness*=0.5
        elif defensive=="WATER":
            effectiveness*=2
        elif defensive=='GRASS':
            effectiveness*=0.5
    return effectiveness

def main():
    runApp()

main()