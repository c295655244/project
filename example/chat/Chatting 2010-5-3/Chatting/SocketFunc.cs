using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

namespace Chatting
{
    public abstract class SocketFunc
    {
        //不管是服务端还是客户端, 建立连接后用这个Socket进行通信
        public Socket communicateSocket = null;

        //服务端和客户端建立连接的方式稍有不同, 子类会重载
        public abstract void Access(string IP, System.Action AccessAciton);

        //发送消息的函数
        public void Send(string message)
        {
            if (communicateSocket.Connected == false)
            {
                throw new Exception("还没有建立连接, 不能发送消息");
            }
            Byte[] msg = Encoding.UTF8.GetBytes(message);
            communicateSocket.BeginSend(msg,0, msg.Length, SocketFlags.None,
                ar => {
                
                }, null);
        }

        //接受消息的函数
        public void Receive(System.Action<string> ReceiveAction)
        {
            //如果消息超过1024个字节, 收到的消息会分为(总字节长度/1024 +1)条显示
            Byte[] msg = new byte[1024];
            //异步的接受消息
            communicateSocket.BeginReceive(msg, 0, msg.Length, SocketFlags.None,
                ar => {
                    //对方断开连接时, 这里抛出Socket Exception
                    //An existing connection was forcibly closed by the remote host 
                        communicateSocket.EndReceive(ar); 
                    ReceiveAction(Encoding.UTF8.GetString(msg).Trim('\0',' '));
                    Receive(ReceiveAction);
                }, null);
        }
    }


    public class ServerSocket:SocketFunc
    {
        //服务端重载Access函数
        public override void Access(string IP, System.Action AccessAciton)
        {
            Socket serverSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            //本机预使用的IP和端口
            IPEndPoint serverIP = new IPEndPoint(IPAddress.Any, 9050);
            //绑定服务端设置的IP
            serverSocket.Bind(serverIP);
            //设置监听个数
            serverSocket.Listen(1);
            //异步接收连接请求
            serverSocket.BeginAccept(ar =>
                {
                    base.communicateSocket = serverSocket.EndAccept(ar);
                    AccessAciton();
                }, null);
        }
    }

    public class ClientSocket:SocketFunc
    {
        //客户端重载Access函数
        public override void Access(string IP, System.Action AccessAciton)
        {
            base.communicateSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            base.communicateSocket.Bind(new IPEndPoint(IPAddress.Any, 9051));
            
            //服务器的IP和端口
            IPEndPoint serverIP;
            try
            {
                serverIP = new IPEndPoint(IPAddress.Parse(IP), 9050);
            }
            catch
            {
                throw new Exception(String.Format("{0}不是一个有效的IP地址!", IP));
            }
            
            //客户端只用来向指定的服务器发送信息,不需要绑定本机的IP和端口,不需要监听
            try
            {
                base.communicateSocket.BeginConnect(serverIP, ar =>
                {
                    AccessAciton();
                }, null);
            }
            catch
            {
                throw new Exception(string.Format("尝试连接{0}不成功!", IP));
            }
        }
    }
}
