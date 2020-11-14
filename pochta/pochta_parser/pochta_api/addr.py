class Addr:
    val=""
    content=""
    stname=""

    def __dict__(self):
        return {
            'val': self.val,
            'content': self.content,
            'stname': self.content,
        }
