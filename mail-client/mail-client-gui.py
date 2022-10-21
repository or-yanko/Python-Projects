import imaplib
import email
import tkinter as tk
from functools import partial
import re

user = 'el_professor@walla.com'
passwd = '*****'
server = 'outlook.office365.com'


def cleaner(tags):
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(cleanr, '', tags)
    return cleantext


class Mail:
    def __init__(self, parent):
        self.parent = parent
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)

        self.width = self.parent.winfo_screenwidth()
        self.height = self.parent.winfo_screenheight()

        self.mainframe = tk.Frame(self.parent)
        self.mainframe['width'] = int(self.width/2)
        self.mainframe['height'] = int(self.height/2)
        self.mainframe.grid(column=0, row=0, sticky='new')
        self.mainframe.grid_columnconfigure(0, weight=3)
        self.mainframe.grid_rowconfigure(0, weight=3)

        self.headerframe = tk.Frame(self.mainframe)
        self.headerframe['width'] = int((self.width/2)-1)
        self.headerframe['relief'] = 'ridge'
        self.headerframe['borderwidth'] = 2
        self.headerframe.grid(column=0, row=0, sticky='new')
        self.headerframe.grid_columnconfigure(0, weight=3)

        self.mini_headerframe = tk.Frame(self.mainframe)
        self.mini_headerframe.grid(column=0, row=1, sticky='new', pady=3)
        self.mini_headerframe.grid_columnconfigure(0, weight=1)
        self.mini_headerframe.grid_columnconfigure(1, weight=10)

        self.subjectframe = tk.Frame(self.mini_headerframe)
        self.subjectframe['relief'] = 'solid'
        self.subjectframe['borderwidth'] = 1
        self.subjectframe['border'] = 0
        self.subjectframe['highlightthickness'] = 1
        self.subjectframe['highlightbackground'] = 'grey65'
        self.subjectframe.grid(column=0, row=1, sticky='news', pady=2, ipady=2)

        self.message_frame = tk.Frame(self.mini_headerframe)
        self.message_frame['relief'] = 'solid'
        self.message_frame['borderwidth'] = 1
        self.message_frame['border'] = 0
        self.message_frame['bg'] = 'white'
        self.message_frame['highlightthickness'] = 1
        self.message_frame['highlightbackground'] = 'grey65'
        self.message_frame.grid(
            column=1, row=1, sticky='news', pady=2, ipady=2)

        self.inbox_label = tk.Label(self.mini_headerframe)
        self.inbox_label['text'] = 'Inbox'
        self.inbox_label['font'] = 'sans 10 bold'
        self.inbox_label['relief'] = 'solid'
        self.inbox_label['borderwidth'] = 1
        self.inbox_label['border'] = 0
        self.inbox_label['highlightthickness'] = 1
        self.inbox_label['highlightbackground'] = 'grey65'
        self.inbox_label['width'] = 50
        self.inbox_label.grid(column=0, row=0, sticky='new')

        # Setup the messages label
        self.msg_label = tk.Label(self.mini_headerframe)
        self.msg_label['text'] = 'Messages'
        self.msg_label['font'] = 'sans 10 bold'
        self.msg_label['relief'] = 'solid'
        self.msg_label['borderwidth'] = 1
        self.msg_label['border'] = 0
        self.msg_label['highlightthickness'] = 1
        self.msg_label['highlightbackground'] = 'grey65'
        self.msg_label['width'] = 80
        self.msg_label.grid(column=1, row=0, sticky='new')

        # Setup the header label
        self.header_label = tk.Label(self.headerframe, padx=5, pady=2)
        self.header_label['text'] = 'Tkinter Email Client'
        self.header_label['font'] = 'sans 16 bold'
        self.header_label['fg'] = 'indigo'
        self.header_label.grid(column=0, row=0, sticky='new')
        self.header_label.grid_columnconfigure(0, weight=3)

        self.scrollbar = tk.Scrollbar(self.message_frame)
        self.message = tk.Text(self.message_frame, wrap='word', padx=5, pady=3)
        self.message['width'] = 87
        self.message['height'] = 26
        self.message['state'] = 'disabled'
        self.scrollbar.config(command=self.message.yview)
        self.message.config(yscrollcommand=self.scrollbar.set)
        self.message.insert(tk.END, ' ')
        self.scrollbar.grid(column=0, row=0, sticky='ns')
        self.message.grid(column=1, row=0, sticky='news')

        self.subjects()

    def subjects(self):
        canvas = tk.Canvas(self.subjectframe)
        canvas['height'] = 450
        canvas['bg'] = 'white'
        canvas['width'] = int(self.width/4)
        scrollbar = tk.Scrollbar(
            self.subjectframe, orient='vertical', command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
        scrollable_frame.bind('<Configure>', lambda e: canvas.configure(
            scrollregion=canvas.bbox('all')))
        canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(column=0, row=0, sticky='ns')
        canvas.grid(column=1, row=0, sticky='news')

        mail = Connect()
        mail = mail.connect(user, passwd, server)

        mailbox = GetInbox()
        uids = mailbox.get_uids(mail)

        headers = GrabHeader()
        header = headers.get_headers(mail, uids)
        i = 0
        for heads in header:
            for head, id in heads.items():
                button = tk.Button(
                    scrollable_frame, cursor='hand2', anchor='w', wraplength=430, justify='left')
                button['text'] = head
                button['relief'] = 'flat'
                button['bg'] = 'white'
                button['fg'] = 'blue'
                button['activeforeground'] = 'red'
                button['command'] = partial(self.messagebox, id=id)
                button['width'] = int(self.width/4)
                button.grid(column=0, row=i, sticky='ew')
                button.bind('<Button-3>', partial(self.delete_message, id))
                i += 1
        mail.close()
        mail.logout()
        self.subjectframe.after(60000, self.subjects)

    def messagebox(self, id):
        mail = Connect()
        mail = mail.connect(user, passwd, server)

        mailbox = GetInbox()
        uids = mailbox.get_uids(mail)
        body = GetBody()
        msg = body.get_body(mail, str(id))

        msg = cleaner(msg)

        self.scrollbar = tk.Scrollbar(self.message_frame)
        self.message = tk.Text(self.message_frame, wrap='word', padx=5, pady=3)
        self.message['width'] = 87
        self.message['height'] = 26
        self.scrollbar.config(command=self.message.yview)
        self.message.config(yscrollcommand=self.scrollbar.set)
        self.message['state'] = 'normal'
        self.message.insert(tk.END, msg)
        self.message['state'] = 'disabled'
        self.scrollbar.grid(column=0, row=0, sticky='ns')
        self.message.grid(column=1, row=0, sticky='news')

        mail.close()
        mail.logout()

    def delete_message(self, id, event):
        mail = Connect()
        mail = mail.connect(user, passwd, server)
        mail.select('inbox')
        mail.uid('STORE', str(id), '+FLAGS', '\\Deleted')
        mail.expunge()
        mail.close()
        mail.logout()
        self.subjectframe.after(0, self.subjects)
        self.message['state'] = 'normal'
        self.message.delete(1.0, tk.END)
        self.message['state'] = 'disabled'


class Connect:
    def connect(self, user, passwd, server):
        mail = imaplib.IMAP4_SSL(server)
        mail.login(user, passwd)
        return mail


class GetInbox:
    def get_uids(self, mail):
        mail.select('inbox')
        result, data = mail.uid('search', None, 'ALL')
        return data


class GrabHeader:
    def get_headers(self, mail, uids):
        subjects = []
        for numbers in range(len(uids[0].split())):
            uid = uids[0].split()[numbers]
            result, data = mail.uid('fetch', uid, '(RFC822)')
            raw_data = data[0][1]
            raw_data_string = raw_data.decode('utf-8')
            message = email.message_from_string(raw_data_string)
            subject = str(email.header.make_header(
                email.header.decode_header(message['subject'])))
            subjects.append({subject: int(uid)})
        return subjects


class GetBody:
    def get_body(self, mail, uid):
        result, data = mail.uid('fetch', uid, '(RFC822)')
        raw_data = data[0][1]
        raw_data_string = raw_data.decode('utf-8')
        message = email.message_from_string(raw_data_string)
        for part in message.walk():
            if part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
                return body.decode()
            else:
                continue


def main():
    root = tk.Tk()
    root.title('Tkinter Email Client')
    root['pady'] = 5
    root['padx'] = 10
    root['borderwidth'] = 2
    root.resizable(False, False)
    Mail(root)
    root.mainloop()


if __name__ == '__main__':
    main()
