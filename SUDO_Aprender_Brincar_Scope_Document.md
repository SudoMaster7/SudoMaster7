# Documento de Escopo: SUDO Aprender & Brincar

## 1. Visão Geral do Projeto

O "SUDO Aprender & Brincar" é um aplicativo móvel inovador, projetado para as plataformas iOS e Android, com o objetivo central de apoiar crianças neurodivergentes e com deficiências intelectuais em seu desenvolvimento. Através de uma abordagem lúdica e interativa, o aplicativo foca no ensino de Atividades de Vida Diária (AVDs) essenciais, no desenvolvimento da coordenação motora fina e na promoção do bem-estar socioemocional.

Acreditamos que o aprendizado pode ser uma jornada divertida e recompensadora. Por isso, o "SUDO Aprender & Brincar" utiliza mecânicas de gamificação cuidadosamente elaboradas para engajar as crianças, oferecendo feedback positivo imediato e um ambiente seguro para a prática e o erro.

O modelo de negócio adotado será o freemium, permitindo um acesso inicial gratuito a um conjunto de funcionalidades e jogos. Para uma experiência completa, com acesso a todos os recursos e conteúdos exclusivos, será oferecida uma assinatura mensal ou anual. Esta abordagem visa tornar o aplicativo acessível ao maior número de famílias, ao mesmo tempo que sustenta o desenvolvimento contínuo e a adição de novas atividades e funcionalidades.

## 2. Público-Alvo Detalhado

Compreender profundamente nossos usuários é fundamental para o sucesso do "SUDO Aprender & Brincar". O aplicativo é desenhado com dois grupos principais em mente:

### Usuário Principal: Crianças Neurodivergentes (4-10 anos)

*   **Características:** Crianças com diagnósticos como Transtorno do Espectro Autista (TEA) de nível 1 e 2, Síndrome de Down, e outras deficiências intelectuais ou condições de neurodesenvolvimento que impactam o aprendizado sequencial, a compreensão de conceitos abstratos e a coordenação motora.
*   **Desafios Comuns:**
    *   **Dificuldade com Abstração:** Preferência por instruções concretas e visuais.
    *   **Sequenciamento de Tarefas:** Desafios em entender e executar tarefas com múltiplos passos.
    *   **Sobrecarga Sensorial:** Sensibilidade a excesso de estímulos visuais ou sonoros. O design deve ser limpo e com opções de personalização de áudio/visual.
    *   **Coordenação Motora Fina:** Dificuldades em movimentos precisos das mãos, como segurar um lápis, abotoar ou amarrar cadarços.
    *   **Motivação para Tarefas Rotineiras:** Baixo interesse intrínseco em atividades de autocuidado ou tarefas percebidas como repetitivas. A gamificação é essencial para manter o engajamento.
*   **Necessidades:**
    *   Ambiente de aprendizado paciente, repetitivo e sem julgamentos.
    *   Feedback imediato e positivo para reforçar o progresso.
    *   Interfaces claras, com ícones grandes e mínimo de texto.
    *   Progressão gradual de dificuldade.

### Usuário Secundário: Pais, Cuidadores e Terapeutas

*   **Objetivos:** Buscam ferramentas eficazes e baseadas em evidências para:
    *   Apoiar o desenvolvimento e aprendizado da criança em casa ou em contexto terapêutico.
    *   Acompanhar o progresso de forma clara e objetiva.
    *   Reforçar e complementar as terapias existentes (Terapia Ocupacional, Fonoaudiologia, Psicopedagogia).
    *   Encontrar maneiras de motivar a criança para o aprendizado de AVDs.
*   **Necessidades:**
    *   Interface de acompanhamento simples e intuitiva.
    *   Relatórios de progresso fáceis de entender e, idealmente, compartilháveis.
    *   Possibilidade de ajustar configurações do aplicativo para adequá-lo às necessidades específicas da criança.
    *   Confiança na segurança e adequação pedagógica do conteúdo.

## 3. Estrutura Completa do Aplicativo

O "SUDO Aprender & Brincar" será organizado em módulos distintos para garantir uma experiência de usuário clara, intuitiva e eficaz.

### 3.1. Módulo de Onboarding e Perfis

Este módulo é o primeiro ponto de contato do usuário com o aplicativo e visa criar uma experiência acolhedora e personalizada.

*   **Tela de Boas-Vindas:**
    *   Design simples, com cores calmantes e um personagem amigável do universo do aplicativo.
    *   Mínimo de texto, com foco em indicações visuais claras.
    *   Botões grandes e de fácil identificação para "Criar Conta" (para pais/responsáveis) ou "Entrar".
*   **Criação de Conta para Pais/Cuidadores:**
    *   Opções de login/cadastro via:
        *   E-mail e Senha.
        *   Conta Google (OAuth).
        *   Conta Apple (OAuth).
    *   Solicitação de informações mínimas: Nome do responsável, e-mail, senha.
    *   Checkbox para aceitação de Termos de Uso e Política de Privacidade.
