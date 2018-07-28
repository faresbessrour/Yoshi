def commands(command):
    args = command.split(' ')[1:]
    command = command.split(' ')[0][1:]

    if command.lower() == 'pokemon': return pokemon_api.pokemon(args)
    if command.lower() == 'ls':
        if args[0] == 'commands': return ls_commands()
        
def ls_commands():
    return ('!pokemon: Get some information about a Pokemon, you can either get the pokemon by pokedex number or by name.'
            '!ls: listing command, can take the \'commands\' argument to list all the commands available.')

