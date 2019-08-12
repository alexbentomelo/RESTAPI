

class CardModel:
    def __init__(self, client_id, card_holder, card_number, month, year, is_active):
        self.client_id = client_id
        self.card_holder = card_holder
        self.card_number = card_number
        self.month = month
        self.year = year
        self.is_active = is_active

    def json(self):
        return{
            'client_id': self.client_id,
            'card_holder': self.card_holder,
            'card_number': self.card_number,
            'month': self.month,
            'year': self.year,
            'is_active': self.is_active
        }