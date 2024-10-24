from locked import *
import discord
import os
from dotenv import load_dotenv

load_dotenv()


class Principal:

  def __init__(self):

    self.bot_token = os.getenv('DISCORD_TOKEN') #Variável onde está armazenada o Token, colocado em .env
    self.guild_ids = [XXXXXXXX,XXXXXXXXX] #Aqui vai o ID do servidor em que quer enviar a mensagem. Toda a vírgula significa um novo ID
    self.canal_ids = [XXXXXXXXX,XXXXXXXXX] #Aqui vai o ID do canal em que quer enviar a mensagem. Toda a vírgula significa um novo ID

    self.controller_instance = Carlinhos(self.bot_token, self.guild_ids, #Instancia a classe do bot.
                                         self.canal_ids)

    self.controller_instance.run()


if __name__ == "__main__":
  principal = Principal()
