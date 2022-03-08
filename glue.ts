import { WebSocketClient, WebSocketServer } from "https://deno.land/x/websocket@v0.1.3/mod.ts";

const wss = new WebSocketServer(8091);
let socket:WebSocketClient;
wss.on("connection", function (ws: WebSocketClient) {
  console.log("websocket established");
  ws.send("websocket established");
  socket=ws;
});

const server = Deno.listen({ port: 8090 });
console.log(`HTTP webserver running.  Access it at:  http://localhost:8090/`);

for await (const conn of server) {
  serveHttp(conn);
}

async function serveHttp(conn: Deno.Conn) {
  const httpConn = Deno.serveHttp(conn);
  for await (const requestEvent of httpConn) {
    let action=requestEvent.request.url.match(/.+?action=(?<action>.+)/)?.groups?.action;
    if(action){
        socket?.send(action);
    }
    requestEvent.respondWith(
      new Response("success", {
        status: 200,
      })
    );
  }
}
