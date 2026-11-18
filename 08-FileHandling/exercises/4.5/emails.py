import re

def _read_email():
    with open('email.txt', 'r', encoding='utf-8') as file:
        return file.read()

def email_sender():
    content = _read_email()
    match = re.search(r'From:\s*(?:.*<)?([^\s<>]+@[^\s<>]+)>?', content) # (?:.*<)? — opcjonalne imię i nazwisko przed nawiasem < (np. Jan Kowalski <). Znak ? na końcu nawiasu oznacza „ten fragment może wystąpić, ale nie musi”.
    return match.group(1) if match else ""

def email_recipient():
    content = _read_email()
    match = re.search(r'To:\s*(?:.*<)?([^\s<>]+@[^\s<>]+)>?', content)
    return match.group(1) if match else ""

def email_subject():
    content = _read_email()
    match = re.search(r'Subject:\s*(.+)', content) # zjada spację (lub kilka spacji) po dwukropku (\s to biały znak, * to zero lub więcej powtórzeń).
    return match.group(1).strip() if match else ""

def email_body():
    content = _read_email()
    match = re.search(r'\r?\n\r?\n([\s\S]*)', content) # \r?\n — to zapis pojedynczego Entera (Windows zapisuje Enter jako \r\n, a Mac/Linux jako samo \n — znak ? sprawia, że kod działa na każdym systemie).
    return match.group(1).strip() if match else ""

#([\s\S]*) — zwykła kropka . zatrzymuje się na końcu jednej linijki, a treść maila ma zwykle wiele akapitów. Zapis [\s\S] oznacza dosłownie „wszystkie białe znaki (\s) ORAZ wszystkie widoczne znaki (\S)”, czyli łapie cały tekst aż do samego końca pliku, nie zatrzymując się na enterach.