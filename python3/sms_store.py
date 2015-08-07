from datetime import datetime

class SMS_store(object):
    """docstring for SMS_store"""
    def __init__(self, store = [], has_been_viewed = False):#, from_number = '', time_arrived = '', text_of_SMS = ""):
        self.store = store
        self.has_been_viewed = has_been_viewed
        #self.from_number = from_number
        #self.time_arrived = time_arrived
        #self.text_of_SMS = text_of_SMS

    #def __repr__(self):
    #    print(my_inbox.store)

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.store.append((self.has_been_viewed, from_number, time_arrived, text_of_SMS))

    def message_count(self):
        return "There are {0} unread messages.".format(len(self.store))

    def get_unread_indexes(self):
        for i in self.store:
            if i[0] == False:
                print("{0}".format(i[1:]))

    def get_all_indexes(self):
        for i in self.store:
            print("{0}".format(i))

    def get_message(self, i):
        if i < len(self.store):
            self.store[i] = (True, self.store[i][1], self.store[i][2], self.store[i][3])
            return self.store[i][1:]
        else:
            return None

    def delete(self, i):
        try:
            del(self.store[i])
            return "Message number {0} has been deleted.".format(i)
        except Exception as e:
            raise e
        '''
        if i < len(self.store):
            del(self.store[i])
            print("Message number {0} has been deleted.".format(i))
        '''

    def clear(self):
        self.store = []
        return "All messages have been cleared."


my_inbox = SMS_store()
my_inbox.add_new_arrival(92328324, datetime.now(), "hello, world!")
my_inbox.add_new_arrival(92328324, datetime.now(), "localized=!")
my_inbox.add_new_arrival(92328324, datetime.now(), "label=''!")
my_inbox.add_new_arrival(92328324, datetime.now(), "widget=!")
my_inbox.add_new_arrival(92328324, datetime.now(), "q!")
print(my_inbox.message_count())
my_inbox.get_unread_indexes()
print(my_inbox.get_message(1))
print(my_inbox.delete(0))
print(my_inbox.message_count())
my_inbox.get_unread_indexes()
my_inbox.get_all_indexes()