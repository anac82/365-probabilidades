Qual a probabilidade de um governador do Rio ser preso?

*Como venho fazendo desde o Dia #111, o texto aqui é o mais simples que eu consigo escrever. O rigor está no notebook, no GitHub, com o código e as contas.*

O tema de hoje surgiu de uma conversa com a minha chefe nos dias em que acompanhamos as apurações do primeiro turno para presidente e para governador. O que ela me trouxe à tona foi a recência e a frequência com que os governadores do estado acabam com algum envolvimento em prisões.

Quando comecei a pesquisar, foi comum encontrar, em postagens e sites, a frase de que todo governador acaba preso. E então eu fui contar. Não os políticos em geral, que ninguém consegue conferir um a um, e sim um universo fechado, as pessoas eleitas para governar o estado desde a volta das eleições diretas, em 1982.

Uma regra antes do primeiro número. O evento contado é ter recebido ao menos uma ordem judicial de prisão, cumprida. O que veio depois, anulação, absolvição, arquivamento ou condenação, está registrado nome a nome no notebook, mas não muda a contagem. A pergunta é quantos governadores do Rio um juiz mandou prender. Não é quantos foram condenados, e os dois não se confundem.

---

A conta que ninguém faz

Nove pessoas foram eleitas governador do Rio de Janeiro de 1982 para cá e tomaram posse. Brizola, duas vezes. Moreira Franco. Marcello Alencar. Anthony Garotinho. Rosinha Garotinho. Sérgio Cabral. Luiz Fernando Pezão. Wilson Witzel. Cláudio Castro. Outras quatro assumiram como vice, por períodos curtos. O décimo eleito, Douglas Ruas, foi proclamado pelo TRE-RJ em 15 de outubro deste ano e toma posse em janeiro; ainda não governou, e por isso fica fora da conta, com a conta refeita com ele mais adiante.

Dos nove eleitos, **cinco foram presos**. Todos entre novembro de 2016 e março de 2019.

Sérgio Cabral, em 17 de novembro de 2016, na Operação Calicute. Ficou preso seis anos e um mês, com cinco ordens de prisão preventiva, e saiu para a prisão domiciliar em dezembro de 2022, depois de uma decisão do STF por três votos a dois. Tem condenações em mais de vinte ações, parte delas revista.

Anthony Garotinho, em novembro de 2016, na Operação Chequinho, e mais três vezes depois, a última em 2019. Rosinha Garotinho, em 22 de novembro de 2017, junto com ele, e mais duas em 2019. A última prisão do casal foi revogada pelo STF em 31 de outubro de 2019, e os casos foram anulados.

Luiz Fernando Pezão, em 29 de novembro de 2018, na Operação Boca de Lobo, ainda no cargo, 32 dias antes do fim do mandato. Ficou preso um ano e onze dias, até a 6ª Turma do STJ mandar soltar. Foi condenado em primeira instância a 98 anos e absolvido pelo TRF-2. Em 2024 foi eleito prefeito de Piraí.

Moreira Franco, em 21 de março de 2019, na mesma operação que prendeu Michel Temer. Ficou quatro dias. O STF anulou as decisões e a denúncia foi arquivada.

Dos outros quatro, Witzel foi afastado pelo STJ em 2020, teve o pedido de prisão negado e sofreu impeachment em 2021. Castro renunciou em março de 2026, foi declarado inelegível pelo TSE e teve buscas da Polícia Federal em maio. Brizola e Marcello Alencar não têm registro.

[→ INSERIR GRÁFICO 1 - dia-143-grafico-01-a-linha-do-tempo.png]

*Os mandatos e a data da primeira prisão de cada um. Nenhuma antes de 2016.*

Cinco em nove só vira número quando tem com o que comparar. Fiz a mesma conta para os outros três estados do Sudeste, governador eleito por governador eleito, desde 1982, com a mesma regra: conta quem recebeu ordem de prisão e foi preso; investigação, denúncia e pedido de prisão negado não contam.

