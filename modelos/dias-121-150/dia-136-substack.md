# Qual a probabilidade de nascerem mais bebês na lua cheia?

*365 Probabilidades · Dia #136*

Esses dias, conversando com uma tia, ouvi a história de uma conhecida dela que estava grávida. A mala da maternidade já estava pronta, porque quando a lua virasse o bebê ia nascer. Disso ela tinha certeza.

Guardei o tema e fiquei esperando a lua virar, para ver o que aconteceria. Enquanto isso, fui atrás dos dados.

Quem já trabalhou numa maternidade costuma ter uma opinião sobre o que a lua cheia faz com o plantão. Quem já pariu também. É uma das crenças mais antigas sobre o corpo, e uma das mais fáceis de testar, porque o Brasil registra o dia de nascimento de todos os bebês.

A lua ficou cheia ontem, à 1h12 da manhã. Fui contar, até que o bebê de verdade nascesse, ou não.

---

## O que a ciência descobriu

Uma dupla da Universidade de Halle, na Alemanha, pegou 4.071.669 nascimentos de Baden-Württemberg, de 1966 a 2003, e procurou na série diária um ciclo de 29,53 dias, que é o período da lua. O método se chama análise espectral. Ele decompõe a série em ciclos e mede a força de cada um.

Os ciclos que apareceram foram a semana e o ano. No período da lua, nada. O teste deu p = 0,688.

Nos Estados Unidos, 564.039 nascimentos da Carolina do Norte, de 1997 a 2001, foram divididos pelas oito fases da lua. Nenhuma fase teve mais nascimentos, mais cesáreas ou mais complicações do que as outras.

Nenhum desses estudos usou dado brasileiro. O Brasil tem o SINASC, o registro nacional de nascidos vivos, com a data de cada nascimento. Baixei os seis anos mais recentes e fiz a conta.

---

## O modelo

São 15.745.215 nascimentos em 2.192 dias, de 2019 a 2024. A posição da lua em cada dia vem do algoritmo de Meeus, o mesmo dos almanaques astronômicos. No período houve 74 luas cheias.

A primeira coisa que a série mostra não é a lua. É o calendário do hospital. Uma segunda-feira tem 7.900 nascimentos. Um domingo tem 5.500, 31% a menos. Um feriado tem 16% a menos. Quase tudo isso é cesárea. No domingo, as cesáreas caem 47% e os partos vaginais caem 3%.

[→ INSERIR GRÁFICO 1 - dia-136-grafico-01-calendario.png]

*O dia da semana manda. A linha dourada é o efeito da lua cheia, na mesma escala.*

Por isso a lua não pode ser comparada com a média. Uma lua cheia que cai no domingo sempre vai parecer vazia. O modelo calcula, para cada dia, quantos nascimentos seriam esperados naquele dia da semana, naquele mês, com ou sem feriado. Depois divide o observado pelo esperado.

Nos 74 dias de lua cheia, o esperado era 535.644 nascimentos. Nasceram 538.282. A razão é 1,0049, ou seja, **0,5% a mais**, com intervalo de 95% de -0,2% a +1,1%. São 35 bebês a mais num dia de 7.200.

Olhando lua por lua, **44 das 74 tiveram mais nascimentos do que o esperado. É 59%**, com intervalo de 48% a 70%. Uma moeda honesta dá 50%.

[→ INSERIR GRÁFICO 2 - dia-136-grafico-02-as-luas-cheias.png]

*As 74 luas cheias, cada uma comparada com o esperado para o seu dia.*

Para saber se 0,5% é alguma coisa, fiz a mesma conta com trinta calendários falsos, com a lua cheia adiantada ou atrasada de 1 a 15 dias. O calendário verdadeiro ficou em terceiro lugar entre os trinta. Se a lua não fizesse nada, a chance de ficar em terceiro ou acima seria de 10%.

[→ INSERIR GRÁFICO 3 - dia-136-grafico-03-calendario-deslocado.png]

*Trinta calendários lunares, um verdadeiro.*

Depois repeti tudo só com os partos vaginais, que são os partos em que o hospital não escolhe a data. Ali o sinal é o mais forte da série, 0,6% a mais, com intervalo de -0,04% a +1,3%. Ainda assim, um dos trinta calendários deslocados deu resultado maior do que o verdadeiro.

Por fim, apliquei o método dos alemães. O periodograma da série brasileira tem um pico enorme nos 7 dias e outro nos 3,5 dias, que é a semana vista duas vezes. Nos 29,53 dias, a potência é 3.300 vezes menor do que a da semana e fica no percentil 72 entre todos os períodos de 2 a 60 dias. Um ciclo que fosse real apareceria como pico. Não aparece.

[→ INSERIR GRÁFICO 4 - dia-136-grafico-04-periodograma.png]

*A semana aparece. A lua, não.*

Três limites. O dia de lua cheia é o dia civil de Brasília que contém o instante da lua cheia, e o país tem quatro fusos; a janela de três dias em volta da lua cheia dá 0,25% a mais, metade do dia isolado. O esperado de cada dia não conhece feriados estaduais nem pontes, que ficam no ruído. E são seis anos de dados, contra 38 do estudo alemão; a direção do resultado é a mesma.

---

## O insight

**Em 59% das luas cheias nasceram mais bebês do que o esperado. O excesso é de 0,5%, e a margem de erro inclui o zero.**

Se a lua cheia faz alguma coisa com a maternidade, ela faz sessenta vezes menos do que o dia da semana. O domingo tira 2.200 bebês de um dia. A lua cheia, no máximo, põe 35.

Quem já viu um plantão lotado numa noite de lua cheia viu de verdade. Também viu, e não guardou, os plantões lotados nas outras noites. A estatística não tem memória seletiva. Ela conta todas as noites.

O bebê da história [nasceu na lua cheia / nasceu antes / ainda não tinha nascido quando fechei este texto]. Com 59% de chance, o resultado seria o mesmo em qualquer caso.

*Qual crença sua sobreviveria a ser contada todos os dias, e não só nos dias marcantes?*

---

O código completo está no GitHub: github.com/anac82/365-probabilidades

Este é o Dia #136 de 365. Todo dia um modelo. Todo dia uma decisão melhor.

#365Probabilidades #DecidindoComDados
