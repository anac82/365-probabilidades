Qual a probabilidade de você achar que mês que vem vai ter mais tempo?

*Como venho fazendo desde o Dia #111, o texto aqui é o mais simples que eu consigo escrever. O rigor está no notebook, no GitHub, com o código e as contas.*

Quando alguém me convida para alguma coisa daqui a um mês, eu digo sim. Um café, uma conversa que ficou pendente, uma palestra. Mês que vem a agenda está vazia, então cabe.

Quando o mês chega, a agenda está igual à de hoje. Cheia das mesmas coisas, mais o que eu aceitei quando ela parecia vazia.

Este é o segundo dia da trilha do tempo. O primeiro mediu a desculpa. Este mede a previsão. Fui ver se alguém já tinha testado se a gente acredita mesmo que o mês que vem vai ter mais tempo do que hoje, e se acredita mais nisso do que no dinheiro.

---

O que a ciência descobriu

Dois pesquisadores de marketing, Gal Zauberman e John Lynch, publicaram em 2005 sete surveys sobre isso, com estudantes. A ideia tem nome: folga esperada. A pessoa olha para o mês que vem e vê tempo sobrando, porque os compromissos de lá ainda não têm nome. Olha para o dinheiro do mês que vem e vê quase o mesmo de hoje, porque dinheiro tem extrato.

O experimento central tem 264 pessoas e uma tarefa só, apresentada de quatro jeitos. Custo em tempo ou em dinheiro. Para hoje ou para daqui a um mês.

Quando o custo é em tempo, **39% aceitam para hoje e 56% aceitam para daqui a um mês**. Quando o custo é em dinheiro, acontece o contrário: 70% aceitam para hoje e 62% para daqui a um mês.

[→ INSERIR GRÁFICO 1 - dia-137-grafico-01-hoje-e-um-mes.png]

*A mesma tarefa, hoje e daqui a um mês. O prazo faz o tempo subir e o dinheiro descer.*

Perguntadas quanto tempo vão ter mês que vem, numa escala de 1 a 10 em que 5,5 é "igual a hoje", 76 pessoas responderam **8,2**. Para dinheiro, 7,0.

---

O modelo

As contas estão no notebook. O que elas mostram é isto.

A resposta do dia é a diferença entre os 56% e os 39%. São 17 pontos, com intervalo largo, porque cada célula tem 66 pessoas. Mas em 97% dos sorteios a diferença é positiva. Daqui a um mês, 1,45 vez mais gente diz sim.

[→ INSERIR GRÁFICO 2 - dia-137-grafico-02-bayesiano.png]

*As duas proporções com a incerteza de 66 pessoas, e a diferença entre elas.*

A segunda parte põe o dinheiro ao lado. O prazo sobe o tempo em 16 pontos e desce o dinheiro em 8. A chance de o prazo ajudar mais o tempo do que o dinheiro é de 98%.

A terceira parte mede o erro. A folga de tempo esperada, 8,2, fica quase um desvio-padrão acima do "igual a hoje". E tem um dado que eu achei o mais revelador do artigo. Em 130 pessoas, a folga de tempo que cada uma esperava para amanhã não tinha relação nenhuma com a que esperava para daqui a duas semanas, correlação de 0,03. Para dinheiro, 0,45. A previsão de tempo é chute. A de dinheiro, não.

[→ INSERIR GRÁFICO 3 - dia-137-grafico-03-o-erro-de-previsao.png]

*A folga esperada de tempo, à esquerda. À direita, o quanto a previsão de amanhã prevê a de duas semanas.*

A quarta parte sorteia um ano com um convite por mês, aceito de longe com os 56% e avaliado na hora com os 39%. Dá cerca de sete aceitos por ano, e dois que viram "droga" quando o dia chega. A chance de passar o ano sem nenhum é de uma em cinco. A conta supõe que quem diria sim na hora também diz sim de longe, e por isso é um limite inferior.

[→ INSERIR GRÁFICO 4 - dia-137-grafico-04-a-agenda.png]

*Doze convites por ano. Quantos "sim" viram "droga".*

Dois limites. São estudantes americanos respondendo a cenários no papel; o único estudo com comportamento real tem 178 pessoas e mede presença numa palestra, em que mais da metade dos que disseram que iam não foram. E as contagens do experimento central são reconstruídas dos percentuais, com 66 por célula.

---

O insight

**A mesma tarefa é aceita por 39% para hoje e por 56% para daqui a um mês.**

Quase um em cada três "sim" dados de longe viraria "não" na hora. Com dinheiro é o contrário. O mês que vem parece folgado porque os compromissos de lá ainda não têm nome, e a previsão de quanto tempo vai sobrar não acerta nem a de amanhã.

*Qual foi o último compromisso que você aceitou porque mês que vem ia estar mais folgado?*

---

O código completo está no GitHub: github.com/anac82/365-probabilidades

Este é o Dia #137 de 365. Todo dia um modelo. Todo dia uma decisão melhor.

#365Probabilidades #DecidindoComDados #ProbabilidadesDoTempo
