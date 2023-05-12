import requests 
import os

#criar pasta
os.makedirs("pokemons")

#lista com nomes dos 150 pokemons
nomes_pokemons = [' Bulbasaur',' Ivysaur',' Venusaur',' Charmander',' Charmeleon',' Charizard',' Squirtle',' Wartortle',' Blastoise',' Caterpie',' Metapod',' Butterfree',' Weedle',' Kakuna',' Beedrill',' Pidgey',' Pidgeotto',' Pidgeot',' Rattata',' Raticate',' Spearow',' Fearow',' Ekans',' Arbok',' Pikachu',' Raichu',' Sandshrew',' Sandslash',' Nidoran♀',' Nidorina',' Nidoqueen',' Nidoran♂',' Nidorino',' Nidoking',' Clefairy',' Clefable',' Vulpix',' Ninetales',' Jigglypuff',' Wigglytuff',' Zubat',' Golbat',' Oddish',' Gloom',' Vileplume',' Paras',' Parasect',' Venonat',' Venomoth',' Diglett',' Dugtrio',' Meowth',' Persian',' Psyduck',' Golduck',' Mankey',' Primeape',' Growlithe',' Arcanine',' Poliwag',' Poliwhirl',' Poliwrath',' Abra',' Kadabra',' Alakazam',' Machop',' Machoke',' Machamp',' Bellsprout',' Weepinbell',' Victreebel',' Tentacool',' Tentacruel',' Geodude',' Graveler',' Golem',' Ponyta',' Rapidash',' Slowpoke',' Slowbro',' Magnemite',' Magneton',' Farfetch',' Doduo',' Dodrio',' Seel',' Dewgong',' Grimer',' Muk',' Shellder',' Cloyster',' Gastly',' Haunter',' Gengar',' Onix',' Drowzee',' Hypno',' Krabby',' Kingler',' Voltorb',' Electrode',' Exeggcute',' Exeggutor',' Cubone',' Marowak',' Hitmonlee',' Hitmonchan',' Lickitung',' Koffing',' Weezing',' Rhyhorn',' Rhydon',' Chansey',' Tangela',' Kangaskhan',' Horsea',' Seadra',' Goldeen',' Seaking',' Staryu',' Starmie',' Mr Mine',' Scyther',' Jynx',' Electabuzz',' Magmar',' Pinsir',' Tauros',' Magikarp',' Gyarados',' Lapras',' Ditto',' Eevee',' Vaporeon',' Jolteon',' Flareon',' Porygon',' Omanyte',' Omastar',' Kabuto',' Kabutops',' Aerodactyl',' Snorlax',' Articuno',' Zapdos',' Moltres',' Dratini',' Dragonair',' Dragonite',' Mewtwo']

for i in range(1,151):
    url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/{i}.gif"
    response = requests.get(url)
    if response.status_code == 200:
        # salva o gif em um arquivo
        with open(f"pokemons/{nomes_pokemons[i-1]}.gif", "wb") as a:
            a.write(response.content)
        print(f"Imagem {i}.gif salva com sucesso!")
    else:
        print(f"Erro ao baixar a imagem {i}.gif")