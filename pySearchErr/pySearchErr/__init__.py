import sys
import traceback
import webbrowser

def searchErr(file):
    try:
        code = compile(open(file).read(), file, 'exec')
        exec(code)
    except Exception:
        full_error_msg = traceback.format_exc()
        split_msg = full_error_msg.split("\n")
        del split_msg[1]
        del split_msg[1]
        print('\n'.join(split_msg))
        err = split_msg[-2]
        err.replace(' ', '+')
        webbrowser.open_new_tab("https://www.google.com/search?q="+err)