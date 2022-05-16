class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"


received_info = input().split(" ")
emails = []

while received_info[0] != "Stop":
    email = Email(received_info[0], received_info[1], received_info[2])
    emails.append(email)
    received_info = input().split(" ")

indices = [int(x) for x in input().split(", ")]

for i in indices:
    emails[i].send()

for email in emails:
    print(email.get_info())
