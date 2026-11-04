from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class LoginHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        page = """
        <form method="POST" action="/login">
            <label>用户名：<input name="username"></label><br>
            <label>密码：<input name="password" type="password"></label><br>
            <button type="submit">登录</button>
        </form>
        """
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(page.encode("utf-8"))

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8")
        data = parse_qs(body)

        username = data.get("username", [""])[0]
        password = data.get("password", [""])[0]

        if username == "alice" and password == "123456":
            message = "登录成功"
        else:
            message = "用户名或密码错误"

        result = f"<p>{message}</p><a href='/'>返回</a>"
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(result.encode("utf-8"))

server = HTTPServer(("localhost", 8000), LoginHandler)
print("服务已启动，请打开 http://localhost:8000")
server.serve_forever()