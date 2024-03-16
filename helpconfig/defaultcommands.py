class DeleteMessages():

  DESCRIPTION = "Deletar Mensagens do Chat de Texto"

  ALIASES = ["deletar"]

  HELP = "Deleta uma quantidade 'X' de mensagens do chat em que o comando foi executado.\
    A quantidade é inclusiva, ou seja, a mensagem do comando também faz parte desta quantidade.\
    O processo pode demorar vários segundos dependendo da quantidade de mensagens no chat."

  BRIEF = "Apaga 'X' mensagens do chat de texto atual"

class PurgeMessages():

  DESCRIPTION = "Apagar Todas as Mensagens do Chat de Texto"

  ALIASES = ["expurgar"]

  HELP = "Apaga todas de mensagens do chat em que o comando foi executado.\
    O processo pode demorar vários segundos ou minutos dependendo da quantidade de mensagens no chat."

  BRIEF = "Apaga todas as mensagens do chat de texto atual"