*   **Criação de Perfil da Criança:**
    *   Após o login do pai/cuidador, este poderá criar perfis para as crianças.
    *   **Nome da Criança:** Campo de texto simples.
    *   **Avatar Personalizável:**
        *   Seleção visual de elementos básicos:
            *   Tom de pele (paleta limitada e inclusiva).
            *   Tipo e cor de cabelo (opções simples e variadas).
            *   Acessórios básicos (ex: óculos, laço – itens que não sobrecarreguem visualmente).
        *   O avatar será usado nos jogos e no lobby, criando identificação.
    *   **Data de Nascimento (Opcional):** Para futuras funcionalidades de acompanhamento de desenvolvimento (não expor a idade diretamente à criança).
*   **Gerenciamento de Perfis:**
    *   Permitir múltiplos perfis de crianças associados a uma única conta de pai/mãe (o número exato dependerá do plano – gratuito vs. premium).
    *   Visualização clara dos perfis criados, com o avatar e nome da criança.
    *   Seleção de perfil ao iniciar o aplicativo (se mais de um perfil existir).
    *   Opção para editar/excluir perfis de criança (protegido por senha do pai/cuidador).
*   **Login para Pais/Cuidadores:**
    *   Acesso à área de gerenciamento de perfis, painel de controle (acompanhamento) e configurações da conta.

### 3.2. Módulo Principal (Lobby de Jogos)

O Lobby de Jogos é o espaço central onde a criança interage para escolher as atividades. O design deve ser extremamente visual, intuitivo e motivador.

*   **Interface Visual e Intuitiva:**
    *   **Baseada em Ícones:** Utilização de ícones grandes, coloridos e facilmente reconhecíveis para cada jogo e categoria. Os ícones devem representar claramente a atividade (ex: um dente sorridente para "Escovando os Dentes").
    *   **Mínimo de Texto:** O nome da categoria ou do jogo pode aparecer abaixo do ícone em fonte legível, mas o design deve funcionar primariamente pelo reconhecimento visual.
    *   **Layout Limpo:** Evitar poluição visual. Espaçamento generoso entre os elementos.
    *   **Personagem Guia (Opcional):** O avatar da criança ou um personagem amigável do app pode estar presente, oferecendo dicas visuais sutis (ex: apontando para um novo jogo).
*   **Categorias de Jogos Bem Definidas:**
    *   Os jogos serão agrupados em três categorias principais, cada uma representada por um ícone ou uma área visual distinta no lobby:
        1.  **"Tarefas do Dia a Dia" (AVDs):** Ícone representando rotina, como uma casa ou um calendário simples.
        2.  **"Habilidades com as Mãos" (Coordenação Motora Fina):** Ícone representando mãos ou ferramentas de criação.
        3.  **"Mente Tranquila" (Bem-Estar Socioemocional):** Ícone representando calma, como uma nuvem serena ou uma flor.
*   **Feedback Imediato:**
    *   **Sonoro:** Ao tocar em um ícone de jogo ou categoria, um som suave e positivo é emitido (ex: um "plim" gentil, uma curta nota musical).
    *   **Visual:** O ícone pode ter uma leve animação ao ser tocado (ex: aumentar de tamanho brevemente, brilhar).
*   **Navegação:**
    *   Simples e direta. Preferencialmente, todos os jogos acessíveis a partir de uma ou duas telas, com navegação por swipe lateral se necessário, indicado por setas grandes e claras.
    *   Botão "Voltar" sempre visível e de fácil acesso para retornar ao lobby a partir de um jogo.
*   **Indicador de Progresso/Novidade (Sutil):**
    *   Jogos concluídos podem ter uma pequena marca de "check" ou estrela.
    *   Novos jogos adicionados podem ter um indicador sutil de "novo" por um tempo limitado.
    *   Evitar sobrecarregar a criança com muitos indicadores.

### 3.3. Módulo de Jogos (Gamification Core)

Este é o coração do aplicativo, onde o aprendizado acontece através de jogos interativos. Cada jogo é projetado para ser divertido, educativo e recompensador.

#### Categoria 1: Tarefas do Dia a Dia (AVDs)

Estes jogos visam ensinar habilidades práticas de autocuidado de forma sequencial e simplificada.

**1. Jogo: Escovando os Dentes**

*   **Objetivo Pedagógico:** Ensinar a sequência correta da escovação dentária, promover hábitos de higiene oral e desenvolver coordenação motora para manusear a escova.
*   **Mecânica (Passo a Passo):**
    1.  **Aplicar Pasta:** Uma escova de dentes virtual e um tubo de pasta são mostrados. A criança deve arrastar o ícone do tubo de pasta sobre as cerdas da escova. Uma animação mostra a pasta sendo aplicada.
    2.  **Escovar os Dentes:** Um avatar com um sorriso mostrando os dentes aparece. A criança deve arrastar a escova (agora com pasta) sobre os dentes virtuais.
        *   **Direções Indicadas:** Setas ou áreas brilhantes podem sugerir os movimentos: para cima e para baixo nos dentes da frente, movimentos circulares nos molares.
        *   **Feedback Visual:** À medida que a escova passa, os dentes podem ficar visivelmente mais "brilhantes" ou "limpos" (remoção de "sujeirinhas" virtuais).
    3.  **Enxaguar:** Um copo d'água virtual aparece. A criança deve arrastar o copo até a boca do avatar. Uma animação mostra o avatar "bochechando" e "cuspindo".
