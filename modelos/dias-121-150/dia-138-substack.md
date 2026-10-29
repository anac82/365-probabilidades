# Qual a probabilidade de um exame positivo estar errado?

*365 Probabilidades · Dia #138*

Antes de ler, faça a conta de cabeça.

Uma doença atinge 1 pessoa em cada 1.000. O exame que detecta essa doença tem 5% de falso positivo, ou seja, de cada 100 pessoas sadias, 5 testam positivo. Uma pessoa sem nenhum sintoma faz o exame e o resultado vem positivo. Qual a chance de ela ter a doença?

Guarde o seu número.

---

## O que a ciência descobriu

Essa pergunta foi feita a médicos duas vezes. Em 1978, a 60 médicos e estudantes de Harvard. Em 2014, a 61 pessoas de hospitais de Boston, entre médicos titulares, residentes e estudantes de medicina.

**A resposta certa é 2%.** Acertaram 11 de 60 em 1978 e 14 de 61 em 2014. **A resposta mais comum, nas duas vezes, foi 95%.** Deram essa resposta 27 pessoas em cada grupo. A mediana das respostas de 2014 foi 66%.

Em 36 anos, nada mudou. A diferença entre os dois grupos não é significativa.

[→ INSERIR GRÁFICO 2 - dia-138-grafico-02-os-medicos.png]

*As respostas dos médicos em 1978 e em 2014.*

---

## O modelo

A conta é mais fácil com pessoas do que com porcentagens.

De 1.000 pessoas, 1 tem a doença, e o exame a encontra. Das 999 sadias, 5% testam positivo, o que dá cerca de 50 pessoas. São 51 resultados positivos. Só 1 é verdadeiro. **A chance de o positivo estar errado é de 98%.**

[→ INSERIR GRÁFICO 1 - dia-138-grafico-01-mil-pessoas.png]

*Mil pessoas, 51 positivos, 1 doente.*

A proporção de doentes antes do exame se chama taxa-base. É ela que a intuição esquece. O exame responde "se a pessoa tem a doença, eu acuso". A pessoa quer saber "se você acusou, eu tenho a doença". As duas perguntas só têm a mesma resposta quando a doença é comum entre quem faz o exame.

O teorema de Bayes é a conta que põe a taxa-base de volta. Com ela, dá para desenhar a curva inteira. O mesmo exame, com 5% de falso positivo, erra 98% dos positivos quando a doença atinge 1 em 1.000, erra 83% quando atinge 1 em 100, e erra 10% quando atinge 3 em 10, que é o caso de quem chega com sintomas. O positivo só passa a ter mais chance de estar certo do que errado quando a taxa-base passa de 4,8%.

[→ INSERIR GRÁFICO 3 - dia-138-grafico-03-a-curva.png]

*A chance de o positivo estar errado, em função de quantas pessoas que fazem o exame têm a doença.*

Simulei 200 mil grupos de 1.000 pessoas rastreadas. Em média aparecem 51 positivos por grupo, entre 38 e 65. Em 37% dos grupos não há nenhum doente, e todos os positivos são falsos.

Fora do laboratório, o erro se repete. Em 2021, 553 profissionais de saúde nos Estados Unidos estimaram a chance de doença depois de um exame positivo em quatro cenários clínicos. Para uma mamografia de rastreio positiva, a estimativa mediana foi 50%; a evidência diz de 3% a 9%. Para um teste de esforço positivo, 70% contra 2% a 11%. Para uma urocultura positiva, 80% contra 0% a 8%. Só no cenário da pneumonia, em que a doença é comum entre quem faz o exame, a estimativa chegou perto.

[→ INSERIR GRÁFICO 4 - dia-138-grafico-04-quatro-exames.png]

*Quatro exames reais. A estimativa dos profissionais contra a faixa da evidência.*

Três limites. As amostras de médicos são pequenas e de uma cidade só. A pergunta do estudo supõe que o exame encontra todos os doentes; com 90% de sensibilidade a resposta certa seria 1,8% em vez de 2%, e nada muda. E a curva vale para qualquer exame com aquela especificidade, mas a taxa-base de cada situação real precisa ser conhecida, e quase nunca está no laudo.

---

## O insight

**Na pergunta do estudo, 98% dos exames positivos estão errados. Três em cada quatro médicos erraram a conta, e a resposta mais comum foi 95%.**

O exame não é ruim. Cinco por cento de falso positivo é um exame bom. O problema é a taxa-base. Quando 1 pessoa em 1.000 tem a doença, o exame procura uma agulha num palheiro de 999 sadios, e 5% do palheiro é mais do que a agulha.

Se você chutou 95% no começo deste texto, está na companhia da maioria dos médicos de Boston. Se chutou perto de 2%, pode receber o resultado do seu próximo exame com outra pergunta na mão.

*Da última vez que um exame seu deu positivo, alguém perguntou quantas pessoas como você fazem esse exame?*

---

O código completo está no GitHub: github.com/anac82/365-probabilidades

Este é o Dia #138 de 365. Todo dia um modelo. Todo dia uma decisão melhor.

#365Probabilidades #DecidindoComDados
