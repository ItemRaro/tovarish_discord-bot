class SyncSlashCommands():
  DESCRIPTION = "Sincroniza os Slash Commands"

  ALIASES = ["sincronizar"]

  HELP = "Sincroniza a árvore de comandos híbridos/slash commands\
  em caso de alteração na lista de comandos híbridos."

  BRIEF = "Sincroniza os Slash Commands"

class CogLoad():
  DESCRIPTION = "Inicia um COG/Módulo"

  ALIASES = ["carregar"]

  HELP = "Carrega e inicia o funcionamento de um COG/Módulo do bot\
  caso o mesmo não tenha sido carregando durante a inicialização.\
  O COG/Módulo deve estar salvo no diretório raíz dentro da pasta 'cogs'.\
  Para carregar o COG/Módulo digite o comando seguido pelo nome do COG/Módulo."

  BRIEF = "Carrega um COG/Módulo do bot"

class CogUnload():
  DESCRIPTION = "Finaliza um COG/Módulo"

  ALIASES = ["descarregar"]

  HELP = "Finaliza o funcionamento de um COG/Módulo do bot que já está inicializado e em execução.\
  Para descarregar o COG/Módulo digite o comando seguido pelo nome do COG/Módulo."

  BRIEF = "Finaliza um COG/Módulo do bot"

class CogReload():
  DESCRIPTION = "Reinicia um COG/Módulo"

  ALIASES = ["recarregar"]

  HELP = "Recarrega um COG/Módulo do bot que já está inicializado e em execução.\
  Para recarregar o COG/Módulo digite o comando seguido pelo nome do COG/Módulo."

  BRIEF = "Reinicia um COG/Módulo do bot"

class ListChannels():
  DESCRIPTION = "Lista todos os canais do servidor atual"

  ALIASES = ["listarcanais"]

  HELP = "Lista todos os canais, texto ou voz, do servidor atual.\
  A lista segue o formato de (NOME DO CANAL)-(TIPO DO CANAL)-(ID DO CANAL)."

  BRIEF = "Lista os canais do servidor"

class ListChannelsFrom():
  DESCRIPTION = "Lista todos os canais de um servidor especificado"

  ALIASES = ["listarcanaisde"]

  HELP = "Lista todos os canais, texto ou voz, do servidor especificado.\
  Ao especificar um servidor o mesmo deve ser escrito de forma exata.\
  A lista segue o formato de (NOME DO CANAL)-(TIPO DO CANAL)-(ID DO CANAL)."

  BRIEF = "Lista os canais de um servidor"