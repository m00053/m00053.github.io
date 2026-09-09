import os
import datetime

# Ordner erstellen, falls er nicht existiert
os.makedirs("public", exist_ok=True)

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Python generierte GitHub Page</title>
    <meta charset="utf-8">
</head>
<body>
    <h1>Hallo von Python!</h1>
    <p>Diese Seite wurde vollautomatisch durch ein Python-Skript generiert.</p>
    <p>Letztes Build-Datum: <strong>{now}</strong></p>
</body>
</html>
"""

# Als index.html im Ordner 'public' speichern
with open("public/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)