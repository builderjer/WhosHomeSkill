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
        p = self.settings.get("person")
        LOGGER.info(p)
        if ping("192.168.0.20"):
            self.speak_dialog("home")
        else:
            self.speak_dialog("Nobody")
        #self.speak_dialog("I am home")
        
def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import subprocess, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + host
    need_sh = False if  platform.system().lower()=="windows" else True

    # Ping
    return subprocess.call(args, shell=need_sh) == 0

def create_skill():
    return WhosHome()
        
