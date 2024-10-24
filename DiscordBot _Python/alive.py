import discord #Faça o download da biblioteca discord!
import os
import random
import asyncio 
from discord import client 
from dotenv import load_dotenv #Faça o download da biblioteca Dotenv!
from messages import *

load_dotenv()


class Alive:

  def __init__(self, client, guild_ids, canal_ids): #Instanciei algumas informações necessárias para o funcionamento do bot, é tudo bem auto-explicativo.
    self.client = client
    self.guild_ids = guild_ids
    self.canal_ids = canal_ids
    self.alone_instance = Alone()

    self.client.event(self.on_ready)

  async def on_ready(self): # Uma depuração que fiz para que saiba quando o bot está conectado ao discord. Após isso ele inicia a task de mensagens_carlinhos
    print(f'Bot {self.client.user} conectado ao Discord!')

    asyncio.create_task(self.mensagens_carlinhos())

  async def mensagens_carlinhos(self): #''Prepara'' as mensagens para que sejam enviadas somente após a conexão ser testada.
    await self.client.wait_until_ready()

  async def enviar_mensagem(self, channel: discord.TextChannel): # Responsável por fazer o bot enviar as mensagens somente no servidor onde for detectada a atividade.
    mensagem_aleatoria = random.choice(self.alone_instance.get_frases())
    await channel.send(mensagem_aleatoria) 


    # Futuramente vou mexer nessa parte do código! Mas ela faz com o que o bot envie mensagens periodicas para os servidores aos quais está conectado 
    # Ele utiliza a classe Messages de onde pega as mensagens contidas em Alone() e assim as envia de acordo com o tempo estipulado na await asyncio.sleep(Tempo desejado)
    # Os códigos de depuração de erros foram utilizados por mim para testar a funcionalidade do bot durante a construção, então achei legal deixar para quem tiver interessado em usar.


    # while not self.client.is_closed():
    #   for guild_id, canal_id in zip(self.guild_ids, self.canal_ids):
    #     guild = discord.utils.get(self.client.guilds, id=guild_id)
    #     if guild is None:
    #       print(
    #           f"Servidor com ID {guild_id} não encontrado ou bot não está no servidor."
    #       )
    #       continue

    #     canal = discord.utils.get(guild.text_channels, id=canal_id)
    #     if canal is None:
    #       print(
    #           f"Canal com ID {canal_id} não encontrado ou bot não tem acesso ao canal."
    #       )
    #       continue

    #     mensagem_aleatoria = random.choice(self.alone_instance.get_frases())
    #     await canal.send(mensagem_aleatoria)

    #   await asyncio.sleep(100)
