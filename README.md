# Hackathon Smiles - Time 58 - Chatbot WhatsApp

## Time
- Alex Koji Misumi 
- Gabriel Paganini de Oliveira Pinto
- Ricardo Nicida Kazama
- Victoria da Costa Gonçalves
- Vinícius Bueno Bernardes

## Produto
Demos vida à Fe Smiles, uma ChatBot de WhatsApp para melhorar a experiência do cliente, ajudando com o planejamento financeiro e, assim, deixar a relação com as viagens mais prática e prazerosa

<div style="text-align:center"><img src="https://user-images.githubusercontent.com/79596598/112763807-6b420d00-8fdc-11eb-92ce-4b7d31572e53.png" /></div>

## Funcionalidades
- [X] Programa personalizado: Ajuda na escolha da viagem e do plano Smiles
- [X] Planejamento de viagem: Acompanhamento da preparação da viagem escolhida 
- [X] Recomendação de ferramentas já existentes no site e no aplicativo Smiles (como Radar Smiles e o Shopping Smiles)

## Exemplo do uso da ferramenta
<table>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/79596598/112765039-aa269180-8fe1-11eb-805e-4e83d1c7f3d4.png"/>
    <td><img src="https://user-images.githubusercontent.com/79596598/112765056-b90d4400-8fe1-11eb-9413-e537fcfeed90.png"/>
    <td><img src="https://user-images.githubusercontent.com/79596598/112765130-1dc89e80-8fe2-11eb-9e69-10f03d95bb88.png"/>
  </tr>
 </table>

## Próximos passos
- [X] Oferecimento de produtos do **Shopping Smiles** de acordo com o tipo de viagem escolhida pelo cliente
- [X] Monitoramento do preço com o **Radar Smiles** através da Fe
- [X] Utilizar ferramentas de PLN (Processamento de Linguagem Natural) para incorporar técnicas mais avançadas de processamento de texto e de áudio com bibliotecas como nltk e spacy
- [X] Utilização de base de dados para técnicas de Machine Learning e Deep Learning (possível utilização de Transfer Learning para aprimorar o entendimento de textos)

## Linguagem de programação
- Linguagem: Python 3.9.2
- IDE: PyCharm

## Módulos utilizados
- Framework **_Flask_**, para poder criar uma aplicação web
- **_Twilio Python Helper Library_**, para trabalhar com API's da Twilio

## Comentários adicionais
- Seguindo boas práticas de programação, o projeto da Fe Smiles foi desenvolvido em um ambiente virtual
- Para enviar mensagens para o WhatsApp, foi preciso criar uma conta no site https://www.twilio.com/whatsapp
- Para tornar o serviço do chatbot acessível a partir da internet, foi utilizado o **_ngrok_** (https://ngrok.com/)
- O chatbot é inicializado com o comando **_python fe_smiles.py_**
- Para mais detalhes das configurações, entre no link https://www.twilio.com/blog/construa-chatbot-whatsapp-python-flask-twilio. Este link foi utilizado como referência para construção do nosso bot.