*   **Reforço Positivo:**
    *   Ao completar cada passo: Som de "check" ou uma pequena estrela aparece.
    *   Ao final da escovação: O avatar dá um grande sorriso brilhante, acompanhado de uma curta animação festiva (ex: estrelas coloridas, confetes virtuais) e um som alegre (ex: "Muito bem!", "Dentes limpinhos!"). Uma estrela de conquista pode ser ganha.

**2. Jogo: Amarrando o Tênis**

*   **Objetivo Pedagógico:** Ensinar os passos para amarrar cadarços, desenvolver coordenação motora fina, paciência e sequenciamento.
*   **Mecânica (Passo a Passo):** O jogo é dividido em fases visuais claras, com cada fase sendo uma mini-conquista. Um tênis virtual com cadarços soltos é mostrado.
    1.  **Apertar os Cadarços:** Dois cadarços virtuais estão soltos. A criança deve arrastar as pontas dos dois cadarços para cima/lados opostos para "apertar" o nó inicial. O tênis se ajusta visualmente.
    2.  **Fazer a Primeira "Orelha":** Um dos cadarços brilha. A criança deve traçar com o dedo o caminho indicado para formar a primeira laçada ("orelha de coelho"). O caminho pode ser uma linha pontilhada que a criança cobre.
    3.  **Passar o Outro Cadarço por Trás:** O outro cadarço brilha. A criança deve traçar o caminho indicado para passar este cadarço ao redor da base da primeira "orelha".
    4.  **Formar a Segunda "Orelha" e Puxar (Alternativa Simplificada):** Se a mecânica anterior for muito complexa, pode-se simplificar para "formar a segunda orelha" e depois "puxar as duas orelhas" para finalizar o nó.
    5.  **Puxar para Finalizar:** As duas "orelhas" (ou pontas, dependendo da técnica ensinada) brilham. A criança deve arrastá-las em direções opostas para "apertar" o nó.
*   **Reforço Positivo:**
    *   Ao completar cada fase: Um som de clique suave, a linha traçada se torna sólida, ou uma pequena animação de "nó apertando".
    *   Ao final do jogo: O tênis aparece com o laço bem feito, uma animação de "joinha" ou estrelas, e um som de comemoração. Ex: "Caderno amarrado!", "Pronto para passear!".

**3. Jogo: Abotoando a Camisa**

*   **Objetivo Pedagógico:** Desenvolver a coordenação olho-mão, a pinça fina e a compreensão da mecânica de abotoar.
*   **Mecânica (Passo a Passo):** Uma camisa virtual com botões abertos é mostrada.
    1.  **Selecionar o Botão:** A criança clica e segura em um botão virtual. O botão pode aumentar ligeiramente de tamanho para indicar que foi selecionado.
    2.  **Arrastar até a Casa do Botão:** A casa do botão correspondente brilha ou é destacada. A criança deve arrastar o botão até a casa. Uma linha guia sutil pode aparecer.
    3.  **Soltar para Abotoar:** Ao soltar o botão sobre a casa correta, uma animação mostra o botão "passando" pela casa e a parte da camisa se fechando.
    *   Repetir para todos os botões da camisa.
*   **Reforço Positivo:**
    *   Ao abotoar cada botão: Um som de "clique" satisfatório, a camisa se fecha um pouco mais.
    *   Ao final do jogo (todos os botões abotoados): A camisa aparece toda abotoada, uma animação de "roupa elegante" ou similar, e um som de sucesso. Ex: "Que elegância!", "Camisa prontinha!".

#### Categoria 2: Habilidades com as Mãos (Coordenação Motora Fina)

Estes jogos são focados no treino de movimentos precisos, fortalecendo a destreza manual.

**4. Jogo: Conecte os Pontos**

*   **Objetivo Pedagógico:** Desenvolver a coordenação motora fina, o reconhecimento de sequências (numéricas ou alfabéticas, ou simplesmente visuais) e a preensão para traçado.
*   **Mecânica (Passo a Passo):**
    1.  **Apresentação:** Uma série de pontos numerados (ou com letras, ou simplesmente pontos coloridos em sequência) aparece na tela, sugerindo o contorno de um objeto ou forma simples.
    2.  **Traçar:** A criança deve tocar no primeiro ponto (ex: "1") e arrastar o dedo até o próximo ponto na sequência (ex: "2"), depois para o "3", e assim por diante.
    3.  **Linha Guia:** Uma linha é desenhada entre os pontos conectados.
    *   **Variações de Dificuldade:**
        *   **Fácil:** Menos pontos, formas simples, números em sequência clara.
        *   **Médio:** Mais pontos, objetos um pouco mais complexos, pode incluir ordem alfabética.
        *   **Avançado (Opcional):** Sem números, apenas a sugestão da forma, exigindo mais percepção visual.
