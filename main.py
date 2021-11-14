import asyncio
import json

import fu


class EchoServerProtocol:
    command = {'00': fu.write_user_to_the_db, '01': fu.read_user_from_db}

    def connection_made(self, transport):
        # print('_')
        self.transport = transport

    def datagram_received(self, data, addr):
        message = data.decode()
        print(message)
        message = json.loads(message)
        body = message['body']
        com = message['command']

        ans = {'code': 0}
        if com in list(EchoServerProtocol.command.keys()):
            try:
                res = EchoServerProtocol.command[com](body)
                ans['body'] = res
            finally:
                pass
        else:
            ans['code'] = 1

        self.transport.sendto(json.dumps(ans).encode(), addr)


async def main():
    print("Starting UDP server")

    loop = asyncio.get_running_loop()

    transport, protocol = await loop.create_datagram_endpoint(
        lambda: EchoServerProtocol(),
        local_addr=('127.0.0.1', 9999))

    try:
        await asyncio.sleep(float('inf'))
    finally:
        transport.close()


asyncio.run(main())
