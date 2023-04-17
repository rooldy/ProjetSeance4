from models import Base
from server import channel

# Définir les informations des files d'attente
queues = [
    ('queue-data-lake', 'logs'),
    ('queue-data-clean', 'logs')
]

# Créer l'échange
channel.exchange_declare('topic-exchange-logs', durable=True, exchange_type='topic')

# Créer les files d'attente et les lier à l'échange
for queue_name, routing_key in queues:
    channel.queue_declare(queue=queue_name)
    channel.queue_bind(exchange='topic-exchange-logs', queue=queue_name, routing_key=routing_key)

# Publier les logs
with open('assets/web-server-nginx.log') as logs_file:
    for line in logs_file:
        channel.basic_publish(exchange='topic-exchange-logs', routing_key='logs', body=line)
