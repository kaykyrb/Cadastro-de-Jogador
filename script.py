player = {}
gols = []
team = []

while True:
  player.clear()
  player['nome'] = input('Nome: ')
  games = int(input(f'quantas partidas {player["nome"]} ele jogou: '))
  gols.clear()

  for i in range(games):
    gols.append(int(input(f'  - Quantos gols na partida {i+1}?')))
    player['gols'] = gols[:]

  total = 0

  
  for t in player['gols']:
    total += t
    player['total'] = total

  team.append(player.copy())
  
  while True:
    proceed = input('Deseja continuar? [S/N]')

    if proceed in 'NnSs':
      break
    elif proceed not in 'NnSs':
      print('ERRO! Por favor digite apenas S ou N')

  if proceed in 'Nn':
    break
  
print('-=' *25)
print('Cod ', end='')
for i in player.keys():
  print(f'{i:<20}', end='')
print()

for i, v in enumerate(team):
  print(f'{i+1:<4}', end='')
  for d in v.values():
    print(f'{str(d):<20}', end='')
  print()
print('-=' *25)

while True:
  search = int(input('Mostrar dados de qual jogador? (999 para parar) '))
  print('--' *25)

  if search == 999:
    break

  if search > len(team):
    print(f'ERRO! Não existe jogador  com o código {search}');
  else:
    print(f'-=- LEVANTAMENTO DO JOGADOR {team[search-1]["nome"]} -=-')
    for i, g in enumerate(team[search-1]['gols']):
      print(f'  - No jogo {i+1} ele fez {g} gols')
  print('-=' *25)
print('>>> FINALIZANDO! VOLTE SEMPRE <<<')