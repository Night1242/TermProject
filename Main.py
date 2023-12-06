import pypokedex
from cmu_graphics import *
from PIL import Image
import random
import pygame

#sprites: https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
#https://downloads.khinsider.com/game-soundtracks/album/pokemon-omega-ruby-and-alpha-sapphire-super-music-complete-nintendo-3ds/1-05%2520Littleroot%2520Town.mp3
#font='orbitron'

# Key X = A
# Key Z = B
# Key Arrow = Move
# Key Escape = Menu
# Key Return = Enter


def onAppStart(app):
    app.width=720
    app.height=480
    app.start=True
    app.start1=False
    app.start2=False
    app.battle=False
    app.Truck=False
    app.opponentMove=None
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
    app.gymX=0
    app.gymY=0
    app.overworld=False
    app.overworldX=-2850
    app.overworldY=-1925
    app.dy=0
    app.dx=0
    app.Overworldplayerx=app.width/2
    app.Overworldplayery=app.height/2
    app.Win=False
    app.Lose=False
    app.time=0
    app.itemSelection=0
    app.PokemonGym=False
    app.PokemonCenter=False
    app.PokemonMart=False
    app.ShopArrow=0
    app.shopMenu=False
    app.Wildbattle=False
    app.caught=False
    app.runAway=False
    app.evolved=set()
    movesList(app)
    trainers(app)
    images(app)
    player(app)
    playIntroSound(app)

def playIntroSound(app): #https://pythonprogramming.net/adding-sounds-music-pygame/
    pygame.mixer.init()
    pygame.mixer.music.load('BestTheme.mp3')
    pygame.mixer.music.play(-1)  # -1 will loop the sound indefinitely

def Start(app):
    introBackground=CMUImage(Image.open('UI Sprites/Intro.png')) #https://www.pinterest.com/pin/151574343683447160/
    drawImage(introBackground, 0,0, align='center')
    drawLabel('Pokemon 112', app.width/2, 200,align='center',size=75, fill='Green' , font='orbitron')
    drawLabel('Press Enter to Start', app.width/2, 285, align='center',size=30, fill='White' , font='orbitron')

