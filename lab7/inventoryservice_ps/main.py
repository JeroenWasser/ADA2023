import logging
import os

from message_puller import MessagePuller
from pub_sub_util import create_subscription, create_topic
from resources.product import Product, Products

logging.basicConfig(level=logging.INFO)
product = Product()
products = Products()
project_id = os.environ['project_id']
MessagePuller(project=project_id, subscription="order_req_sub", product=product)