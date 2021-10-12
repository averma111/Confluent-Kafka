from producer import confluentproducer
from consumer import confluentconsumer


def main():
    create_producer = confluentproducer.ConfluentProducer()
    message = "Hello this message will be sent to the kafka topic."
    create_producer.send_msg_async(message)

    create_consumer = confluentconsumer.ConfluenteConsumer()
    create_consumer.start_listener()




if __name__ == '__main__':
    main()