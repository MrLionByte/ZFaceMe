from channels.generic.websocket import AsyncWebsocketConsumer
import json
import asyncio


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "TestRoom"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        print(self.channel_layer, self.room_group_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        print("DISCONNECTED")

    async def receive(self, text_data=None, bytes_data=None):
        receive_dict = json.loads(text_data)
        print("Received Dict :", receive_dict)
        message = receive_dict.get("message", {})
        action = receive_dict.get("action", "")
        print("Message received: ", message)
        print("action: ", action)
        print("self.channel_name: ", self.channel_name)

        if (action == "new-offer") or (action == "new-answer"):
            receiver_channel_name = message.get("receiver_channel_name", "")
            message["receiver_channel_name"] = self.channel_name
            # receiver_channel_name = receive_dict['message']['receiver_channel_name']
            # receive_dict['message']['receiver_channel_name'] = self.channel_name

            await self.channel_layer.send(
                receiver_channel_name,
                {"type": "send.sdp", "receive_dict": receive_dict},
            )
            return
        if action == "user-leave":
            await self.channel_layer.group_send(
                self.room_group_name,
                {"type": "user_leave", "peer": receive_dict["peer"]},
            )
            return

        if not isinstance(message, dict):
            message = {}

        message["receiver_channel_name"] = self.channel_name
        receive_dict["message"] = message

        await self.channel_layer.group_send(
            self.room_group_name, {"type": "send.sdp", "receive_dict": receive_dict}
        )

    async def send_sdp(self, event):
        receive_dict = event["receive_dict"]
        print("SEND SDP DICT:", receive_dict)
        action = receive_dict.get("action")
        message = receive_dict["message"]
        print("SEND SDP :", action)
        await self.send(text_data=json.dumps(receive_dict))

    async def user_leave(self, event):
        peer = event["peer"]
        await self.send(
            text_data=json.dumps(
                {
                    "peer": peer,
                    "action": "user-leave",
                    "message": f"{peer} has left the chat",
                }
            )
        )
