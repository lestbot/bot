        if message.content.lower().startswith('!ajuda'):
           embed = discord.Embed(title=":heart: Vyper Network",color=0xe67e22,description="Fundada em 4 de março de 2018 A Vyper Network é uma rede de servidores para minecraft PE (pocket edition),temos desenvolvedores próprios que estão trabalhando duro em plugins exclusivos apenas para os nossos servidores. Todo o dinheiro que ganhamos em nossa loja gastamos para melhorar a qualidade de nossos servidores. Viemos para fazer a diferença - Vyper Network\n**Criador desse bot foi o Thug#6929**\nEm Breve, Estaremos Aberto Para Vocês!!!\n",url="http://grewoss.com/")
           embed.set_author(name="Vyper Network",icon_url="https://cdn.discordapp.com/attachments/436762142142889985/436905578388914176/u7HRAS5M_400x400.jpg")
           embed.add_field(name=":blue_heart:  Twiiter E Site",value="Twiiter: @VyperMCPE\nSite: vypermc.xyz",inline=False)
           embed.add_field(name=":blue_book: Lista de comandos",value="!mensagem\n!moeda\n!ajuda\n!apagar\n""!tag\n!ping",inline=False)
           embed.add_field(name="Os Criadores Dessa Rede São!",value="Twitter : @MrMarcuus, Discord: MarcusGplay#1709\nNão Sei , se tem outro dono na rede!\n",inline=False)
           embed.set_footer(text="© Thug 2017-2018 | Contato: thughqck12@gmail.com (Poblemas com o bot)",icon_url="https://cdn.discordapp.com/attachments/436762142142889985/436905578388914176/u7HRAS5M_400x400.jpg")
           embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/436762142142889985/436905578388914176/u7HRAS5M_400x400.jpg")
           await client.send_message(message.channel, embed=embed)
