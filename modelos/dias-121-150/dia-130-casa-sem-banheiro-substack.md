Qual a probabilidade de uma casa no Brasil ainda não ter banheiro?

*Como venho fazendo desde o Dia #111, o texto aqui é o mais simples que eu consigo escrever. O rigor está no notebook, no GitHub, com o código e as contas.*

Um leitor comentou o Dia #120, o da pia que era sonho e virou bancada. Ele contou que entrevistou os avós para entender o que foi ser criança nos anos 1940, e pediu mais dias sobre as mudanças na vida da população. E fechou com uma lista do que ele valorizava, não podia ter, e hoje banaliza: a fotografia, o ar-condicionado, a fruta de outro país.

Comecei pelo item que não estava na lista dele, porque ninguém põe na lista. O banheiro.

Em 1940, menos de 20% dos lares brasileiros tinham um. Fui ver quantos ainda não têm.

---

A conta que ninguém faz

O Censo pergunta a cada casa do país se há banheiro, quantos são e de quem é o uso. Banheiro, para o IBGE, é o cômodo com vaso sanitário e chuveiro. A casa pode ter um só dela, um dividido com outra casa, só um sanitário ou buraco no terreno, ou nada.

Em 2022, de 72,5 milhões de domicílios:

**367 mil** não tinham banheiro nem sanitário. Uma casa em 197. Nelas moravam 1,2 milhão de pessoas.

**675 mil** tinham só um sanitário ou um buraco no terreno. **329 mil** tinham só um banheiro dividido com outra casa.

Somando tudo o que não é um banheiro só da casa, **1,37 milhão de domicílios, 1,9%**, uma casa em 53. São 4,5 milhões de pessoas.

[→ INSERIR GRÁFICO 1 - dia-130-grafico-01-a-serie.png]

*Em 2000, uma casa em seis não tinha banheiro. Em 2022, uma em 70.*

O número de hoje é pequeno porque a queda foi enorme. Em 2000, 16,7% das casas não tinham banheiro; no campo, mais da metade, 54%. Em 2010, 6,7%. Em 2022, 1,4%. Como o Censo conta todo mundo, não há intervalo de confiança aqui. É a resposta.

---

O modelo

As contas estão no notebook. O que elas fazem com a resposta é medir a velocidade, perguntar de quem é a casa e traduzir a fração em algo que se vê.

A velocidade. Entre 2000 e 2022, a fração de casas sem banheiro caiu 11% ao ano, o que significa cair pela metade a cada 6 anos. De 1940 a 2000, o ritmo tinha sido de 2,6% ao ano. Se a velocidade atual se mantiver, o país chega a 0,5% por volta de 2032. É extrapolação, e a última milha costuma ser mais lenta.

De quem é a casa. O 1,9% não é uma média espalhada pelo país. É um endereço. No Acre e no Maranhão, uma casa em sete não tem banheiro só dela. Em São Paulo, uma em mil. A razão entre os extremos é de 155 vezes.

[→ INSERIR GRÁFICO 2 - dia-130-grafico-02-estado-a-estado.png]

*A mesma pergunta, estado a estado.*

E é a casa das crianças. Entre os menores de 15 anos, 3,5% moram em casa sem banheiro exclusivo, contra 1,3% dos maiores de 65. São 1,4 milhão de crianças, e 354 mil delas em casa sem banheiro nem sanitário.

[→ INSERIR GRÁFICO 3 - dia-130-grafico-03-as-criancas.png]

*Quanto mais nova a pessoa, maior a chance de a casa não ter banheiro.*

A sala de aula. Se uma turma de 30 crianças fosse sorteada do país inteiro, a chance de ao menos uma voltar para uma casa sem banheiro seria de 65%. No Piauí e no Maranhão, acima de 90%. Em São Paulo, 3%.

[→ INSERIR GRÁFICO 4 - dia-130-grafico-04-a-sala-de-aula.png]

*A conta é 1 − (1 − p)ⁿ. Turmas reais são de um bairro, e o bairro importa mais que o estado.*

---

O insight

**Uma casa em cada 53 no Brasil não tem banheiro só dela. Uma em cada 197 não tem banheiro nem sanitário.**

Em 1940 o banheiro era minoria. Em 2000, faltava em uma casa de cada seis. Hoje falta em uma de cada 70, e a fração cai pela metade a cada 6 anos.

O leitor tinha razão. A fotografia, o ar-condicionado e a fruta de outro país ficaram baratos e a gente banalizou. O banheiro chegou mais longe que todos eles. E ainda não chegou em todo mundo. Quem falta mora no Norte e no Nordeste, e é criança.

*Você sabe o ano em que a casa dos seus avós ganhou um banheiro?*

---

O código completo está no GitHub: github.com/anac82/365-probabilidades

Este é o Dia #130 de 365. Todo dia um modelo. Todo dia uma decisão melhor.

#365Probabilidades #DecidindoComDados
