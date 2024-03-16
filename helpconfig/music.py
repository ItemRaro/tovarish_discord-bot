class MusicPlay():

  DESCRIPTION = "Busca, adiciona e toca músicas"

  ALIASES = ["p"]

  HELP = "Digitar o comando seguido pelo nome de alguma música faz com que o mamaco busque,\
  uma música. Se o player não estiver em execução a música é tocada na hora.\
  Se o player estiver em execução a música é adicionada como a próxima a tocar na fila.\
  A fila segue a ordem de primeiro a entrar/primeiro a sair."

  BRIEF = "Busca, adiciona e toca músicas."

class MusicPause():

  DESCRIPTION = "Pausa o player"

  ALIASES = ["pp"]

  HELP = "Pausa a música em execução no player."

  BRIEF = "Pausa a música"

class MusicResume():

  DESCRIPTION = "Despausa o player"

  ALIASES = ["rp"]

  HELP = "Despausa a música em execução no player."

  BRIEF = "Despausa a música"

class MusicSkip():

  DESCRIPTION = "Pula música em execução"

  ALIASES = ["proxima"]

  HELP = "Pula a música em execução no momento para a próxima da fila."

  BRIEF = "Pula música"

class MusicStop():

  DESCRIPTION = "Para a execução do player"

  ALIASES = ["s"]

  HELP = "Para a música em execução, limpa a fila atual e desconecta o bot do canal de voz."

  BRIEF = "Para a música"

class MusicQueue():

  DESCRIPTION = "Lista a fila de próximas músicas"

  ALIASES = ["fila"]

  HELP = "Lista a fila de próximas músicas a serem tocadas.\
  A fila segue a ordem de primero a entrar/primeiro a sair."

  BRIEF = "Lista as próximas músicas"

class MusicQueueShuffle():

  DESCRIPTION = "Embaralha a fila de próximas músicas"

  ALIASES = ["aleatorio"]

  HELP = "Embaralha a fila atual de próximas músicas."

  BRIEF = "Embaralha a fila de músicas"

class MusicQueueDelete():

  DESCRIPTION = "Apaga uma música da fila de próximas músicas"

  ALIASES = ["apagar"]

  HELP = "Digitar o comando seguido por um número de alguma música da fila\
  faz com que ela seja excluída."

  BRIEF = "Apaga uma música da fila"

class MusicBye():

  DESCRIPTION = "Desconecta o player do canal de voz"

  ALIASES = ["tchau"]

  HELP = "Desconecta o player do canal de voz atual.\
  Não limpa a fila de músicas, apenas desconecta."

  BRIEF = "Desconecta o player"

class MusicReset():

  DESCRIPTION = "Reinicia o player"

  ALIASES = ["reiniciar"]

  HELP = "Reinicia o player caso os comandos não estejam sendo aceitos ou\
  ele esteja travado no canal de voz sem responder.\
  Use em caso de emergências."

  BRIEF = "Reinicia o player"