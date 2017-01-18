#!/usr/bin/python

import configparser
from classes.git import git_servant

def main():
    config = configparser.RawConfigParser(allow_no_value=True)
    config_file_name = 'config.cfg'
    read_files = config.read(config_file_name)

    if not read_files:
        print("No Config File found!")
        exit(1)

    # Initialisiere das Repository und lese schonmal alle Forks aus
    git = git_servant(config)

    #hole dir die Zeit zu der die Aufgabe commited wurde aus dem Master Repository
    masterAufgabe = git.getAufgabeMaster(config('codingchaos', 'ordner'))

    #Gebe die Zeit an eine Funktion weiter, die durch alle Forks iterriert und berechne den diff des letzten Commits
    #mit dem des commits der masterAufgabe
    #mache daraus eine liste mit Ordnername + Zeit und pipe die in eine HTML-Datei mit einem einfachen Table
if __name__ == '__main__':
    main()