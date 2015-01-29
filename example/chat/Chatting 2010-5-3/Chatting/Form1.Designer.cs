namespace Chatting
{
    partial class MainForm
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.txtSendMsg = new System.Windows.Forms.TextBox();
            this.lblFriendIP = new System.Windows.Forms.Label();
            this.txtIP = new System.Windows.Forms.TextBox();
            this.btnConnect = new System.Windows.Forms.Button();
            this.btnSendMsg = new System.Windows.Forms.Button();
            this.btnWaitAccess = new System.Windows.Forms.Button();
            this.txtGetMsg = new System.Windows.Forms.RichTextBox();
            this.lblState = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // label1
            // 
            resources.ApplyResources(this.label1, "label1");
            this.label1.BackColor = System.Drawing.Color.Transparent;
            this.label1.ForeColor = System.Drawing.SystemColors.Window;
            this.label1.Name = "label1";
            // 
            // label2
            // 
            resources.ApplyResources(this.label2, "label2");
            this.label2.BackColor = System.Drawing.Color.Transparent;
            this.label2.ForeColor = System.Drawing.SystemColors.Window;
            this.label2.Name = "label2";
            // 
            // txtSendMsg
            // 
            this.txtSendMsg.BorderStyle = System.Windows.Forms.BorderStyle.None;
            resources.ApplyResources(this.txtSendMsg, "txtSendMsg");
            this.txtSendMsg.Name = "txtSendMsg";
            // 
            // lblFriendIP
            // 
            resources.ApplyResources(this.lblFriendIP, "lblFriendIP");
            this.lblFriendIP.ForeColor = System.Drawing.SystemColors.Window;
            this.lblFriendIP.Name = "lblFriendIP";
            // 
            // txtIP
            // 
            resources.ApplyResources(this.txtIP, "txtIP");
            this.txtIP.Name = "txtIP";
            // 
            // btnConnect
            // 
            resources.ApplyResources(this.btnConnect, "btnConnect");
            this.btnConnect.Name = "btnConnect";
            this.btnConnect.UseVisualStyleBackColor = true;
            this.btnConnect.Click += new System.EventHandler(this.btnConnect_Click);
            // 
            // btnSendMsg
            // 
            resources.ApplyResources(this.btnSendMsg, "btnSendMsg");
            this.btnSendMsg.Name = "btnSendMsg";
            this.btnSendMsg.UseVisualStyleBackColor = true;
            this.btnSendMsg.Click += new System.EventHandler(this.btnSendMsg_Click);
            // 
            // btnWaitAccess
            // 
            resources.ApplyResources(this.btnWaitAccess, "btnWaitAccess");
            this.btnWaitAccess.Name = "btnWaitAccess";
            this.btnWaitAccess.UseVisualStyleBackColor = true;
            this.btnWaitAccess.Click += new System.EventHandler(this.btnWaitAccess_Click);
            // 
            // txtGetMsg
            // 
            this.txtGetMsg.BackColor = System.Drawing.SystemColors.Window;
            this.txtGetMsg.BorderStyle = System.Windows.Forms.BorderStyle.None;
            resources.ApplyResources(this.txtGetMsg, "txtGetMsg");
            this.txtGetMsg.Name = "txtGetMsg";
            this.txtGetMsg.ReadOnly = true;
            // 
            // lblState
            // 
            resources.ApplyResources(this.lblState, "lblState");
            this.lblState.ForeColor = System.Drawing.SystemColors.Window;
            this.lblState.Name = "lblState";
            // 
            // MainForm
            // 
            this.AcceptButton = this.btnSendMsg;
            resources.ApplyResources(this, "$this");
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.Navy;
            this.Controls.Add(this.lblState);
            this.Controls.Add(this.txtGetMsg);
            this.Controls.Add(this.btnWaitAccess);
            this.Controls.Add(this.btnSendMsg);
            this.Controls.Add(this.btnConnect);
            this.Controls.Add(this.txtIP);
            this.Controls.Add(this.lblFriendIP);
            this.Controls.Add(this.txtSendMsg);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.Name = "MainForm";
            this.Load += new System.EventHandler(this.MainForm_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox txtSendMsg;
        private System.Windows.Forms.Label lblFriendIP;
        private System.Windows.Forms.TextBox txtIP;
        private System.Windows.Forms.Button btnConnect;
        private System.Windows.Forms.Button btnSendMsg;
        private System.Windows.Forms.Button btnWaitAccess;
        private System.Windows.Forms.RichTextBox txtGetMsg;
        private System.Windows.Forms.Label lblState;
    }
}

