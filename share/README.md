# PAG

Die PAG (Programmierer-Arbeitsgruppe) hat zum Ziel eine Arbeitsgemeinschaft zu bilden, die gemeinsame Projekte umsetzt und dabei sich gegenseitig weiterbildet. Die Treffs sind aktuell auf einen zwei-wöchigen Rhythmus in die ungeraden Wochen am Dienstag um 17:00 Uhr gelegt. Die Treffs sind mit zwei Stunden Dauer angesetzt.

Wir programmieren zunächst zwar in Python, legen uns darauf aber nicht fest.

## Get started

Die Projekte der PAG sind in Repositories verteilt und sind über das Internet erreichbar. Dazu ist ein Account am gitlab der PAG erforderlich. Das share-Verzeichnis, in dem gemeinschaftliche Dokumente, Information, etc. liegen, ist über http://3176gw1.dyndnshussein.de/PAG/share.git erreichbar.

### Umgebung einrichten

* git herunterladen mit Standard-Einstellungen installieren
* python, aktuelle 3er-Version installieren
  * Setzt das Häkchen: add  Phyton to Path
  * Geht auf Customize installation, next, setzt den Haken 'install for all users'
  * install
* Visual Studio Code herunterladen und installieren
* erstellt eine Verknüpfung zu VSCode und setzt das Häkchen 'Als Administrator starten'
* In Visual Studio Code
  * die Extensions Python und GitLens installieren
  * Terminal / New Terminal im Menü wählen
  * in Terminal eintippen:
    * python -m pip install --upgrade pip
    * pip install pylint
    * pip install PySide2

### Projekt startup clonen

* Ein Verzeichnis für PAG-Projekte erstellen
* In das eigene PAG-Verzeichnis das Repo clonen mit 'git clone http://3176gw1.dyndnshussein.de/PAG/startup.git'
* Im Startup-Projekt gibt es diverse Beispiele, um sich mit Python vertraut zu machen.
* In manchen Projekten werden zusätzliche Abhängigkeiten benötigt. Man beachte dazu die Readme des jeweiligen Projektes.

### Unittests mit pytest

In der testgetriebenen Entwicklung wird erst eine Testfunktion geschrieben und dann die Implementierung der Funktionalität. Dazu benutzen wir in python 'pytest'.
* im Terminal/in Console eintippen: pip install pytest
* zum Ausführen des Unittest eintippen: pytest

Pytest geht alle Dateien durch, sammelt geschriebene tests ein und führt sie aus. Die Ausgabe sind entweder grüne Punkte für Erfolg oder FAILURES mit roter Schrift für Misserfolgte Tests.
Nachträglich kommt eine statistische Ausgabe mit der Anzahl der erfolgreichen und fehlgeschlagenen Tests.
