from flask_restful import Resource, reqparse
from models.cartao import CardModel

cartoes = [
        {
        'client_id': 22,
        'card_holder': 'Roberto Justus',
        'card_number': '**********9374',
        'month': 2,
        'year': 2021,
        'is_active': 'true'
        },
        {
        'client_id': 20,
        'card_holder': 'Lucius Dominus',
        'card_number': '**********9374',
        'month': 2,
        'year': 2020,
        'is_active': 'true'
        },
        {
        'client_id': 26,
        'card_holder': 'Albert Eistein',
        'card_number': '**********9374',
        'month': 2,
        'year': 2020,
        'is_active': 'true'
        },
        {
        'client_id': 23,
        'card_holder': 'Luciano Huck',
        'card_number': '**********3649',
        'month': 3,
        'year': 2021,
        'is_active': 'true'
        },
        {
        'client_id': 24,
        'card_holder': 'Fabiana Maria',
        'card_number': '**********9374',
        'month': 4,
        'year': 2022,
        'is_active': 'true'
        },
        {
        'client_id': 25,
        'card_holder': 'Bento César',
        'card_number': '**********3649',
        'month': 5,
        'year': 2023,
        'is_active': 'true'
        }
]

def normalize_path_params(month=1,
                           year=2019, **dados):

    return {
        'month':month,
        'year':year
    }

path_params = reqparse.RequestParser()
path_params.add_argument('month', type=int)
path_params.add_argument('year', type=int)



class Cartoes(Resource):
    def get(self):
        return {'cartoes': cartoes}

class Card(Resource):
    def find_card_holder(card_holder):
        for cartao in cartoes:
            if cartao['card_holder'] == card_holder:
                return cartao
        return None
    def get(self, card_holder):
        cartao = Card.find_card_holder(card_holder)
        if cartao:
            return cartao
        return {'message': 'Cartao/Nome não encontrado'}, 404

class Validthru(Resource):
    def get(self):
        global cartoes

        dados = path_params.parse_args()

        print(dados)

        dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None}

        parametros = normalize_path_params(**dados_validos)
       
        cartoes = [cartao for cartao in cartoes if (cartao['month'] == parametros.get('month') and cartao['year'] == parametros.get('year'))]
        if cartoes:
            return {'cartoes': cartoes}
        return {'message': 'Cartao não encontrado'}, 404

class NewCard(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('card_holder')
    argumentos.add_argument('card_number')
    argumentos.add_argument('month')
    argumentos.add_argument('year')
    argumentos.add_argument('is_active')
    def find_card(client_id):
        for cartao in cartoes:
            if cartao['client_id'] == client_id:
                return cartao
        return None

    def post(self, client_id):
        dados = NewCard.argumentos.parse_args()

        novo_card = CardModel(client_id, **dados)

        novo_card = novo_card.json()

        cartoes.append(novo_card)
        return novo_card, 200
     
    def put(self, client_id):
        dados = NewCard.argumentos.parse_args()

        novo_card = CardModel(client_id, **dados)

        novo_card = novo_card.json()

        cartao = NewCard.find_card(client_id)
        if cartao:
            cartao.update(novo_card)
            return novo_card, 200
        cartoes.append(novo_card)
        return novo_card, 201
    
    def delete(self, client_id):
        global cartoes
        cartoes = [cartao for cartao in cartoes if cartao['client_id'] != client_id]
        return {'message': 'Cartao Deletado'}
