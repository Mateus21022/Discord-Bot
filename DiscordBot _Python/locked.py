import discord 
import os
from dotenv import load_dotenv
from discord.ext import commands
from alive import Alive
from messages import *

load_dotenv()


class Carlinhos: 

    def __init__(self, token, guild_ids, canal_ids):
        self.TOKEN = token
        self.guild_ids = guild_ids
        self.canal_ids = canal_ids

        if self.TOKEN is None:
            print("Token não carregado.")
            exit()

        self.intents = discord.Intents.default()
        self.intents.message_content = True #Verifica se algum conteúdo foi capturado como mensagem.
        self.client = commands.Bot(command_prefix='CA!', intents=self.intents) #Define o Prefixo!

        self.client.event(self.on_ready)
        self.client.event(self.on_message)

        self.dalva_instance = Classe1()
        self.help_instance = Classe2()
        self.exp_instance = Classe3()
        self.info_instance = Classe4() #Instanciar as Classes que serão utilizadas, pode dar algum erro a principio porque eu mudei o nome das classes durante a documentação :)

        self.alive_instance = None

    async def on_ready(self):
        print(f'Bot conectado como {self.client.user}')
        self.alive_instance = Alive(self.client, self.guild_ids,
                                    self.canal_ids)
        self.client.loop.create_task(self.alive_instance.mensagens_carlinhos())

    async def on_message(self, message):
        if message.author == self.client.user:
            return

        print(
            f'Mensagem recebida: "{message.content}" | Autor: "{message.author}" | ID: "{message.id}" | Canal: "{message.channel}" | Servidor: "{message.guild}"' 
        )#Gera um log de onde as mensagens estão sendo enviadas, o log só é gerado a partir do start do bot e caso seja reiniciado ele perde o log anterior. 
         # A finalidade é somente captar o que está sendo enviado para que possamos utilizar as condicionais corretamente.

        if message.content.startswith('CA!'): #Prefixo do bot é CA! se for detectado isso no início da frase ele será jogado para os outros condicionais abaixo que chamam o metódo equivalente na classe mensagem()
            command = message.content[len('CA!'):].strip()

            if command == "Classe1": #Futuramente (Provavelmente já tenha atualizado, mas irei acrescentar o content.lower() ) em cada um desses coamndos para que sejam reconhecidos independente de sua formatação.
                dalva_message = self.dalva_instance.get_mensagem()
                await message.channel.send(dalva_message)

            elif command == "Classe2":
                exp_message = self.exp_instance.get_mensagem()
                await message.channel.send(exp_message)

            elif command == "Classe3":
                info_message = self.info_instance.get_mensagem()
                await message.channel.send(info_message)

            elif command == "Classe4":
                info_message = self.help_instance.get_mensagem()
                await message.channel.send(info_message)

        elif message.content.lower().startswith('MensagemDesejada'): #Reconhece sempre que o conteúdo entre as '' for colocado. Assim ele redirecionada para uma otura atividade.
            if self.alive_instance: #Verifica se a instância de Alive foi criada.
                await self.alive_instance.enviar_mensagem(message.channel) #Envia as mensagens contidas em Alive especificamente no metodo Alone()
            else:
                print("Não criada.")

    def run(self):
        if self.TOKEN:
            try:
                self.client.run(self.TOKEN) #Verifica o Token! Achei interessante manter essa parte da depuração para que possam verificar quando o Token está válido ou não!
            except Exception as e:
                print(f'Ocorreu um erro: {e}')
        else:
            print("Token não disponível para executar o bot.")


if __name__ == "__main__": 
    bot_token = os.getenv('DISCORD_TOKEN') #Ele captura o Token para a incialização do bot.
    guild_ids = [XXXXXXXX,XXXXXXX] #Aqui vai o ID do servidor em que quer enviar a mensagem. Toda a vírgula significa um novo ID
    canal_ids = [XXXXXXX,XXXXXX] #Aqui vai o id do Canal que quer enviar a mensagem. Toda a vírgula significa um novo ID

    carlinhos_bot = Carlinhos(bot_token, guild_ids, canal_ids) #Instanciando a classe Carlinhos com os parametros necessários
    carlinhos_bot.run() #Iniciando o bot conforme instanciado!