São Paulo, sete pessoas, nenhuma prisão localizada. Espírito Santo, sete, nenhuma. Minas Gerais, nove, uma: Eduardo Azeredo, preso em 23 de maio de 2018 depois de condenado pelo Tribunal de Justiça a 20 anos no caso do mensalão tucano.

Somando os três vizinhos, **um governador preso em 23**. No Rio, **cinco em nove**.

[→ INSERIR GRÁFICO 5 - dia-143-grafico-05-o-sudeste.png]

*Os quatro estados do Sudeste, com o intervalo de cada um.*

---

O modelo

As contas estão no notebook. Elas fazem duas perguntas: o que nove pessoas conseguem dizer, e se o Rio é diferente dos vizinhos.

O que nove pessoas dizem. Cinco em nove é 56%. É uma frequência histórica, o que aconteceu com nove pessoas, e não a chance de prisão do próximo governador. Mas nove pessoas são nove pessoas. A posterior com prior de Jeffreys dá **56%, com intervalo de 25% a 83%**. Cinquenta e sete pontos de largura. Com esse universo, a conta não distingue 30% de 80%. Para o intervalo apertar a dez pontos seriam precisos uns 370 governadores, o que, com uma eleição a cada quatro anos, dá mais de mil anos. Se a conta inclui os quatro vices que assumiram, cinco em treze, a resposta é 39%, com intervalo de 16% a 65%. Se inclui o eleito de 2026, que ainda não governou, cinco em dez, 50%, com intervalo de 22% a 78%. As três leituras apontam para o mesmo lugar.

[→ INSERIR GRÁFICO 2 - dia-143-grafico-02-nove-pessoas.png]

*A curva vermelha é o que nove pessoas conseguem dizer. A pontilhada é a mesma proporção com 377.*

A vizinhança. O Rio é diferente dos vizinhos? O teste exato de Fisher, que é o teste para tabelas pequenas assim, dá p = 0,003. Sorteando as duas chances dentro dos seus intervalos, a do Rio é maior que a dos vizinhos em 99,9% dos sorteios, e a razão mediana entre elas é de onze vezes. Com a chance dos vizinhos, ver cinco em nove teria 0,01% de probabilidade.

Fica uma segunda régua, de ordem de grandeza e não de teste. O SISDEPEN contou 905 mil pessoas sob sanção penal no Brasil em 31 de dezembro de 2024, 670 mil em celas, perto de meio por cento dos adultos num dia qualquer. É uma medida de um instante, e a dos governadores é de uma vida inteira; por isso ela não entra na conta, só no notebook, como contexto.

---

O insight

**Entre os eleitos desde 1982, cinco dos nove governadores do Rio foram presos. Nos outros três estados do Sudeste, um em 23.**

O 56% é frequência histórica, não previsão. Com nove pessoas, a estatística não diz se a chance é de um em três ou de quatro em cinco. O que ela diz, com p = 0,003, é que o Rio é diferente dos vizinhos, e que a diferença é grande o bastante para merecer explicação.

A explicação, o modelo não dá. Ele conta ordens de prisão cumpridas, e uma ordem de prisão é o encontro de duas coisas: o que a pessoa fez e o que o sistema de justiça decidiu fazer com ela. O Rio teve mais governadores envolvidos em crimes, ou mais governadores alcançados por operações que terminaram em prisão? Os dados deste dia não separam uma coisa da outra. Prisão é o evento contado; condenação é outro, e quatro dos cinco tiveram as prisões anuladas, arquivadas ou foram absolvidos depois.

*Cinco em nove contra um em 23: o que você acha que explica a diferença?*

---

O código completo está no GitHub: github.com/anac82/365-probabilidades

Este é o Dia #143 de 365. Todo dia um modelo. Todo dia uma decisão melhor.

#365Probabilidades #DecidindoComDados
