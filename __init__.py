from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft import intent_handler

__author__ = 'builderjer'

LOGGER = getLogger(__name__)

class WhosHome(MycroftSkill):
    def __init__(self):
        super(WhosHome, self).__init__(name="WhosHome")
        self.people = []
        
    @intent_handler(IntentBuilder("WhosHomeIntent").require("WhosKeyword").require("HomeKeyword"))
    def handle_whos_home_intent(self, message):
        self.speak_dialog("I am home")
        
        
def create_skill():
    return WhosHome()
        
