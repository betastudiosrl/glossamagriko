from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type , is_intent_name

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self,handler_input):
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self,handler_input):
        handler_input.response_builder.speak("Benvenuto nel dizionario italiano-griko. Chiedimi di tradurre qualsiasi parola e io lo farò per te.").set_should_end_session(False)
        return handler_input.response_builder.response

class CatchAllExcetionHandler(AbstractExceptionHandler):
    def can_handle(self , handler_input, exception):
        return True

    def handle(self , handler_input, exception):
        print(exception)
        handler_input.response_builder.speak("Nessuna corrispondenza trovata. Per favore, riprova.")
        return handler_input.response_builder.response

class GlossamaIntentHandler(AbstractRequestHandler):
    def can_handle(self,handler_input):
        return is_intent_name("ParolaItalianaIntent")(handler_input)

    def handle(self,handler_input):
        word = handler_input.request_envelope.request.intent.slots['SearchQuery'].value
        speech_text = "La tua parola è gatto."
        handler_input.response_builder.speak(speech_text).set_should_end_session(False)
        return handler_input.response_builder.response


sb = SkillBuilder()
sb.add_request_handler(LaunchRequestHandler())
sb.add_exception_handler(CatchAllExcetionHandler())
sb.add_request_handler(GlossamaIntentHandler())

def handler(event,context):
    return sb.lambda_handler()(event,context)