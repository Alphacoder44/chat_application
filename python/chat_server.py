import asyncio
import websockets
from flask import Flask, render_template

app = Flask(__name__)

# Store connected clients in a set
connected_clients = set()

async def handle_client(websocket, path):
    try:
        # Add the new client to the set
        connected_clients.add(websocket)

        async for message in websocket:
            # Broadcast the received message to all connected clients
            for client in connected_clients:
                await client.send(message)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Remove the client from the set when they disconnect
        connected_clients.remove(websocket)

@app.route("/")
def chat():
    return render_template("chat.html")

async def main():
    server = await websockets.serve(handle_client, "localhost", 8765)
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