*   **Reforço Positivo:**
    *   Ao conectar cada par de pontos corretamente: Um som suave (ex: "ding"), a linha traçada se torna mais espessa ou colorida.
    *   Ao completar a forma: O contorno se preenche com cor, o objeto final é revelado (ex: uma maçã, um carro), uma animação curta do objeto (ex: a maçã brilha, o carro buzina) e um som de celebração. Ex: "Você formou uma estrela!", "Que desenho lindo!".

**5. Jogo: Mestre do Arraste**

*   **Objetivo Pedagógico:** Aprimorar a habilidade de arrastar e soltar, o reconhecimento de formas e o encaixe espacial.
*   **Mecânica (Passo a Passo):**
    1.  **Apresentação:** Formas geométricas coloridas (círculo, quadrado, triângulo, estrela, etc.) aparecem em uma área da tela. Em outra área, contornos vazados correspondentes a essas formas são mostrados (os "buracos").
    2.  **Arrastar e Soltar:** A criança deve tocar em uma forma, arrastá-la e soltá-la sobre o seu respectivo "buraco".
    3.  **Encaixe:** Se a forma correta é solta sobre o buraco correto, ela se encaixa com uma animação suave e um som de "encaixe". Se for a forma errada, ela volta para a posição original ou treme levemente com um som de "erro" suave.
    *   **Variações de Dificuldade:**
        *   **Fácil:** Poucas formas (2-3), cores distintas, formas bem diferentes.
        *   **Médio:** Mais formas (4-5), algumas podem ter cores similares, exigindo mais atenção à forma.
        *   **Difícil:** Formas podem precisar ser rotacionadas (com um gesto simples de girar com dois dedos, se a plataforma permitir e for adequado ao público) para encaixar.
*   **Reforço Positivo:**
    *   Ao encaixar cada forma: Som de "clack" ou "ploc" de encaixe, a forma fica fixa no lugar.
    *   Ao completar todas as formas: Todas as formas brilham, uma melodia curta e alegre, e uma mensagem como "Muito bem!", "Formas no lugar!".

**6. Jogo: Pega-Peixe**

*   **Objetivo Pedagógico:** Desenvolver o tempo de reação, a coordenação olho-mão e a atenção focada.
*   **Mecânica (Passo a Passo):**
    1.  **Ambiente Aquático:** Uma tela simulando um aquário ou lago, com peixes coloridos (ou outros objetos amigáveis, como bolhas ou estrelas do mar) aparecendo e se movendo.
    2.  **Clicar para Pegar:** A criança deve tocar/clicar nos peixes antes que eles sumam da tela (ex: nadam para fora da borda).
    3.  **Pontuação:** Cada peixe "pego" pode adicionar um ponto a um contador visual.
    *   **Tipos de Peixe (Opcional):**
        *   Peixes normais: Valem 1 ponto.
        *   Peixes rápidos: Valem mais pontos ou dão um bônus de tempo.
        *   Evitar "peixes ruins" ou penalidades negativas, focar no reforço positivo.
    *   **Ajuste de Velocidade:** A velocidade com que os peixes aparecem e se movem deve ser ajustável (nas configurações para pais ou automaticamente com base no desempenho).
*   **Reforço Positivo:**
    *   Ao pegar um peixe: Som de "bolha" ou "splash", o peixe pode fazer uma pequena animação antes de sumir e o contador de pontos aumenta.
    *   Ao final do tempo do jogo ou ao atingir uma meta: Uma tela de "Parabéns!" com o total de peixes pegos, sons de aplausos virtuais, e talvez uma animação de um aquário cheio e feliz. Ex: "Pescador Mestre!", "Quantos peixes!".

#### Categoria 3: Mente Tranquila (Bem-Estar Socioemocional)

Estes jogos são projetados para ajudar a criança a desenvolver autoconsciência emocional, técnicas de relaxamento e regulação emocional.

**7. Jogo: Respiração da Flor**

