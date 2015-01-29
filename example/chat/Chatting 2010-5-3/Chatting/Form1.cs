using System;
using System.Drawing;
using System.Windows.Forms;
using System.Net.Sockets;

namespace Chatting
{
    public partial class MainForm : Form
    {

        public MainForm()
        {
            InitializeComponent();
        }

        SocketFunc socket;
        System.Action<string> ReceiveAction;
        System.Action AccessAction;

        private void MainForm_Load(object sender, EventArgs e)
        {
            //异步建立连接回调
            AccessAction = () =>
            {
                this.Invoke((MethodInvoker)delegate()
                {
                    lblFriendIP.Visible = false;
                    txtIP.Visible = false;
                    btnConnect.Visible = false;
                    btnWaitAccess.Visible = false;

                    String friendIP = socket.communicateSocket.RemoteEndPoint.ToString();
                    lblState.Text = String.Format("连接成功. 对方IP:{0}", friendIP);

                    try
                    {
                        socket.Receive(ReceiveAction);
                    }
                    catch (Exception exp)
                    {
                        MessageBox.Show(exp.Message, "错误");
                    }
                });

            };
            //异步接收消息回调
            ReceiveAction = msg =>
            {
                txtGetMsg.Invoke((MethodInvoker)delegate()
                {
                    UpdateGetMsgTextBox(false, msg, Color.Red);
                });
            };
        }

        private void btnWaitAccess_Click(object sender, EventArgs e)
        {
            this.socket = new ServerSocket();
            try
            {
                this.socket.Access("", this.AccessAction);
            }
            catch (Exception ecp)
            {
                MessageBox.Show(ecp.Message, "错误");
            }

            lblState.Text = "等待对方连接...";
        }

        private void btnConnect_Click(object sender, EventArgs e)
        {
            this.socket = new ClientSocket();
            try
            {
                this.socket.Access(txtIP.Text, this.AccessAction);
            }
            catch (Exception ecp)
            {
                MessageBox.Show(ecp.Message, "错误");
            }
            lblState.Text = "正在连接对方...";
        }

        private void btnSendMsg_Click(object sender, EventArgs e)
        {
            string message = txtSendMsg.Text.Trim();
            if (string.IsNullOrEmpty(message))
            {
                MessageBox.Show("消息内容不能为空!", "错误");
                txtSendMsg.Focus();
                return;
            }

            try
            {
                socket.Send(message);
            }
            catch(Exception ecp)
            {
                MessageBox.Show(ecp.Message, "错误");
                return;
            }

            UpdateGetMsgTextBox(true, message, Color.Blue);
            txtSendMsg.Text = "";
        }

        private void UpdateGetMsgTextBox(bool sendMsg, string message, Color color)
        {
            string appendText;
            if (sendMsg == true)
            {
                appendText = "Me:           " + System.DateTime.Now.ToString()
                    + Environment.NewLine
                    + message + Environment.NewLine;
            }
            else
            {
                appendText = "Friend:           " + System.DateTime.Now.ToString()
                    + Environment.NewLine
                    + message + Environment.NewLine;
            }
            int txtGetMsgLength = txtGetMsg.Text.Length;
            txtGetMsg.AppendText(appendText);
            txtGetMsg.Select(txtGetMsgLength, appendText.Length - Environment.NewLine.Length*2 -message.Length);
            txtGetMsg.SelectionColor = color;

            txtGetMsg.ScrollToCaret();
        }
    }
}