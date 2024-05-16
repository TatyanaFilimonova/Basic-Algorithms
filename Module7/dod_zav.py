class Comment:

    def __init__(self, comment_text, author):
        self.comment_text = comment_text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self):
        self.comment_text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, step=0):
        if self.is_deleted:
            print("\t" * step + f"{self.comment_text}")
        else:
            print("\t" * step + f"{self.author}: {self.comment_text}")
        for reply in self.replies:
            reply.display(step + 1)


root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()
