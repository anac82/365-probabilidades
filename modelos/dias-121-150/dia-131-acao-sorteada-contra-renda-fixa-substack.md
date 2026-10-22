Qual a probabilidade de uma ação sorteada perder para a renda fixa?

*Como venho fazendo desde o Dia #111, o texto aqui é o mais simples que eu consigo escrever. O rigor está no notebook, no GitHub, com o código e as contas.*

Todo mundo tem uma ação assim. A que o amigo falou, a que apareceu na reportagem, a que "ia explodir". Você comprou um pouco, só para ver. Faz uns anos. Ela não explodiu. Ou explodiu e você vendeu antes. E neste período de instabilidade, provocado por vários fatores, entre eles as eleições, você olha para ela de novo e se pergunta se não teria sido melhor deixar o dinheiro na renda fixa.

A frase que fez você comprar é a frase que o mercado inteiro repete, ação rende mais do que renda fixa no longo prazo. Para a bolsa inteira, a frase é verdadeira. Fui ver se vale para uma ação.

---

O que a ciência descobriu

Hendrik Bessembinder, da Arizona State University, pegou todas as ações que passaram pela bolsa americana entre 1926 e 2016. **25.967 ações**, da listagem até o dia em que saíram do pregão. Para cada uma, comparou o que ela rendeu na vida inteira com o que teria rendido o título do Tesouro americano de um mês, o ativo mais seguro que existe em dólar. No Brasil, o equivalente é o Tesouro Selic. É isso que "renda fixa" quer dizer aqui.

**57,4% das ações perderam para o Tesouro.** Quatro em cada sete. Menos da metade teve retorno positivo. A vida mediana de uma ação na bolsa é de 7,5 anos.

[→ INSERIR GRÁFICO 1 - dia-131-grafico-01-os-horizontes.png]

*Em um mês, cara ou coroa. Em dez anos, cara ou coroa. Na vida inteira, quatro em sete perdem.*

O desenho por prazo é o que explica. Uma ação sorteada ganha do Tesouro em 47,8% dos meses, em 51,6% dos anos e em 49,5% das décadas. Moeda honesta, mais ou menos. E ainda assim, na vida inteira, só 42,6% ganham.

Em 2023, o mesmo autor repetiu a conta com 64 mil ações de 42 países, entre 1990 e 2020. Deu a mesma coisa, 55% das americanas e 57% das estrangeiras abaixo do Tesouro.

---

O modelo

As contas estão no notebook. O que elas fazem é mostrar o mecanismo, desenhar a escada e medir a concentração.

O mecanismo é a assimetria. O máximo que uma ação perde é 100%. O máximo que ela ganha não tem teto. Quando a cauda da direita é longa, a média fica acima da mediana, e os juros compostos esticam a cauda a cada ano. Montei um modelo simples de retorno mensal, calibrado nos números do paper, e sorteei uma ação pela vida mediana de 7,5 anos, vinte mil vezes. A ação do meio rendeu 5% a menos que o Tesouro. A média rendeu 73% a mais. As duas coisas ao mesmo tempo, na mesma distribuição.

[→ INSERIR GRÁFICO 2 - dia-131-grafico-02-a-assimetria.png]

*A média fica acima do Tesouro. A ação do meio fica abaixo. O modelo não tem falência, por isso é mais gentil que o dado real.*

A escada. O paper sorteia carteiras e segura por dez anos. Com uma ação, a carteira ganha do Tesouro em 47,8% das vezes. Com 25 ações, em 86,9%. Com 100, em 93,1%. O meu modelo reproduz os três pontos com erro de um a três pontos e preenche o meio, com 2 ações, 62%; com 5, 76%; com 10, 84%.

[→ INSERIR GRÁFICO 3 - dia-131-grafico-03-a-escada.png]

*A mesma moeda viciada, jogada muitas vezes ao mesmo tempo. A linha tracejada é a chance de a carteira conter uma das empresas que fizeram o ganho.*

A concentração. Quando a conta é feita em dólares, e não em contagem, **1.092 empresas, 4,3% do total, explicam todo o ganho líquido da bolsa americana em noventa anos**, cerca de 35 trilhões de dólares acima do Tesouro. Noventa empresas fizeram mais da metade. As outras 96%, somadas, empataram com o Tesouro. Uma ação sorteada tem 4,3% de chance de ser uma das 1.092. Uma carteira de 25 tem 67%. Uma de 100, 99%.

[→ INSERIR GRÁFICO 4 - dia-131-grafico-04-a-concentracao.png]

*4,3% das empresas, 100% do ganho líquido.*

---

O insight

**Quatro em cada sete ações perderam para o Tesouro ao longo da vida. 57,4%, com N = 25.967.**

A frase do mercado é verdadeira para a bolsa inteira e falsa para a ação típica. As duas coisas ao mesmo tempo, pelo mesmo motivo. A média é feita por pouquíssimas empresas, e a cauda que puxa a média fica com poucos.

A escada é a conta que falta. Uma ação sorteada ganha do Tesouro em 48% das décadas. Vinte e cinco, em 87%. Cem, em 93%.

Nada aqui é recomendação. É a distribuição.

*Qual é a ação que você comprou porque "ia explodir", e quanto do seu dinheiro está nela?*

---

O código completo está no GitHub: github.com/anac82/365-probabilidades

Este é o Dia #131 de 365. Todo dia um modelo. Todo dia uma decisão melhor.

#365Probabilidades #DecidindoComDados
