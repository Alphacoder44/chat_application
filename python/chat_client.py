import asyncio
import websockets

async def receive_messages():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            print(f"Received: {message}")

async def send_messages():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            message = input("Enter your message: ")
            await websocket.send(message)

async def main():
    await asyncio.gather(receive_messages(), send_messages())

if __name__ == "__main__":
    asyncio.run(main())
