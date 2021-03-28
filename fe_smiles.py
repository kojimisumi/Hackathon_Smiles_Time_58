# importação dos módulos
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


# instanciando o Flask
app = Flask(__name__)


# ChatBot
@app.route('/bot', methods=['POST'])
def bot():

    # mensagem que o ChatBot recebe do usuário
    incoming_msg = request.values.get('Body', '')

    # condicionais para um exemplo do fluxo de mensagens do produto
    if str(incoming_msg) == 'Oi':
        resp = MessagingResponse()
        msg = resp.message()
        msg.body('Olá, Vinícius! Eu sou a *Fe Smiles*!\n\nA Smiles tem como propósito promover a evolução das pessoas por meio da _viagem_.\n\nVocê tem alguma viagem dos sonhos? Se sim, me diga qual!')
        return str(resp)

    if str(incoming_msg) == 'Não sei':
        resp = MessagingResponse()
        msg = resp.message()
        msg.body('Eu sei que é difícil se planejar para uma viagem... Quanto que você consegue economizar por mês?')
        return str(resp)

    if 'reais' in str(incoming_msg):
        resp = MessagingResponse()
        msg = resp.message()
        msg.body('Muito bem, Vinícius! E de qual cidade você é?')
        return str(resp)

    if 'Sao Paulo' in str(incoming_msg):
        resp = MessagingResponse()
        msg = resp.message()
        msg.body('Olha essa sugestão!!\n\nPassagem de ida e volta para *Fortaleza* + hospedagem por 5 noites:  R$1500 comprando com 15 dias de antecedência...\n\nVocê gostaria de *pagar menos* por essa viagem?')
        # envio da imagem da Praia de Fortaleza para o usuário
        msg.media('https://www.cvc.com.br/dicas-de-viagem/wp-content/uploads/2019/02/FOrtaleza-praias-topo_1100655731.jpg')
        return str(resp)

    if str(incoming_msg) == 'Sim':
        resp = MessagingResponse()
        msg = resp.message()
        #msg.body('Você pode economizar mais de R$400 com planejamento e o Clube Smiles, pagando 56.000 milhas, e ainda acumulando mais milhas para poder viajar!\n\nPara obtenção das milhas, recomendamos para você o Clube Smiles, mas você pode conhecer outros planos no site da Smiles: https://www.smiles.com.br/clube-smiles/bonus-de-montao-23-03-21%27 ')
        msg.body('Economize mais de *R$400* com planejamento e o Clube Smiles, pagando 56.000 milhas, e ainda acumulando mais milhas para poder viajar!\n\nPara obter as milhas, sugerimos o *Plano 2000*: https://www.smiles.com.br/clube-smiles/\n\nVinícius, me avise quando adquirir um plano!')
        return str(resp)

    if 'plano' in str(incoming_msg):
        resp = MessagingResponse()
        msg = resp.message()
        msg.body('Perfeito, Vinícius! Agora que você é *Clube Smiles*, você só precisa economizar R$40/mês para realizar a viagem dos seus sonhos em 11 meses!\n\nAtive o *Radar Smiles* no aplicativo para receber atualizações de preços da sua viagem e aproveite o *Shopping Smiles* para obter ainda mais milhas!')
        return str(resp)

# definindo a instância main
if __name__ == '__main__':
   app.run(debug=True)