*   **Objetivo Pedagógico:** Ensinar uma técnica de respiração consciente para promover calma e auto-regulação, ajudando a criança a lidar com ansiedade ou sobrecarga sensorial.
*   **Mecânica (Passo a Passo):**
    1.  **Visual Central:** Uma flor grande e amigável (ou um balão, ou uma estrela que pulsa) é mostrada no centro da tela.
    2.  **Inspirar (Cheirar a Flor):** A flor começa a desabrochar lentamente (ou o balão a encher). Uma sugestão visual (ex: setas subindo, a palavra "Inspire" aparecendo suavemente) e/ou uma narração calma (ex: "Vamos cheirar a flor bem devagar...") guia a criança a inspirar profundamente enquanto a flor cresce.
    3.  **Segurar (Opcional):** Uma breve pausa com a flor totalmente aberta.
    4.  **Expirar (Assoprar a Vela):** A flor começa a se fechar lentamente (ou o balão a esvaziar, ou as pétalas da flor a "voar" suavemente como se soprada). Uma sugestão visual (ex: setas descendo, a palavra "Expire" aparecendo) e/ou narração (ex: "Agora, assopre a vela devagarinho...") guia a criança a expirar lentamente.
    *   **Duração:** O ciclo se repete algumas vezes (ex: 3-5 respirações).
*   **Reforço Positivo:**
    *   **Ambiente Sonoro:** Música de fundo calma e sons da natureza (pássaros, vento suave) durante todo o exercício.
    *   Ao final do ciclo: A tela pode ficar suavemente iluminada, a flor pode brilhar ou soltar pequenas partículas brilhantes. Uma mensagem como "Que calma...", "Você se sente mais tranquilo(a)?" (sem exigir resposta).
    *   Não há "ganhar" ou "perder", apenas a experiência.

**8. Jogo: Que Emoção é Essa?**

*   **Objetivo Pedagógico:** Ajudar no reconhecimento e nomeação de emoções básicas, promovendo a inteligência emocional.
*   **Mecânica (Passo a Passo):**
    1.  **Apresentação da Emoção:** Um avatar (pode ser o avatar da criança ou um personagem padrão) é mostrado no centro da tela exibindo uma expressão facial clara de uma emoção básica (ex: alegria, tristeza, raiva, medo, surpresa).
    2.  **Opções de Resposta:** Abaixo do avatar, 2 a 4 ícones representando diferentes emoções são mostrados. Cada ícone é uma carinha simples com a expressão correspondente. O nome da emoção pode estar escrito abaixo do ícone para reforço (opcional, dependendo do nível de leitura).
    3.  **Escolha da Criança:** A criança deve tocar no ícone que corresponde à emoção demonstrada pelo avatar principal.
    *   **Variações:**
        *   Pode-se usar sons curtos associados à emoção (ex: uma risada para alegria, um soluço suave para tristeza).
        *   Introduzir uma emoção por vez, depois misturá-las.
*   **Reforço Positivo:**
    *   **Escolha Correta:** O ícone selecionado brilha, o avatar principal pode dar um feedback positivo (ex: o avatar alegre acena, o avatar triste recebe um "abraço" virtual). Um som de confirmação alegre. Ex: "Isso mesmo, ele está alegre!".
    *   **Escolha Incorreta:** Um feedback suave, não punitivo. Ex: "Tente outra vez." O ícone errado pode tremer levemente e o jogo permite uma nova tentativa. O foco é no aprendizado.
    *   Ao acertar algumas seguidas: Uma pequena celebração, como estrelinhas ou confetes.

**9. Jogo: Jardim Zen**

*   **Objetivo Pedagógico:** Oferecer um espaço de livre expressão criativa e relaxamento, sem metas ou pressão, promovendo a calma e a exploração sensorial.
*   **Mecânica (Passo a Passo):**
    1.  **Tela de Areia Virtual:** A tela se apresenta como uma caixa de areia virtual com uma textura realista.
    2.  **Desenhar com os Dedos:** A criança pode usar o dedo (ou múltiplos dedos) para "desenhar" na areia. O traço do dedo deixa um rastro na areia, como se estivesse realmente desenhando.
    3.  **Ferramentas Simples (Opcional):**
        *   Um botão para "alisar" a areia e começar de novo (como um ancinho virtual).
        *   Seleção de "pedrinhas" ou "conchas" virtuais que podem ser arrastadas e colocadas na areia.
        *   Diferentes texturas de "rastros" (ex: linha fina, linha grossa).
    *   **Sem Objetivos Definidos:** É um ambiente de exploração livre.
*   **Reforço Positivo:**
    *   **Sons Relaxantes:** Sons suaves de areia sendo movida quando a criança desenha. Música ambiente calma e sons da natureza (água correndo, vento).
    *   **Feedback Visual:** A "areia" responde de forma realista ao toque.
    *   Não há "vitória" ou "derrota". O reforço é a própria experiência relaxante e criativa. A tela pode ter um brilho sutil ou cores suaves que mudam lentamente para aumentar a sensação de calma.

### 3.4. Módulo de Acompanhamento para Pais/Terapeutas (Painel de Controle)

Este módulo é acessível apenas através da conta principal (pais/cuidadores/terapeutas) e fornece ferramentas para monitorar o progresso da criança e gerenciar as configurações do aplicativo. O acesso deve ser protegido por senha ou autenticação da conta principal para garantir a privacidade.

*   **Acesso Seguro:**
    *   Login com as credenciais da conta principal.
    *   Pode exigir uma confirmação de senha se já estiver logado no app, antes de acessar esta área sensível.
