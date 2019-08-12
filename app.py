from flask import Flask
from flask_restful import Api
from urllib.parse import urlparse
from resources.cartao import Cartoes, Card, NewCard, Validthru

app = Flask(__name__)
api = Api(app)


api.add_resource(Cartoes, '/cartoes')
api.add_resource(Card, '/cartoes/<string:card_holder>')
api.add_resource(NewCard, '/novocartao/<string:client_id>')
api.add_resource(Validthru, '/validthru')


if __name__ == '__main__':
    app.run(debug=True)