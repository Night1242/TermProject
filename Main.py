import pypokedex
from cmu_graphics import *
from PIL import Image
import random

#sprites: https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
#font='orbitron'

def onAppStart(app):
    app.width=720
    app.height=480
    app.start=True
    app.start1=False
    app.start2=False
    app.battle=False
    app.Truck=False
    app.starter=False
    app.menu=False
    app.PokemonMenu=False
    app.BagMenu=False
    app.NameMenu=False
    app.PokedexMenu=False
    app.selectionArrow=0
    app.PokemonOn=0
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
    app.Win=False
    app.Lose=False
    app.time=0
    app.itemSelection=0
    movesList(app)
    trainers(app)
    images(app)
    player(app)

def Start(app):
    introBackground=CMUImage(Image.open('Intro.png')) #https://www.pinterest.com/pin/151574343683447160/
    drawImage(introBackground, 0,0, align='center')
    drawLabel('Pokemon 112', app.width/2, 200,align='center',size=75, fill='Green' , font='orbitron')
    drawLabel('Press Enter to Start', app.width/2, 285, align='center',size=30, fill='White' , font='orbitron')

def images(app):
    app.map=CMUImage(Image.open('Map.jpg')) #https://www.reddit.com/r/pokemon/comments/r0d3wt/couldnt_find_a_good_copy_of_the_entire_emerald/
    app.professor=CMUImage(Image.open('Professor.png')) #https://forums.pokemmo.com/index.php?/topic/157591-hoenn-overworld-main-story-nds-style-characters-mod/
    app.girl=CMUImage(Image.open('girl.png')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
    app.boy=CMUImage(Image.open('boy.png')) #https://www.deviantart.com/hyo-oppa/art/WIP-Emerald-Brendan-DPPt-HGSS-Gen-4-Sprite-Sheet-864378236
    app.truck=CMUImage(Image.open('Truck.jpg')) #https://www.emulatorgames.net/roms/gameboy-advance/pokemon-emerald-version/
    app.wally=CMUImage(Image.open('WallyFront.png')) #https://www.deviantart.com/kleinstudio/art/Kymotonian-Wally-Complete-209209501
    app.PokemonMenuBackground=CMUImage(Image.open('PokemonMenuBackground.jpg')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
    app.ItemMenuBackground=CMUImage(Image.open('ItemMenu.jpg')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
    app.PokedexMenuBackground=CMUImage(Image.open('PokedexBackground.jpg')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
    app.girlTrainerCard=CMUImage(Image.open('GirlTrainerCard.jpg')) #https://www.emulatorgames.net/roms/gameboy-advance/pokemon-emerald-version/
    app.boyTrainerCard=CMUImage(Image.open('BoyTrainerCard.jpg')) #https://www.emulatorgames.net/roms/gameboy-advance/pokemon-emerald-version/
    app.PokeballSprite=CMUImage(Image.open('Pokeball.png'))  #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
    app.PotionSprite=CMUImage(Image.open('Potion.png'))  #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
    app.poochyena=CMUImage(Image.open('pooch.png'))   #https://www.deviantart.com/noscium/art/pokemon-E-poochyena-mightyena-426227703

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
    drawLabel(app.name,40, 175, align='top-left', size=30, font='orbitron')

def Truck(app):
    
    drawRect(0,0, app.width, app.height, fill='black')
    drawImage(app.truck, app.width/2,app.height/2, width=80*2,height=72*2 ,align='center')
    drawImage(app.direction, app.playerx, app.playery, width=18*2, height=23*2)
    
def Overworld(app):
    drawImage(app.map, app.overworldX, app.overworldY, width=2*2353, height=2*1579)
    if type(app.mystarter)==int:
        drawImage(app.professor, 100, -350+app.dy,width=20*2, height=25*2)
        drawImage(app.poochyena, 100, -300+app.dy,width=20*2, height=25*2)
    if app.Rival1.defeated==False and type(app.mystarter)!=int :
        drawImage(app.wally,200, -350+app.dy,width=20*2, height=25*2)
    drawImage(app.direction,app.Overworldplayerx, app.Overworldplayery, width=20*2, height=25*2)

def Menu(app):
    drawRect(500, 100, 200, 300, fill='white', border='green', borderWidth=12)
    list=['Pokedex', 'Pokemon', 'Bag', app.name]
    for i in range(len(list)):
        drawLabel(list[i], 540, 130+50*i, size=20, align='top-left', bold=True, font='orbitron')
        if app.selectionArrow==i:
            drawRegularPolygon(520, 137+50*i, 13, 3, rotateAngle=90)

def Starter(app):
    mudkip=CMUImage(Image.open('Mudkip.png'))  #https://www.emulatorgames.net/roms/gameboy-advance/pokemon-emerald-version/
    torchic=CMUImage(Image.open('Torchic.png'))  #https://www.emulatorgames.net/roms/gameboy-advance/pokemon-emerald-version/
    treecko=CMUImage(Image.open('Treecko.png'))  #https://www.emulatorgames.net/roms/gameboy-advance/pokemon-emerald-version/
    if app.mystarter%3==0:
        drawImage(torchic, app.width/2,app.height/2,height=app.height, width=app.width+45,align='center')
    if app.mystarter%3==1:
        drawImage(mudkip, app.width/2,app.height/2,height=app.height, width=app.width+45,align='center')
    if app.mystarter%3==2:
        drawImage(treecko, app.width/2,app.height/2,height=app.height, width=app.width+45,align='center')

def Battle(app, opponent):
    app.Win=False
    app.Lose=False
    app.opponent=opponent
    name=str(app.player.pokemon[0])
    pokemonUs=pypokedex.get(name=name)
    name=str(app.opponent.pokemon[0])
    pokemonOppo=pypokedex.get(name=name)
    app.OpponentPokemon=app.opponent.pokemon[0]
    app.PlayerPokemon=app.player.pokemon[0]
    app.spriteFront=pokemonOppo.sprites.front.get('default')
    print(app.spriteFront)
    app.spriteBack=pokemonUs.sprites.back.get('default')
    app.battleArrowX=387
    app.battleArrowY=385
    app.movesArrowX=50
    app.movesArrowY=380
    app.BattleGrass=CMUImage(Image.open('BattleGrass.png')) #http://www.pokemontopaz.net/battlebackgrounds/
    app.BattleBar=CMUImage(Image.open('Battle2.jpg')) #https://www.liveabout.com/pokemon-emerald-cheats-codes-hacks-4588515
    app.BattleMoves=CMUImage(Image.open('BattleMoves.jpg')) # #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
    app.BattleResultBlank=CMUImage(Image.open('BattleResult.jpg')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
    app.battleMoves=False
    app.battleMain=True
    app.battleResults=False

def player(app):
    app.player=Player(app.name)

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
    app.Rival1=Trainer('Rival')
    Poocheyena(app)

def Rival1(app):
    app.Rival1.addPokemon(app.RivalStarter)

def Poocheyena(app):
    app.Poocheyena=Trainer('poochyena')
    pokemon1=Pokemon('poochyena', 2, [None, app.Tackle, None, None])
    app.Poocheyena.addPokemon(pokemon1)

def PokemonMenu(app):
    drawImage(app.PokemonMenuBackground, 0, 0, width=app.width, height=app.height)
    for i in range(6):
        color='cornflowerBlue'
        if i==app.PokemonOn:
            color='lightblue'
        if i%2==0:
            drawRect(75, 40+60*i, 250, 100, fill=color)
        else:
            drawRect(350, 50+60*(i-1), 250, 100, fill=color)

    for i in range(len(app.player.pokemon)):
        if i%2==0:
            drawLabel(f"{app.player.pokemon[i].nickname} LV:{app.player.pokemon[i].level}",75+100, 60+60*i, align='top-left', size=16, font='orbitron' )
            drawImage(app.PokemonMenuSprites[i], 80, 40+60*i)
            PlayerPercentage=app.player.pokemon[i].hp/app.player.pokemon[i].basehp
            drawRect(75+100, 80+60*i, 125, 15, fill='gray', border='black')
            if PlayerPercentage < 0.2:
                fill='red'
            elif PlayerPercentage < 0.5:
                fill='orange'
            else:
                fill='green'
            if PlayerPercentage>0:
                drawRect(75+100, 80+60*i, 125*PlayerPercentage, 15, fill=fill, border='black')
                drawLabel(f'{app.player.pokemon[i].hp}/{app.player.pokemon[i].basehp}', 75+100, 100+60*i, size=20, align='top-left', font='orbitron')
        else:
            drawLabel(f"{app.player.pokemon[i].nickname} LV:{app.player.pokemon[i].level}",350+100, 70+60*(i-1), align='top-left', size=16, font='orbitron')
            drawImage(app.PokemonMenuSprites[i], 350, 50+60*(i-1))
            PlayerPercentage=app.player.pokemon[i].hp/app.player.pokemon[i].basehp
            drawRect(350+100, 90+60*(i-1), 125, 15, fill='gray', border='black')
            if PlayerPercentage < 0.2:
                fill='red'
            elif PlayerPercentage < 0.5:
                fill='orange'
            else:
                fill='green'
            if PlayerPercentage>0:
                drawRect(350+100, 90+60*(i-1), 125*PlayerPercentage, 15, fill=fill, border='black')
                drawLabel(f'{app.player.pokemon[i].hp}/{app.player.pokemon[i].basehp}', 350+100, 110+60*(i-1), size=20, align='top-left', font='orbitron')
    drawLabel("Escape", 585, 420, align='top-left', size=30, bold=True)
def PokemonMenuSprites(app):
    list=[]
    for i in range(len(app.player.pokemon)):
        list.append(app.player.sprite(i))
    return list
        
def ItemMenu(app):
    drawImage(app.ItemMenuBackground, 0, 0, width=app.width, height=app.height)
    i=0
    for item in app.player.item:
        drawLabel(item.upper(), 375, 70+i*50, size=30, font='orbitron', align='top-left')
        drawLabel(f'x {app.player.item[item]}', 625, 70+i*50, size=30, font='orbitron', align='top-left')
        if app.itemSelection==i:
            drawRegularPolygon(350, 70+(i)*50, 13, 3, rotateAngle=90,align='top-left' )
            if item=='pokeball':
                drawImage(app.PokeballSprite,15,215, width=87, height=75)
                drawLabel('Catches wild Pokémon',10, 330, align='top-left', size=30)
            if item=='potion':
                drawImage(app.PotionSprite,15,215, width=87, height=75)
                drawLabel('Restores 20 HP',10, 330, align='top-left', size=30)
        i+=1
   
def NameMenu(app):
    if app.gender=='Female':
        drawImage(app.girlTrainerCard, 0, 0, width=app.width, height=app.height)
    if app.gender=='Male':
        drawImage(app.boyTrainerCard, 0, 0, width=app.width, height=app.height)
    drawLabel(app.name, 160, 135, size=30, align='top-left', font='orbitron', bold=True)
    drawLabel(f"{len(app.player.pokedex)}", 350, 255, size=30, align='top-right', font='orbitron', bold=True)
    drawLabel(app.player.money, 350, 205, size=30,align='top-right', font='orbitron', bold=True)
    drawLabel(f"{(app.time//60)//60}", 350, 300, size=30,align='top-right', font='orbitron', bold=True)

def PokedexMenu(app):
    drawImage(app.PokedexMenuBackground, 0, 0, width=app.width, height=app.height)
    pokedex=sorted(app.player.pokedex)
    for i in range(3):
        pokedex.append(None)
    list=[None, None, None, None, None, None, None]
    Spritelist=[None, None, None, None, None, None, None]
    num=app.Pokedexnum
    for pokemonNum in pokedex:
        if pokemonNum!=None:
            if num+3==7:
                break
            pokemon=pypokedex.get(dex=pokemonNum)
            list[num+3]=f"NO.{pokemonNum} {pokemon.name.upper()}"
            sprite=pokemon.sprites.front.get('default')
            Spritelist[num+3]=sprite
            num+=1
        else:
            if num+3==7:
                break
            list[num+3]=None
            num+=1
    for i in range(7):
        if list[i]!=None:
            drawLabel(list[i],445, 75+54*i, size=20, bold=True, align='top-left')
            if i ==3:
                drawImage(Spritelist[i], 280, 230, align='center', height=150, width=150)

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
    if app.menu==True:
       Menu(app) 
    if app.PokemonMenu==True:
        PokemonMenu(app)
    if app.BagMenu==True:
        ItemMenu(app)
    if app.NameMenu==True:
        NameMenu(app)
    if app.PokedexMenu==True:
        PokedexMenu(app)

def battleBackground(app):
    if app.Lose==False and app.Win==False:
        drawImage(app.BattleGrass, 0, 0, width=app.width, height=(app.width/480)*224)
        drawImage(app.spriteFront, 535, 25, height=150, width=150)
        drawImage(app.spriteBack,0, 175, height=250, width=250)
    #OpponentBox
        drawRect(300,50, 200, 50,fill=rgb(255, 250, 205), border='black')
        drawLabel(f'{str(app.OpponentPokemon.nickname).upper()}    LV {app.OpponentPokemon.level}', 310, 60, size=20, align='top-left', font='orbitron')
        drawRect(310, 80, 175, 15, fill='gray', border='black')
        EnemyPercentage=app.OpponentPokemon.hp/app.OpponentPokemon.basehp
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
        drawLabel(f'{str(app.PlayerPokemon.nickname).upper()}    LV {app.PlayerPokemon.level}', 260, 260, size=20, align='top-left', )
        PlayerPercentage=app.PlayerPokemon.hp/app.PlayerPokemon.basehp
        drawRect(260, 280, 175, 15, fill='gray', border='black')
        if PlayerPercentage < 0.2:
            fill='red'
        elif PlayerPercentage < 0.5:
            fill='orange'
        else:
            fill='green'
        if PlayerPercentage>0:
            drawRect(260, 280, 175*PlayerPercentage, 15, fill=fill, border='black')
            drawLabel(f'{app.PlayerPokemon.hp}/{app.PlayerPokemon.basehp}', 370, 300, size=20, align='top-left', font='orbitron')
        else:
            drawLabel(f'0/{app.PlayerPokemon.basehp}', 370, 300, size=20, align='top-left', font='orbitron')
        if app.battleMain==True:
            drawImage(app.BattleBar, 0, (app.width/480)*224,width=app.width, height=app.height-(app.width/480)*224 )
            drawRegularPolygon(app.battleArrowX, app.battleArrowY, 13, 3, rotateAngle=90)
            drawLabel('What will', 30, 370, size=35, fill='white', align='top-left', font='orbitron')
            drawLabel(f'{app.PlayerPokemon.nickname.upper()} do?', 30, 415, size=35, fill='white',  align='top-left', font='orbitron')
            drawLabel('FIGHT', 410, 373, size=30,align='top-left', font='orbitron')
            drawLabel('POKéMON', 410, 373+52, size=27, align='top-left', font='orbitron')
            drawLabel('BAG', 410+170, 373, size=30,align='top-left', font='orbitron')
            drawLabel('RUN', 410+170, 373+50, size=30,align='top-left', font='orbitron')

        if app.battleMoves==True:
            drawImage(app.BattleMoves, 0, (app.width/480)*224,width=app.width, height=app.height-(app.width/480)*224 )
            x=75
            y=370
            for moves in app.PlayerPokemon.moves:
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
        app.opponent.defeated=True
        drawRect(0,0, app.width, app.height, fill='black')
        drawLabel(f"{app.name} WON", app.width/2, app.height/2, size=40, fill='White')
    if app.Lose==True:
        drawRect(0,0, app.width, app.height, fill='black')
        drawLabel(f"{app.name} Blackout", app.width/2, app.height/2, size=40, fill='White')


def onKeyPress(app, key):
    if app.Win==True or app.Lose==True:
            if key=='x' or key=='enter':
                app.battle=False
                app.battleResults=False
                app.Win=False
                app.Lose=False
                app.overworld=True

    elif app.battle==True:
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
                app.east=CMUImage(Image.open('Right.png')) #https://www.deviantart.com/hyo-oppa/art/WIP-Emerald-Brendan-DPPt-HGSS-Gen-4-Sprite-Sheet-864378236
                app.west=CMUImage(Image.open('Left.png')) #https://www.deviantart.com/hyo-oppa/art/WIP-Emerald-Brendan-DPPt-HGSS-Gen-4-Sprite-Sheet-864378236
                app.north=CMUImage(Image.open('Up.png')) #https://www.deviantart.com/hyo-oppa/art/WIP-Emerald-Brendan-DPPt-HGSS-Gen-4-Sprite-Sheet-864378236
                app.south=CMUImage(Image.open('Down.png')) #https://www.deviantart.com/hyo-oppa/art/WIP-Emerald-Brendan-DPPt-HGSS-Gen-4-Sprite-Sheet-864378236
                app.walkingeast=CMUImage(Image.open('BoyWalkRight.png')) #https://www.deviantart.com/hyo-oppa/art/WIP-Emerald-Brendan-DPPt-HGSS-Gen-4-Sprite-Sheet-864378236
                app.walkingwest=CMUImage(Image.open('BoyWalkLeft.png')) #https://www.deviantart.com/hyo-oppa/art/WIP-Emerald-Brendan-DPPt-HGSS-Gen-4-Sprite-Sheet-864378236
                app.walkingnorth=CMUImage(Image.open('BoyWalkUp.png')) #https://www.deviantart.com/hyo-oppa/art/WIP-Emerald-Brendan-DPPt-HGSS-Gen-4-Sprite-Sheet-864378236
                app.walkingsouth=CMUImage(Image.open('BoyWalkDown.png')) #https://www.deviantart.com/hyo-oppa/art/WIP-Emerald-Brendan-DPPt-HGSS-Gen-4-Sprite-Sheet-864378236
                app.direction=app.east
            elif app.gender%2==1:
                app.gender="Female"
                app.east=CMUImage(Image.open('GirlRight.png')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
                app.west=CMUImage(Image.open('GirlLeft.png')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
                app.north=CMUImage(Image.open('GirlUp.png')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
                app.south=CMUImage(Image.open('GirlDown.png')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
                app.walkingeast=CMUImage(Image.open('GirlWalkingRight.png')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
                app.walkingwest=CMUImage(Image.open('GirlWalkingLeft.png')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
                app.walkingnorth=CMUImage(Image.open('GirlWalkingUp.png')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
                app.walkingsouth=CMUImage(Image.open('GirlWalkingDown.png')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
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
        if key=='right':
            app.mystarter+=1
        if key=='left':
            app.mystarter-=1
        if key=='x':
            print('x')
            if app.mystarter%3==0:
                app.mystarter=Pokemon('torchic', 5, [app.Ember, app.Tackle, None, None])
                app.player.addPokemon(app.mystarter)
                app.player.addPokedex(255)
                app.RivalStarter=Pokemon('mudkip', 5, [None, app.Tackle, None, None])
            elif app.mystarter%3==1:
                app.mystarter=Pokemon('mudkip', 5, [app.WaterGun, app.Tackle, None, None])
                app.player.addPokemon(app.mystarter)
                app.player.addPokedex(258)
                app.RivalStarter=Pokemon('treecko', 5, [None, app.Tackle, None, None])
            elif app.mystarter%3==2:
                app.mystarter=Pokemon('treecko', 5, [app.VineWhip, app.Tackle, None, None])
                app.player.addPokemon(app.mystarter)
                app.player.addPokedex(252)
                app.RivalStarter=Pokemon('torchic', 5, [None, app.Tackle, None, None])
            app.starter=False
            Battle(app, app.Poocheyena)
            app.battle=True
    elif app.overworld==True:
        if key=='escape':
            app.menu=not app.menu
            app.selectionArrow=0
        if app.menu==False:
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
            if app.overworldY<-900:
                if key=='up':
                    if app.direction!=app.north:
                        app.direction=app.north
                    else:
                        app.overworldY-=5
                        app.dy-=5
            if app.overworldY>-2450:
                if key=='down ':
                    if app.direction!=app.south:
                        app.direction=app.south
                    else:
                        app.overworldY+=5
                        app.dy+=5
        elif app.menu==True:
            if key=='up':
                app.selectionArrow-=1
                if app.selectionArrow==-1:
                    app.selectionArrow=3
            if key=='down':
                app.selectionArrow+=1
                if app.selectionArrow==4:
                    app.selectionArrow=0
            if key=='x':
                if app.selectionArrow==0:
                    app.PokedexMenu=True
                    app.Pokedexnum=0
                if app.selectionArrow==1:
                    app.PokemonMenu=True
                    app.PokemonMenuSprites=PokemonMenuSprites(app)
                if app.selectionArrow==2:
                    app.BagMenu=True
                    app.itemSelection=0
                if app.selectionArrow==3: 
                    app.NameMenu=True
                app.menu=False
                app.overworld=False
    elif app.PokemonMenu==True:
        if key=='right':
            app.PokemonOn+=1
            if app.PokemonOn==6:
                app.PokemonOn=0
        if key=='left':
            app.PokemonOn-=1
            if app.PokemonOn==-1:
                app.PokemonOn=5
        if key=='up':
            app.PokemonOn-=2
            if app.PokemonOn==-1:
                app.PokemonOn=5
            if app.PokemonOn==-2:
                app.PokemonOn=4
        if key=='down':
            app.PokemonOn+=2
            if app.PokemonOn==6:
                app.PokemonOn=0
            if app.PokemonOn==7:
                app.PokemonOn=1
        if key=='escape':
            app.PokemonMenu=False
            app.overworld=True
    elif app.BagMenu==True:
        if key=='up':
            app.itemSelection-=1
            if app.itemSelection==-1:
                app.itemSelection=len(app.player.item)-1
        if key=='down':
            app.itemSelection+=1
            if app.itemSelection==len(app.player.item):
                app.itemSelection=0
        if key=='escape':
            app.BagMenu=False
            app.overworld=True
        if key=='x':
            if app.itemSelection==0:
                if app.player.pokemon!=[]:
                    app.player.pokemon[0].hp+=20
                    app.player.item['potion']-=1
                    if app.player.pokemon[0].hp > app.player.pokemon[0].basehp:
                        app.player.pokemon[0].hp=app.player.pokemon[0].basehp

    elif app.NameMenu==True:
        if key=='escape':
            app.NameMenu=False
            app.overworld=True
    elif app.PokedexMenu==True:
        if key=='up':
            app.Pokedexnum+=1
            if app.Pokedexnum==1:
                app.Pokedexnum=-(len(app.player.pokedex)-1)
        if key=='down':
            app.Pokedexnum-=1
            if app.Pokedexnum==-(len(app.player.pokedex)):
                app.Pokedexnum=0
        if key=='escape':
            app.PokedexMenu=False
            app.overworld=True

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
        if app.menu==False:
            if -1000<=app.overworldY<=-900 and app.Overworldplayerx<=50 :
                if 'left' in keys:
                    while app.Overworldplayerx!=app.width/2:
                        app.direction=app.walkingwest
                        app.overworldX+=1
                        app.Overworldplayerx+=1
            if -1000<=app.overworldY<=-900 and app.overworldX<=-2500:
                if 'right' in keys:
                    while app.overworldX!=-2900:
                        app.direction=app.walkingeast
                        app.overworldX-=1
                        app.Overworldplayerx-=1

            if app.overworldX>-2900:
                if 'left' in keys:
                    if app.overworldX<-305 and app.Overworldplayerx==app.width/2:
                        app.direction=app.walkingwest
                        app.overworldX+=5
                    else:
                        app.direction=app.walkingwest
                        app.Overworldplayerx-=5
                if 'right' in keys:
                    if app.overworldX<-305 and app.Overworldplayerx==app.width/2:
                        app.direction=app.walkingeast
                        app.overworldX-=5
                    else:
                        app.direction=app.walkingeast
                        app.Overworldplayerx+=5
                if 'down' in keys:
                        if app.overworldY>-1050 and app.Overworldplayery==app.height/2 :
                            app.direction=app.walkingsouth
                            app.overworldY-=5
                            app.dy-=5
                        else:
                            app.Overworldplayery+=5
                            app.direction=app.walkingsouth

                if 'up' in keys:
                        if app.overworldX>=-600:
                            if app.overworldY<-550 and app.Overworldplayery==app.height/2:
                                app.direction=app.walkingnorth
                                app.overworldY+=5
                                app.dy+=5
                            if app.Overworldplayery<app.height/2:
                                app.overworldY+=5
                                app.direction=app.walkingnorth
                            else:
                                app.Overworldplayery-=5
                                app.direction=app.walkingnorth
                        elif app.overworldY<-900:
                            app.direction=app.walkingnorth
                            app.overworldY+=5
                            app.dy+=5
                        else:
                            app.Overworldplayery-=5
                            app.direction=app.walkingnorth

            elif -2600<=app.overworldY<=-800 and app.overworldX==-2900 :
                if app.overworldY>=-2450 and app.Overworldplayery==app.height/2:
                    if 'down' in keys:
                        app.direction=app.walkingsouth
                        app.overworldY-=5
                        app.dy-=5
                elif app.overworldY<-2450:
                    if 'down' in keys:
                        app.Overworldplayery+=5
                        app.direction=app.walkingsouth
                    if 'up' in keys:
                        app.Overworldplayery-=5
                        app.direction=app.walkingnorth
                if app.overworldY<=-900 and app.Overworldplayery==app.height/2:
                    if 'up' in keys:
                        app.direction=app.walkingnorth
                        app.overworldY+=5
                        app.dy+=5
                elif app.overworldY>-900:
                    if 'down' in keys:
                        app.Overworldplayery+=5
                        app.direction=app.walkingsouth
                    if 'up' in keys:
                        app.Overworldplayery-=5
                        app.direction=app.walkingnorth
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
    if app.menu==False:
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
        if 150<=app.Overworldplayerx<=250 and 450<app.dy<600 and type(app.mystarter)!=int and app.Rival1.defeated==False:
            app.overworld=False
            Rival1(app)
            Battle(app, app.Rival1) 
            app.battle=True
    app.time+=1

class Pokemon:
    def __init__(self, name, level, moves):
        self.level=level
        self.pokemon=pypokedex.get(name=name)
        self.type=self.pokemon.types
        self.name=name.upper()
        self.nickname=name.upper()
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
        self.money=3000
        self.pokemon=[]
        self.item={'potion':5, "pokeball":5}
        self.pokedex=set()


    def addPokemon(self, other):
        self.pokemon.append(other)
    
    def addPokedex(self, other):
        self.pokedex.add(other)
    
    def sprite(self, i):
        pokemon=self.pokemon[i].pokemon
        if i >= len(self.pokemon):
            return None
        return pokemon.sprites.front.get('default')

class Trainer:
    def __init__(self, name):
        self.name=name
        self.money=0
        self.pokemon=[]
        self.defeated=False
    
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