*   **Seleção de Perfil (se houver múltiplos):**
    *   Caso haja mais de um perfil de criança na conta, o adulto deve selecionar qual perfil deseja visualizar os relatórios ou ajustar as configurações.
*   **Relatórios de Progresso:**
    *   Interface clara e com gráficos simples para facilitar a visualização.
    *   **Visão Geral:**
        *   **Tempo de Uso:** Gráfico de tempo de uso diário e semanal.
        *   **Jogos Mais Jogados:** Lista ou gráfico mostrando os jogos com maior engajamento.
        *   **Últimas Conquistas:** Resumo das conquistas e troféus recentes.
    *   **Progresso por Habilidade/Jogo:**
        *   Detalhes sobre o desempenho em jogos específicos (ex: "Completou 'Amarrar o Tênis' 5 vezes com sucesso", "Nível alcançado em 'Pega-Peixe'").
        *   Para jogos de AVD, pode mostrar a frequência de conclusão e talvez o tempo médio para completar a tarefa.
        *   Para jogos de coordenação, pode mostrar pontuações ou níveis alcançados.
        *   Para jogos de bem-estar, pode mostrar a frequência de uso (ex: "Realizou 'Respiração da Flor' 3 vezes esta semana").
    *   **Conquistas e Troféus:**
        *   Galeria visual dos troféus ou medalhas virtuais desbloqueados pela criança.
        *   Data de desbloqueio de cada conquista.
    *   **Compartilhamento de Relatórios (Funcionalidade Premium):**
        *   Opção para gerar um resumo do progresso em formato PDF, que pode ser salvo ou enviado por e-mail para terapeutas ou outros profissionais envolvidos.
*   **Configurações do Aplicativo (por perfil de criança):**
    *   **Ajuste de Dificuldade dos Jogos:**
        *   Permitir que os pais/terapeutas ajustem globalmente ou individualmente a dificuldade de certos jogos.
        *   Exemplos: Menos etapas em AVDs, mais tempo em jogos cronometrados, menor velocidade em "Pega-Peixe", dicas visuais mais proeminentes.
    *   **Controles de Som:**
        *   Ligar/desligar a música de fundo.
        *   Ligar/desligar os efeitos sonoros dos jogos.
        *   Controle de volume geral (se não sobrepuser o controle do dispositivo).
    *   **Lembretes (Opcional):**
        *   Configurar lembretes para horários de uso do aplicativo ou para praticar certas AVDs.
    *   **Gerenciar Assinatura:**
        *   Visualizar o status da assinatura (gratuita ou premium).
        *   Opções para fazer upgrade para premium ou gerenciar a assinatura existente (link para as lojas de aplicativos).
    *   **Notificações:**
        *   Controlar as notificações enviadas pelo aplicativo (ex: novidades, relatórios semanais).
*   **Recursos e Suporte:**
    *   Link para FAQ (Perguntas Frequentes).
    *   Contato do suporte técnico.
    *   Informações sobre a pedagogia do aplicativo.

## 4. Estratégia de Monetização (Modelo Freemium)

O "SUDO Aprender & Brincar" adotará um modelo de negócio freemium para equilibrar acessibilidade e sustentabilidade do projeto. O objetivo é permitir que todos experimentem o valor do aplicativo, oferecendo funcionalidades mais robustas e conteúdo expandido através de uma assinatura.

### Versão Gratuita

A versão gratuita funcionará como uma introdução ao universo do "SUDO Aprender & Brincar", permitindo que pais, crianças e terapeutas avaliem sua eficácia e adequação.

*   **Acesso a Conteúdo Limitado:**
    *   **Jogos:** Acesso a uma seleção de 3 jogos, estrategicamente escolhidos para representar cada uma das categorias principais:
        *   1 jogo de "Tarefas do Dia a Dia" (ex: "Escovando os Dentes").
        *   1 jogo de "Habilidades com as Mãos" (ex: "Conecte os Pontos").
        *   1 jogo de "Mente Tranquila" (ex: "Respiração da Flor").
    *   A seleção de jogos gratuitos pode ser rotacionada periodicamente para manter o interesse.
*   **Perfis de Criança:**
    *   Criação de apenas **1 perfil de criança**.
*   **Relatórios de Progresso:**
    *   Acesso a relatórios de progresso **básicos** (ex: tempo de uso, jogos jogados, últimas conquistas).
    *   Sem opção de compartilhamento ou detalhamento avançado.
*   **Personalização de Avatar:**
    *   Opções limitadas de personalização para o avatar da criança.
*   **Publicidade:**
    *   A versão gratuita **não conterá publicidade de terceiros** para garantir um ambiente seguro e focado para as crianças. A monetização virá exclusivamente da versão premium.
*   **Incentivo para Upgrade:**
    *   Presença de chamadas visuais discretas para o upgrade para a versão premium, destacando os benefícios adicionais (ex: "Desbloqueie todos os jogos!", "Crie mais perfis!").

