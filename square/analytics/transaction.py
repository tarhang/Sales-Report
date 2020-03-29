from datetime import datetime


class Transaction(object):
    def __init__(self, date, t, gross_sale, tax, payment_type, transaction_id, payment_id, event_type, url, description, device_collected=None):
        date, time = date.split('/'), t.split(':')
        self._sales_time = datetime(int('20' + date[2]), int(date[0]), int(date[0]), int(time[0]), int(time[1]), int(time[2]))
        self._gross_sale = gross_sale
        self._tax = tax
        self._total_sale = self._gross_sale + self._tax
        self._payment_type = payment_type
        self._transaction_id = transaction_id
        self._payment_id = payment_id
        self._event_type = 1 if 'payment' in event_type else -1
        self._sales_url = url
        self._desc = description
        self._device_name = device_collected
