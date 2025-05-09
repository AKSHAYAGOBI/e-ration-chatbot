
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCheckStatus(Action):
    def name(self):
        return "action_check_status"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Your ration booking is being processed.")
        return []

class ActionBookRation(Action):
    def name(self):
        return "action_book_ration"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="I have booked your ration. You will receive an update soon!")
        return []

class ActionAskDocuments(Action):
    def name(self):
        return "action_ask_documents"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="You will need a valid Ration Card and an Aadhaar ID for verification.")
        return []
