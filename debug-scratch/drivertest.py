from notifications.notifications import NotificationHandler
import win32clipboard

def instockCall(stocklist:list):
    stocklist.append("- - - - - - - - - - - - - - - - - - - - - - \n\n")
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText("\n\n".join(stocklist))
    win32clipboard.CloseClipboard()
    notification_handler = NotificationHandler()
    notification_handler.urgent_call("\n\n".join(stocklist))

stocklist = ["https://www.amazon.com/GIGABYTE-GeForce-Graphics-WINDFORCE-GV-N3080GAMING/dp/B08HJTH61J?ref_=ast_sto_dp","https://why"]

instockCall(stocklist)
