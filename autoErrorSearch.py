import sys
import traceback
import webbrowser

if len(sys.argv) < 2:
    print("Pls specify a script to run.")
    sys.exit()

try:
    exec(open(sys.argv[1]).read())
except Exception as e:
    full_error_msg = traceback.format_exc()
    print(full_error_msg)
    err = full_error_msg.split("\n")[-2]
    err.replace(' ', '+')
    webbrowser.open_new_tab("https://www.google.com/search?q="+err)