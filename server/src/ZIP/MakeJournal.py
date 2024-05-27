from DataType import Journal, Comment
import time

class JournalManagementSystem:
    def __init__(self):
        self.journals = []

    def add_journal(self, journal: Journal):
        self.journals.append(journal)
    
    def add_comment_to_journal(self, journal_name: str, comment: Comment):
        for journal in self.journals:
            if journal.journalName == journal_name:
                # 确保 journalComment 被正确初始化为列表
                if journal.journalComment is None:
                    journal.journalComment = []
                journal.journalComment.append(comment)  # 使用 append 方法添加评论
                break
    
    def get_journals(self):
        return [(journal.journalName, journal.journalDate) for journal in self.journals]
    
    def get_comments_for_journal(self, journal_name: str):
        for journal in self.journals:
            if journal.journalName == journal_name:
                # 返回 journalComment 列表中评论的所有者和文本
                return [(comment.commentOwner, comment.commentText) for comment in journal.journalComment]
            # 返回日志名字与日期，可以在其中添加其他信息
        return []

if __name__ == "__main__":
    journal_system = JournalManagementSystem()

    # 创建一些Journal和Comment实例
    journal1 = Journal("Journal 1", 8.5, "Content of Journal 1", None, time.localtime(time.time()))
    journal2 = Journal("Journal 2", 7.2, "Content of Journal 2", None, time.localtime(time.time()))

    comment1 = Comment("User 1", "This is a comment.", None, time.localtime(time.time()))
    comment2 = Comment("User 2", "Another comment.", None, time.localtime(time.time()))

    # 将Journal添加到系统中
    journal_system.add_journal(journal1)
    journal_system.add_journal(journal2)

    # 添加评论到Journal中
    journal_system.add_comment_to_journal("Journal 1", comment1)
    journal_system.add_comment_to_journal("Journal 2", comment2)

    # 获取所有日志
    journals = journal_system.get_journals()
    print("All Journals:")
    for journal in journals:
        print(journal)

    # 获取特定日志的评论
    comments = journal_system.get_comments_for_journal("Journal 1")
    print("\nComments for Journal 1:")
    for comment in comments:
        print(comment)