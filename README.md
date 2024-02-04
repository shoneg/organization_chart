# Organization Chart

This Python script can be used to generate an organization chart.

The script was originally written for a German group and therefore contains a lot of German language. However, it can be used for any language; the results will then be in the corresponding language.

- [Organization Chart](#organization-chart)
  - [Features - German](#features---german)
  - [Feature - English](#feature---english)
  - [Usage - German](#usage---german)
  - [Usage - English](#usage---english)
  - [Disclaimer - German](#disclaimer---german)
  - [Disclaimer - English](#disclaimer---english)
  - [Based on …](#based-on-)

## Features - German

- Erzeugt skalierbare Vektorgrafiken
- Die meisten Parameter sind optional
- Flexible Nutzung
- MIT Lizenz
- Adressangaben sind klickbar
- Zu jeder Person wird ein v-Card QR-Code erstellt
- Schnelle Ausführung
- Leicht Änderbar
- Kein Entwickler:innenwissen zur Nutzung notwendig

## Feature - English

- Creates scalable vector graphics
- Most parameters are optional
- Flexible use
- MIT license
- Address details are clickable
- A v-Card QR code is created for each person
- Fast execution
- Easy to change
- No developer knowledge required for use

## Usage - German

In der Datei *config.ym*l kann eine Liste von Organisationen angegeben werden, die jeweils beliebig viele Personen beherbergen können. Eine Person muss eine „Position“ haben. Zusätzlich kann ein „Vorname“, ein „Nachname“, eine „Mail“, eine „Telefon“(-nummer), eine „Adresse“, eine URL zu einem „Bild“ und eine URL zu einer „Website“ angegeben werden. Das Skript `orgranigramm.py` kann dann im Ordner, der die config.yml enthält, ausgeführt werden. Nun wird im Ordner *results* für jede angegebene Organisation eine SVG-Datei generiert.

Um bei langen Positionstiteln Überlappungen zu vermeiden, kann in der Konfigurationsdatei für jede Person zusätzliche die „Positionszeilen“ angegeben werden. Diese können 1, 2 oder 3 sein. Wird nichts angegeben, wird 1 verwendet.

Das Repository enthält eine beispielhafte [config.yml-Datei](./config.yml). Das zugehörige [Organigramm](./results/Hallo-Welt.svg) ist bereits im results-Ordner zu sehen.

## Usage - English

A list of organizations can be specified in the *config.yml* file, each of which can accommodate any number of people. A person must have a "Position". In addition, a "Vorname", a "Nachname", a "Telefon"(-number), a "Mail", a URL to an "Adresse" and a URL to a "Website" can be specified. The `orgranigramm.py` script can then be executed in the folder containing the config.yml. An SVG file is now generated in the *results* folder for each specified organization.

To avoid overlaps with long position titles, additional "Positionszeilen" can be specified for each person in the configuration file. These can be 1, 2 or 3. If nothing is specified, 1 is used.

The repository contains an example [config.yml file](./config.yml). The corresponding [organization chart](./results/Hallo-Welt.svg) can already be seen in the results folder.

## Disclaimer - German

Die erstellten Organigramme sind nicht perfekt. Das Skript wurde für einen relativ spezifischen Anwendungsfall erstellt. Das kann dazu führen, dass in anderen Fällen die berechneten Längen nicht optimal sind. Wenn Basisprogrammierkenntnisse vorhanden sind können die Abstände aber leicht angepasst werden, da der Quellcode relativ klein ist.

## Disclaimer - English

The organizational charts created are not perfect. The script was created for a relatively specific use case. This may mean that the calculated lengths are not optimal in other cases. However, if basic programming skills are available, the distances can be easily adjusted as the source code is relatively small.

## Based on …

- [yaml](https://pypi.org/project/PyYAML/)
- [numpy](https://pypi.org/project/numpy/)
- [QR Code Generator](https://qrcode.tec-it.com)
