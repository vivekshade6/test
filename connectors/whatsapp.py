import logging
import jsonpickle
import pickle
import json
from sanic import Blueprint, response
from sanic.request import Request
from typing import Text, Optional, Callable, Awaitable, List, Dict, Any
from rasa.core.agent import Agent
from sanic.response import HTTPResponse
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.core.channels.channel import UserMessage, OutputChannel
from rasa.core.channels.channel import InputChannel
from rasa.core.channels.channel import CollectingOutputChannel
from rasa.utils.endpoints import EndpointConfig
from rasa.core.run import configure_app

logger = logging.getLogger(__name__)

whatsapp_number='737377463663'
auth_token='gxhsghhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhcjhsvhabjbchbjbc'
class Whatsapp(InputChannel):
    """A custom http input channel.
    This implementation is the basis for a custom implementation of a chat
    frontend. You can customize this to send messages to Rasa Core and
    retrieve responses from the agent."""

    #@classmethod
    #def name(cls):
    #    return "Whatsapp"

    def blueprint(self, on_new_message: Callable[[UserMessage], Awaitable[None]]):

        custom_webhook = Blueprint('custom_webhook', __name__)

        @custom_webhook.route("/", methods=["GET"])
        async def health(request: Request) -> HTTPResponse:
            return response.json({"status": "ok"})

        @custom_webhook.route("/webhook", methods=["POST"])
        async def receive(request: Request) -> HTTPResponse:
            #file= open('text.txt','w')
            a=request.json.get("contacts")[0]
            b=request.json.get("messages")[0].get("text").get("body")
            sender_id=a.get("wa_id")
            #sender_id = request.json.get("contacts") # method to get sender_id 
            text = b
            input_channel = "Whatsapp" # method to fetch input channel
            metadata = "" # method to get metadata
            #text=pickle.loads(data)
            #text=data["messages"]["text"]["body"]
            collector = CollectingOutputChannel()
            Out_channel=self.get_output_channel()

            # include exception handling

            await on_new_message(
                UserMessage(
                    text,
                    Out_channel,
                    sender_id,
                    input_channel=input_channel,
                    metadata=metadata,
                )
            )

            return response.json(collector.messages)

        return custom_webhook

    def get_output_channel(self) -> OutputChannel:
        return WhatsappOutput()


class WhatsappOutput(OutputChannel):

    async def _send_message(self, message_data: Dict[Text, Any]) -> "MessageInstance":
        message = "hello"
        #while not message and self.send_retry < self.max_retry:
            #message = self.messages.create(**message_data)
            #self.send_retry += 1
        #if not message and self.send_retry == self.max_retry:
            #logger.error("Failed to send message. Max number of retires exceeded.")

        return message

    async def send_text_message(
        self, recipient_id: Text, text: Text, **kwargs: Any
    ) -> None:
        """Sends text message"""

        message_data = {"to": recipient_id, "from_": "5266262688"}
        for message_part in text.strip().split("\n\n"):
            message_data.update({"body": message_part})
            await self._send_message(message_data)



