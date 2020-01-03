#!/usr/bin/env python3

class SMS_store():
    def __init__(self):
        self.inbox = []
        self.from_number = None
        self.time_arrived = None
        self.text_of_SMS = None
        self.has_been_viewed = False
        self.message = None

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS, has_been_viewed=False):
        self.from_number = from_number
        self.time_arrived = time_arrived
        self.text_of_SMS = text_of_SMS
        self.has_been_viewed = has_been_viewed
        self.message = (self.has_been_viewed, self.from_number, self.time_arrived, self.text_of_SMS)
        self.inbox.append(self.message)
        return 0

    def message_count(self):
        return len(self.inbox)

    def get_unread_indexes(self):
        return [msg[0] for msg in enumerate(self.inbox) if msg[1][0] == False]

    def get_message(self, i):
        read = list(self.inbox[i])
        read[0] = True
        self.inbox[i] = tuple(read)
        return self.inbox[i][1:]

    def delete(self, i):
        self.inbox.pop(i)
        return 0

    def clear(self):
        self.inbox = []
        return 0


my_inbox = SMS_store()
my_inbox.add_new_arrival(92328322, '1 jan 2019', "0 Hello world")
print(my_inbox.message_count())
my_inbox.add_new_arrival(92328322, '1 jan 2019', "1 Hello world")
print(my_inbox.message_count())
my_inbox.add_new_arrival(92328322, '1 jan 2019', "2 Hello world")
print(my_inbox.message_count())
print(my_inbox.get_unread_indexes())
print(my_inbox.get_message(0))
print(my_inbox.get_unread_indexes())
my_inbox.delete(0)
print(my_inbox.get_unread_indexes())
my_inbox.clear()
print(my_inbox.get_unread_indexes())
print(my_inbox.message_count())