def images(app):
    app.map=Image.open('Background Sprites/Map.png') #https://www.deviantart.com/darkshadedx/art/Hoenn-Pokemon-Emerald-Full-Region-Map-796286390
    size=(2*2149, 2*1502)
    app.map=app.map.resize(size)
    app.map=CMUImage(app.map)
    app.map2=Image.open('Background Sprites/MapPixels.jpg')
    app.map2=app.map2.resize(size)
    app.professor=CMUImage(Image.open('Player Trainer Sprites/Professor.png')) #https://forums.pokemmo.com/index.php?/topic/157591-hoenn-overworld-main-story-nds-style-characters-mod/
    app.girl=CMUImage(Image.open('Background Sprites/girl.png')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
    app.boy=CMUImage(Image.open('Background Sprites/boy.png')) #https://www.deviantart.com/hyo-oppa/art/WIP-Emerald-Brendan-DPPt-HGSS-Gen-4-Sprite-Sheet-864378236
    app.truck=CMUImage(Image.open('Background Sprites/Truck.jpg')) #https://www.emulatorgames.net/roms/gameboy-advance/pokemon-emerald-version/
    app.wally=CMUImage(Image.open('Player Trainer Sprites/WallyFront.png')) #https://www.deviantart.com/kleinstudio/art/Kymotonian-Wally-Complete-209209501
    app.PokemonMenuBackground=CMUImage(Image.open('UI Sprites/PokemonMenuBackground.jpg')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
    app.ItemMenuBackground=CMUImage(Image.open('UI Sprites/ItemMenu.jpg')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
    app.PokedexMenuBackground=CMUImage(Image.open('UI Sprites/PokedexBackground.jpg')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
    app.girlTrainerCard=CMUImage(Image.open('UI Sprites/GirlTrainerCard.jpg')) #https://www.emulatorgames.net/roms/gameboy-advance/pokemon-emerald-version/
    app.boyTrainerCard=CMUImage(Image.open('UI Sprites/BoyTrainerCard.jpg')) #https://www.emulatorgames.net/roms/gameboy-advance/pokemon-emerald-version/
    app.PokeballSprite=CMUImage(Image.open('Items Sprites/Pokeball.png'))  #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
    app.PotionSprite=CMUImage(Image.open('Items Sprites/Potion.png'))  #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
    app.poochyena=CMUImage(Image.open('Pokemon Sprites/pooch.png'))   #https://www.deviantart.com/noscium/art/pokemon-E-poochyena-mightyena-426227703
    screenSize=(app.width, app.height)
    app.PokemonCenterBackground=CMUImage(Image.open('Background Sprites/PokemonCenterBackground.png'))
    app.PokemonCenterBackground2=Image.open('Background Sprites/PokemonCenterBackgroundPixels.jpg')
    app.PokemonCenterBackground2=app.PokemonCenterBackground2.resize(screenSize)
    app.PokemonMartBackground=CMUImage(Image.open('Background Sprites/PokemonMartBackground.png'))
    app.PokemonMartBackground2=Image.open('Background Sprites/PokemonMartBackgroundPixels.jpg')
    app.PokemonMartBackground2=app.PokemonMartBackground2.resize(screenSize)
    gymsize=(rounded(178*3), rounded(322*3))
    app.GymBackground=(Image.open('Background Sprites/Gym1Background\.jpg'))
    app.GymBackground=app.GymBackground.resize(gymsize)
    app.GymBackground=CMUImage(app.GymBackground)
    app.GymBackground2=(Image.open('Background Sprites/Gym1Background2.jpg'))
    app.GymBackground2=app.GymBackground2.resize(gymsize)
    app.GymBackground3=CMUImage(Image.open('Background Sprites/GymBackgroundOverlay.png'))
    app.repelSprite=CMUImage(Image.open('Items Sprites/Repel.png'))
    app.berrySprite=CMUImage(Image.open('Items Sprites/berry.png'))
    app.TrainerLeft=CMUImage(Image.open('Player Trainer Sprites/WildTrainerLeft.png'))
    PokemonSprites(app)

def PokemonSprites(app):
    app.f76 =CMUImage(Image.open('Pokemon Sprites/76.png'))
    app.f95 =CMUImage(Image.open('Pokemon Sprites/95.png'))
    app.f112 =CMUImage(Image.open('Pokemon Sprites/112.png'))
    app.f252 =CMUImage(Image.open('Pokemon Sprites/252.png'))
    app.b252 =CMUImage(Image.open('Pokemon Sprites/252-2.png'))
    app.f253 =CMUImage(Image.open('Pokemon Sprites/253.png'))
    app.b253 =CMUImage(Image.open('Pokemon Sprites/253-2.png'))
    app.f254 =CMUImage(Image.open('Pokemon Sprites/254.png'))
    app.b254 =CMUImage(Image.open('Pokemon Sprites/254-2.png'))
    app.f255 =CMUImage(Image.open('Pokemon Sprites/255.png'))
    app.b255 =CMUImage(Image.open('Pokemon Sprites/255-2.png'))
    app.f256 =CMUImage(Image.open('Pokemon Sprites/256.png'))
    app.b256 =CMUImage(Image.open('Pokemon Sprites/256-2.png'))
    app.f257 =CMUImage(Image.open('Pokemon Sprites/257.png'))
    app.b257 =CMUImage(Image.open('Pokemon Sprites/257-2.png'))
    app.f258 =CMUImage(Image.open('Pokemon Sprites/258.png'))
    app.b258 =CMUImage(Image.open('Pokemon Sprites/258-2.png'))
    app.f259 =CMUImage(Image.open('Pokemon Sprites/259.png'))
    app.b259 =CMUImage(Image.open('Pokemon Sprites/259-2.png'))
    app.f260 =CMUImage(Image.open('Pokemon Sprites/260.png'))
    app.b260 =CMUImage(Image.open('Pokemon Sprites/260-2.png'))
    app.f261 =CMUImage(Image.open('Pokemon Sprites/261.png'))
    app.b261 =CMUImage(Image.open('Pokemon Sprites/261-2.png'))
    app.f262 =CMUImage(Image.open('Pokemon Sprites/262.png'))
    app.b262 =CMUImage(Image.open('Pokemon Sprites/262-2.png'))
    app.f263 =CMUImage(Image.open('Pokemon Sprites/263.png'))
    app.b263 =CMUImage(Image.open('Pokemon Sprites/263-2.png'))
    app.f264 =CMUImage(Image.open('Pokemon Sprites/264.png'))
    app.b264 =CMUImage(Image.open('Pokemon Sprites/264-2.png'))
    app.f265 =CMUImage(Image.open('Pokemon Sprites/265.png'))
    app.b265 =CMUImage(Image.open('Pokemon Sprites/265-2.png'))
    app.f266 =CMUImage(Image.open('Pokemon Sprites/266.png'))
    app.b266 =CMUImage(Image.open('Pokemon Sprites/266-2.png'))
    app.f267 =CMUImage(Image.open('Pokemon Sprites/267.png'))
    app.b267 =CMUImage(Image.open('Pokemon Sprites/267-2.png'))
    app.f268 =CMUImage(Image.open('Pokemon Sprites/268.png'))
    app.b268 =CMUImage(Image.open('Pokemon Sprites/268-2.png'))
    app.f269 =CMUImage(Image.open('Pokemon Sprites/269.png'))
    app.b269 =CMUImage(Image.open('Pokemon Sprites/269-2.png'))
    app.f270 =CMUImage(Image.open('Pokemon Sprites/270.png'))
    app.b270 =CMUImage(Image.open('Pokemon Sprites/270-2.png'))
    app.f271 =CMUImage(Image.open('Pokemon Sprites/271.png'))
    app.b271 =CMUImage(Image.open('Pokemon Sprites/271-2.png'))
    app.f272 =CMUImage(Image.open('Pokemon Sprites/272.png'))
    app.b272 =CMUImage(Image.open('Pokemon Sprites/272-2.png'))
    app.f280 =CMUImage(Image.open('Pokemon Sprites/280.png'))
    app.b280 =CMUImage(Image.open('Pokemon Sprites/280-2.png'))
    app.f281 =CMUImage(Image.open('Pokemon Sprites/281.png'))
    app.b281 =CMUImage(Image.open('Pokemon Sprites/281-2.png'))
    app.f282 =CMUImage(Image.open('Pokemon Sprites/282.png'))
    app.b282 =CMUImage(Image.open('Pokemon Sprites/282-2.png'))
    app.f299 =CMUImage(Image.open('Pokemon Sprites/299.png'))
    app.f304 =CMUImage(Image.open('Pokemon Sprites/304.png'))
    app.f306 =CMUImage(Image.open('Pokemon Sprites/306.png'))
    app.f337 =CMUImage(Image.open('Pokemon Sprites/337.png'))
    app.f338 =CMUImage(Image.open('Pokemon Sprites/338.png'))
    app.f377 =CMUImage(Image.open('Pokemon Sprites/377.png'))
    app.f476 =CMUImage(Image.open('Pokemon Sprites/476.png'))

def Start1(app):
    if app.gender%2==0:
        drawImage(app.boy, app.width/2,app.height/2,height=app.height, width=app.width+45,align='center')
    if app.gender%2==1:
        drawImage(app.girl, app.width/2,app.height/2,height=app.height, width= app.width+45,align='center')

def Start2(app):
    if app.gender=="Male":
        boy=CMUImage(Image.open('Background Sprites/boy1.png'))
        drawImage(boy, app.width/2,app.height/2,height=app.height, width=app.width+45,align='center')
    if app.gender=="Female":
        girl=CMUImage(Image.open('Background Sprites/girl1.png'))
        drawImage(girl, app.width/2,app.height/2,height=app.height, width= app.width+45,align='center')
    drawRect(25, 150, 300, 75, fill='white', border='green', borderWidth=10)
    drawLabel(app.name,40, 175, align='top-left', size=30, font='orbitron')

def Truck(app):
    drawRect(0,0, app.width, app.height, fill='black')
    drawImage(app.truck, app.width/2,app.height/2, width=80*2,height=72*2 ,align='center')
    drawImage(app.direction, app.playerx, app.playery, width=18*2, height=23*2)
    
def Overworld(app):
    drawImage(app.map, app.overworldX, app.overworldY, align='top-left')
    if type(app.mystarter)==int:
        drawImage(app.professor, 500+app.dx, -250+app.dy,width=20*2, height=25*2)
        drawImage(app.poochyena, 500+app.dx, -200+app.dy,width=20*2, height=25*2)
    if app.Rival1.defeated==False and type(app.mystarter)!=int:
        drawImage(app.wally,600+app.dx, -700+app.dy,width=20*2, height=25*2)
    if app.Trainer1.defeated==False:
        drawImage(app.TrainerLeft, 900 +app.dx, -500+app.dy,width=20*2, height=25*2)
    drawImage(app.direction,app.Overworldplayerx, app.Overworldplayery, width=20*2, height=25*2)

def Menu(app):
    drawRect(500, 100, 200, 300, fill='white', border='green', borderWidth=12)
    list=['Pokedex', 'Pokemon', 'Bag', app.name]
    for i in range(len(list)):
        drawLabel(list[i], 540, 130+50*i, size=20, align='top-left', bold=True, font='orbitron')
        if app.selectionArrow==i:
            drawRegularPolygon(520, 137+50*i, 13, 3, rotateAngle=90)

def Starter(app):
    mudkip=CMUImage(Image.open('Background Sprites/Mudkip.png'))  #https://www.emulatorgames.net/roms/gameboy-advance/pokemon-emerald-version/
    torchic=CMUImage(Image.open('Background Sprites/Torchic.png'))  #https://www.emulatorgames.net/roms/gameboy-advance/pokemon-emerald-version/
    treecko=CMUImage(Image.open('Background Sprites/Treecko.png'))  #https://www.emulatorgames.net/roms/gameboy-advance/pokemon-emerald-version/
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
    app.OpponentPokemon=app.opponent.pokemon[0]
    name=str(app.player.pokemon[0])
    app.pokemonUs=pypokedex.get(name=name)
    name=str(app.opponent.pokemon[0])
    app.pokemonOppo=pypokedex.get(name=name)
    app.PlayerPokemon=app.player.pokemon[0]
    app.spriteFront=app.OpponentPokemon.frontsprites(app)
    app.spriteBack=app.PlayerPokemon.backsprites(app)
    app.battleArrowX=387
    app.battleArrowY=385
    app.movesArrowX=50
    app.movesArrowY=380
    app.BattleGrass=CMUImage(Image.open('Background Sprites/BattleGrass.png')) #http://www.pokemontopaz.net/battlebackgrounds/
    app.BattleBar=CMUImage(Image.open('UI Sprites/Battle2.jpg')) #https://www.liveabout.com/pokemon-emerald-cheats-codes-hacks-4588515
    app.BattleMoves=CMUImage(Image.open('UI Sprites/BattleMoves.jpg')) # #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
    app.BattleResultBlank=CMUImage(Image.open('UI Sprites/BattleResult.jpg')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
    app.battleMoves=False
    app.battleMain=True
    app.battleResults=False

def WildBattle(app, opponent):
    app.Win=False
    app.Lose=False
    app.OpponentPokemon=opponent
    name=str(app.player.pokemon[0])
    app.pokemonUs=pypokedex.get(name=name)
    name=app.OpponentPokemon.name
    app.pokemonOppo=pypokedex.get(name=name)
    app.PlayerPokemon=app.player.pokemon[0]
    app.spriteFront=app.OpponentPokemon.frontsprites(app)
    app.spriteBack=app.PlayerPokemon.backsprites(app)
    app.battleArrowX=387
    app.battleArrowY=385
    app.movesArrowX=50
    app.movesArrowY=380
    app.BattleGrass=CMUImage(Image.open('Background Sprites/BattleGrass.png')) #http://www.pokemontopaz.net/battlebackgrounds/
    app.BattleBar=CMUImage(Image.open('UI Sprites/Battle2.jpg')) #https://www.liveabout.com/pokemon-emerald-cheats-codes-hacks-4588515
    app.BattleMoves=CMUImage(Image.open('UI Sprites/BattleMoves.jpg')) # #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
    app.BattleResultBlank=CMUImage(Image.open('UI Sprites/BattleResult.jpg')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
    app.battleMoves=False
    app.battleMain=True
    app.battleResults=False

def player(app):
    app.player=Player(app.name)

def movesList(app):
    app.Tackle=Moves("Tackle", 35, 40, 100, "Normal", 'physical')
    app.Crunch=Moves("Crunch", 35, 80, 100, "Dark", 'physical')
    app.BugBite=Moves("Bug Bite", 35, 60, 100, "Bug", 'physical')
    app.Confusion=Moves("Confusion", 35, 50, 100, "Psychic", 'physical')
    app.Thunderbolt=Moves("Thunderbolt", 15, 90, 100, "Electric", 'special')
    app.WaterGun=Moves("Water Gun", 25, 40, 100, "Water", 'special')
    app.Ember=Moves("Ember", 25, 40, 100, "Fire", 'special')
    app.VineWhip=Moves("Vine Whip", 10, 45, 100, "Grass", 'physical')
    app.IceBeam=Moves("Ice Beam", 10, 90, 100, "Ice", 'special')
    app.Earthquake=Moves("Earthquake", 10, 100, 100, "Ground", 'physical')
    app.Psychic=Moves("Psychic", 10, 90, 100, "Psychic", 'special')
    app.ShadowBall=Moves("Shadow Ball", 15, 80, 100, "Ghost", 'special')
    app.SludgeBomb=Moves("Sludge Bomb", 10, 90, 100, "Poison", 'special')
    app.AerialAce=Moves("Aerial Ace", 20, 60, 100, "Flying", 'physical')
    app.RockSlide=Moves("Rock Slide", 10, 75, 90, "Rock", 'physical')
    app.StoneEdge=Moves("Stone Edge", 10, 100, 90, "Rock", 'physical')
    app.AncientPower=Moves("Ancient Power", 60, 100, 90, "Rock", 'special')
    app.DragonClaw=Moves("Dragon Claw", 15, 80, 100, "Dragon", 'physical')
    app.Surf=Moves("Surf", 15, 90, 100, "Water", 'special'),
    app.Thunder=Moves("Thunder", 10, 110, 70, "Electric", 'special')
    app.FireBlast=Moves("Fire Blast", 5, 110, 85, "Fire", 'special')
    
    app.Growl=Moves("Growl", 40, "-Attack", 100, "Normal", "status") #Lowers Attack
    app.Confide=Moves("Confide", 20, '-spAttack', 100, "Normal", "status") #Lowers spAttack
    app.Leer=Moves("Leer", 30, "-Defense", 100, "Normal", 'status') #Lowers Defense
    app.FakeTears=Moves("Fake Tears", 20, '-spDefense', 100, "Dark", 'status')  #Lowers SpDefense
    app.ScaryFace=Moves("ScaryFace", 20, '-speed', 100, "Normal", 'status') #Lowers Speed

    app.SwordsDance=Moves("Swords Dance", 20, "+Attack", 100, "Normal", "status") #Increases Attack
    app.NastyPlot=Moves("Nasty Plot", 20, '+spAttack', 100, 'Dark', "status") #Increases spAttack
    app.Harden=Moves("Harden", 30, '+Defense', 100, "Normal", 'status') #Increases Defense
    app.Amnesia=Moves("Amnesia", 20, "+spDefense", 100, "Dark", 'status')  #Increases SpDefense
    app.Agility=Moves("Agility", 20, '+speed', 100, "Psychic", 'status') #Increases Speed
    app.Recover=Moves("Recover", 20, '+HP', 100, "Normal", 'status') #Increases HP




def trainers(app):
    app.Rival1=Trainer('Rival', 500)
    Poocheyena(app)
    Trainer1(app)
    GymTrainer1(app)
    GymTrainer2(app)
    GymTrainer3(app)
    GymTrainer4(app)
    GymLeader(app)


def Rival1(app):
    app.Rival1.addPokemon(app.RivalStarter)

def Trainer1(app):
    app.Trainer1=Trainer('Trainer', 200)
    pokemon1=Pokemon('zigzagoon', 3, [app.Growl, app.Tackle, None, None])
    pokemon2=Pokemon('wurmple', 3, [app.ScaryFace, app.Tackle, None, None])
    app.Trainer1.addPokemon(pokemon1)
    app.Trainer1.addPokemon(pokemon2)

def Poocheyena(app):
    app.Poocheyena=Trainer('poochyena', 0)
    pokemon1=Pokemon('poochyena', 2, [app.Growl, app.Tackle, None, None])
    app.Poocheyena.addPokemon(pokemon1)

def GymTrainer1(app):
    pokemon1=Pokemon('lunatone', 15, [app.NastyPlot, app.AncientPower, app.Earthquake, app.Psychic])
    app.GymTrainer1=Trainer('Gym Trainer', 500)
    app.GymTrainer1.addPokemon(pokemon1)

def GymTrainer2(app):
    pokemon1=Pokemon('solrock', 15, [app.NastyPlot, app.AncientPower, app.Earthquake, app.Psychic])
    app.GymTrainer2=Trainer('Gym Trainer', 500)
    app.GymTrainer2.addPokemon(pokemon1)

def GymTrainer3(app):
    pokemon1=Pokemon('rhydon', 10, [app.Leer, app.RockSlide, app.Earthquake, app.Harden])
    pokemon2=Pokemon('onix', 10, [app.Leer, app.RockSlide, app.Earthquake, app.Harden])
    app.GymTrainer3=Trainer('Gym Trainer', 500)
    app.GymTrainer3.addPokemon(pokemon1)
    app.GymTrainer3.addPokemon(pokemon2)

def GymTrainer4(app):
    pokemon1=Pokemon('aron', 10, [app.Leer, app.RockSlide, app.Earthquake, app.Harden])
    pokemon2=Pokemon('nosepass', 10, [app.SwordsDance, app.AncientPower, app.Earthquake, app.Harden])
    app.GymTrainer4=Trainer('Gym Trainer', 500)
    app.GymTrainer4.addPokemon(pokemon1)
    app.GymTrainer4.addPokemon(pokemon2)

def GymLeader(app):
    pokemon1=Pokemon('golem', 16, [app.DragonClaw, app.StoneEdge, app.Earthquake, app.Harden])
    pokemon2=Pokemon('aggron', 16, [app.SwordsDance, app.StoneEdge, app.Earthquake, app.Harden])
    pokemon3=Pokemon('probopass', 16, [app.Thunder, app.StoneEdge, app.Earthquake, app.Harden])
    pokemon4=Pokemon('regirock', 16, [app.ScaryFace, app.StoneEdge, app.Earthquake, app.Harden])
    app.GymLeader=Trainer('Gym Leader', 1000)
    app.GymLeader.addPokemon(pokemon1)
    app.GymLeader.addPokemon(pokemon2)
    app.GymLeader.addPokemon(pokemon3)
    app.GymLeader.addPokemon(pokemon4)


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
        list.append(app.player.sprite(app, i))
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
            if item=='repel':
                drawImage(app.repelSprite,56,250,width=14*3, height=22*3, align='center')
                drawLabel('Repels Pokemon',10, 330, align='top-left', size=30)
                drawLabel('for a bit',10, 360, align='top-left', size=30)
            if item=='berry':
                drawImage(app.berrySprite,56,250, width=19*3, height=18*3, align='center')
                drawLabel('Heals Pokemon mid-battle',10, 330, align='top-left', size=25)
                drawLabel('when HP is critical',10, 360, align='top-left', size=25)
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
            sprite=getSprite(app, pokemonNum, 'front')
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

def pokemonCenter(app):
    drawRect(0,0, app.width, app.height, fill='black')
    drawImage(app.PokemonCenterBackground, app.width/2, app.height/2, align='center', width=app.width, height=app.height)
    drawImage(app.direction, app.playerx, app.playery, width=18*3, height=23*3)

def pokemonMart(app):
    drawRect(0,0, app.width, app.height, fill='black')
    drawImage(app.PokemonMartBackground, app.width/2, app.height/2, align='center',width=app.width, height=app.height)
    drawImage(app.direction, app.playerx, app.playery, width=18*3, height=23*3)

def pokemonGym(app):
    drawRect(0,0, app.width, app.height, fill='black')
    drawImage(app.GymBackground, app.gymX, app.gymY)
    drawImage(app.direction, app.width/2, app.height/2, width=18*2, height=23*2)
    drawImage(app.GymBackground3,app.width/2, app.height/2, align='center')

def shopMenu(app):
    drawRect(500, 100-50, 200, 400, fill='white', border='blue', borderWidth=12)
    drawRect(34, 36, 150, 50, fill='white', border='blue',borderWidth=6)
    drawLabel(f'{app.player.money}', 44, 46, size=40, bold=True, align='top-left')
    list=['POTION 200', 'POKEBALL 300', 'REPEL 500', 'BERRY 400']
    for i in range(len(list)):
        drawLabel(list[i], 540, 130-50+50*i, size=20, align='top-left', bold=True, font='orbitron')
        if app.ShopArrow==i:
            drawRegularPolygon(520, 137-50+50*i, 13, 3, rotateAngle=90)

def redrawAll(app):
    if app.battle==True or app.Wildbattle==True:
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
    if app.caught==True:
        if len(app.player.pokemon) != 6:
            drawLabel(f'{app.OpponentPokemon} was Caught', app.width/2, app.height/2, align='center', size=20)
        if len(app.player.pokemon) == 6:
            drawLabel(f'{app.OpponentPokemon} was Caught', app.width/2, app.height/2, align='center', size=20)
            drawLabel(f'TEAM WAS FULL, SENT TO PC', app.width/2, app.height/2+100, align='center', size=20)
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
    if app.PokemonCenter==True:
        pokemonCenter(app)
    if app.PokemonGym==True:
        pokemonGym(app)
    if app.PokemonMart==True:
        pokemonMart(app)
    if app.shopMenu==True:
        shopMenu(app)
    if app.runAway==True:
        drawLabel('YOU RAN AWAY', app.width/2, app.height/2, align='center', size=30, bold=True)
    if app.evolved != {}:
        i=0
        for pokemonNum in app.evolved:
            nextNum=pokemonNum + 1
            drawLabel(f'{pypokedex.get(dex=pokemonNum).name.upper()} evolved into {pypokedex.get(dex=nextNum).name.upper()}', app.width/2, app.height/2+50*(i+1), align='center', size=25, bold=True)
            i+=1

def battleBackground(app):
    if app.battle==True:
        if app.Lose==False and app.Win==False:
            drawImage(app.BattleGrass, 0, 0, width=app.width, height=(app.width/480)*224)
            drawImage(app.spriteFront, 535, 25, height=150, width=150)
            drawImage(app.spriteBack,0, 175, height=250, width=250)
        #OpponentBox
            drawRect(300,50, 225, 50,fill=rgb(255, 250, 205), border='black')
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
            drawRect(250,250, 225, 75,fill=rgb(255, 250, 205), border='black')
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
                drawLabel('CATCH', 410+170, 373, size=30,align='top-left', font='orbitron')
                drawLabel('RUN', 410+170, 373+50, size=30,align='top-left', font='orbitron')

            if app.battleMoves==True:
                drawImage(app.BattleMoves, 0, (app.width/480)*224,width=app.width, height=app.height-(app.width/480)*224 )
                x=75
                y=370
                for moves in app.PlayerPokemon.moves:
                    if moves==None:
                        continue
                    moves=moves.name
                    drawLabel(moves, x, y, size=30, align='top-left', font='orbitron')
                    if x==75:
                        x+=190
                    elif x==190+75:
                        x=75
                        y+=50
                drawRegularPolygon(app.movesArrowX, app.movesArrowY, 13, 3, rotateAngle=90)
                if app.movesSelected!=None:
                    drawLabel(f"{app.movesSelected.basepp}/{app.movesSelected.pp}", 600, 380, size=30, font='orbitron')
                    drawLabel(f"TYPE/{app.movesSelected.type}", 600, 430, size=30, font='orbitron')
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
                for pokemon in app.player.pokemon:
                    pokemon.attack=pokemon.baseattack
                    pokemon.defense=pokemon.basedefense
                    pokemon.spAttack=pokemon.basespAttack
                    pokemon.spDefense=pokemon.basespDefense
                    pokemon.speed=pokemon.basespeed
                if app.Wildbattle==False:
                    app.player.money+=app.opponent.money
                app.battleResults=False
                app.Win=False
                app.Lose=False
                if app.opponent == app.GymTrainer3 or app.opponent == app.GymTrainer1 or app.opponent == app.GymTrainer2 or app.opponent == app.GymTrainer4 or app.opponent == app.GymLeader:
                    app.PokemonGym=True
                else:
                    app.overworld=True
                app.battle=False
                app.Wildbattle=False
    if app.caught==True:
        if key=='x':
            app.caught=False
            app.overworld=True
    if app.evolved != set():
        if key=='x':
            app.evolved=set()
    if app.runAway==True:
        app.runAway=False
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
                if app.battleArrowX==387+170 and app.battleArrowY == 385:
                    if app.Wildbattle==True and app.player.item['pokeball']!=0:
                        if len(app.player.pokemon) < 6:
                            app.player.pokemon.append(app.OpponentPokemon)
                            moves=app.OpponentPokemon.moves
                            app.player.pokemon[-1].moves=moves
                        name=app.OpponentPokemon.name
                        pokemon=pypokedex.get(name=name)
                        dexNum=pokemon.dex    
                        app.player.pokedex.add(dexNum)
                        app.battleMain=False
                        app.battleMoves=False
                        app.battleResults=False
                        app.Wildbattle=False
                        app.battle=False
                        app.Win=True
                        app.caught=True
                        i=0
                        for pokemon in app.player.pokemon:
                            pokemon.EXP += 300
                            pokemon.LevelUp(app)
                            if evolve(app, pokemon) != False or  evolve(app, pokemon)!= None:
                                app.player.pokemon[i]=evolve(app, pokemon)
                            i+=1
                        app.player.item['pokeball']-=1
                if app.battleArrowX==387+170 and app.battleArrowY == 385+50:
                    if app.Wildbattle==True:
                        app.battle=False
                        app.runAway=True
                if app.battleArrowX==387 and app.battleArrowY == 385+50:
                    pass
                
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
                lastmove=None
                if app.movesSelected!=None:
                    if app.player.pokemon[0].speed >= app.OpponentPokemon.speed:
                        app.resultList=[f"{(app.player.pokemon[0].nickname.upper())} used {app.movesSelected.name.upper()} "]
                        app.player.pokemon[0].damage(app, app.movesSelected, app.OpponentPokemon)
                        if app.OpponentPokemon.hp>0:
                            if  app.opponentMove!=None:
                                if app.opponentMove.attack=='status':
                                    lastmove='status'
                            app.opponentMove=None
                            app.opponentStatusOptions=[]
                            app.opponentMovesOptions=[]
                            for moves in app.OpponentPokemon.moves:
                                if moves == None:
                                    continue
                                if effective(moves, app.player.pokemon[0]) == 2:
                                    app.opponentMove=moves
                                elif effective(moves, app.player.pokemon[0]) == 1 and moves.attack!='status':
                                    app.opponentMovesOptions.append(moves)
                                if moves.attack=='status':
                                    app.opponentStatusOptions.append(moves)
                            if app.opponentMove == None and len(app.opponentMovesOptions)!=1:
                                app.opponentMove=app.opponentMovesOptions[random.randrange(0, len(app.opponentMovesOptions)-1)]
                            elif app.opponentMove == None and len(app.opponentMovesOptions) == 1:
                                app.opponentMove=app.opponentMovesOptions[0]
                            if len(app.opponentStatusOptions)>1 and 0.75<(app.OpponentPokemon.hp/app.OpponentPokemon.basehp) and 0.75<(app.player.pokemon[0].hp/app.player.pokemon[0].basehp) and lastmove!='status':
                                app.opponentMove=app.opponentStatusOptions[random.randrange(0, len(app.opponentStatusOptions)-1)]
                            elif len(app.opponentStatusOptions)==1 and 0.75>(app.OpponentPokemon.hp/app.OpponentPokemon.basehp) and 0.75<(app.player.pokemon[0].hp/app.player.pokemon[0].basehp) and lastmove!='status':
                                app.opponentMove=app.opponentStatusOptions[0]
                            app.resultList.append(f"{(app.OpponentPokemon.nickname.upper())} used {app.opponentMove.name.upper()} ")
                            app.OpponentPokemon.damage(app, app.opponentMove, app.player.pokemon[0])
                        else: 
                            app.resultList.append(f"{(app.OpponentPokemon.nickname.upper())} fainted!")
                            if app.Wildbattle==False:
                                app.opponent.pokemon.pop(0)
                                i=0
                                for pokemon in app.player.pokemon:
                                    pokemon.EXP += 300
                                    pokemon.LevelUp(app)
                                    if evolve(app, pokemon)!=False or evolve(app, pokemon)!=None:
                                        app.player.pokemon[i]=evolve(app, pokemon)
                                    i+=1
                                if app.opponent.pokemon !=[]:
                                    app.OpponentPokemon=app.opponent.pokemon[0]
                                    app.spriteFront=app.OpponentPokemon.frontsprites(app)
                                if len(app.opponent.pokemon)>1:
                                    app.resultList.append(f"Opponent sent out {(app.opponent.pokemon[1].nickname.upper())}")
            
                            
                    elif app.player.pokemon[0].speed < app.OpponentPokemon.speed:
                        if app.OpponentPokemon.hp>0:
                            if  app.opponentMove!=None:
                                if app.opponentMove.attack=='status':
                                    lastmove='status'
                            app.opponentMove=None
                            app.opponentStatusOptions=[]
                            app.opponentMovesOptions=[]
                            for moves in app.OpponentPokemon.moves:
                                if moves == None:
                                    continue
                                if effective(moves, app.player.pokemon[0]) == 2:
                                    app.opponentMove=moves
                                elif effective(moves, app.player.pokemon[0]) == 1:
                                    app.opponentMovesOptions.append(moves)
                                if moves.attack=='status':
                                    app.opponentStatusOptions.append(moves)
                            if app.opponentMove == None and len(app.opponentMovesOptions)!=1:
                                app.opponentMove=app.opponentMovesOptions[random.randrange(0, len(app.opponentMovesOptions)-1)]
                            elif app.opponentMove == None and len(app.opponentMovesOptions) == 1:
                                app.opponentMove=app.opponentMovesOptions[0]
                            if len(app.opponentStatusOptions)>1 and 0.75<(app.OpponentPokemon.hp/app.OpponentPokemon.basehp) and 0.75<(app.player.pokemon[0].hp/app.player.pokemon[0].basehp) and lastmove!='status':
                                app.opponentMove=app.opponentStatusOptions[random.randrange(0, len(app.opponentStatusOptions)-1)]
                            elif len(app.opponentStatusOptions)==1 and 0.75>(app.OpponentPokemon.hp/app.OpponentPokemon.basehp) and 0.75<(app.player.pokemon[0].hp/app.player.pokemon[0].basehp) and lastmove!='status':
                                app.opponentMove=app.opponentStatusOptions[0]
                            app.resultList=[(f"{(app.OpponentPokemon.nickname.upper())} used {app.opponentMove.name.upper()} ")]
                            app.OpponentPokemon.damage(app, app.opponentMove, app.player.pokemon[0])
                        if app.player.pokemon[0].hp>0:
                            app.resultList.append(f"{(app.player.pokemon[0].nickname.upper())} used {app.movesSelected.name.upper()} ")
                            app.player.pokemon[0].damage(app, app.movesSelected, app.OpponentPokemon)
                            if app.OpponentPokemon.hp <=0:
                                i=0
                                for pokemon in app.player.pokemon:
                                    pokemon.EXP += 300
                                    pokemon.LevelUp(app)
                                    if evolve(app, pokemon)!=False or evolve(app, pokemon) != None:
                                        app.player.pokemon[i]=evolve(app, pokemon)
                                    i+=1
                                    
                    
                    app.battleMain=False
                    app.battleMoves=False
                    app.battleResults=True
    
        elif app.battleResults==True:
            if app.Wildbattle==False:
                if key=='x' or key=='z':
                    app.resultList.pop(0)
                    if len(app.resultList)==0:
                        if app.player.pokemon[0] != None and app.player.pokemon[0].hp<=0:
                            app.player.pokemon[0].hp=0
                            fainted=app.player.pokemon.pop(0)
                            app.player.pokemon.append(fainted)
                            app.PlayerPokemon=app.player.pokemon[0]
                            app.spriteBack=app.PlayerPokemon.backsprites(app)
                            lose=0
                            for pokemon in app.player.pokemon:
                                if pokemon.hp <= 0:
                                    lose+=1
                            if lose==len(app.player.pokemon):
                                app.Lose=True
                        if len(app.opponent.pokemon)==0:
                            app.Win=True
                        else:
                            lose=0
                            for pokemon in app.opponent.pokemon:
                                if pokemon.hp<=0:
                                    lose+=1
                            if lose == len(app.opponent.pokemon):
                                app.Win=True
                        app.battleMain=True
                        app.battleMoves=False
                        app.battleResults=False
            if app.Wildbattle==True:
                if key=='x' or key=='z':
                    app.resultList.pop(0)
                    if len(app.resultList)==0:
                        if app.player.pokemon[0].hp<=0:
                            app.player.pokemon[0].hp=0
                            fainted=app.player.pokemon.pop(0)
                            app.player.pokemon.append(fainted)
                            app.PlayerPokemon=app.player.pokemon[0]
                            app.spriteBack=app.PlayerPokemon.backsprites(app)
                            lose=0
                            for pokemon in app.player.pokemon:
                                if pokemon.hp <= 0:
                                    lose+=1
                            if lose==len(app.player.pokemon):
                                app.Lose=True
                        if app.OpponentPokemon.hp<=0:
                            app.Win=True
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
                app.east=CMUImage(Image.open('Player Trainer Sprites/Right.png')) #https://www.deviantart.com/hyo-oppa/art/WIP-Emerald-Brendan-DPPt-HGSS-Gen-4-Sprite-Sheet-864378236
                app.west=CMUImage(Image.open('Player Trainer Sprites/Left.png')) #https://www.deviantart.com/hyo-oppa/art/WIP-Emerald-Brendan-DPPt-HGSS-Gen-4-Sprite-Sheet-864378236
                app.north=CMUImage(Image.open('Player Trainer Sprites/Up.png')) #https://www.deviantart.com/hyo-oppa/art/WIP-Emerald-Brendan-DPPt-HGSS-Gen-4-Sprite-Sheet-864378236
                app.south=CMUImage(Image.open('Player Trainer Sprites/Down.png')) #https://www.deviantart.com/hyo-oppa/art/WIP-Emerald-Brendan-DPPt-HGSS-Gen-4-Sprite-Sheet-864378236
                app.walkingeast=CMUImage(Image.open('Player Trainer Sprites/BoyWalkRight.png')) #https://www.deviantart.com/hyo-oppa/art/WIP-Emerald-Brendan-DPPt-HGSS-Gen-4-Sprite-Sheet-864378236
                app.walkingwest=CMUImage(Image.open('Player Trainer Sprites/BoyWalkLeft.png')) #https://www.deviantart.com/hyo-oppa/art/WIP-Emerald-Brendan-DPPt-HGSS-Gen-4-Sprite-Sheet-864378236
                app.walkingnorth=CMUImage(Image.open('Player Trainer Sprites/BoyWalkUp.png')) #https://www.deviantart.com/hyo-oppa/art/WIP-Emerald-Brendan-DPPt-HGSS-Gen-4-Sprite-Sheet-864378236
                app.walkingsouth=CMUImage(Image.open('Player Trainer Sprites/BoyWalkDown.png')) #https://www.deviantart.com/hyo-oppa/art/WIP-Emerald-Brendan-DPPt-HGSS-Gen-4-Sprite-Sheet-864378236
                app.direction=app.east
            elif app.gender%2==1:
                app.gender="Female"
                app.east=CMUImage(Image.open('Player Trainer Sprites/GirlRight.png')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
                app.west=CMUImage(Image.open('Player Trainer Sprites/GirlLeft.png')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
                app.north=CMUImage(Image.open('Player Trainer Sprites/GirlUp.png')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
                app.south=CMUImage(Image.open('Player Trainer Sprites/GirlDown.png')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
                app.walkingeast=CMUImage(Image.open('Player Trainer Sprites/GirlWalkingRight.png')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
                app.walkingwest=CMUImage(Image.open('Player Trainer Sprites/GirlWalkingLeft.png')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
                app.walkingnorth=CMUImage(Image.open('Player Trainer Sprites/GirlWalkingUp.png')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
                app.walkingsouth=CMUImage(Image.open('Player Trainer Sprites/GirlWalkingDown.png')) #https://www.spriters-resource.com/game_boy_advance/pokemonemerald/
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
            if app.mystarter%3==0:
                app.mystarter=Pokemon('torchic', 5, [app.Ember, app.Tackle, app.Growl, None])
                app.player.addPokemon(app.mystarter)
                app.player.addPokedex(255)
                app.RivalStarter=Pokemon('mudkip', 5, [app.Tackle, app.WaterGun, app.ScaryFace, None])
            elif app.mystarter%3==1:
                app.mystarter=Pokemon('mudkip', 5, [app.WaterGun, app.Tackle, app.ScaryFace, None])
                app.player.addPokemon(app.mystarter)
                app.player.addPokedex(258)
                app.RivalStarter=Pokemon('treecko', 5, [app.VineWhip, app.Tackle, app.Leer, None])
            elif app.mystarter%3==2:
                app.mystarter=Pokemon('treecko', 5, [app.VineWhip, app.Tackle, app.Leer, None])
                app.player.addPokemon(app.mystarter)
                app.player.addPokedex(252)
                app.RivalStarter=Pokemon('torchic', 5, [app.Ember, app.Tackle, app.Growl, None])
            app.starter=False
            Battle(app, app.Poocheyena)
            app.battle=True
    elif app.overworld==True:
        if key=='escape':
            app.menu=not app.menu
            app.selectionArrow=0
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
                if app.player.item['potion']!=0:
                    if app.player.pokemon!=[]:
                        app.player.pokemon[0].hp+=20
                        app.player.item['potion']-=1
                        if app.player.pokemon[0].hp > app.player.pokemon[0].basehp:
                            app.player.pokemon[0].hp=app.player.pokemon[0].basehp
            if app.itemSelection==2:
                if app.player.item['repel']!=0:
                    app.player.repel+=500
                    app.player.item['repel']-=1
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
    elif app.PokemonCenter==True:
        if key=='x':
            for x in range((rounded(app.playerx)), rounded(app.playerx+40)):
                for y in range(rounded(app.playery),rounded(app.playery+50)):
                    print(ColorPixel(app.PokemonCenterBackground2, x, y))
                    if (249, 2, 2)==ColorPixel(app.PokemonCenterBackground2, x, y):
                        for pokemon in app.player.pokemon:
                            pokemon.hp=pokemon.basehp
                        app.PokemonCenter=False
                        app.overworld=True
    elif app.PokemonMart==True:
        if app.shopMenu==False:
            if key=='x':
                for x in range((rounded(app.playerx)), rounded(app.playerx+40)):
                    for y in range(rounded(app.playery),rounded(app.playery+50)):
                        if (0,2,251)==ColorPixel(app.PokemonMartBackground2, x, y):
                            app.shopMenu=True
        elif app.shopMenu==True:
            if key=='up':
                app.ShopArrow-=1
                if app.ShopArrow==-1:
                    app.ShopArrow=3
            if key=='down':
                app.ShopArrow+=1
                if app.ShopArrow==4:
                    app.ShopArrow=0
            if key=='escape':
                app.shopMenu=False
            if key=='x':
                if app.ShopArrow==0:
                    if app.player.money>=200:
                        app.player.money-=200
                        app.player.item['potion']+=1
                if app.ShopArrow==1:
                    if app.player.money>=300:
                        app.player.money-=300
                        app.player.item['pokeball']+=1
                if app.ShopArrow==2:
                    if app.player.money>=500:
                        app.player.money-=500
                        app.player.item['repel']+=1
                if app.ShopArrow==3:
                    if app.player.money>=400:
                        app.player.money-=400
                        app.player.item['berry']+=1


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
            original=(app.overworldX, app.overworldY, app.dx, app.dy)
            black=False
            green=False
            if app.player.repel!=0:
                app.player.repel-=1
            if 'down' in keys:
                app.overworldY-=5
                app.dy-=5
                app.direction=app.walkingsouth
            if 'up' in keys:
                app.overworldY+=5
                app.dy+=5
                app.direction=app.walkingnorth
                for x in range(abs(rounded(app.overworldX-(app.width/2))), abs(rounded(app.overworldX-(app.width/2)-40))):
                    for y in range(abs(rounded(app.overworldY-(app.height/2))),abs(rounded(app.overworldY-(app.height/2)-50))):
                        if (255, 0, 0)==ColorPixel(app.map2, x, y):
                            app.PokemonCenter=True
                            app.overworld=False
                            app.playery=390
                            app.playerx=app.width/2
                            black=True
                        if (0, 0, 255)==ColorPixel(app.map2, x, y):
                            app.PokemonMart=True
                            app.overworld=False
                            app.playery=390
                            app.playerx=260
                            black=True
                        if (255, 204, 0)==ColorPixel(app.map2, x, y):
                            app.PokemonGym=True
                            app.overworld=False
                            app.gymX=80
                            app.gymY=-650
                            black=True 
            if 'right' in keys:
                    app.direction=app.walkingeast
                    app.overworldX-=5
                    app.dx-=5
            if 'left' in keys:
                    app.direction=app.walkingwest
                    app.overworldX+=5
                    app.dx+=5
            for x in range(abs(rounded(app.overworldX-(app.width/2))), abs(rounded(app.overworldX-(app.width/2)-40))):
                for y in range(abs(rounded(app.overworldY-(app.height/2))),abs(rounded(app.overworldY-(app.height/2)-50))):
                    if (0, 0, 0)==ColorPixel(app.map2, x, y):
                        black=True
                        break
                    if (1,255,17)==ColorPixel(app.map2, x, y):
                        green=True
                if black==True or green==True:
                    break
            if black==True:
                (app.overworldX, app.overworldY, app.dx, app.dy)=original
            if green==True and app.player.repel==0:
                randomPokemon=random.randrange(0, 500)
                if 5<randomPokemon<10:
                    pokemon=Pokemon('poochyena', randomPokemon-5, [app.Crunch, app.Growl, None, None])
                    WildBattle(app, pokemon)
                    app.Wildbattle=True
                    app.battle=True
                    app.overworld=False
                elif 25<randomPokemon<30:
                    pokemon=Pokemon('wurmple', randomPokemon-25, [app.BugBite, app.ScaryFace, None, None])
                    WildBattle(app, pokemon)
                    app.Wildbattle=True
                    app.battle=True
                    app.overworld=False
                elif 45<randomPokemon<50:
                    pokemon=Pokemon('zigzagoon', randomPokemon-45, [app.Tackle, app.Leer, None, None])
                    WildBattle(app, pokemon)
                    app.Wildbattle=True
                    app.battle=True
                    app.overworld=False
                elif 65<randomPokemon<70:
                    pokemon=Pokemon('lotad', randomPokemon-65, [app.WaterGun, app.VineWhip, app.Leer, None])
                    WildBattle(app, pokemon)
                    app.Wildbattle=True
                    app.battle=True
                    app.overworld=False
                elif 85<randomPokemon<90:
                    pokemon=Pokemon('ralts', randomPokemon-85, [app.Confusion, app.FakeTears, None, None])
                    WildBattle(app, pokemon)
                    app.Wildbattle=True
                    app.battle=True
                    app.overworld=False

    if app.PokemonCenter==True:
        original=(app.playerx, app.playery)
        black=False
        if 'left' in keys:
            app.playerx-=5
            app.direction=app.walkingwest
        if 'right' in keys:
            app.playerx+=5
            app.direction=app.walkingeast
        if 'down' in keys:
            app.playery+=5
            app.direction=app.walkingsouth
            if 400<=app.playery<=app.height  and 290<=app.playerx<=410:
                app.PokemonCenter=False
                app.overworld=True
        if 'up' in keys:
            app.playery-=5
            app.direction=app.walkingnorth
        for x in range((rounded(app.playerx)), rounded(app.playerx+40)):
                for y in range(rounded(app.playery),rounded(app.playery+50)):
                    if (0, 0, 0)==ColorPixel(app.PokemonCenterBackground2, x, y):
                        black=True
                        break
                if black==True:
                    break
        if black==True:
            app.playerx, app.playery = original
    if app.PokemonMart==True and app.shopMenu==False:
        original=(app.playerx, app.playery)
        black=False
        if 'left' in keys:
            app.playerx-=5
            app.direction=app.walkingwest
        if 'right' in keys:
            app.playerx+=5
            app.direction=app.walkingeast
        if 'down' in keys:
            app.playery+=5
            app.direction=app.walkingsouth
            if 420<=app.playery<=app.height  and 200<=app.playerx<=325:
                app.PokemonMart=False
                app.overworld=True
        if 'up' in keys:
            app.playery-=5
            app.direction=app.walkingnorth
        for x in range((rounded(app.playerx)), rounded(app.playerx+40)):
                for y in range(rounded(app.playery),rounded(app.playery+50)):
                    if (0, 0, 0)==ColorPixel(app.PokemonMartBackground2, x, y):
                        black=True
                        break
                if black==True:
                    break
        if black==True:
            app.playerx, app.playery = original
    if app.PokemonGym==True:
        original= app.gymX, app.gymY
        black=False
        if 'left' in keys:
            app.gymX+=5
            app.direction=app.walkingwest
        if 'right' in keys:
            app.gymX-=5
            app.direction=app.walkingeast
        if 'down' in keys:
            app.gymY-=5
            app.direction=app.walkingsouth
            if 0<app.gymX<150 and -700<app.gymY<-650:
                app.PokemonGym=False
                app.overworld=True
        if 'up' in keys:
            app.gymY+=5
            app.direction=app.walkingnorth
        if 120>app.gymX>80 and -440<app.gymY<-380 and app.GymTrainer1.defeated==False :
            app.PokemonGym=False
            Battle(app, app.GymTrainer1) 
            app.battle=True
        if 100<app.gymX<115 and -310<app.gymY<-220 and app.GymTrainer4.defeated==False :
            app.PokemonGym=False
            Battle(app, app.GymTrainer4)
            app.battle=True
        if 305>=app.gymX>=300 and -355<app.gymY<-295 and app.GymTrainer3.defeated==False :
            app.PokemonGym=False
            Battle(app, app.GymTrainer3)
            app.battle=True
        if 305>=app.gymX>=250 and -90<app.gymY<-25 and app.GymTrainer2.defeated==False :
            app.PokemonGym=False
            Battle(app, app.GymTrainer2)
            app.battle=True
        if 135>=app.gymX>=80 and 60<=app.gymY<=95 and  app.GymLeader.defeated==False:
            app.PokemonGym=False
            Battle(app, app.GymLeader)
            app.battle=True
        for x in range(abs(rounded(app.gymX-(app.width/2))), abs(rounded(app.gymX-(app.width/2)-40))):
                for y in range(abs(rounded(app.gymY-(app.height/2))),abs(rounded(app.gymY-(app.height/2)-50))):
                    if (0, 0, 0)==ColorPixel(app.GymBackground2, x, y):
                        black=True
                        break
                if black==True:
                    break
        if black==True:
            app.gymX, app.gymY = original

def onKeyRelease(app, key):
    if app.Truck==True:
        if key=='left':
            app.direction=app.west
        if key=='right':
            app.direction=app.east
    if app.menu==False:
        if app.overworld==True or app.PokemonCenter==True or app.PokemonMart==True and app.shopMenu==False:
            if key=='left':
                app.direction=app.west
            if key=='right':
                app.direction=app.east
            if key=='up':
                app.direction=app.north
            if key=='down':
                app.direction=app.south

def onStep(app):
    i=0
    for pokemon in app.player.pokemon:
        if pokemon==None:
            app.player.pokemon.pop(i)
        i+=1
    if app.Lose==True:
        app.PokemonGym=False
        app.overworld=True
        app.battle=False
        app.overworldX=-2850
        app.overworldY=-1925
        app.dy=0
        app.dx=0
        for pokemon in app.player.pokemon:
            pokemon.hp=pokemon.basehp
        for pokemon in app.opponent.pokemon:
            pokemon.hp=pokemon.basehp

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
        if -180<=app.dx<=-140 and 440<app.dy<500 and type(app.mystarter)==int:
            app.overworld=False
            app.starter=True
        if -325<=app.dx<=-210 and 750<app.dy<1000 and type(app.mystarter)!=int and app.Rival1.defeated==False:
            app.overworld=False
            Rival1(app)
            Battle(app, app.Rival1) 
            app.battle=True
        if -550<=app.dx<=-435 and 730<app.dy<770 and app.Trainer1.defeated==False:
            app.overworld=False
            Battle(app, app.Trainer1) 
            app.battle=True
        

    app.time+=1

def ColorPixel(image, x, y):
    return image.getpixel((x, y))

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
        self.baseattack=rounded((self.basestats[1]*2*level)/100+5)
        self.defense=rounded((self.basestats[2]*2*level)/100+5)
        self.basedefense=rounded((self.basestats[2]*2*level)/100+5)
        self.spAttack=rounded((self.basestats[3]*2*level)/100+5)
        self.basespAttack=rounded((self.basestats[3]*2*level)/100+5)
        self.spDefense=rounded((self.basestats[4]*2*level)/100+5)
        self.basespDefense=rounded((self.basestats[4]*2*level)/100+5)
        self.speed=rounded((self.basestats[5]*2*level)/100+5)
        self.basespeed=rounded((self.basestats[5]*2*level)/100+5)
        self.moves=moves
        self.EXP=0
        self.RequiredEXP=self.level*100

    def __repr__(self):
        return self.name
    
    def LevelUp(self, app):
        while self.EXP >= self.RequiredEXP:
            self.EXP-=self.RequiredEXP
            self.level+=1
            self.RequiredEXP=self.level*100
    
    def damage(self, app, move, other):
        if move.attack!='status':
            randomDamage=random.randrange(85, 100)
            if self.type == move.type:
                STAB=1.5
            else:
                STAB=1
            effectiveness=effective(move, other)
            if effectiveness==2:
                app.resultList.append("It's super effective!")
            elif effectiveness==0.5:
                app.resultList.append("It's not very effective!")
            if move.attack=='physical':
                damage=rounded(((((2*self.level/5)+2)*move.power*(self.attack/other.defense))/50)*STAB*effectiveness*(randomDamage/100))
                other.hp-=damage
            elif move.attack=='special':
                damage=rounded(((((2*self.level/5)+2)*move.power*(self.spAttack/other.spDefense))/50)*STAB*effectiveness*(randomDamage/100))
                other.hp-=damage
        else:
            if move.power=='+Attack':
                self.attack*=1.5
            if move.power=='+Defense':
                self.defense*=1.5
            if move.power=='+spAttack':
                self.spAttack*=1.5
            if move.power=='+spDefense':
                self.spDefense*=1.5
            if move.power=='+speed':
                self.speed*=1.5
            if move.power=='-Attack':
                other.attack*=0.5
            if move.power=='-Defense':
                other.defense*=0.5
            if move.power=='-spAttack':
                other.spAttack*=0.5
            if move.power=='-spDefense':
                other.spDefense*=0.5
            if move.power=='-speed':
                other.speed*=0.5
            if move.power=='+HP':
                self.hp+=rounded(self.hp/2)

    def frontsprites(self, app):
       dexNum=self.pokemon.dex
       return getSprite(app, dexNum, 'front')

    def backsprites(self, app):
       dexNum=self.pokemon.dex
       return getSprite(app, dexNum, 'back')
     
class Player:
    def __init__(self, name):
        self.name=name
        self.money=3000
        self.pokemon=[]
        self.repel=0
        self.item={'potion':3, "pokeball":3, 'repel':1, 'berry':1}
        self.pokedex=set()


    def addPokemon(self, other):
        self.pokemon.append(other)
    
    def addPokedex(self, other):
        self.pokedex.add(other)
    
    def sprite(self, app, i):
        pokemon=self.pokemon[i]
        if i >= len(self.pokemon):
            return None
        return pokemon.frontsprites(app)

class Trainer:
    def __init__(self, name, money):
        self.name=name
        self.money=0
        self.pokemon=[]
        self.money=money
        self.defeated=False
    
    def addPokemon(self, other):
        self.pokemon.append(other)
    
    def __repr__(self):
        return self.name

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

def evolve(app, pokemon):
    if pokemon.pokemon.dex==252:
        if pokemon.level==7:
            app.evolved.add(pokemon.pokemon.dex)
            return Pokemon(pypokedex.get(dex=253).name, pokemon.level, pokemon.moves)
        return pokemon
    elif pokemon.pokemon.dex==253:
        if pokemon.level==13:
            app.evolved.add(pokemon.pokemon.dex)
            return Pokemon(pypokedex.get(dex=254).name, pokemon.level, pokemon.moves)  
        return pokemon
    elif pokemon.pokemon.dex==255:
        if pokemon.level==7:
            app.evolved.add(pokemon.pokemon.dex)
            return Pokemon(pypokedex.get(dex=256).name, pokemon.level, pokemon.moves) 
        return pokemon 
    elif pokemon.pokemon.dex==256:
        if pokemon.level==13:
            app.evolved.add(pokemon.pokemon.dex)
            return Pokemon(pypokedex.get(dex=257).name, pokemon.level, pokemon.moves) 
        return pokemon
    elif pokemon.pokemon.dex==258:
        if pokemon.level==7:
            app.evolved.add(pokemon.pokemon.dex)
            return Pokemon(pypokedex.get(dex=259).name, pokemon.level, pokemon.moves)  
        return pokemon
    elif pokemon.pokemon.dex==259:
        if pokemon.level==13:
            app.evolved.add(pokemon.pokemon.dex)
            return Pokemon(pypokedex.get(dex=260).name, pokemon.level, pokemon.moves) 
        return pokemon
    elif pokemon.pokemon.dex==261:
        if pokemon.level==8:
            app.evolved.add(pokemon.pokemon.dex)
            return Pokemon(pypokedex.get(dex=262).name, pokemon.level, pokemon.moves) 
        return pokemon
    elif pokemon.pokemon.dex==263:
        if pokemon.level==8:
            app.evolved.add(pokemon.pokemon.dex)
            return Pokemon(pypokedex.get(dex=264).name, pokemon.level, pokemon.moves) 
    elif pokemon.pokemon.dex==265:
        if pokemon.level==5:
            app.evolved.add(pokemon.pokemon.dex)
            return Pokemon(pypokedex.get(dex=num).name, pokemon.level, pokemon.moves) 
        return pokemon
    elif pokemon.pokemon.dex==266:
        if pokemon.level==8:
            app.evolved.add(pokemon.pokemon.dex)
            return Pokemon(pypokedex.get(dex=267).name, pokemon.level, pokemon.moves) 
    elif pokemon.pokemon.dex==268:
        if pokemon.level==8:
            app.evolved.add(pokemon.pokemon.dex)
            return Pokemon(pypokedex.get(dex=269).name, pokemon.level, pokemon.moves) 
        return pokemon
    elif pokemon.pokemon.dex==270:
        if pokemon.level==7:
            app.evolved.add(pokemon.pokemon.dex)
            return Pokemon(pypokedex.get(dex=271).name, pokemon.level, pokemon.moves) 
    elif pokemon.pokemon.dex==271:
        if pokemon.level==13:
            app.evolved.add(pokemon.pokemon.dex)
            return Pokemon(pypokedex.get(dex=272).name, pokemon.level, pokemon.moves) 
    elif pokemon.pokemon.dex==280:
        if pokemon.level==7:
            app.evolved.add(pokemon.pokemon.dex)
            return Pokemon(pypokedex.get(dex=281).name, pokemon.level, pokemon.moves) 
    elif pokemon.pokemon.dex==281:
        if pokemon.level==7:
            app.evolved.add(pokemon.pokemon.dex)
            return Pokemon(pypokedex.get(dex=282).name, pokemon.level, pokemon.moves) 
        return pokemon
    else:
        return pokemon
                    
        
  
def effective(move, Pokemon):
    effectiveness=1
    offense=move.type.upper()
    defensive=Pokemon.type
    for defensiveType in defensive:
        defensive=defensiveType.upper()
        if offense=='WATER':
            if defensive=='FIRE':
                effectiveness*=2
            elif defensive=="WATER":
                effectiveness*=0.5
            elif defensive=='GRASS':
                effectiveness*=0.5
            elif defensive=='ROCK':
                effectiveness*=2
            elif defensive=='GROUND':
                effectiveness*=2
        elif offense=='FIRE':
            if defensive=='FIRE':
                effectiveness*=0.5
            elif defensive=="WATER":
                effectiveness*=0.5
            elif defensive=='GRASS':
                effectiveness*=2
            elif defensive=='ROCK':
                effectiveness*=0.5
            elif defensive=='STEEL':
                effectiveness*=2
            elif defensive=='BUG':
                effectiveness*=2
        elif offense=='GRASS':
            if defensive=='FIRE':
                effectiveness*=0.5
            elif defensive=="WATER":
                effectiveness*=2
            elif defensive=='GRASS':
                effectiveness*=0.5
            elif defensive=='ROCK':
                effectiveness*=2
            elif defensive=='GROUND':
                effectiveness*=2
            elif defensive=='STEEL':
                effectiveness*=0.5
        elif offense=='GROUND':
            if defensive=='FIRE':
                effectiveness*=2
            elif defensive=='GRASS':
                effectiveness*=0.5
        elif offense=='STEEL':
            if defensive=='ROCK':
                effectiveness*=2
        elif offense=='BUG': 
            if defensive=='ROCK':
                effectiveness*=0.5
            if defensive=='STEEL':
                effectiveness*=0.5
            if defensive=='PSYCHIC':
                effectiveness*=2
        elif offense=='PSYCHIC': 
            if defensive=='FIGHTING':
                effectiveness*=2
            if defensive=='DARK':
                effectiveness=0
        elif offense=='DARK':
            if defensive=='FIGHTING':
                effectiveness*=0.5
            if defensive=='PSYCHIC':
                effectiveness*=2
        elif offense=='FIGHTING':
            if defensive=='DARK':
                effectiveness*=2
            if defensive=='PSYCHIC':
                effectiveness*=0.5
            if defensive=='BUG':
                effectiveness*=0.5



    return effectiveness

def getSprite(app, dexNum, direction):
    if direction=='front':
        if dexNum == 76:
            return app.f76 
        elif dexNum == 95:
            return app.f95 
        elif dexNum == 112:
            return app.f112 
        elif dexNum == 252:
            return app.f252
        elif dexNum == 253:
            return app.f253
        elif dexNum == 254:
            return app.f254 
        elif dexNum == 255:
            return app.f255 
        elif dexNum == 256:
            return app.f256 
        elif dexNum == 257:
            return app.f257
        elif dexNum == 258:
            return app.f258
        elif dexNum == 259:
            return app.f259
        elif dexNum == 260:
            return app.f260
        elif dexNum == 261:
            return app.f261
        elif dexNum == 262:
            return app.f262
        elif dexNum == 263:
            return app.f263
        elif dexNum == 264:
            return app.f264
        elif dexNum == 265:
            return app.f265
        elif dexNum == 266:
            return app.f266
        elif dexNum == 267:
            return app.f267
        elif dexNum == 268:
            return app.f268
        elif dexNum == 269:
            return app.f269
        elif dexNum == 270:
            return app.f270
        elif dexNum == 271:
            return app.f271
        elif dexNum == 272:
            return app.f272
        elif dexNum == 280:
            return app.f280
        elif dexNum == 281:
            return app.f281
        elif dexNum == 282:
            return app.f282
        elif dexNum == 299:
            return app.f299
        elif dexNum == 304:
            return app.f304 
        elif dexNum == 306:
            return app.f306 
        elif dexNum == 337:
            return app.f337 
        elif dexNum == 338:
            return app.f338 
        elif dexNum == 377:
            return app.f377 

    if direction=='back':
        if dexNum == 76:
            return app.b76 
        elif dexNum == 95:
            return app.b95 
        elif dexNum == 112:
            return app.b112 
        elif dexNum == 252:
            return app.b252
        elif dexNum == 253:
            return app.b253
        elif dexNum == 254:
            return app.b254 
        elif dexNum == 255:
            return app.b255 
        elif dexNum == 256:
            return app.b256 
        elif dexNum == 257:
            return app.b257
        elif dexNum == 258:
            return app.b258
        elif dexNum == 259:
            return app.b259
        elif dexNum == 260:
            return app.b260
        elif dexNum == 261:
            return app.b261
        elif dexNum == 262:
            return app.b262
        elif dexNum == 263:
            return app.b263
        elif dexNum == 264:
            return app.b264
        elif dexNum == 265:
            return app.b265
        elif dexNum == 266:
            return app.b266
        elif dexNum == 267:
            return app.b267
        elif dexNum == 268:
            return app.b268
        elif dexNum == 269:
            return app.b269
        elif dexNum == 270:
            return app.b270
        elif dexNum == 271:
            return app.b271
        elif dexNum == 272:
            return app.b272
        elif dexNum == 280:
            return app.b280
        elif dexNum == 281:
            return app.b281
        elif dexNum == 282:
            return app.b282
        elif dexNum == 299:
            return app.b299
        elif dexNum == 304:
            return app.b304 
        elif dexNum == 306:
            return app.b306 
        elif dexNum == 337:
            return app.b337 
        elif dexNum == 338:
            return app.b338 
        elif dexNum == 377:
            return app.b377 
        elif dexNum == 476:
            return app.b476 

def main():
    runApp()

main()