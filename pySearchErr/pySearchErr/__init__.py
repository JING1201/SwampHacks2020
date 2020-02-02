import sys
import traceback
import webbrowser

def searchErr(file):
    try:
        exec(open(file).read())
    except Exception:
        full_error_msg = traceback.format_exc()
        print(full_error_msg)
        err = full_error_msg.split("\n")[-2]
        err.replace(' ', '+')
        webbrowser.open_new_tab("https://www.google.com/search?q="+err)