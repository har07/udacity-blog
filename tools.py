import cgi

def custom_escape_html(s):
    if s:
        #replace & first:
        s = s.replace("&", "&amp;")
        special_chars = {">": "&gt;",
                     "<": "&lt;",
                     '"': "&quot;"}
        for c in special_chars:
            s = s.replace(c, special_chars[c])

    return s

def escape_html(s):
    return cgi.escape(s, quote=True)