### Versão Premium (Assinatura Mensal/Anual)

A versão premium oferecerá a experiência completa do "SUDO Aprender & Brincar", com todos os recursos desbloqueados e conteúdo adicional.

*   **Acesso Ilimitado a Conteúdo:**
    *   **Todos os Jogos:** Acesso ilimitado a todos os jogos existentes nas três categorias.
    *   **Conteúdo Futuro:** Acesso a todos os novos jogos, atividades e tarefas que forem adicionados mensalmente.
*   **Perfis de Criança:**
    *   Criação de **até 4 perfis de crianças** em uma única conta, ideal para famílias com mais de uma criança ou para terapeutas que utilizam o app com múltiplos pacientes.
*   **Relatórios de Progresso Avançados:**
    *   Relatórios detalhados sobre o desenvolvimento da criança, incluindo análises por habilidade e progresso ao longo do tempo.
    *   **Relatórios Compartilháveis:** Opção de exportar relatórios de progresso em formato PDF, facilitando o compartilhamento com terapeutas, escolas ou outros cuidadores.
*   **Personalização Avançada de Avatares:**
    *   Acesso a uma gama maior de opções de cabelos, roupas, acessórios e cores para os avatares, permitindo maior expressão individual.
*   **Conteúdo Novo Mensalmente:**
    *   Compromisso de adicionar novos jogos, novas tarefas de AVDs, ou expansões para os jogos existentes regularmente, mantendo o aplicativo sempre interessante e desafiador.
*   **Opções de Assinatura:**
    *   **Mensal:** Cobrança recorrente mensal.
    *   **Anual:** Cobrança recorrente anual, geralmente com um desconto em relação ao plano mensal, incentivando um compromisso de longo prazo.
    *   As assinaturas serão gerenciadas através das plataformas das lojas de aplicativos (Google Play Store e Apple App Store).

## 5. Sugestão de Stack Tecnológico

A escolha da stack tecnológica é crucial para o desenvolvimento eficiente, a manutenibilidade e a escalabilidade do "SUDO Aprender & Brincar". Sugerimos uma combinação de tecnologias modernas e comprovadas:

*   **Frontend (Aplicativo Móvel): Flutter**
    *   **Justificativa:** Flutter é um framework de UI toolkit da Google que permite o desenvolvimento de aplicativos nativamente compilados para mobile (iOS e Android), web e desktop a partir de uma única base de código.
    *   **Vantagens:**
        *   **Desenvolvimento Multiplataforma:** Redução significativa de tempo e custo de desenvolvimento, pois não é necessário manter duas bases de código separadas para iOS e Android.
        *   **UI Expressiva e Flexível:** Permite a criação de interfaces de usuário ricas, personalizadas e com animações fluidas, essenciais para um aplicativo infantil atraente.
        *   **Performance Nativa:** Os aplicativos Flutter compilam para código ARM nativo, garantindo alta performance.
        *   **Hot Reload & Hot Restart:** Agiliza o desenvolvimento, permitindo que os desenvolvedores vejam as alterações no código quase instantaneamente.
        *   **Comunidade Crescente:** Grande comunidade de desenvolvedores e vasta documentação.
*   **Backend (Servidor e Banco de Dados): Firebase**
    *   **Justificativa:** Firebase é uma plataforma de desenvolvimento de aplicativos móveis e web do Google que oferece um conjunto integrado de ferramentas e serviços de backend.
    *   **Serviços a Serem Utilizados:**
        *   **Firebase Authentication:** Para gerenciamento seguro de login de usuários (e-mail/senha, Google Sign-In, Apple Sign-In) com pouca configuração.
        *   **Firestore:** Um banco de dados NoSQL, flexível e escalável, ideal para armazenar dados de perfis de usuários, progresso nos jogos, configurações e conteúdo do aplicativo. Sua natureza orientada a documentos se adapta bem à estrutura de dados do aplicativo.
        *   **Firebase Cloud Functions:** Para executar lógica de backend sem a necessidade de gerenciar servidores. Pode ser usado para validações complexas, processamento de dados em segundo plano (ex: agregação de relatórios de progresso) ou integração com outros serviços.
        *   **Firebase Cloud Storage (Opcional):** Se necessário armazenar arquivos maiores, como assets de áudio ou vídeo que não estão no bundle do app.
    *   **Vantagens:**
        *   **Backend como Serviço (BaaS):** Reduz a necessidade de gerenciamento de infraestrutura de servidor.
        *   **Escalabilidade:** Os serviços do Firebase são projetados para escalar automaticamente com o uso.
        *   **Tempo Real:** Firestore oferece sincronização de dados em tempo real, o que pode ser útil para atualizar o progresso da criança instantaneamente no painel dos pais.
        *   **Integração Fácil:** SDKs bem documentados para Flutter.
