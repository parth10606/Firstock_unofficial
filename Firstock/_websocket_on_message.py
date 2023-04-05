def feed_handler(self,message):
    print(message)
    if self.feed_message_handler!=None:
        self.feed_message_handler(message)

def order_feed_handler(self,message):
    print(message)
    if self.order_feed_message_handler!=None:
        self.order_feed_message_handler(message)

def depth_feed_handler(self,message):
    print(message)
    if self.depth_feed_message_handler!=None:
        self.depth_feed_message_handler(message)