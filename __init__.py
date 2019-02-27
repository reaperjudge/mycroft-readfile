# Importing IntentBuilder
from adapt.intent import IntentBuilder
# Importing MycroftSkill class
from mycroft.skills.core import MycroftSkill

__author__ = 'reaperjudge'

# Creating Readfile extending MycroftSkill
class Readfile(MycroftSkill):
    def __init__(self):
        super(Readfile, self).__init__(name="Readfile")

    def initialize(self):
        # Creating activationIntent requiring activation vocab
        activation = IntentBuilder("activationIntent"). \
            require("activation.voc").build()
        # Associating a callback with the Intent
        self.register_intent(activation,
                             self.handle_activation)

    def handle_activation(self, message):
        # Sending a command to mycroft, speak activation Dialog
        self.speak_dialog("respond")


    def stop(self):
        pass

def create_skill():
    return Readfile()
