# Qual a probabilidade de o seu sobrenome desaparecer?

*365 Probabilidades · Dia #142*

[UMA LINHA DA ANA: o seu sobrenome, de onde ele veio ou quem ainda o carrega.]

Dia de Finados é dia de ler nomes. Nas lápides, nas placas de rua, nos ossários, os sobrenomes ficam depois das pessoas. Alguns parecem eternos. Outros ninguém mais ouve falar.

Em 1873, Francis Galton publicou uma pergunta num jornal de matemática. As famílias inglesas de nome ilustre estavam sumindo, e ele queria saber se isso era azar ou aritmética. Um reverendo chamado Henry William Watson resolveu a conta, e os dois publicaram juntos em 1875. Watson concluiu que toda família acaba. Estava errado, e o erro levou cinquenta anos para ser corrigido. Mas a conta dele, consertada, é até hoje o jeito de responder quanto tempo um nome dura.

Fui fazer essa conta com os números do Brasil.

---

## O que a ciência descobriu

A ideia de Galton é simples. Um sobrenome passa de pai para filho como uma árvore cresce. Cada homem tem um certo número de filhos homens, cada filho repete a história, e se em alguma geração ninguém tem filho homem, a linhagem acaba. O que decide o destino do nome é um número só, que os matemáticos chamam de **m**, e que é a média de filhos homens que cada homem deixa.

Quando m é maior que 1, a linhagem tem uma chance real de durar para sempre. Quando m é menor ou igual a 1, a extinção é certa, e a única pergunta passa a ser quando. Foi aí que Watson errou. A conta dele dava extinção certa em qualquer caso, e um dinamarquês chamado Steffensen mostrou, em 1930, que isso só valia de um lado da linha.

O Brasil cruzou essa linha há pouco tempo. Em 1960, cada mulher tinha em média **6,28 filhos**, segundo o IBGE. Pelo Censo 2022, divulgado em junho de 2025, são **1,55**. Como 51,2% dos nascidos são meninos (contei isso no SINASC, no Dia #136), cada homem deixa hoje, em média, **0,79 filho homem**. Em 1960 deixava 3,2. A linha que separa os dois mundos fica em 1,95 filhos por mulher, e o país passou por ela por volta de 2010.

Dois detalhes do Censo que entram na conta. Em 2022, 16,2% das mulheres não tinham filhos, contra 10% em 2000. E a fecundidade varia bastante por grupo. Entre as mulheres amarelas é 1,22, brancas 1,35, pretas 1,59, pardas 1,68, indígenas 2,48. Só o último grupo ainda está do lado de cima da linha.

A mesma matemática explica uma coisa que a gente vê em outros países. Na Coreia do Sul, pelo censo de 2015, **21,5% das pessoas se chamam Kim, 14,7% Lee e 8,4% Park**. Três sobrenomes em 45% do país. Ali a concentração tem muita história por trás, famílias comuns foram adotando nomes de elite durante séculos, então o modelo não explica a Coreia. Mas ele explica a direção. Quando as linhagens vão se apagando, os nomes raros somem primeiro e os comuns ficam. No Japão, um pesquisador da Universidade de Tohoku fez em 2024 o exercício de levar a tendência atual ao limite e calculou que, mantida a lei do sobrenome único, em 2531 todo japonês se chamaria Sato. É uma provocação, não um dado, mas mostra para onde a conta aponta.

---

## O modelo

As contas estão no notebook. Elas respondem a quatro perguntas.

**Qual a chance de o sobrenome de um homem acabar?** Com a fecundidade de hoje, **45% de chance de acabar já na próxima geração**, porque 45% dos homens não deixam filho homem. **87% em cinco gerações. 97% em dez.** Uma linhagem que começa hoje dura, em média, 2,9 gerações, pouco mais de oitenta anos.

[→ INSERIR GRÁFICO 1 - dia-142-grafico-01-geracao-a-geracao.png]

*A chance de a linhagem já ter acabado, geração a geração. Em vermelho, o Brasil de 2022. Em verde, o de 1960.*

**E se fosse em 1960?** Com 6,28 filhos por mulher, a chance de o nome acabar algum dia era de 4,7%. Noventa e cinco por cento das linhagens durariam para sempre. A diferença entre as duas curvas do gráfico não é sorte. É um número que caiu de 3,2 para 0,79.

[→ INSERIR GRÁFICO 2 - dia-142-grafico-02-a-linha.png]

*A linha de Galton e Watson. À esquerda de 1,95 filhos por mulher, a extinção é certa. Os pontos dourados são os grupos do Censo 2022.*

**O que acontece com cem sobrenomes?** Sorteei cem linhagens que começam com um homem hoje. Na primeira geração sobram 57. Na quinta, 13. Na décima, 3. A fórmula previa quase exatamente isso.

[→ INSERIR GRÁFICO 3 - dia-142-grafico-03-cem-linhagens.png]

*Cem sobrenomes sorteados por dez gerações, e a curva que a fórmula de 1875 previa.*

**E os nomes comuns?** Um sobrenome carregado por mil homens é, na prática, mil linhagens independentes, e só acaba quando a última delas acaba. Um nome com um homem hoje passa de 50% de chance de ter sumido na segunda geração. Com dez homens, na oitava. Com cem, na décima sétima. **Com dez mil homens, só na trigésima sétima geração, mais de mil anos.** É por isso que um país de fecundidade baixa perde variedade de nomes sem perder os nomes.

[→ INSERIR GRÁFICO 4 - dia-142-grafico-04-raro-e-comum.png]

*Quanto tempo um sobrenome dura, conforme quantos homens o carregam hoje.*

Vale dizer o que o modelo simplifica. O número de filhos por homem segue uma distribuição de Poisson com a média do Censo, que é a hipótese clássica; com famílias mais desiguais, a extinção na primeira geração sobe para 53% e a de longo prazo quase não muda. A fecundidade foi mantida constante, e ela caiu de 6,28 para 1,55 em sessenta anos, então pode mudar de novo. E o nome passa só pelo filho homem, que é a regra do modelo original. No Brasil muita gente carrega os dois sobrenomes, e se qualquer filho levar o nome a conta muda bastante, e a chance de acabar algum dia cai para 39%.

---

## O insight

**Com a fecundidade do Brasil de hoje, o sobrenome de um homem tem 45% de chance de acabar já na próxima geração, 87% em cinco gerações e 97% em dez. Em 1960, a chance de acabar algum dia era de 5%.**

O que mudou não foi a sorte, foi a média. Quando cada homem deixa menos de um filho homem, e hoje deixa 0,79, a extinção de cada linhagem deixa de ser possível e passa a ser certa. A conta é de 1875 e continua valendo.

O que isso não quer dizer é que o Brasil vai ficar sem sobrenomes. Os raros somem primeiro, os comuns ficam, e um nome com dez mil homens leva mil anos para correr o mesmo risco que um nome com um homem só corre em uma geração.

No Dia de Finados, os nomes nas lápides parecem a parte que fica. A matemática diz que a maioria deles é a parte que passa. O que fica é outra coisa.

*Quantas gerações para trás você consegue dizer o sobrenome inteiro? E para a frente?*

---

O código completo está no GitHub: github.com/anac82/365-probabilidades

Este é o Dia #142 de 365. Todo dia um modelo. Todo dia uma decisão melhor.

#365Probabilidades #DecidindoComDados