*   **Design de Assets (Gráficos e Visuais): Vetores (SVG)**
    *   **Justificativa:** Utilizar Gráficos Vetoriais Escaláveis (SVG) para todos os elementos gráficos do aplicativo (personagens, ícones, elementos de jogos, botões).
    *   **Vantagens:**
        *   **Escalabilidade Perfeita:** SVGs podem ser redimensionados para qualquer tamanho de tela ou resolução sem perda de qualidade ou nitidez, crucial para a diversidade de dispositivos Android e iOS.
        *   **Tamanho de Arquivo Menor:** Geralmente resultam em arquivos menores em comparação com bitmaps para formas e ícones, otimizando o tamanho do aplicativo.
        *   **Facilidade de Animação e Manipulação:** SVGs podem ser facilmente animados e manipulados via código, o que é útil para feedback visual e animações de jogos.
        *   **Clareza e Nitidez:** Garantem que os visuais sejam sempre nítidos e claros, importante para crianças com dificuldades de processamento visual.
*   **Ferramentas Adicionais (Sugestões):**
    *   **Controle de Versão:** Git (com plataformas como GitHub, GitLab ou Bitbucket).
    *   **Gerenciamento de Projeto:** Ferramentas como Jira, Trello ou Asana.
    *   **Design de UI/UX:** Figma ou Adobe XD para prototipagem e design de interface.

Esta stack tecnológica oferece um bom equilíbrio entre eficiência de desenvolvimento, performance, escalabilidade e custo, sendo bem adequada para o escopo do "SUDO Aprender & Brincar".

## 6. Análise dos Jogos Escolhidos

A seleção e estruturação dos jogos foram pensadas para cobrir áreas de desenvolvimento cruciais para o público-alvo, conforme detalhado abaixo:

*   **Tarefas do Dia a Dia:** Ataca diretamente o problema principal de dificuldades com AVDs (como escovar dentes, amarrar tênis). Dividir tarefas complexas em passos simples e gamificados é a chave para o aprendizado nesse público. A repetição e o reforço positivo em cada etapa constroem a confiança e a habilidade.

*   **Habilidades com as Mãos:** São jogos fundamentais que treinam a base da coordenação motora fina (arrastar, clicar, traçar). Dominar essas ações torna mais fácil o aprendizado de tarefas mais complexas no mundo real e no próprio aplicativo. Estes jogos servem como um alicerce para habilidades motoras mais refinadas.

*   **Mente Tranquila:** Este é o diferencial para a "saúde mental" e bem-estar emocional. Jogos de respiração e identificação de emoções são ferramentas terapêuticas comprovadas para ajudar crianças neurodivergentes a regular a ansiedade, a se compreenderem melhor e a desenvolverem a inteligência emocional. A inclusão desta categoria visa aumentar a confiança e fornecer mecanismos de enfrentamento.

A combinação dessas três categorias busca oferecer uma abordagem holística, endereçando não apenas as habilidades práticas, mas também o desenvolvimento motor e o equilíbrio emocional da criança.

## 7. Próximos Passos Após Usar o Documento

Este documento de escopo serve como um guia fundamental para o desenvolvimento do "SUDO Aprender & Brincar". Os próximos passos recomendados são:

1.  **Analise o Resultado:** Revise este documento cuidadosamente. Ele é o ponto de partida e deve ser ajustado conforme necessário para alinhar completamente com a visão do projeto.
2.  **Valide com Profissionais:** Se possível, apresente este documento a psicopedagogos, terapeutas ocupacionais, psicólogos infantis ou outros especialistas em desenvolvimento infantil e neurodivergência. Eles podem oferecer insights valiosos para refinar os jogos, as abordagens pedagógicas e a usabilidade geral do aplicativo.
3.  **Contrate a Equipe de Desenvolvimento e Design:** Com este documento detalhado em mãos, a busca por desenvolvedores (Flutter, Firebase) e designers de UI/UX será mais eficiente. O escopo claro facilitará a obtenção de orçamentos precisos e o alinhamento de expectativas.
4.  **Crie os Assets Visuais e Sonoros:** Contrate um designer gráfico para criar todos os elementos visuais (avatares, cenários de jogos, ícones, botões, etc.), seguindo as diretrizes de simplicidade, clareza e apelo visual para o público-alvo. Da mesma forma, planeje os assets sonoros (músicas, efeitos de feedback) para serem agradáveis e não excessivamente estimulantes.
5.  **Desenvolvimento Iterativo:** Adote uma metodologia de desenvolvimento ágil, com ciclos curtos de desenvolvimento, testes com o público-alvo (se possível) e iterações baseadas no feedback.
6.  **Planejamento de Testes:** Defina uma estratégia de testes que inclua testes de usabilidade com crianças dentro do espectro do público-alvo, além de testes funcionais e de performance.
7.  **Marketing e Lançamento:** Planeje a estratégia de marketing e lançamento do aplicativo, considerando os canais mais eficazes para alcançar pais, cuidadores e terapeutas.

Este documento é uma ferramenta viva e pode evoluir à medida que o projeto avança e novos aprendizados são adquiridos.
