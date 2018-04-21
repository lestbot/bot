    if message.content.lower().startswith('/cmds'):
        cargos == ["cargo1","cargo2","cargo3"]
        role = discord.utils.get(message.server.roles, name=cargos)
        if not role in message.author.roles:
            return await client.send_message(message.channel, "Sem permissão.Voçe nao possuir o cargo")
        await client.send_message(message.author, "Lista de cmds aqui")
