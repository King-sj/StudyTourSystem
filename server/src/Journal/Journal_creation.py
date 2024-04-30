from ..DataType import Journal,Comment

class JournalManagementSystem:
    def __init__(self):
        self.journals = []

    def add_journal(self, journal: Journal):
        self.journals.append(journal)
    
    def add_comment_to_journal(self, journal_name: str, comment: Comment):
        for journal in self.journals:
            if journal.journalName == journal_name:
                journal.journalComment.add(comment)
                break
    
    def get_journals(self):
        return [(journal.journalName, journal.journalDate) for journal in self.journals]
    
    def get_comments_for_journal(self, journal_name: str):
        for journal in self.journals:
            if journal.journalName == journal_name:
                return [(comment.commentOwner, comment.commentText) for comment in journal.journalComment]
        return []