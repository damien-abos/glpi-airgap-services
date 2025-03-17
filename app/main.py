from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def status():
    return {"status": "up"}

#@app.get("/api/registration")
#def registration():
#    return {}

@app.get("/api/registration/info")
def registration_info():
    return {
        "key": "%%REGISTRATION_KEY%%",
        "is_valid": True,
        "owner": {
            "name": "%%REGISTRATION_OWNER%%"
        },
        "subscription": {
            "offer_reference": "virtual",
            "title": "Enregistré",
            "is_running": True,
            "begin_date": None,
            "end_date": None,
            "features": []
        }
    }

@app.get("/api/registration/offers")
def registration_offers():
    # Request Headers:
    # - X-Registration-Key: %%REGISTRATION_KEY%%
    # - X-Glpi-Network-Uid: %%GLPI_NETWORK_UID%%
    return [
        {
            "offer_reference": "starter",
            "title": "Support Starter",
            "features": [
                "marketplace",
                "last-glpi-version"
            ]
        },
        {
            "offer_reference": "network-basic",
            "title": "Basic",
            "features": [
                "marketplace",
                "annual-commitment",
                "last-glpi-version",
                "additional_services",
                "plugins-basic"
            ]
        },
        {
            "offer_reference": "network-standard",
            "title": "Standard",
            "features": [
                "marketplace",
                "annual-commitment",
                "last-glpi-version",
                "additional_services",
                "plugins-basic",
                "plugins-standard"
            ]
        },
        {
            "offer_reference": "network-advanced",
            "title": "Advanced",
            "features": [
                "marketplace",
                "annual-commitment",
                "last-glpi-version",
                "additional_services",
                "plugins-basic",
                "plugins-standard",
                "plugins-advanced"
            ]
        }
    ]


@app.get("/api/marketplace/plugins")
def markplace_plugins():
    # Request Headers:
    # - X-Registration-Key: %%REGISTRATION_KEY%%
    # - X-Glpi-Network-Uid: %%GLPI_NETWORK_UID%%
    # - X-Range: 0-199

    # Response Headers:
    # - X-Content-Type-Options: nosniff
    # - Accept-Range: 104 model
    # - Content-Range: 0-199/104
    # - Cache-Control: no-cache, private
    # - X-RateLimit-Limit: 60
    # - X-RateLimit-Remaining: 58
    return [
        {
            "id": 2,
            "key": "additionalalerts",
            "name": "Additional Alerts",
            "logo_url": "https://raw.githubusercontent.com/InfotelGLPI/additionalalerts/master/additionalalerts.png",
            "xml_url": "https://raw.githubusercontent.com/InfotelGLPI/additionalalerts/master/additionalalerts.xml",
            "homepage_url": "https://github.com/InfotelGLPI/additionalalerts",
            "download_url": "https://github.com/InfotelGLPI/additionalalerts/releases",
            "issues_url": "https://github.com/InfotelGLPI/additionalalerts/issues",
            "readme_url": "https://raw.githubusercontent.com/InfotelGLPI/additionalalerts/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2009-08-07T00:00:00.000000Z",
            "date_updated": "2022-04-25T00:00:00.000000Z",
            "download_count": 37443,
            "note": 3.0833333333333335,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                }
            ],
            "versions": [
                {
                    "num": "2.4.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/additionalalerts/releases/download/2.4.0/glpi-additionalalerts-2.4.0.tar.bz2",
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Envoi d&#039;alertes supplémentaires. Ce plugin vous permet d’envoyer les alertes email concernant les matériels ayant une date d&#039;achat vide et les cartouches ayant un niveau faible.",
                    "long_description": "Ce plugin vous permet d’envoyer les alertes email supplémentaires :<br />- Matériels ayant une date d&#039;achat vide (Choix des types pris en charge : pour ne pas prendre en compte les matériels non achetés),<br />- Niveaux de cartouches faible (fusion Inventory)."
                },
                {
                    "lang": "en",
                    "short_description": "Sending of additional alerts. This plugin enables you to send email alerts regarding the items with empty buy date and Cartridges whose level is low.",
                    "long_description": "This plugin enables you to send email supplementary alerts :<br />- Items with empty buy date (Choice of supported types : for not taking into account the equipment not purchased),<br />- Cartridges whose level is low (fusion Inventory)."
                }
            ],
            "required_offers": None,
            "short_description": "Sending of additional alerts. This plugin enables you to send email alerts regarding the items with empty buy date and Cartridges whose level is low."
        },
        {
            "id": 3,
            "key": "addressing",
            "name": "IP Report",
            "logo_url": "https://github.com/pluginsGLPI/addressing/blob/master/addressing.png?raw=true",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/addressing/master/addressing.xml",
            "homepage_url": "https://github.com/pluginsGLPI/addressing",
            "download_url": "https://github.com/pluginsGLPI/addressing/releases",
            "issues_url": "https://github.com/pluginsGLPI/addressing/issues",
            "readme_url": "https://github.com/pluginsGLPI/addressing/wiki",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2009-08-07T00:00:00.000000Z",
            "date_updated": "2024-11-27T00:00:00.000000Z",
            "download_count": 93094,
            "note": 3.2464788732394365,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 4,
                    "name": "Gilles Portheault"
                },
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                },
                {
                    "id": 5,
                    "name": "Remi Collet"
                },
                {
                    "id": 6,
                    "name": "Nelly Mahu-Lasson"
                }
            ],
            "versions": {
                "0": {
                    "num": "3.0.3",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/addressing/releases/download/3.0.3/glpi-addressing-3.0.3.tar.bz2",
                    "stability": "stable"
                },
                "1": {
                    "num": "3.0.2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/addressing/releases/download/3.0.2/glpi-addressing-3.0.2.tar.bz2",
                    "stability": "stable"
                },
                "2": {
                    "num": "3.0.1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/addressing/releases/download/3.0.1/glpi-addressing-3.0.1.tar.bz2",
                    "stability": "stable"
                },
                "5": {
                    "num": "3.0.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/addressing/releases/download/3.0.0/glpi-addressing-3.0.0.tar.bz2",
                    "stability": "stable"
                },
                "3": {
                    "num": "3.0.0-rc2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/addressing/releases/download/3.0.0-rc2/glpi-addressing-3.0.0-rc2.tar.bz2",
                    "stability": "RC"
                },
                "4": {
                    "num": "3.0.0-rc1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/addressing/releases/download/3.0.0-rc1/glpi-addressing-3.0.0-rc1.tar.bz2",
                    "stability": "RC"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Rapport IP. Ce plugin vous permet créer un rapport IP afin de visualiser les adresses ip utilisées et libres sur un réseau donné. Génération de la liste des ip attribuées / libres / réservées / doublons. Personnalisation de l’affichage. Fonction ping adresses libres",
                    "long_description": "Ce plugin vous permet créer des rapports IP afin de visualiser les adresses ip utilisées et libres sur un réseau donné.<br />-Génération de la liste des ip attribuées / libres / réservées / doublons pour tout type de matériel ayant une IP.<br />-Réservations d&#039;IP.<br />-Ping adresses libres sur divers systèmes."
                },
                {
                    "lang": "en",
                    "short_description": "IP reports. This plugin enables you to create IP report for visualize IP addresses used and free on a given network.",
                    "long_description": "This plugin enables you to create IP reports for visualize IP addresses used and free on a given network.<br />-List generation of ip assigned / free / reserved / doubles for all items with IP field.<br />-IP reservations.<br />-Ping fonction for free ip for many systems."
                },
                {
                    "lang": "cs",
                    "short_description": "Výkazy o IP adresách. Tento zásuvný modul umožňuje vytvářet výkaz o IP adresách pro vizualizaci použitých a volných adres na dané síti.",
                    "long_description": "Výkazy o IP adresách. Tento zásuvný modul umožňuje vytvářet výkaz o IP adresách pro vizualizaci použitých a volných adres na dané síti.<br />- Vytváření seznamu přiřazených/volných/rezervovaných/duplicitních IP adres pro všechny položky s kolonkou IP adresa.<br />- Rezervace IP adres.<br />- Ping funkce pro volné IP adresy pro mnoho systémů."
                }
            ],
            "required_offers": None,
            "short_description": "IP reports. This plugin enables you to create IP report for visualize IP addresses used and free on a given network."
        },
        {
            "id": 5,
            "key": "manageentities",
            "name": "Entities Management",
            "logo_url": "https://raw.githubusercontent.com/InfotelGLPI/manageentities/master/manageentities.png",
            "xml_url": "https://raw.githubusercontent.com/InfotelGLPI/manageentities/master/manageentities.xml",
            "homepage_url": "https://github.com/InfotelGLPI/manageentities",
            "download_url": "https://github.com/InfotelGLPI/manageentities/releases",
            "issues_url": None,
            "readme_url": None,
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2009-08-07T00:00:00.000000Z",
            "date_updated": "2022-10-08T00:00:00.000000Z",
            "download_count": 31654,
            "note": 2.566666666666667,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                },
                {
                    "id": 49,
                    "name": "Infotel"
                }
            ],
            "versions": {
                "3": {
                    "num": "4.0.3",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/manageentities/releases/download/4.0.3/glpi-manageentities-4.0.3.tar.bz2",
                    "stability": "stable"
                },
                "4": {
                    "num": "4.0.2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/manageentities/releases/download/4.0.2/glpi-manageentities-4.0.2.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Gestion d’entités. Ce plugin vous permet de gérer vos entités. Lier des documents, contacts, contrats. De plus vous pouvez créer des rapports d&#039;interventions, et faire le suivi contrat de vos entités.",
                    "long_description": "Ce plugin vous permet de gérer vos entités. Lier des documents, contacts, contrats. De plus vous pouvez créer des rapports d&#039;interventions, et faire le suivi contrat de vos entités. Pour une entité donnée, vous définissez<br />- Les contacts associés (ainsi que le responsable),<br />- Les contrats associés ( ainsi que celui utilisé par défaut),<br />- Le tarif journalier pour un type d&#039;intervention donné,<br />- Les documents associés.<br />- Puis dans le détail du contrat, vous définissez le solde initial (nombre de jours x un type d&#039;intervention donné).<br />- Une fois ceci fait, vous pourrez créer des rapports d&#039;intervention et ainsi avoir le décompte du contrat utilisé.<br />- Possibilité de lancement du plugin au démarrage de GLPI"
                },
                {
                    "lang": "en",
                    "short_description": "Entities management. This plugin allows you to manage entities. Link with documents, contacts, contracts. You can also create intervention reports and do contract management of your entities.",
                    "long_description": "This plugin allows you to manage entities. Link with documents, contacts, contracts. You can also create intervention reports and do contract management of your entities. For a given entity, you define :<br />- The associated contacts (and the manager),<br />- The contracts involved (and those used by default),<br />- The daily rate for a given type of intervention,<br />- The associated documents.<br />- Then in the details of the contract, you set the initial balance (number of days x the type of intervention).<br />- Once done, you can create reports of intervention and thus have the breakdown of contract used.<br />- The plugin can be launched when GLPI loading"
                }
            ],
            "required_offers": None,
            "short_description": "Entities management. This plugin allows you to manage entities. Link with documents, contacts, contracts. You can also create intervention reports and do contract management of your entities."
        },
        {
            "id": 6,
            "key": "manufacturersimports",
            "name": "Manufacturers Web Imports",
            "logo_url": "https://raw.githubusercontent.com/InfotelGLPI/manufacturersimports/master/manufacturersimports.png",
            "xml_url": "https://raw.githubusercontent.com/InfotelGLPI/manufacturersimports/master/manufacturersimports.xml",
            "homepage_url": "https://github.com/InfotelGLPI/manufacturersimports",
            "download_url": "https://github.com/InfotelGLPI/manufacturersimports/releases",
            "issues_url": "https://github.com/InfotelGLPI/manufacturersimports/issues",
            "readme_url": "https://raw.githubusercontent.com/InfotelGLPI/manufacturersimports/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2009-08-07T00:00:00.000000Z",
            "date_updated": "2024-11-02T00:00:00.000000Z",
            "download_count": 48644,
            "note": 2.8207547169811322,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                },
                {
                    "id": 49,
                    "name": "Infotel"
                },
                {
                    "id": 7,
                    "name": "Bazile Lebeau"
                }
            ],
            "versions": {
                "1": {
                    "num": "3.0.9",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/manufacturersimports/releases/download/3.0.9/glpi-manufacturersimports-3.0.9.tar.bz2",
                    "stability": "stable"
                },
                "2": {
                    "num": "3.0.8",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/manufacturersimports/releases/download/3.0.8/glpi-manufacturersimports-3.0.8.tar.bz2",
                    "stability": "stable"
                },
                "3": {
                    "num": "3.0.7",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/manufacturersimports/releases/download/3.0.7/glpi-manufacturersimports-3.0.7.tar.bz2",
                    "stability": "stable"
                },
                "4": {
                    "num": "3.0.6",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/manufacturersimports/releases/download/3.0.6/glpi-manufacturersimports-3.0.6.tar.bz2",
                    "stability": "stable"
                },
                "5": {
                    "num": "3.0.5",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/manufacturersimports/releases/download/3.0.5/glpi-manufacturersimports-3.0.5.tar.bz2",
                    "stability": "stable"
                },
                "6": {
                    "num": "3.0.4",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/manufacturersimports/releases/download/3.0.4/glpi-manufacturersimports-3.0.4.tar.bz2",
                    "stability": "stable"
                },
                "7": {
                    "num": "3.0.3",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/manufacturersimports/releases/download/3.0.3/glpi-manufacturersimports-3.0.3.tar.bz2",
                    "stability": "stable"
                },
                "8": {
                    "num": "3.0.2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/manufacturersimports/releases/download/3.0.2/glpi-manufacturersimports-3.0.2.tar.bz2",
                    "stability": "stable"
                },
                "9": {
                    "num": "3.0.1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/manufacturersimports/releases/download/3.0.1/glpi-manufacturersimports-3.0.1.tar.bz2",
                    "stability": "stable"
                },
                "11": {
                    "num": "3.0.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/manufacturersimports/releases/download/3.0.0/glpi-manufacturersimports-3.0.0.tar.bz2",
                    "stability": "stable"
                },
                "10": {
                    "num": "3.0.0-rc1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/manufacturersimports/releases/download/3.0.0-rc1/glpi-manufacturersimports-3.0.0-rc1.tar.bz2",
                    "stability": "RC"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "\n                Imports des informations financières des matériels directement depuis le site web des fabricants.<br />Fonctionne avec Dell, HP, Toshiba, Fujitsu-Siemens et Lenovo",
                    "long_description": "\n               Ce plugin vous permet d’injecter des informations financières depuis les sites fabricants directement dans GLPI.\n                - Vous sélectionnez vos types de matériels et si au préalable vous avez fourni numéro de série et numéro de modèle (selon les fabricants) vous pourrez importer la garantie, la date d&#039;achat, ainsi qu&#039;enregistrer la page hmtl des fabricants.\n                - Fonctionne avec Dell, HP, Toshiba, Lenovo (&gt; 1.5.0) et Fujitsu-Siemens\n            "
                },
                {
                    "lang": "en",
                    "short_description": "\n                Imports of financials informations for items from manufacturers web site.<br />Works with Dell, HP, Toshiba, Fujitsu-Siemens and Lenovo",
                    "long_description": "\n                This plugin allows you to inject financials informations from manufacturers web site files in GLPI.\n                - You select your type of equipment in advance and if you provided serial number and model number (different from manufacturers) you can import the warranty, the date of purchase and save the page HMTL manufacturers.\n                - Works with Dell, HP, Toshiba, Lenovo (&gt; 1.5.0) and Fujitsu-Siemens\n            "
                },
                {
                    "lang": "cs",
                    "short_description": "\n                Importy finančních informací pro položky z webu výrobce.<br />Funguje s Dell, HP, Toshiba, Fujitsu-Siemens a Lenovo",
                    "long_description": "\n                Tento zásuvný modul umožňuje vpravovat finannčí informace z webů výrobců do GLPI.\n                - Předem vyberete typ vybavení a když zadáte sériové číslo a označení modelu (liší se mezi výrobci) můžete importovat informace o záruce, datu zakoupení a uložit v podobě HTML stránky.\n                - Funguje s Dell, HP, Toshiba, Lenovo (verze &gt; 1.5.0) a Fujitsu-Siemens\n            "
                }
            ],
            "required_offers": None,
            "short_description": "\n                Imports of financials informations for items from manufacturers web site.<br />Works with Dell, HP, Toshiba, Fujitsu-Siemens and Lenovo"
        },
        {
            "id": 7,
            "key": "accounts",
            "name": "Accounts Inventory",
            "logo_url": "https://raw.githubusercontent.com/InfotelGLPI/accounts/master/wiki/accounts.png",
            "xml_url": "https://raw.githubusercontent.com/InfotelGLPI/accounts/master/accounts.xml",
            "homepage_url": "https://github.com/InfotelGLPI/accounts",
            "download_url": "https://github.com/InfotelGLPI/accounts/releases",
            "issues_url": "https://github.com/InfotelGLPI/accounts/issues",
            "readme_url": "https://raw.githubusercontent.com/InfotelGLPI/accounts/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2009-08-07T00:00:00.000000Z",
            "date_updated": "2024-01-27T00:00:00.000000Z",
            "download_count": 50370,
            "note": 3.2714285714285714,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                },
                {
                    "id": 49,
                    "name": "Infotel"
                }
            ],
            "versions": {
                "0": {
                    "num": "3.0.4",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/accounts/releases/download/3.0.4/glpi-accounts-3.0.4.tar.bz2",
                    "stability": "stable"
                },
                "1": {
                    "num": "3.0.3",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/accounts/releases/download/3.0.3/glpi-accounts-3.0.3.tar.bz2",
                    "stability": "stable"
                },
                "2": {
                    "num": "3.0.2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/accounts/releases/download/3.0.2/glpi-accounts-3.0.2.tar.bz2",
                    "stability": "stable"
                },
                "3": {
                    "num": "3.0.1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/accounts/releases/download/3.0.1/glpi-accounts-3.0.1.tar.bz2",
                    "stability": "stable"
                },
                "6": {
                    "num": "3.0.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/accounts/releases/download/3.0.0/glpi-accounts-3.0.0.tar.bz2",
                    "stability": "stable"
                },
                "4": {
                    "num": "3.0.0-rc2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/accounts/releases/download/3.0.0-rc2/glpi-accounts-3.0.0-rc2.tar.bz2",
                    "stability": "RC"
                },
                "5": {
                    "num": "3.0.0-rc1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/accounts/releases/download/3.0.0-rc1/glpi-accounts-3.0.0-rc1.tar.bz2",
                    "stability": "RC"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Gestion de comptes (login / mot de passe).<br />Ce plugin vous permet de gérer les comptes de votre réseau et de les associer à des éléments de l’inventaire.<br />Les comptes sont cryptés en base à l&#039;aide d&#039;un hash et d&#039;une clé de cryptage.<br />Un système d&#039;alertes mail permet de vérifier les comptes expirés.",
                    "long_description": "Ce plugin vous permet de gérer les comptes de votre réseau et de les associer à des éléments de l’inventaire.<br />- Détail d&#039;un compte : login / mot de passe, utilisateur, dates de création et d&#039;expiration,<br />- Utilisation d&#039;un hash et d&#039;une clé de cryptage pour le hash,<br />- Envoi de mails à l&#039;expiration de comptes,<br />- Utilisable depuis le helpdesk,<br />- Peut être intégré au plugin environment."
                },
                {
                    "lang": "en",
                    "short_description": "Manage accounts (login / password). <br />This plugin enables you to manage the accounts of your network and associate them with elements of the inventory.<br />The accounts are crypted in database with hash and crypting key.<br />A mailing system allow to verify expired accounts.",
                    "long_description": "This plugin enables you to manage the accounts of your network and associate them with elements of the inventory.<br />- Account detail : login / password, user, creation and expiration,<br />-Using hash and crypting key,<br />- Mailing system allow to verify expired accounts,<br />- Can be used with helpdesk,<br />- Can be integrated into Environment plugin."
                }
            ],
            "required_offers": None,
            "short_description": "Manage accounts (login / password). <br />This plugin enables you to manage the accounts of your network and associate them with elements of the inventory.<br />The accounts are crypted in database with hash and crypting key.<br />A mailing system allow to verify expired accounts."
        },
        {
            "id": 9,
            "key": "appliances",
            "name": "Appliances Inventory",
            "logo_url": "https://raw.githusercontent.com/yllen/appliances/appliances.png",
            "xml_url": "https://raw.githubusercontent.com/yllen/appliances/master/appliances.xml",
            "homepage_url": "https://github.com/yllen/appliances",
            "download_url": "https://github.com/yllen/appliances/releases",
            "issues_url": None,
            "readme_url": None,
            "changelog_url": "",
            "license": "AGPLv3",
            "date_added": "2009-08-07T00:00:00.000000Z",
            "date_updated": "2023-05-09T00:00:00.000000Z",
            "download_count": 20896,
            "note": 3.5,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                },
                {
                    "id": 5,
                    "name": "Remi Collet"
                },
                {
                    "id": 6,
                    "name": "Nelly Mahu-Lasson"
                }
            ],
            "versions": [],
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Gestion d&#039;applicatifs. Ce plugin vous permet de créer des applicatifs (ensemble d’élements constituant un applicatif).",
                    "long_description": "Ce plugin vous permet de créer des applicatifs (ensemble d’élements constituant un applicatif).<br />-Création d’applicatifs composé de plusieurs items<br />-Gestion directe à partir de l’item<br />-Intégration avec l&#039;assistance<br />NB : Ce plugin peut être intégré au plugin environment et être utilisé avec avec le plugin archires."
                },
                {
                    "lang": "en",
                    "short_description": "Appliances management. This plugin enables you to create appliance (several elements constituting a unit).",
                    "long_description": "This plugin enables you to create appliance (several elements constituting a unit).<br />-Appliances creation (composed by various inventory item)<br />-Direct management from items<br />-Integrated with Helpdesk<br />NB : This plugin can be integrated in environment plugin and be used with archires plugin."
                }
            ],
            "required_offers": None,
            "short_description": "Appliances management. This plugin enables you to create appliance (several elements constituting a unit)."
        },
        {
            "id": 12,
            "key": "badges",
            "name": "Badges Inventory",
            "logo_url": "https://raw.githubusercontent.com/InfotelGLPI/badges/master/badges.png",
            "xml_url": "https://raw.githubusercontent.com/InfotelGLPI/badges/master/badges.xml",
            "homepage_url": "https://github.com/InfotelGLPI/badges",
            "download_url": "https://github.com/InfotelGLPI/badges/releases",
            "issues_url": "https://github.com/InfotelGLPI/badges/issues",
            "readme_url": "https://raw.githubusercontent.com/InfotelGLPI/badges/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2009-08-07T00:00:00.000000Z",
            "date_updated": "2022-04-25T00:00:00.000000Z",
            "download_count": 19683,
            "note": 3.4,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                },
                {
                    "id": 49,
                    "name": "Infotel"
                }
            ],
            "versions": {
                "1": {
                    "num": "3.0.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/badges/releases/download/3.0.0/glpi-badges-3.0.0.tar.bz2",
                    "stability": "stable"
                },
                "0": {
                    "num": "3.0.0-beta",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/badges/releases/download/3.0.0-beta/glpi-badges-3.0.0-beta.tar.bz2",
                    "stability": "beta"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Gestion de badges. Ce plugin vous permet de gérer les badges de votre réseau et de les associer à des éléments de l’inventaire.<br />Un système d&#039;alertes mail permet de vérifier les badges qui vont ou qui ont expirés.",
                    "long_description": "Ce plugin vous permet de gérer les badges de votre réseau et de les associer à des éléments de l’inventaire.<br />Un système d&#039;alertes mail permet de vérifier les badges qui vont ou qui ont expirés.<br />- Utilisable depuis le helpdesk<br />- Peut être intégré au plugin environment."
                },
                {
                    "lang": "en",
                    "short_description": "Badges management. This plugin enables you to manage your badges into your network and associate them with elements of the inventory.<br />A mailing system allow to verify already expired or soon expired badges.",
                    "long_description": "This plugin enables you to manage your badges into your network and associate them with elements of the inventory.<br />A mailing system allow to verify already expired or soon expired badges.<br />- Can be used with helpdesk<br />- Can be integrated into Environment plugin."
                },
                {
                    "lang": "cs",
                    "short_description": "Správa jmenovek. Tento zásuvný modul umožňuje spravovat jmenovky v síti a přiřazovat je k prvkům inventáře.<br />Systém posílání e-mailů umožňuje ověřovat jmenovky se skončenou platností nebo ty, kterým brzy končí.",
                    "long_description": "Správa jmenovek. Tento zásuvný modul umožňuje spravovat jmenovky v síti a přiřazovat je k prvkům inventáře.<br />Systém posílání e-mailů umožňuje ověřovat jmenovky se skončenou platností nebo ty, kterým brzy končí.<br />- Je možné použít se službou podpory<br />- Je možné začlenit do zásuvného modulu Prostředí."
                }
            ],
            "required_offers": None,
            "short_description": "Badges management. This plugin enables you to manage your badges into your network and associate them with elements of the inventory.<br />A mailing system allow to verify already expired or soon expired badges."
        },
        {
            "id": 14,
            "key": "databases",
            "name": "Databases Inventory",
            "logo_url": "https://raw.githubusercontent.com/InfotelGLPI/databases/master/databases.png",
            "xml_url": "https://raw.githubusercontent.com/InfotelGLPI/databases/master/databases.xml",
            "homepage_url": "https://github.com/InfotelGLPI/databases",
            "download_url": "https://github.com/InfotelGLPI/databases/releases",
            "issues_url": "https://github.com/InfotelGLPI/databases/issues",
            "readme_url": "https://raw.githubusercontent.com/InfotelGLPI/databases/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2009-08-07T00:00:00.000000Z",
            "date_updated": "2021-04-16T00:00:00.000000Z",
            "download_count": 25593,
            "note": 3.022727272727273,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                },
                {
                    "id": 49,
                    "name": "Infotel"
                }
            ],
            "versions": [],
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Gestion de bases de données. Ce plugin vous permet de gérer les bases de données de votre réseau et de les associer à des éléments de l’inventaire.<br />-Inventaire des instances<br />-Inventaire des scripts",
                    "long_description": "Ce plugin vous permet de gérer les bases de données de votre réseau et de les associer à des éléments de l’inventaire.<br />- Inventaire des instances<br />- Inventaire des scripts.<br />- Utilisable depuis le helpdesk<br />- Peut être intégré au plugin environment."
                },
                {
                    "lang": "en",
                    "short_description": "Databases management. This plugin enables you to manage the databases of your network and associate them with elements of the inventory.<br />-Instances inventory<br />-Scripts inventory",
                    "long_description": "This plugin enables you to manage the databases of your network and associate them with elements of the inventory.<br />- Instances inventory<br />- Scripts inventory.<br />- Can be used with helpdesk<br />-Can be integrated into Environment plugin."
                },
                {
                    "lang": "cs",
                    "short_description": "Správa databází. Tento zásuvný modul umožňuje spravovat databáze na síti a přiřazovat je prvkům v inventáři.<br />-Inventář instancí<br />-Inventář skriptů",
                    "long_description": "Tento zásuvný modul umožňuje spravovat databáze na síti a přiřazovat je prvkům v inventáři.<br />-Inventář instancí<br />-Inventář skriptů.<br />- Je možné použít se službou podpory<br />-Je možné začlenit do zásuvného modulu Prostředí."
                }
            ],
            "required_offers": None,
            "short_description": "Databases management. This plugin enables you to manage the databases of your network and associate them with elements of the inventory.<br />-Instances inventory<br />-Scripts inventory"
        },
        {
            "id": 17,
            "key": "financialreports",
            "name": "Financial Reports",
            "logo_url": "https://raw.githubusercontent.com/InfotelGLPI/financialreports/master/financialreports.png",
            "xml_url": "https://raw.githubusercontent.com/InfotelGLPI/financialreports/master/financialreports.xml",
            "homepage_url": "https://github.com/InfotelGLPI/financialreports",
            "download_url": "https://github.com/InfotelGLPI/financialreports/releases",
            "issues_url": "https://github.com/InfotelGLPI/financialreports/issues",
            "readme_url": "https://raw.githubusercontent.com/InfotelGLPI/financialreports/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2009-08-07T00:00:00.000000Z",
            "date_updated": "2022-04-25T00:00:00.000000Z",
            "download_count": 22740,
            "note": 2.4047619047619047,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                },
                {
                    "id": 49,
                    "name": "Infotel"
                }
            ],
            "versions": {
                "2": {
                    "num": "3.0.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/financialreports/releases/download/3.0.0/glpi-financialreports-3.0.0.tar.bz2",
                    "stability": "stable"
                },
                "0": {
                    "num": "3.0.0-rc2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/financialreports/releases/download/3.0.0-rc2/glpi-financialreports-3.0.0-rc2.tar.bz2",
                    "stability": "RC"
                },
                "1": {
                    "num": "3.0.0-rc1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/financialreports/releases/download/3.0.0-rc1/glpi-financialreports-3.0.0-rc1.tar.bz2",
                    "stability": "RC"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Rapport financier : Arrété du parc. Ce plugin vous permet de générer un arrété du parc à une date donnée.<br />- Export Csv, Pdf",
                    "long_description": "Ce plugin vous permet de générer un arrété du parc à une date donnée.<br />- Dans la configuration, renseignez l&#039;identifiant pour chaque type de matériel de l&#039;inventaire correspondant au numéro d&#039;inventaire. (exemple : Vos pcs portables ont un numéro d&#039;inventaire commençant par PO renseignez donc le plugin avec PO, Serveurs : SE, PC Fixes : PC etc).<br />- Générez le rapport.<br />- Export Csv, Pdf"
                },
                {
                    "lang": "en",
                    "short_description": "Financial report : Asset situation. This plugin allows you to generate a financial report (asset situation) for a given date.<br />- Export Csv, Pdf",
                    "long_description": "This plugin allows you to generate a financial report (asset situation) for a given date.<br />- In plugin setup, add identifier for each type of equipment inventory related to the inventory number (example : your notebooks have un inventory number beginnning with &#039;PO&#039; so fill the setup plugin with PO, Servers : SE, Computers : PC etc).<br />- Generate the report.<br />- Export Csv, Pdf."
                }
            ],
            "required_offers": None,
            "short_description": "Financial report : Asset situation. This plugin allows you to generate a financial report (asset situation) for a given date.<br />- Export Csv, Pdf"
        },
        {
            "id": 23,
            "key": "reports",
            "name": "reports",
            "logo_url": "https://raw.githubusercontent.com/yllen/reports/master/report_page.png",
            "xml_url": "https://raw.githubusercontent.com/yllen/reports/master/reports.xml",
            "homepage_url": "https://github.com/yllen/reports",
            "download_url": "https://github.com/yllen/reports/releases",
            "issues_url": None,
            "readme_url": None,
            "changelog_url": "",
            "license": "GPL v3+",
            "date_added": "2009-08-07T00:00:00.000000Z",
            "date_updated": "2024-04-16T00:00:00.000000Z",
            "download_count": 141840,
            "note": 2.830210772833724,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 6,
                    "name": "Nelly Mahu-Lasson"
                },
                {
                    "id": 5,
                    "name": "Remi Collet"
                }
            ],
            "versions": [
                {
                    "num": "1.16.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/yllen/reports/releases/download/v1.16.0/glpi-reports-1.16.0.tar.gz",
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Rapports. Ce plugin fournit des rapports supplémentaires. Il permet également \n         d’ajouter très facilement de nouveaux rapports.",
                    "long_description": "Ce plugin fournit des rapports supplémentaires.<br />Fonctionnalités \n         principales :<br />-Il permet d’ajouter très facilement de nouveaux rapports (via l’ajout \n         d’un fichier PHP pour le rapport et un fichier de langue associé).<br />-Il prend en charge\n          la gestion de droits de tout nouveau rapport ajouté.<br />-Il fournit quelques rapports \n         (pour exemple)<br />Rapports disponibles dans la version 1.3.0 :<br />-Arborescence des \n         lieux<br />-Catalogue des règles<br />-Historique des dernières installations de logiciels\n         <br />-Historique des dernières modifications de matériels<br />-Informations financières\n         <br />-Liste des groupes et membres<br />-Liste des licences par expiration<br />-Liste des\n          équipements par groupe<br />-Nombre d’équipements par entité<br />-Nombre d’équipements \n          par lieu<br />-Ordinateurs en doublons<br />-Etat détaillé des licences"
                },
                {
                    "lang": "en",
                    "short_description": "Reports. This plugin enables additional reports. It also allow you to add new \n         reports in a simply way.",
                    "long_description": "This plugin enables additional reports.<br />Main features :<br />-It also \n         plugin allow you to add new reports in a simply way (one PHP script for the report and one \n         for the translation).<br />-It handle the right for each new report<br />-It provides some \n         new reports (as sample)<br />Reports available in version 1.3.0 :<br />-Detailed license \n         report<br />-Duplicate computers<br />-Financial information<br />-History of last \n         hardware’s installations<br />-History of last software’s installations<br />-Licenses by \n         expiration date<br />-List all devices of a group, order by users<br />-List of groups and \n         members<br />-Location tree<br />-Number of equipments by location<br />-Number of items by\n          entity<br />-Rule’s catalog"
                },
                {
                    "lang": "cs",
                    "short_description": "Výkazy. Tento zásuvný modul přidává další hlášení. Také vám umožní snadno přidat nové.",
                    "long_description": "Tento zásuvný modul přidává další hlášení.<br />Hlavní funkce :<br />-Také \n         umožňuje snadno přidávat nová hlášení (jeden PHP skript pro výkaz a jeden pro překlady).\n         <br />-Obsluhuje práva na každý z nových výkazů<br />-Poskytuje některé nové výkazy (pro ukázku)\n         <br />Výkazy, které jsou k dispozici ve verzi 1.3.0 :<br />-Podrobný výkaz o licencích<br />\n         -Duplicitní počítače<br />-Finanční informace<br />-Historie nedávných instalací hardware<br />\n         -Historie nedávných instalací software<br />-Licence podle data skončení platnosti<br />\n         -Seznam všech zařízení skupiny, seřazené podle uživatelů<br />-Seznam skupina a jejich členů\n         <br />-Strom umístění<br />-Počty vybavení podle umístění<br />-Počty položek podle entit\n         <br />-Katalog pravidla"
                }
            ],
            "required_offers": None,
            "short_description": "Reports. This plugin enables additional reports. It also allow you to add new \n         reports in a simply way."
        },
        {
            "id": 25,
            "key": "resources",
            "name": "Human Resources Management",
            "logo_url": "https://raw.githubusercontent.com/InfotelGLPI/resources/master/resources.png",
            "xml_url": "https://raw.githubusercontent.com/InfotelGLPI/resources/master/resources.xml",
            "homepage_url": "https://github.com/InfotelGLPI/resources",
            "download_url": "https://github.com/InfotelGLPI/resources/releases",
            "issues_url": "https://github.com/InfotelGLPI/resources/issues",
            "readme_url": "https://raw.githubusercontent.com/InfotelGLPI/resources/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2009-08-07T00:00:00.000000Z",
            "date_updated": "2025-02-05T00:00:00.000000Z",
            "download_count": 49478,
            "note": 2.781456953642384,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                },
                {
                    "id": 49,
                    "name": "Infotel"
                }
            ],
            "versions": {
                "1": {
                    "num": "3.0.7",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/resources/releases/download/3.0.7/glpi-resources-3.0.7.tar.bz2",
                    "stability": "stable"
                },
                "2": {
                    "num": "3.0.6",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/resources/releases/download/3.0.6/glpi-resources-3.0.6.tar.bz2",
                    "stability": "stable"
                },
                "3": {
                    "num": "3.0.5",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/resources/releases/download/3.0.5/glpi-resources-3.0.5.tar.bz2",
                    "stability": "stable"
                },
                "4": {
                    "num": "3.0.4",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/resources/releases/download/3.0.4/glpi-resources-3.0.4.tar.bz2",
                    "stability": "stable"
                },
                "5": {
                    "num": "3.0.3",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/resources/releases/download/3.0.3/glpi-resources-3.0.3.tar.bz2",
                    "stability": "stable"
                },
                "6": {
                    "num": "3.0.2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/resources/releases/download/3.0.2/glpi-resources-3.0.2.tar.bz2",
                    "stability": "stable"
                },
                "7": {
                    "num": "3.0.1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/resources/releases/download/3.0.1/glpi-resources-3.0.1.tar.bz2",
                    "stability": "stable"
                },
                "10": {
                    "num": "3.0.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/resources/releases/download/3.0.0/glpi-resources-3.0.0.tar.bz2",
                    "stability": "stable"
                },
                "8": {
                    "num": "3.0.0-rc2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/resources/releases/download/3.0.0-rc2/glpi-resources-3.0.0-rc2.tar.bz2",
                    "stability": "RC"
                },
                "9": {
                    "num": "3.0.0-rc1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/resources/releases/download/3.0.0-rc1/glpi-resources-3.0.0-rc1.tar.bz2",
                    "stability": "RC"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Gestion de ressources humaines. Ce plugin vous permet de gérer les ressources humaines afin de gérer correctement l&#039;attribution de matériel.<br />- Gestion des divers modes de fonctionnement (privé, public, SSII)<br />- Gestion de checklists / tâches<br />- Système de notifications<br />- Utilisable depuis le helpdesk",
                    "long_description": "Ce plugin vous permet de gérer les ressources humaines afin de gérer correctement l&#039;attribution de matériel.<br />- Gestion des divers modes de fonctionnement (privé, public, SSII)<br />Fonctionnalités : <br />- Gestion de checklists<br />- Gestion de tâches<br />- Système de notifications<br />- Utilisable avec le plugin badges<br />- Utilisable depuis le helpdesk<br />- Utilisable avec le plugin PDF"
                },
                {
                    "lang": "en",
                    "short_description": "Resources management. This plugin allows you to manage human resources to properly manage the allocation of material.<br />- Management of various modes (private, public, SSII)<br />- Checklists / Tasks management<br />- Notifications system<br />- Can be used with helpdesk",
                    "long_description": "This plugin allows you to manage human resources to properly manage the allocation of material.<br />- Management of various modes (private, public, SSII)<br />Features : <br />- Checklists management<br />- Tasks management<br />- Notifications system<br />- Can be used with helpdesk<br />- Can be used with badges plugin<br />- Can be used with PDF plugin"
                }
            ],
            "required_offers": None,
            "short_description": "Resources management. This plugin allows you to manage human resources to properly manage the allocation of material.<br />- Management of various modes (private, public, SSII)<br />- Checklists / Tasks management<br />- Notifications system<br />- Can be used with helpdesk"
        },
        {
            "id": 31,
            "key": "webapplications",
            "name": "Appliances Dashboard",
            "logo_url": "https://raw.githubusercontent.com/InfotelGLPI/webapplications/master/webapplications.png",
            "xml_url": "https://raw.githubusercontent.com/InfotelGLPI/webapplications/master/webapplications.xml",
            "homepage_url": "https://github.com/InfotelGLPI/webapplications",
            "download_url": "https://github.com/InfotelGLPI/webapplications/releases",
            "issues_url": "https://github.com/InfotelGLPI/webapplications/issues",
            "readme_url": "https://github.com/InfotelGLPI/webapplications/blob/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2009-08-09T00:00:00.000000Z",
            "date_updated": "2024-11-24T00:00:00.000000Z",
            "download_count": 30728,
            "note": 3.2142857142857144,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                },
                {
                    "id": 49,
                    "name": "Infotel"
                }
            ],
            "versions": [
                {
                    "num": "5.0.2",
                    "compatibility": "~10.0.11",
                    "download_url": "https://github.com/InfotelGLPI/webapplications/releases/download/5.0.2/glpi-webapplications-5.0.2.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "5.0.1",
                    "compatibility": "~10.0.11",
                    "download_url": "https://github.com/InfotelGLPI/webapplications/releases/download/5.0.1/glpi-webapplications-5.0.1.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "5.0.0",
                    "compatibility": "~10.0.11",
                    "download_url": "https://github.com/InfotelGLPI/webapplications/releases/download/5.0.0/glpi-webapplications-5.0.0.tar.bz2",
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Dashboard applicatif. Ce plugin vous permet d&#039;afficher sous forme de dashboard, vos applicatifs métiers avec l&#039;ensemble de leurs caractéristiques",
                    "long_description": "Dashboard applicatif. Ce plugin vous permet d&#039;afficher sous forme de dashboard, vos applicatifs métiers avec l&#039;ensemble de leurs caractéristiques"
                },
                {
                    "lang": "en",
                    "short_description": "Appliance dashboard. This plugin allows you to display your business applications with all their characteristics in the form of a dashboard.",
                    "long_description": "Appliance dashboard. This plugin allows you to display your business applications with all their characteristics in the form of a dashboard."
                }
            ],
            "required_offers": None,
            "short_description": "Appliance dashboard. This plugin allows you to display your business applications with all their characteristics in the form of a dashboard."
        },
        {
            "id": 34,
            "key": "treeview",
            "name": "Tree View",
            "logo_url": "https://github.com/pluginsGLPI/treeview/blob/main/treeview.png?raw=true",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/treeview/main/treeview.xml",
            "homepage_url": "https://github.com/pluginsGLPI/treeview",
            "download_url": "https://github.com/pluginsGLPI/treeview/releases",
            "issues_url": "https://github.com/pluginsGLPI/treeview/issues",
            "readme_url": "https://github.com/pluginsGLPI/treeview/wiki",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2009-08-09T00:00:00.000000Z",
            "date_updated": "2024-02-08T00:00:00.000000Z",
            "download_count": 37702,
            "note": 4.166666666666667,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                },
                {
                    "id": 13,
                    "name": "Hussein AL-Rubeiy"
                },
                {
                    "id": 6,
                    "name": "Nelly Mahu-Lasson"
                },
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": {
                "3": {
                    "num": "1.10.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/treeview/releases/download/1.10.2/glpi-treeview-1.10.2.tar.bz2",
                    "stability": "stable"
                },
                "4": {
                    "num": "1.10.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/treeview/releases/download/1.10.1/glpi-treeview-1.10.1.tar.bz2",
                    "stability": "stable"
                },
                "5": {
                    "num": "1.10.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/treeview/releases/download/1.10.0/glpi-treeview-1.10.0.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Vue en arborescence. Ce plugin vous permet de voir votre parc GLPI sous forme d’arborescence.",
                    "long_description": "Ce plugin vous permet de voir votre parc GLPI sous forme d’arborescence.<br />-Possibilité d&#039;utiliser les répertoires des lieux sous forme de liens<br />-Les noeuds peuvent être en surbrillance.<br />-L&#039;arborescence peut être dessinée avec des lignes ou des icônes.<br />-Possibilité de lancement du plugin au démarrage de GLPI"
                },
                {
                    "lang": "en",
                    "short_description": "Tree view. This plugin allows you to see your asset with tree view.",
                    "long_description": "This plugin allows you to see your asset with tree view.<br />-Should folders be links<br />-Nodes can be highlighted.<br />-Tree can be drawn with lines or pics.<br />-The plugin can be launched when GLPI loading"
                }
            ],
            "required_offers": None,
            "short_description": "Tree view. This plugin allows you to see your asset with tree view."
        },
        {
            "id": 35,
            "key": "centreon",
            "name": "centreon",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/centreon/main/docs/logo.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/centreon/main/centreon.xml",
            "homepage_url": "https://github.com/pluginsGLPI/centreon",
            "download_url": "https://github.com/pluginsGLPI/centreon/releases",
            "issues_url": "https://github.com/pluginsGLPI/centreon/issues",
            "readme_url": "https://github.com/pluginsGLPI/centreon/blob/main/README.md",
            "changelog_url": "",
            "license": "GPL V3+",
            "date_added": "2009-08-09T00:00:00.000000Z",
            "date_updated": "2025-01-08T00:00:00.000000Z",
            "download_count": 5580,
            "note": 3.625,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": [
                {
                    "num": "1.0.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/centreon/releases/download/1.0.2/glpi-centreon-1.0.2.tar.bz2",
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Centreon GLPI plugin",
                    "long_description": "This plugin allows displaying in the GLPI interface the general information of a machine that is also monitored in Centreon.\n         It is also possible to view the status of its services, its history, and to perform common actions such as checks, downtime, and acknowledgements.\n         "
                },
                {
                    "lang": "fr",
                    "short_description": "Plugin GLPI Centreon",
                    "long_description": "Ce plugin permet d&#039;afficher dans l&#039;interface GLPI les informations générales d&#039;une machine qui est également monitorée dans Centreon.\n         Il est également possible de consulter l&#039;état de ses services, son historique et d&#039;effectuer des actions courantes telles que les &#34;checks&#34;, les &#34;downtimes&#34; et les &#34;acknowledgements&#34;.\n         "
                }
            ],
            "required_offers": None,
            "short_description": "Centreon GLPI plugin"
        },
        {
            "id": 38,
            "key": "pdf",
            "name": "PDF",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/pdf/master/pdf.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/pdf/refs/heads/main/pdf.xml",
            "homepage_url": "https://github.com/pluginsGLPI/pdf",
            "download_url": "https://github.com/pluginsGLPI/pdf/releases",
            "issues_url": None,
            "readme_url": None,
            "changelog_url": "",
            "license": "AGPLv3",
            "date_added": "2009-08-12T00:00:00.000000Z",
            "date_updated": "2025-03-10T00:00:00.000000Z",
            "download_count": 115246,
            "note": 3.477777777777778,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 44,
                    "name": "Teclib"
                },
                {
                    "id": 5,
                    "name": "Remi Collet"
                },
                {
                    "id": 6,
                    "name": "Nelly Mahu-Lasson"
                }
            ],
            "versions": {
                "1": {
                    "num": "4.0.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/pdf/releases/download/4.0.1/glpi-pdf-4.0.1.tar.bz2",
                    "stability": "stable"
                },
                "2": {
                    "num": "4.0.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/pdf/releases/download/4.0.0/glpi-pdf-4.0.0.tar.bz2",
                    "stability": "stable"
                },
                "0": {
                    "num": "3.0.0",
                    "compatibility": "~10.0.3",
                    "download_url": "https://github.com/yllen/pdf/releases/download/v3.0.0/glpi-pdf-3.0.0.tar.gz",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Ce plugin vous permet d’exporter en PDF la fiche d&#039;un élément de \n\tl&#039;inventaire.\n\t",
                    "long_description": "Ce plugin vous permet d’exporter en pdf la fiche d&#039;un élément de \n\tl&#039;inventaire.\n\t<br />- types d&#039;équipement de GLPI\n        <br />- types d&#039;équipement de certains plugins\n        <br />- données additionnelles de certains plugins\n    \t<br />- un seul ou plusieurs objet(s) dans un fichier\n\t"
                },
                {
                    "lang": "en",
                    "short_description": "This plugin allow you to select and export informations of an \n\tequipment to PDF file.\n\t",
                    "long_description": "This plugin allow you to select and export informations of an \n\tequipment to PDF file.\n    \t<br />- equipment types from GLPI\n    \t<br />- equipment types from some plugins\n    \t<br />- additional data from some plugins\n    \t<br />- one or many object(s) in a file\n\t"
                }
            ],
            "required_offers": None,
            "short_description": "This plugin allow you to select and export informations of an \n\tequipment to PDF file.\n\t"
        },
        {
            "id": 39,
            "key": "datainjection",
            "name": "Data Injection",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/datainjection/main/datainjection.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/datainjection/main/datainjection.xml",
            "homepage_url": "http://plugins.glpi-project.org/#/plugin/datainjection",
            "download_url": "https://github.com/pluginsGLPI/datainjection/releases",
            "issues_url": "https://github.com/pluginsGLPI/datainjection/issues",
            "readme_url": "https://glpi-plugins.readthedocs.io/en/latest/datainjection/index.html",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2009-08-24T00:00:00.000000Z",
            "date_updated": "2024-12-27T00:00:00.000000Z",
            "download_count": 147138,
            "note": 3.3472222222222223,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 14,
                    "name": "Walid Nouh"
                },
                {
                    "id": 15,
                    "name": "Dévi Balpe"
                },
                {
                    "id": 5,
                    "name": "Remi Collet"
                },
                {
                    "id": 6,
                    "name": "Nelly Mahu-Lasson"
                },
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                }
            ],
            "versions": {
                "8": {
                    "num": "2.14.1",
                    "compatibility": "~10.0.11",
                    "download_url": "https://github.com/pluginsGLPI/datainjection/releases/download/2.14.1/glpi-datainjection-2.14.1.tar.bz2",
                    "stability": "stable"
                },
                "9": {
                    "num": "2.14.0",
                    "compatibility": "~10.0.11",
                    "download_url": "https://github.com/pluginsGLPI/datainjection/releases/download/2.14.0/glpi-datainjection-2.14.0.tar.bz2",
                    "stability": "stable"
                },
                "10": {
                    "num": "2.13.5",
                    "compatibility": "~10.0.11",
                    "download_url": "https://github.com/pluginsGLPI/datainjection/releases/download/2.13.5/glpi-datainjection-2.13.5.tar.bz2",
                    "stability": "stable"
                },
                "11": {
                    "num": "2.13.4",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/datainjection/releases/download/2.13.4/glpi-datainjection-2.13.4.tar.bz2",
                    "stability": "stable"
                },
                "12": {
                    "num": "2.13.3",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/datainjection/releases/download/2.13.3/glpi-datainjection-2.13.3.tar.bz2",
                    "stability": "stable"
                },
                "13": {
                    "num": "2.13.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/datainjection/releases/download/2.13.2/glpi-datainjection-2.13.2.tar.bz2",
                    "stability": "stable"
                },
                "14": {
                    "num": "2.13.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/datainjection/releases/download/2.13.1/glpi-datainjection-2.13.1.tar.bz2",
                    "stability": "stable"
                },
                "15": {
                    "num": "2.13.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/datainjection/releases/download/2.13.0/glpi-datainjection-2.13.0.tar.bz2",
                    "stability": "stable"
                },
                "16": {
                    "num": "2.12.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/datainjection/releases/download/2.12.1/glpi-datainjection-2.12.1.tar.bz2",
                    "stability": "stable"
                },
                "17": {
                    "num": "2.12.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/datainjection/releases/download/2.12.0/glpi-datainjection-2.12.0.tar.bz2",
                    "stability": "stable"
                },
                "18": {
                    "num": "2.11.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/datainjection/releases/download/2.11.2/glpi-datainjection-2.11.2.tar.bz2",
                    "stability": "stable"
                },
                "19": {
                    "num": "2.11.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/datainjection/releases/download/2.11.1/glpi-datainjection-2.11.1.tar.bz2",
                    "stability": "stable"
                },
                "20": {
                    "num": "2.11.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/datainjection/releases/download/2.11.0/glpi-datainjection-2.11.0.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "cs",
                    "short_description": "Tento zásuvný modul umožňuje importovat do GLPI data z CSV souborů.",
                    "long_description": "Umožňuje vytváření modelů importu pro budoucí opětovné využití. Byl vytvořen pro:<br /> - import dat pocházejících z jiných softwarů pro správu majetku<br /> - import formulářů elektronického doručení<br />Data k importu pomocí tohoto zásuvného modulu jsou:<br /> - data inventáře (s výjimkou software a licencí)<br /> - správní data (smlouvy, kontakty, dodavatelé)<br /> - data nastavení (uživatel, skupina, entita)"
                },
                {
                    "lang": "en",
                    "short_description": "This plugin allows data import into GLPI using CSV files.",
                    "long_description": "It allows to create models of injection for a future re-use. It&#039;s been created in order to:<br /> - import data coming from others asset management softwares<br /> - inject electronic delivery forms<br />Data to be imported using the plugin are:<br /> - inventory data (except softwares and licenses)<br /> - management data (contract, contact, supplier)<br /> - configuration data (user, group, entity)"
                },
                {
                    "lang": "fr",
                    "short_description": "Cette extension permet l&#039;import de données dans GLPI à l&#039;aide de fichiers CSV.",
                    "long_description": "Elle permet de créer des modèles d’injection pour une réutilisation future et a été créée afin de répondre aux besoins suivants :<br /> - reprise des données d&#039;autres outils d&#039;inventaires<br /> - injection de bons de livraisons électroniques<br />Les données pouvant-être injectées sont :<br /> - données d&#039;inventaires (sauf logiciels et licences)<br /> - données de gestion (contrat, contact, fournisseur)<br /> - données de configuration (utilisateur, groupe, entité)"
                }
            ],
            "required_offers": None,
            "short_description": "This plugin allows data import into GLPI using CSV files."
        },
        {
            "id": 40,
            "key": "genericobject",
            "name": "Generic Objects Management",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/genericobject/main/genericobject.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/genericobject/main/genericobject.xml",
            "homepage_url": "https://github.com/pluginsGLPI/genericobject",
            "download_url": "https://github.com/pluginsGLPI/genericobject/releases",
            "issues_url": "https://github.com/pluginsGLPI/genericobject/issues",
            "readme_url": "https://glpi-plugins.readthedocs.io/en/latest/genericobject/index.html",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2009-08-24T00:00:00.000000Z",
            "date_updated": "2024-12-27T00:00:00.000000Z",
            "download_count": 94445,
            "note": 2.801694915254237,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 14,
                    "name": "Walid Nouh"
                }
            ],
            "versions": {
                "17": {
                    "num": "2.14.11",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/genericobject/releases/download/2.14.11/glpi-genericobject-2.14.11.tar.bz2",
                    "stability": "stable"
                },
                "18": {
                    "num": "2.14.10",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/genericobject/releases/download/2.14.10/glpi-genericobject-2.14.10.tar.bz2",
                    "stability": "stable"
                },
                "9": {
                    "num": "2.14.9",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/genericobject/releases/download/2.14.9/glpi-genericobject-2.14.9.tar.bz2",
                    "stability": "stable"
                },
                "10": {
                    "num": "2.14.8",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/genericobject/releases/download/2.14.8/glpi-genericobject-2.14.8.tar.bz2",
                    "stability": "stable"
                },
                "11": {
                    "num": "2.14.7",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/genericobject/releases/download/2.14.7/glpi-genericobject-2.14.7.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Faites l&#039;inventaire de nouveaux types d&#039;objets",
                    "long_description": "Ce plugin vous permet de faire l&#039;inventaire de nouveaux types d&#039;objets génériques, sans avoir à programmer. Generic Objects vous permet de créer ces nouveaux types, les champs disponibles pour ces types. Il est intégré à GLPi dans ses fonctionnalités mère (Helpdesk, réservation, gabarits, etc.). Generic Objects est compatible avec le plugin File Injection permettant l&#039;injection des données."
                },
                {
                    "lang": "en",
                    "short_description": "Do the inventory of new, non-native object types",
                    "long_description": "This plugin allows you to do the inventory of new item types without having to code, it allows you to create those new item types, it allows type creation, manages available fields. Has full integration with the software (Helpdesk, loans, templates, etc.) It has support and connectivity for and with the File Injection plugin"
                },
                {
                    "lang": "cs",
                    "short_description": "Inventarizace nových, nenativních typů objektů",
                    "long_description": "Tento zásuvný modul umožňuje inventarizovat nové typy položek, aniž by bylo třeba programovat. Umožňuje vytvářet tyto nové typy položek, typů a spravovat kolonky, které budou k dispozici. Je plně začleněný do software (Služba podpory, zápůjčky, šablony, atd.) Má podporu a propojení pro a se zásuvným modulem Vkládání dat ze souboru"
                }
            ],
            "required_offers": None,
            "short_description": "Do the inventory of new, non-native object types"
        },
        {
            "id": 41,
            "key": "order",
            "name": "Order Management",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/order/main/order.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/order/main/plugin.xml",
            "homepage_url": "https://github.com/pluginsGLPI/order/",
            "download_url": "https://github.com/pluginsGLPI/order/releases",
            "issues_url": "https://github.com/pluginsGLPI/order/issues",
            "readme_url": "https://glpi-plugins.readthedocs.io/en/latest/order/index.html",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2009-08-24T00:00:00.000000Z",
            "date_updated": "2024-03-08T00:00:00.000000Z",
            "download_count": 60235,
            "note": 3.206896551724138,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 14,
                    "name": "Walid Nouh"
                },
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                },
                {
                    "id": 16,
                    "name": "François Legastelois"
                },
                {
                    "id": 17,
                    "name": "Benjamin Fontan"
                }
            ],
            "versions": {
                "18": {
                    "num": "2.10.6",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/order/releases/download/2.10.6/glpi-order-2.10.6.tar.bz2",
                    "stability": "stable"
                },
                "19": {
                    "num": "2.10.5",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/order/releases/download/2.10.5/glpi-order-2.10.5.tar.bz2",
                    "stability": "stable"
                },
                "20": {
                    "num": "2.10.4",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/order/releases/download/2.10.4/glpi-order-2.10.4.tar.bz2",
                    "stability": "stable"
                },
                "21": {
                    "num": "2.10.3",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/order/releases/download/2.10.3/glpi-order-2.10.3.tar.bz2",
                    "stability": "stable"
                },
                "22": {
                    "num": "2.10.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/order/releases/download/2.10.2/glpi-order-2.10.2.tar.bz2",
                    "stability": "stable"
                },
                "23": {
                    "num": "2.10.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/order/releases/download/2.10.1/glpi-order-2.10.1.tar.bz2",
                    "stability": "stable"
                },
                "24": {
                    "num": "2.10.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/order/releases/download/2.10.0/glpi-order-2.10.0.tar.bz2",
                    "stability": "stable"
                },
                "14": {
                    "num": "2.9.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/order/releases/download/2.9.0/glpi-order-2.9.0.tar.bz2",
                    "stability": "stable"
                },
                "15": {
                    "num": "2.8.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/order/releases/download/2.8.2/glpi-order-2.8.2.tar.bz2",
                    "stability": "stable"
                },
                "16": {
                    "num": "2.8.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/order/releases/download/2.8.1/glpi-order-2.8.1.tar.bz2",
                    "stability": "stable"
                },
                "17": {
                    "num": "2.8.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/order/releases/download/2.8.0/glpi-order-2.8.0.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Gestion des commandes de matériels",
                    "long_description": "Cette extension vous permet de gérer le processus de commande de matériels à l&#039;intérieur de GLPI :<br /> - Gestion des références produits<br /> - Gestion des commandes (avec workflow de soumission)<br /> - Gestion des budgets"
                },
                {
                    "lang": "en",
                    "short_description": "Order management",
                    "long_description": "This plugin allows you to manage order management within GLPI :<br /> - Products references management<br /> - Order management (with approval workflow)<br /> - Budgets management"
                },
                {
                    "lang": "de",
                    "short_description": "Bestellverwaltung",
                    "long_description": "Dieses Plugin ergänzt GLPI mit einer Bestellverwaltung:<br /> - Verwaltung der Produktreferenzen<br /> - Bestellverwaltung mit Freigabeprozedur<br /> - Budgetverwaltung"
                },
                {
                    "lang": "cs",
                    "short_description": "Správa objednávek",
                    "long_description": "Tento zásuvný modul umožňuje spravovat objednávky pomocí GLPI :<br /> - Správa odkazů na produkty<br /> - Správa objednávek (s procesem schvalování)<br /> - Správa rozpočtů"
                }
            ],
            "required_offers": None,
            "short_description": "Order management"
        },
        {
            "id": 42,
            "key": "uninstall",
            "name": "Uninstall",
            "logo_url": "https://raw.githubusercontent.com/pluginsglpi/uninstall/main/uninstall.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/uninstall/main/uninstall.xml",
            "homepage_url": "https://github.com/pluginsglpi/uninstall",
            "download_url": "https://github.com/pluginsglpi/uninstall/releases",
            "issues_url": "https://github.com/pluginsglpi/uninstall/issues",
            "readme_url": "https://glpi-plugins.readthedocs.io/en/latest/uninstall/index.html",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2009-08-24T00:00:00.000000Z",
            "date_updated": "2024-06-10T00:00:00.000000Z",
            "download_count": 21076,
            "note": 2.7976190476190474,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 14,
                    "name": "Walid Nouh"
                },
                {
                    "id": 16,
                    "name": "François Legastelois"
                },
                {
                    "id": 5,
                    "name": "Remi Collet"
                }
            ],
            "versions": {
                "5": {
                    "num": "2.9.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/uninstall/releases/download/2.9.2/glpi-uninstall-2.9.2.tar.bz2",
                    "stability": "stable"
                },
                "6": {
                    "num": "2.9.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/uninstall/releases/download/2.9.1/glpi-uninstall-2.9.1.tar.bz2",
                    "stability": "stable"
                },
                "7": {
                    "num": "2.9.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/uninstall/releases/download/2.9.0/glpi-uninstall-2.9.0.tar.bz2",
                    "stability": "stable"
                },
                "8": {
                    "num": "2.8.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/uninstall/releases/download/2.8.1/glpi-uninstall-2.8.1.tar.bz2",
                    "stability": "stable"
                },
                "9": {
                    "num": "2.8.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/uninstall/releases/download/2.8.0/glpi-uninstall-2.8.0.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Désinstallez facilement les objets obsolètes de votre inventaire",
                    "long_description": "Ce plugin vous permet de classer ou supprimer facilement et proprement les objets en fin de vie de votre parc"
                },
                {
                    "lang": "en",
                    "short_description": "Easy uninstall of obsolete assets in your inventory",
                    "long_description": "This plugin let you to archive easily assets which reached their end of life"
                },
                {
                    "lang": "cs",
                    "short_description": "Snadná odinstalace zastaralého majetku z inventáře",
                    "long_description": "Tento zásuvný modul umožňuje snadno zaarchivovat záznamy zařízení, kterým už skončila životnost"
                }
            ],
            "required_offers": None,
            "short_description": "Easy uninstall of obsolete assets in your inventory"
        },
        {
            "id": 43,
            "key": "geninventorynumber",
            "name": "Inventory Number Generation",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/geninventorynumber/main/geninventorynumber.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/geninventorynumber/main/plugin.xml",
            "homepage_url": "https://github.com/pluginsGLPI/geninventorynumber",
            "download_url": "https://github.com/pluginsGLPI/geninventorynumber/releases",
            "issues_url": "https://github.com/pluginsGLPI/geninventorynumber/issues",
            "readme_url": "https://raw.githubusercontent.com/pluginsGLPI/geninventorynumber/main/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2009-08-24T00:00:00.000000Z",
            "date_updated": "2024-11-08T00:00:00.000000Z",
            "download_count": 30868,
            "note": 3.4324324324324325,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 14,
                    "name": "Walid Nouh"
                }
            ],
            "versions": {
                "2": {
                    "num": "2.8.6",
                    "compatibility": "~10.0.11",
                    "download_url": "https://github.com/pluginsGLPI/geninventorynumber/releases/download/2.8.6/glpi-geninventorynumber-2.8.6.tar.bz2",
                    "stability": "stable"
                },
                "3": {
                    "num": "2.8.5",
                    "compatibility": "~10.0.11",
                    "download_url": "https://github.com/pluginsGLPI/geninventorynumber/releases/download/2.8.5/glpi-geninventorynumber-2.8.5.tar.bz2",
                    "stability": "stable"
                },
                "4": {
                    "num": "2.8.4",
                    "compatibility": "~10.0.11",
                    "download_url": "https://github.com/pluginsGLPI/geninventorynumber/releases/download/2.8.4/glpi-geninventorynumber-2.8.4.tar.bz2",
                    "stability": "stable"
                },
                "5": {
                    "num": "2.8.3",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/geninventorynumber/releases/download/2.8.3/glpi-geninventorynumber-2.8.3.tar.bz2",
                    "stability": "stable"
                },
                "6": {
                    "num": "2.8.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/geninventorynumber/releases/download/2.8.2/glpi-geninventorynumber-2.8.2.tar.bz2",
                    "stability": "stable"
                },
                "7": {
                    "num": "2.8.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/geninventorynumber/releases/download/2.8.1/glpi-geninventorynumber-2.8.1.tar.bz2",
                    "stability": "stable"
                },
                "8": {
                    "num": "2.8.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/geninventorynumber/releases/download/2.8.0/glpi-geninventorynumber-2.8.0.tar.bz2",
                    "stability": "stable"
                },
                "9": {
                    "num": "2.7.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/geninventorynumber/releases/download/2.7.0/glpi-geninventorynumber-2.7.0.tar.bz2",
                    "stability": "stable"
                },
                "10": {
                    "num": "2.6.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/geninventorynumber/releases/download/2.6.0/glpi-geninventorynumber-2.6.0.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "cs",
                    "short_description": "Vytváření inventárních čísel",
                    "long_description": "Tento zásuvný modul umožňuje vytvářet inventární čísla. Nastavení umožňuje určit:<br /> - Typy pro které je automatické vytváření zapnuté<br /> - Šablony inventárních čísel<br /> - Zda jsou čítače globální nebo jen pro určitý typ"
                },
                {
                    "lang": "fr",
                    "short_description": "Génération de numéros d&#039;inventaire",
                    "long_description": "Cette extention vous permet de générer automatiquement un numéro d’inventaire. La configuration donne la possibilité de définir :<br /> - Les types qui nécessitent cette automatisation<br /> - Les modèles de numéros à générer<br /> - Si les compteurs sont globaux ou spécifiques pour chaque type"
                },
                {
                    "lang": "en",
                    "short_description": "Inventory numbers generation",
                    "long_description": "This plugin enables inventory numbers automatic generation. The configuration allows you to define :<br /> - The types for which automatic generation is enabled<br /> - Inventory number templates<br /> - If counters are globals or type specific"
                }
            ],
            "required_offers": None,
            "short_description": "Inventory numbers generation"
        },
        {
            "id": 48,
            "key": "connections",
            "name": "Connections",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/connections/master/pics/icon.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/connections/master/connections.xml",
            "homepage_url": "https://github.com/pluginsGLPI/connections",
            "download_url": "https://github.com/pluginsGLPI/connections/releases",
            "issues_url": "https://github.com/pluginsGLPI/connections/issues",
            "readme_url": "https://github.com/pluginsGLPI/connections/blob/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2009-10-18T00:00:00.000000Z",
            "date_updated": "2022-08-28T00:00:00.000000Z",
            "download_count": 11457,
            "note": 3.2142857142857144,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 69,
                    "name": "Jean Marc GRISARD"
                },
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                },
                {
                    "id": 18,
                    "name": "Damien BARON"
                },
                {
                    "id": 48,
                    "name": "Emmanuel HAGUET"
                },
                {
                    "id": 65,
                    "name": "Jérémy Moreau"
                }
            ],
            "versions": {
                "1": {
                    "num": "10.0.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/connections/releases/download/10.0.0/glpi-connections-10.0.0.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "This plugin allows you to manage the connections of your network and associate them with elements of the inventory.",
                    "long_description": "This plugin allows you to manage the connections of your network and associate them with elements of the inventory."
                },
                {
                    "lang": "fr",
                    "short_description": "Ce plugin vous permet de gérer les liaisons de votre réseau et de les associer à des éléments de l&#039;inventaire.",
                    "long_description": "Ce plugin vous permet de gérer les liaisons de votre réseau et de les associer à des éléments de l&#039;inventaire."
                }
            ],
            "required_offers": None,
            "short_description": "This plugin allows you to manage the connections of your network and associate them with elements of the inventory."
        },
        {
            "id": 63,
            "key": "behaviors",
            "name": "Behaviors",
            "logo_url": "https://raw.githubusercontent.com/yllen/behaviors/master/behaviors.png",
            "xml_url": "https://raw.githubusercontent.com/yllen/behaviors/master/behaviors.xml",
            "homepage_url": "https://github.com/yllen/behaviors",
            "download_url": "https://github.com/yllen/behaviors/releases",
            "issues_url": None,
            "readme_url": None,
            "changelog_url": "",
            "license": "AGPL v3+",
            "date_added": "2011-05-25T00:00:00.000000Z",
            "date_updated": "2024-03-12T00:00:00.000000Z",
            "download_count": 64358,
            "note": 3.5052083333333335,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 5,
                    "name": "Remi Collet"
                },
                {
                    "id": 6,
                    "name": "Nelly Mahu-Lasson"
                }
            ],
            "versions": [
                {
                    "num": "2.7.3",
                    "compatibility": "~10.0.5",
                    "download_url": "https://github.com/yllen/behaviors/releases/download/v2.7.3/glpi-behaviors-2.7.3.tar.gz",
                    "stability": "stable"
                },
                {
                    "num": "2.7.2",
                    "compatibility": "~10.0.3",
                    "download_url": "https://github.com/yllen/behaviors/releases/download/v2.7.2/glpi-behaviors-2.7.2.tar.gz",
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Cette extension permet d&#039;ajouter des comportements optionnels à GLPI.",
                    "long_description": "Cette extension permet d&#039;ajouter des comportements optionnels à GLPI.\n        <br />- champs obligatoires\n        <br />- groupe du demandeur\n        <br />- format des numéros de tickets\n        <br />- nouveaux évènements dans les notifications\n   "
                },
                {
                    "lang": "en",
                    "short_description": "This plugin allows you to add optional behaviors to GLPI.",
                    "long_description": "This plugin allows you to add optional behaviors to GLPI.\n      <br />- mandatory fields\n      <br />- requester&#039;s group\n      <br />- ticket&#039;s number format\n      <br />- new events in notifications \n   "
                }
            ],
            "required_offers": None,
            "short_description": "This plugin allows you to add optional behaviors to GLPI."
        },
        {
            "id": 66,
            "key": "barcode",
            "name": "Barcode",
            "logo_url": "https://github.com/pluginsGLPI/barcode/blob/master/barscode.png?raw=true",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/barcode/master/barcode.xml",
            "homepage_url": "https://github.com/pluginsGLPI/barcode",
            "download_url": "https://github.com/pluginsGLPI/barcode/releases",
            "issues_url": None,
            "readme_url": None,
            "changelog_url": "",
            "license": "AGPL v3+",
            "date_added": "2011-11-22T00:00:00.000000Z",
            "date_updated": "2022-07-18T00:00:00.000000Z",
            "download_count": 53343,
            "note": 3.1762295081967213,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 8,
                    "name": "David Durieux"
                }
            ],
            "versions": {
                "6": {
                    "num": "2.7.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/barcode/releases/download/2.7.1/glpi-barcode-2.7.1.tar.bz2",
                    "stability": "stable"
                },
                "7": {
                    "num": "2.7.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/barcode/releases/download/2.7.0/glpi-barcode-2.7.0.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Ce plugin vous permet de générer des codes barre",
                    "long_description": "Ce plugin vous permet de générer et d&#039;export en PDF des codes barre et QRcode"
                },
                {
                    "lang": "en",
                    "short_description": "This plugin allow you to generate bars code",
                    "long_description": "This plugin allow you to generate and export in PDF bars code and QRcode"
                },
                {
                    "lang": "cs",
                    "short_description": "Tento zásuvný modul umožňuje vytvářet čárové kódy",
                    "long_description": "Tento zásuvný modul umožňuje vytvářet a exportovat do PDF čárové a QR kódy"
                }
            ],
            "required_offers": None,
            "short_description": "This plugin allow you to generate bars code"
        },
        {
            "id": 68,
            "key": "formcreator",
            "name": "FormCreator",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/formcreator/master/icon.png",
            "xml_url": "https://raw.githubusercontent.com/TECLIB/formcreator/master/plugin.xml",
            "homepage_url": "https://pluginsglpi.github.io/formcreator/",
            "download_url": "https://github.com/pluginsGLPI/formcreator/releases",
            "issues_url": "https://github.com/pluginsGLPI/formcreator/issues",
            "readme_url": "https://glpi-plugins.readthedocs.io/en/latest/formcreator/index.html",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2012-08-29T00:00:00.000000Z",
            "date_updated": "2025-02-27T00:00:00.000000Z",
            "download_count": 131918,
            "note": 3.474910394265233,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": {
                "17": {
                    "num": "2.13.10",
                    "compatibility": "~10.0.10",
                    "download_url": "https://github.com/pluginsGLPI/formcreator/releases/download/2.13.10/glpi-formcreator-2.13.10.tar.bz2",
                    "stability": "stable"
                },
                "15": {
                    "num": "2.13.9",
                    "compatibility": "~10.0.10",
                    "download_url": "https://github.com/pluginsGLPI/formcreator/releases/download/2.13.9/glpi-formcreator-2.13.9.tar.bz2",
                    "stability": "stable"
                },
                "16": {
                    "num": "2.13.8",
                    "compatibility": "~10.0.10",
                    "download_url": "https://github.com/pluginsGLPI/formcreator/releases/download/2.13.8/glpi-formcreator-2.13.8.tar.bz2",
                    "stability": "stable"
                },
                "13": {
                    "num": "2.13.7",
                    "compatibility": "~10.0.9",
                    "download_url": "https://github.com/pluginsGLPI/formcreator/releases/download/2.13.7/glpi-formcreator-2.13.7.tar.bz2",
                    "stability": "stable"
                },
                "14": {
                    "num": "2.13.6",
                    "compatibility": "~10.0.7",
                    "download_url": "https://github.com/pluginsGLPI/formcreator/releases/download/2.13.6/glpi-formcreator-2.13.6.tar.bz2",
                    "stability": "stable"
                },
                "18": {
                    "num": "2.13.5",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/formcreator/releases/download/2.13.5/glpi-formcreator-2.13.5.tar.bz2",
                    "stability": "stable"
                },
                "19": {
                    "num": "2.13.4",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/formcreator/releases/download/2.13.4/glpi-formcreator-2.13.4.tar.bz2",
                    "stability": "stable"
                },
                "20": {
                    "num": "2.13.3",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/formcreator/releases/download/2.13.3/glpi-formcreator-2.13.3.tar.bz2",
                    "stability": "stable"
                },
                "21": {
                    "num": "2.13.2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/formcreator/releases/download/2.13.2/glpi-formcreator-2.13.2.tar.bz2",
                    "stability": "stable"
                },
                "22": {
                    "num": "2.13.1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/formcreator/releases/download/2.13.1/glpi-formcreator-2.13.1.tar.bz2",
                    "stability": "stable"
                },
                "23": {
                    "num": "2.13.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/formcreator/releases/download/2.13.0/glpi-formcreator-2.13.0.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Formcreator est un plugin permettant la création de formulaires personnalisés simples d&#039;accès aux utilisateurs aboutissant à la création d&#039;un ou plusieurs tickets ou changements.",
                    "long_description": "\nFormcreator est un plugin permettant la création de formulaires personnalisés simples d&#039;accès aux utilisateurs aboutissant à la création d&#039;un ou plusieurs tickets ou changements.\n\nFonctionnalités\n---------------\n\n1. Accès par menu direct en interface self-service\n2. Mise en avant de formulaires en pages d&#039;accueil\n3. Accès des formulaires contrôlés : accès public, accès utilisateurs identifiés, accès restreint à certains profils\n4. Des formulaires simples et personnalisables\n5. Des formulaires organisés par catégories, par entités et par langues.\n6. Des questions ouvertes ou fermées, de tout type de présentation : Champs textes, listes, LDAP, fichiers, etc.\n7. Organisation des questions par sections. Choix de l&#039;ordre d&#039;affichage.\n8. Possibilité de n&#039;afficher une question que selon certains critères (réponse à une autre question)\n9. Un contrôle pointu sur les réponses de formulaires : Texte, nombres, taille des champs, e-mail, champs obligatoires, expressions réguliaires, etc.\n10. Création d&#039;un ou plusieurs tickets ou changements à partir des réponses aux formulaires\n11. Ajout de description par champs, par section de questions, par formulaires, par entités et langues.\n12. Formatage du/des ticket(s) créé(s) : réponses aux questions à afficher, gabarits de tickets.\n13. Prévisualisation du formulaire créé directement dans la configuration.\n         "
                },
                {
                    "lang": "en",
                    "short_description": "Formcreator is a plugin that allow creation of custom, easy to access forms for users when they want to create one or more tickets or changes.",
                    "long_description": "\nFormcreator is a plugin that allow creation of custom, easy to access forms for users when they want to create one or more tickets or changes.\n\nFeatures\n--------\n1. Direct access to forms self-service interface in main menu\n2. Highlighting forms in homepages\n3. Access to forms controlled: public access, identified user access, restricted access to some profiles\n4. Simple and customizable forms\n5. Forms organized by categories, entities and languages.\n6. Questions of any type of presentation: Textareas, lists, LDAP, files, etc.\n7. Questions organised in sections. Choice of the display order.\n8. Possibility to display a question based on certain criteria (response to a further question)\n9. A sharp control on responses from forms: text, numbers, size of fields, email, mandatory fields, regular expressions, etc.\n10. Creation of one or more tickets or changes from form answers\n11. Adding a description per fields, per sections, per forms, entities or languages.\n12. Formatting the ticket set: answers to questions displayed, tickets templates.\n13. Preview form created directly in the configuration.\n         "
                }
            ],
            "required_offers": None,
            "short_description": "Formcreator is a plugin that allow creation of custom, easy to access forms for users when they want to create one or more tickets or changes."
        },
        {
            "id": 70,
            "key": "positions",
            "name": "Cartography",
            "logo_url": "https://raw.githubusercontent.com/InfotelGLPI/positions/master/positions.png",
            "xml_url": "https://raw.githubusercontent.com/InfotelGLPI/positions/master/positions.xml",
            "homepage_url": "https://github.com/InfotelGLPI/positions",
            "download_url": "https://github.com/InfotelGLPI/positions/releases",
            "issues_url": "https://github.com/InfotelGLPI/positions/issues",
            "readme_url": "https://github.com/InfotelGLPI/positions/wiki",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2013-02-12T00:00:00.000000Z",
            "date_updated": "2024-01-27T00:00:00.000000Z",
            "download_count": 28760,
            "note": 2.678977272727273,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 63,
                    "name": "Ludovic Dupont"
                },
                {
                    "id": 49,
                    "name": "Infotel"
                }
            ],
            "versions": [
                {
                    "num": "6.0.3",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/positions/releases/download/6.0.3/glpi-positions-6.0.3.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "6.0.2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/positions/releases/download/6.0.2/glpi-positions-6.0.2.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "6.0.1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/positions/releases/download/6.0.1/glpi-positions-6.0.1.tar.bz2",
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Cartographie. Ce plugin permet d’ajouter des coordonnées à des matériels / ressources humaines et ainsi de les positionner sur des cartes",
                    "long_description": "Ce plugin permet d’ajouter des coordonnées à des matériels / ressources humaines et ainsi de les positionner sur des cartes.<br />Fonctionnalités :<br />- Zoom de la carte<br />- Recherche d’éléments de la carte<br />- Déplacement d’éléments en masse<br />- Personnalisation des informations à visualiser<br />- Gestion d’icônes liés aux types de matériel<br />- Gestion des bureaux (sous-lieux)<br />- ClickAndCall : En cliquant sur le numéro de téléphone, un appel se lancera directement sur le téléphone IP<br />- Utilisable avec le plugin Ressources humaines"
                },
                {
                    "lang": "en",
                    "short_description": "Cartography. This plugin allows you to add coordinates to any asset / human resources and so the place it on maps.",
                    "long_description": "This plugin allows you to add coordinates to any asset / human resources and so the place it on maps..<br />Features :<br />- Zoom on map<br />- Asset seach on map<br />- Massive move of assets<br />- Customizing of information to see<br />- Management of icons related to asset types<br />- Management offices (sub-site)<br />- ClickAndCall : By clicking on the phone number, a call will run directly on the IP phone<br />- Can be used with Human ressources plugin"
                },
                {
                    "lang": "cs",
                    "short_description": "Kartografie. Tento zásuvný modul umožňuje přidávat souřadnice k libovolnému majektu / pracovním místům a umisťovat je tak na mapy.",
                    "long_description": "Tento zásuvný modul umožňuje přidávat souřadnice k libovolnému majektu / pracovním místům a umisťovat je tak na mapy.<br />Funkce:<br />- Přiblížit na mapě<br />- Hledání majetku na mapě<br />- Hromadný přesun majetků<br />- Přizpůsobit informace, které zobrazit<br />- Správa ikon souvisejících s typy majetku<br />- Správa kanceláří<br />- Zavolat kliknutím: kliknutím na tel. číslo je na IP telefonu přímo zahájen hovor<br />- Je možné použít se zásuvným modulem Personalistika"
                }
            ],
            "required_offers": None,
            "short_description": "Cartography. This plugin allows you to add coordinates to any asset / human resources and so the place it on maps."
        },
        {
            "id": 72,
            "key": "typology",
            "name": "Typology",
            "logo_url": "https://raw.githubusercontent.com/InfotelGLPI/typology/master/typology.png",
            "xml_url": "https://raw.githubusercontent.com/InfotelGLPI/typology/master/typology.xml",
            "homepage_url": "https://github.com/InfotelGLPI/typology",
            "download_url": "https://github.com/InfotelGLPI/typology/releases",
            "issues_url": "https://github.com/InfotelGLPI/typology/issues",
            "readme_url": "https://raw.githubusercontent.com/InfotelGLPI/typology/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2013-03-07T00:00:00.000000Z",
            "date_updated": "2022-04-25T00:00:00.000000Z",
            "download_count": 20570,
            "note": 3.5714285714285716,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                },
                {
                    "id": 49,
                    "name": "Infotel"
                }
            ],
            "versions": {
                "4": {
                    "num": "3.0.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/typology/releases/download/3.0.0/glpi-typology-3.0.0.tar.bz2",
                    "stability": "stable"
                },
                "3": {
                    "num": "3.0.0-rc1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/typology/releases/download/3.0.0-rc1/glpi-typology-3.0.0-rc1.tar.bz2",
                    "stability": "RC"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Typology. Ce plugin permet de définir des typologies d’usage (gestion de configurations) à partir des informations des éléments inventoriés dans GLPI.",
                    "long_description": "Ce plugin permet de définir des typologies d’usage (gestion de configurations) à partir des informations des éléments inventoriés dans GLPI.<br />Fonctionnalités :<br />- Utilisation d&#039;un moteur de règle d&#039;affectation de typologie<br />- Définition de critères (Informations générales de l&#039;ordinateur / Composants / Réseau / Logiciels)<br />- Alertes : Vérification des typologies respectées<br />- Actions automatiques : Mise à jour automatique des typologies affectées<br />- Rapport : Liste des typologies par service"
                },
                {
                    "lang": "en",
                    "short_description": "Typology. This plugin allows you to define typologies of use (configuration management) from the information items inventoried in GLPI.",
                    "long_description": "This plugin allows you to define typologies of use (configuration management) from the information items inventoried in GLPI.<br />Features :<br />- Use of an rule engine for typologies assignment<br />- Definition of criteria (General Information Computer / Components / Network / Software)<br />- Alerts: Checking typologies observed<br />- Automatic Actions: Automatic update typologies affected<br />- Report : List of typologies of services"
                },
                {
                    "lang": "cs",
                    "short_description": "Typologie. Tento zásuvný modul umožňuje definovat typologie použítí (správa nastavení) z informací položek, evidovaných v GLPI.",
                    "long_description": "Tento zásuvný modul umožňuje definovat typologie použítí (správa nastavení) z informací položek, evidovaných v GLPI.<br />Funkce:<br />- Použití engine pravidel pro přiřazení typologií<br />- Definice kritérií (obecný počítač / komponenty / síť / software)<br />- Výstrahy: Kontrola zpozorovaných technologií<br />- Automatické akce: automatická aktualizace typologií, kterých se týká<br />- Výkaz: seznam typologií služeb"
                }
            ],
            "required_offers": None,
            "short_description": "Typology. This plugin allows you to define typologies of use (configuration management) from the information items inventoried in GLPI."
        },
        {
            "id": 74,
            "key": "ocsinventoryng",
            "name": "OCS Inventory NG",
            "logo_url": "https://github.com/pluginsGLPI/ocsinventoryng/blob/master/ocsinventoryng.png?raw=true",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/ocsinventoryng/master/ocsinventoryng.xml",
            "homepage_url": "https://github.com/pluginsGLPI/ocsinventoryng",
            "download_url": "https://github.com/pluginsGLPI/ocsinventoryng/releases",
            "issues_url": "https://github.com/pluginsGLPI/ocsinventoryng/issues",
            "readme_url": "https://github.com/pluginsGLPI/ocsinventoryng/wiki",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2013-07-25T00:00:00.000000Z",
            "date_updated": "2022-11-24T00:00:00.000000Z",
            "download_count": 173037,
            "note": 3.4766081871345027,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 5,
                    "name": "Remi Collet"
                },
                {
                    "id": 6,
                    "name": "Nelly Mahu-Lasson"
                },
                {
                    "id": 8,
                    "name": "David Durieux"
                },
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                },
                {
                    "id": 14,
                    "name": "Walid Nouh"
                }
            ],
            "versions": {
                "0": {
                    "num": "2.0.4",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/ocsinventoryng/releases/download/2.0.4/glpi-ocsinventoryng-2.0.4.tar.bz2",
                    "stability": "stable"
                },
                "1": {
                    "num": "2.0.3",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/ocsinventoryng/releases/download/2.0.3/glpi-ocsinventoryng-2.0.3.tar.bz2",
                    "stability": "stable"
                },
                "2": {
                    "num": "2.0.2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/ocsinventoryng/releases/download/2.0.2/glpi-ocsinventoryng-2.0.2.tar.bz2",
                    "stability": "stable"
                },
                "3": {
                    "num": "2.0.1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/ocsinventoryng/releases/download/2.0.1/glpi-ocsinventoryng-2.0.1.tar.bz2",
                    "stability": "stable"
                },
                "6": {
                    "num": "2.0.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/ocsinventoryng/releases/download/2.0.0/glpi-ocsinventoryng-2.0.0.tar.bz2",
                    "stability": "stable"
                },
                "4": {
                    "num": "2.0.0-rc2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/ocsinventoryng/releases/download/2.0.0-rc2/glpi-ocsinventoryng-2.0.0-rc2.tar.bz2",
                    "stability": "RC"
                },
                "5": {
                    "num": "2.0.0-rc1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/ocsinventoryng/releases/download/2.0.0-rc1/glpi-ocsinventoryng-2.0.0-rc1.tar.bz2",
                    "stability": "RC"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Synchronisation OCSInventory-NG",
                    "long_description": "Ce plugin permet de synchroniser GLPI avec la solution d&#039;inventaire OCS Inventory NG. Il remplace le mode OCS natif de GLPI et apporte les fonctionnalités du plugin massocsimport afin d&#039;offrir une meilleure compatibilité et évolutivité avec OCS Inventory. Il est composée d’un script (PHP ou Shell) permettant d’automatiser l’import et la mise à jour des machines (le mode Expert doit être opérationnel).<br />Une interface affiche la liste des scripts en cours ou terminés, ainsi que l&#039;ensemble des données qui s&#039;y rattachent."
                },
                {
                    "lang": "en",
                    "short_description": "OCSInventory-NG synchronisation",
                    "long_description": "This plugin allows you to synchronize with GLPI inventory solution OCS Inventory NG. It&#039;s replace native mode OCS of GLPI and use the plugin massocsimport functionalities to provide better compatibility and expandability with OCS. It&#039;s composed of a script (PHP or Shell) to automate import or synchronisation of computers (need that Expert mode is operational)<br />A graphical interface displays the list of scripts running or finished and all the datas related ot them."
                },
                {
                    "lang": "cs",
                    "short_description": "Synchronizace s OCSInventory-NG",
                    "long_description": "Tento zásuvný modul umožňuje synchronizovat s řešením GLPI pro inventuru s OCS Inventory NG. Nahradí nativní režim OCS GLPI a použije funkce zásuvného modulu massocsimport pro poskytnutí lepší kompatibility a rozšiřitelnosti s OCS. Je složen ze skriptu (PHP nebo shell) pro automatizaci importu nebo synchronizaci počítačů (potřebuje, aby byl funkční Expertní režim)<br />Grafické rozhraní zobrazuje seznam spuštěných nebo dokončených skriptů a všech souvisejících dat."
                }
            ],
            "required_offers": None,
            "short_description": "OCSInventory-NG synchronisation"
        },
        {
            "id": 80,
            "key": "vip",
            "name": "VIP",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/vip/main/pics/vip.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/vip/main/vip.xml",
            "homepage_url": "https://github.com/pluginsGLPI/vip",
            "download_url": "https://github.com/pluginsGLPI/vip/releases",
            "issues_url": "https://github.com/pluginsGLPI/vip/issues",
            "readme_url": "https://raw.githubusercontent.com/pluginsGLPI/vip/master/README.md",
            "changelog_url": "",
            "license": "AGPL v3+",
            "date_added": "2014-03-12T00:00:00.000000Z",
            "date_updated": "2024-11-24T00:00:00.000000Z",
            "download_count": 8835,
            "note": 2.66,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 49,
                    "name": "Infotel"
                },
                {
                    "id": 79,
                    "name": "PROBESYS"
                },
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                },
                {
                    "id": 27,
                    "name": "Philippe Godot"
                },
                {
                    "id": 28,
                    "name": "Maxime Bonillo"
                }
            ],
            "versions": [
                {
                    "num": "1.8.3",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/vip/releases/download/1.8.3/glpi-vip-1.8.3.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "1.8.2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/vip/releases/download/1.8.2/glpi-vip-1.8.2.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "1.8.1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/vip/releases/download/1.8.1/glpi-vip-1.8.1.tar.bz2",
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "VIP. Ce plugin permet d&#039;indiquer dans l&#039;interface du ticket si le demandeur du ticket fait partie d&#039;un groupe VIP.",
                    "long_description": "Ce plugin permet d&#039;indiquer dans l&#039;interface du ticket si le demandeur du ticket fait partie d&#039;un groupe VIP :<br />* Paramétrage dans l&#039;interface du groupe :<br />     - Création d&#039;un groupe, indication dans l&#039;onget &#34;VIP&#34; du paramètre si oui ou non &#34;Groupe VIP&#34;<br />* Indication dans l&#039;interface du ticket par un logo &#34;VIP&#34; et colorisation du nom de l&#039;utilisateur en rouge si le demandeur du ticket fait partie d&#039;un groupe VIP"
                },
                {
                    "lang": "en",
                    "short_description": "VIP. This plugin allows you to indicate in the ticket interface if the ticket requester belongs to a VIP group.",
                    "long_description": "This plugin allows you to indicate in the ticket interface if the ticket requester belongs to a VIP group :<br />* Parameter setting in the group interface:<br />     - Creation of a group, indication in the &#34;VIP&#34; window of the parameter if yes or no &#34;VIP Group&#34;.<br />* Indication in the ticket interface by a &#34;VIP&#34; logo and colouring of the user&#039;s name in red if the ticket requester belongs to a VIP group"
                }
            ],
            "required_offers": None,
            "short_description": "VIP. This plugin allows you to indicate in the ticket interface if the ticket requester belongs to a VIP group."
        },
        {
            "id": 82,
            "key": "mantis",
            "name": "MantisBT synchronization",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/mantis/master/mantis.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/mantis/master/mantis.xml",
            "homepage_url": "https://pluginsglpi.github.io/mantis/",
            "download_url": "https://github.com/pluginsGLPI/mantis/releases",
            "issues_url": "https://github.com/pluginsGLPI/mantis/issues",
            "readme_url": "https://raw.githubusercontent.com/pluginsGLPI/mantis/master/README.md",
            "changelog_url": "",
            "license": "GPLv3",
            "date_added": "2014-07-01T00:00:00.000000Z",
            "date_updated": "2022-02-01T00:00:00.000000Z",
            "download_count": 2624,
            "note": 3.375,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": [],
            "descriptions": [
                {
                    "lang": "cs",
                    "short_description": "Tento zásuvný modul umožňuje synchronizovat požadavky, problémy a změny s nástrojem MantisBT.",
                    "long_description": "Tento zásuvný modul umožňuje synchronizovat požadavky, problémy a změny s nástrojem MantisBT.\n             <br />Toto je seznam funkcí, které jsou v současnosti k dispozici:\n             <ul><li>Propojení prostřednictvím webových služeb MantisBT (MantisConnect);</li>\n             <li>Vytváření nových MantisBT požadavků z požadavku, problému nebo změny v GLPi;</li>\n             <li>Propojování existujících MantisBT požadavků z požadavku, problému nebo změny v GLPi;</li>\n             <li>Přenos informací z GLPi objektu do vytvořeného/propojeného MantisBT požadavku;</li>\n             <li>Přenos a automatická aktualizace příloh GLPi objektu do MantisBT vytvořeného/propojeného požadavku;</li>\n             <li>Automatická aktualizace GLPi objektu (přechod do stavu vyřešeno) když je vyřešen požadavek v MantisBT;</li>\n             <li>Správa oprávnění pro zásuvný modul;</li>\n             <li>Správa nastavení propojení.</li>\n         </ul>"
                },
                {
                    "lang": "en",
                    "short_description": "This plugin allows to synchronize tickets, problems and changes with the MantisBT tool.",
                    "long_description": "This plugin allows to synchronize tickets, problems and changes with the MantisBT tool.\n             <br />Here is a list of current features:\n             <ul><li>Connection via webservices of MantisBT (MantisConnect);</li>\n             <li>Creation of a new MantisBT issue from a ticket, problem or GLPi change;</li>\n             <li>Link an existing MantisBT issue from a ticket, problem or GLPi change;</li>\n             <li>Transmission of information from the GLPi object to the created / linked MantisBT issue;</li>\n             <li>Transfer and auto-update attachments of GLPi object to the MantisBT created / linked issue;</li>\n             <li>Automatic update of GLPi object (transition to the resolved state) when the MantisBT issue is resolved;</li>\n             <li>Management rights for the plugin;</li>\n             <li>Configuration management of interconnection.</li>\n         </ul>"
                },
                {
                    "lang": "fr",
                    "short_description": "Ce plugin permet de synchroniser les tickets, problèmes et changements avec l&#039;outil MantisBT.",
                    "long_description": "Ce plugin permet de synchroniser les tickets, problèmes et changements avec l&#039;outil MantisBT.\n            <br />Voici une liste de ses fonctionnalités actuelles :\n            <ul><li>Connexion via les Webservices de MantisBT (MantisConnect);</li>\n            <li>Création d&#039;une nouvelle issue MantisBT depuis un ticket, un problème ou un changement GLPi;</li>\n            <li>Liaison d&#039;une issue MantisBT existante depuis un ticket, un problème ou un changement GLPi;</li>\n            <li>Transmission des informations de l&#039;objet GLPi vers l&#039;issue MantisBT créée/liéée;</li>\n            <li>Transfert et mise à jour des pièces jointes de l&#039;objet GLPi vers l&#039;issue MantisBT créée/liéée;</li>\n            <li>Tâche automatique de mise à jour de l&#039;objet GLPi (passage à l&#039;état résolu) lors que l&#039;issue MantisBT est résolue;</li>\n            <li>Gestion des droits sur le plugin;</li>\n            <li>Gestion de la configuration de l&#039;interconnexion.</li>\n         </ul>"
                }
            ],
            "required_offers": None,
            "short_description": "This plugin allows to synchronize tickets, problems and changes with the MantisBT tool."
        },
        {
            "id": 91,
            "key": "sccm",
            "name": "SCCM",
            "logo_url": "https://raw.githubusercontent.com/TECLIB/sccm/master/screenshots/iconmonstr-database-10-icon-128.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/sccm/main/sccm.xml",
            "homepage_url": "https://pluginsglpi.github.io/sccm/",
            "download_url": "https://github.com/pluginsGLPI/sccm/releases",
            "issues_url": "https://github.com/pluginsGLPI/sccm/issues",
            "readme_url": "https://github.com/pluginsGLPI/sccm/blob/develop/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2015-08-14T00:00:00.000000Z",
            "date_updated": "2023-06-19T00:00:00.000000Z",
            "download_count": 6538,
            "note": 3.4166666666666665,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": {
                "8": {
                    "num": "2.4.3",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/sccm/releases/download/2.4.3/glpi-sccm-2.4.3.tar.bz2",
                    "stability": "stable"
                },
                "9": {
                    "num": "2.4.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/sccm/releases/download/2.4.2/glpi-sccm-2.4.2.tar.bz2",
                    "stability": "stable"
                },
                "10": {
                    "num": "2.4.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/sccm/releases/download/2.4.1/glpi-sccm-2.4.1.tar.bz2",
                    "stability": "stable"
                },
                "11": {
                    "num": "2.4.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/sccm/releases/download/2.4.0/glpi-sccm-2.4.0.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Synchronisation des données avec l&#039;outil Microsoft SCCM",
                    "long_description": "Synchronisation des données avec l&#039;outil Microsoft SCCM\n\nPlugin permettant de synchroniser les ordinateurs présents dans SCCM avec GLPI.\n\n* Le plugin interroge le serveur SCCM au moyen de requêtes MsSQL ;\n* il construit un XML au format GLPI ;\n* et l&#039;injecte directement dans l&#039;inventaire natif GLPI en HTTP (via cURL).\n\n\nPré-requis :\n\n* PHP curl_init : http://php.net/manual/fr/function.curl-init.php\n* PHP mssql_connect : http://php.net/manual/fr/function.mssql-connect.php\n* Microsoft System Center Configuration Manager"
                },
                {
                    "lang": "en",
                    "short_description": "Data synchronization with Microsoft SCCM",
                    "long_description": "Data synchronization with Microsoft SCCM\n\nPlugin to synchronize computers from SCCM to GLPI.\n\n* The plugin ask the SCCM server with MsSQL queries ;\n* it builds an XML file for each computer\n* and injects it directly into the GLPI native inventory over HTTP(s) (via cURL).\n\n\nPrerequisite :\n\n* PHP curl_init : http://php.net/manual/en/function.curl-init.php\n* PHP mssql_connect : http://php.net/manual/en/function.mssql-connect.php\n* Microsoft System Center Configuration Manager"
                }
            ],
            "required_offers": None,
            "short_description": "Data synchronization with Microsoft SCCM"
        },
        {
            "id": 93,
            "key": "tag",
            "name": "Tag",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/tag/main/icon.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/tag/main/plugin.xml",
            "homepage_url": "https://github.com/pluginsGLPI/tag",
            "download_url": "https://github.com/pluginsGLPI/tag/releases",
            "issues_url": "https://github.com/pluginsGLPI/tag/issues",
            "readme_url": "https://github.com/pluginsGLPI/tag/blob/main/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2015-08-18T00:00:00.000000Z",
            "date_updated": "2025-02-19T00:00:00.000000Z",
            "download_count": 22408,
            "note": 3.5,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": {
                "10": {
                    "num": "2.12.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/tag/releases/download/2.12.2/glpi-tag-2.12.2.tar.bz2",
                    "stability": "stable"
                },
                "11": {
                    "num": "2.12.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/tag/releases/download/2.12.1/glpi-tag-2.12.1.tar.bz2",
                    "stability": "stable"
                },
                "12": {
                    "num": "2.12.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/tag/releases/download/2.12.0/glpi-tag-2.12.0.tar.bz2",
                    "stability": "stable"
                },
                "13": {
                    "num": "2.11.7",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/tag/releases/download/2.11.7/glpi-tag-2.11.7.tar.bz2",
                    "stability": "stable"
                },
                "14": {
                    "num": "2.11.6",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/tag/releases/download/2.11.6/glpi-tag-2.11.6.tar.bz2",
                    "stability": "stable"
                },
                "15": {
                    "num": "2.11.5",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/tag/releases/download/2.11.5/glpi-tag-2.11.5.tar.bz2",
                    "stability": "stable"
                },
                "16": {
                    "num": "2.11.4",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/tag/releases/download/2.11.4/glpi-tag-2.11.4.tar.bz2",
                    "stability": "stable"
                },
                "17": {
                    "num": "2.11.3",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/tag/releases/download/2.11.3/glpi-tag-2.11.3.tar.bz2",
                    "stability": "stable"
                },
                "18": {
                    "num": "2.11.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/tag/releases/download/2.11.2/glpi-tag-2.11.2.tar.bz2",
                    "stability": "stable"
                },
                "19": {
                    "num": "2.11.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/tag/releases/download/2.11.1/glpi-tag-2.11.1.tar.bz2",
                    "stability": "stable"
                },
                "20": {
                    "num": "2.11.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/tag/releases/download/2.11.0/glpi-tag-2.11.0.tar.bz2",
                    "stability": "stable"
                },
                "21": {
                    "num": "2.10.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/tag/releases/download/2.10.0/glpi-tag-2.10.0.tar.bz2",
                    "stability": "stable"
                },
                "7": {
                    "num": "2.9.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/tag/releases/download/2.9.2/glpi-tag-2.9.2.tar.bz2",
                    "stability": "stable"
                },
                "8": {
                    "num": "2.9.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/tag/releases/download/2.9.1/glpi-tag-2.9.1.tar.bz2",
                    "stability": "stable"
                },
                "9": {
                    "num": "2.9.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/tag/releases/download/2.9.0/glpi-tag-2.9.0.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Ajout de tags sur n&#039;importe quel objet de GLPI",
                    "long_description": "\n* Ajout de &#34;tags&#34; à n&#039;importe quel objet de GLPI (étendant CommonDBTM).\n* Les tags sont administrables dans les intitulés.\n* Les tags sont visibles et modifiables en entête de l&#039;objet (en dessous du titre).\n* Les tags peuvent être recherchés et visualisés dans les listes d&#039;objets.\n* Dans l&#039;administration on peut visualiser un rapport des objets associés.\n         "
                },
                {
                    "lang": "cs",
                    "short_description": "Přidání štítku k libovolnému objektu v GLPI",
                    "long_description": "\n* Přídání „Štítků“ k libovolnému objektu v GLPI (rozšíření CommonDBTM).\n* Štítky je možné spravovat v titulcích.\n* Štítky jsou viditelné a upravitelné v hlavičce objektu (pod názvem).\n* Štítky lze vyhledávat a prohlížet v seznamu objektů.\n* Ve správě je možné zobrazit výkaz o souvisejících objektech.\n         "
                }
            ],
            "required_offers": None,
            "short_description": "Ajout de tags sur n&#039;importe quel objet de GLPI"
        },
        {
            "id": 94,
            "key": "news",
            "name": "News",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/news/main/pics/icon.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/news/main/plugin.xml",
            "homepage_url": "https://github.com/pluginsGLPI/news",
            "download_url": "https://github.com/pluginsGLPI/news/releases",
            "issues_url": "https://github.com/pluginsGLPI/news/issues",
            "readme_url": "https://glpi-plugins.readthedocs.io/en/latest/news/index.html",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2015-08-18T00:00:00.000000Z",
            "date_updated": "2024-11-08T00:00:00.000000Z",
            "download_count": 39951,
            "note": 3.340909090909091,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": {
                "8": {
                    "num": "1.12.4",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/news/releases/download/1.12.4/glpi-news-1.12.4.tar.bz2",
                    "stability": "stable"
                },
                "9": {
                    "num": "1.12.3",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/news/releases/download/1.12.3/glpi-news-1.12.3.tar.bz2",
                    "stability": "stable"
                },
                "10": {
                    "num": "1.12.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/news/releases/download/1.12.2/glpi-news-1.12.2.tar.bz2",
                    "stability": "stable"
                },
                "11": {
                    "num": "1.12.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/news/releases/download/1.12.1/glpi-news-1.12.1.tar.bz2",
                    "stability": "stable"
                },
                "12": {
                    "num": "1.12.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/news/releases/download/1.12.0/glpi-news-1.12.0.tar.bz2",
                    "stability": "stable"
                },
                "13": {
                    "num": "1.11.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/news/releases/download/1.11.0/glpi-news-1.11.0.tar.bz2",
                    "stability": "stable"
                },
                "14": {
                    "num": "1.10.6",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/news/releases/download/1.10.6/glpi-news-1.10.6.tar.bz2",
                    "stability": "stable"
                },
                "15": {
                    "num": "1.10.5",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/news/releases/download/1.10.5/glpi-news-1.10.5.tar.bz2",
                    "stability": "stable"
                },
                "16": {
                    "num": "1.10.4",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/news/releases/download/1.10.4/glpi-news-1.10.4.tar.bz2",
                    "stability": "stable"
                },
                "17": {
                    "num": "1.10.3",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/news/releases/download/1.10.3/glpi-news-1.10.3.tar.bz2",
                    "stability": "stable"
                },
                "18": {
                    "num": "1.10.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/news/releases/download/1.10.2/glpi-news-1.10.2.tar.bz2",
                    "stability": "stable"
                },
                "19": {
                    "num": "1.10.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/news/releases/download/1.10.1/glpi-news-1.10.1.tar.bz2",
                    "stability": "stable"
                },
                "20": {
                    "num": "1.10.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/news/releases/download/1.10.0/glpi-news-1.10.0.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "This plugin allows to display messages on the GLPI&#039;s homepage.",
                    "long_description": "\nThis plugin allows to display messages on the GLPI&#039;s homepage.\n\nFeatures\n--------\n\n1. Create alerts with rich text like notes.\n2. Choose the desired publication start and end dates.\n3. Manage alerts by entity.\n4. Displays the alerts according to the user&#039;s profile\n         "
                },
                {
                    "lang": "cs",
                    "short_description": "Tento zásuvný modul umožňuje zobrazovat zprávy na hlavní stránce rozhraní GLPI.",
                    "long_description": "\nTento zásuvný modul umožňuje zobrazování zpráv na hlavní stránce rozhraní GLPi.\n\nFunkce\n--------\n\n1. Vytvářet upozornění pomocí poznámek v podobě formátovaného textu.\n2. Zvolit datum požadovaného začátku a konce zveřejnění.\n3. Spravovat upozornění podle entit.\n4. Zobrazit upozornění v závislosti na profilu uživatele\n         "
                },
                {
                    "lang": "fr",
                    "short_description": "Ce plugin permet d&#039;afficher des messages sur la page d&#039;accueil de GLPI.",
                    "long_description": "\nCe plugin permet d&#039;afficher des messages sur la page d&#039;accueil de GLPI.\n\nFonctionnalités\n---------------\n\n1. Création d&#039;une alerte avec du texte riche comme les notes.\n2. Choix d&#039;une date de début / date de fin de publication.\n3. Gestion des alertes par entité.\n4. Affichage des alertes en fonction du profil.\n         "
                }
            ],
            "required_offers": None,
            "short_description": "This plugin allows to display messages on the GLPI&#039;s homepage."
        },
        {
            "id": 96,
            "key": "mreporting",
            "name": "More Reporting",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/mreporting/main/pics/chart-garea.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/mreporting/main/mreporting.xml",
            "homepage_url": "https://github.com/pluginsGLPI/mreporting/",
            "download_url": "https://github.com/pluginsGLPI/mreporting/releases",
            "issues_url": "https://github.com/pluginsGLPI/mreporting/issues",
            "readme_url": "https://raw.githubusercontent.com/pluginsGLPI/mreporting/main/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2015-08-21T00:00:00.000000Z",
            "date_updated": "2025-01-29T00:00:00.000000Z",
            "download_count": 66510,
            "note": 3.233695652173913,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                },
                {
                    "id": 49,
                    "name": "Infotel"
                }
            ],
            "versions": {
                "5": {
                    "num": "1.8.7",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/mreporting/releases/download/1.8.7/glpi-mreporting-1.8.7.tar.bz2",
                    "stability": "stable"
                },
                "6": {
                    "num": "1.8.6",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/mreporting/releases/download/1.8.6/glpi-mreporting-1.8.6.tar.bz2",
                    "stability": "stable"
                },
                "7": {
                    "num": "1.8.5",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/mreporting/releases/download/1.8.5/glpi-mreporting-1.8.5.tar.bz2",
                    "stability": "stable"
                },
                "8": {
                    "num": "1.8.4",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/mreporting/releases/download/1.8.4/glpi-mreporting-1.8.4.tar.bz2",
                    "stability": "stable"
                },
                "9": {
                    "num": "1.8.3",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/mreporting/releases/download/1.8.3/glpi-mreporting-1.8.3.tar.bz2",
                    "stability": "stable"
                },
                "10": {
                    "num": "1.8.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/mreporting/releases/download/1.8.2/glpi-mreporting-1.8.2.tar.bz2",
                    "stability": "stable"
                },
                "11": {
                    "num": "1.8.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/mreporting/releases/download/1.8.1/glpi-mreporting-1.8.1.tar.bz2",
                    "stability": "stable"
                },
                "12": {
                    "num": "1.8.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/mreporting/releases/download/1.8.0/glpi-mreporting-1.8.0.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "cs",
                    "short_description": "Přidání (a vytváření) nových výkazů s grafy pro glpi",
                    "long_description": "Přidání (a vytváření) nových výkazů s grafy pro glpi.   \n\nTento zásuvný modul obsahuje sadu nových statistických výkazů: \n\n* Služba podpory\n  * Nahromaděné požadavky\n  * Stáří požadavku\n  * Požadavky podle skupiny nebo technika\n  * Nejčastější kategorie nebo skupiny žadatelů\n  * Počet změn skupin\n  * 5 SLA výkazů\n\n* Inventory\n  * Verze operačních systémů a distribuce\n  * Nejčastější výrobci\n  * Nejčastější typy (server, notebook, …)\n  * Nejčastější stavy\n  * Stáří počítačů\n  * FusionInventory agenti\n\n* Distribuce záznamů o událostech\n\nMůžete si také vytvořit nový výkaz pomocí kostry zásuvného modulu.  \nViz dokumentace: https://github.com/PluginsGLPI/mreporting/wiki\n         "
                },
                {
                    "lang": "en",
                    "short_description": "Add (and develop) new graphical reports for glpi",
                    "long_description": "Add (and develop) new graphical reports for glpi.   \n\nThis plugins embed a set of new statistics reports : \n\n* Helpdesk\n  * Backlog\n  * Ticket age\n  * Tickets per group or technician\n  * Top categories or requester groups\n  * Number of group changes\n  * 5 SLA reports\n\n* Inventory\n  * Os versions and distributions\n  * Top manufacturers\n  * Top types (server, laptop, ...)\n  * Top status\n  * Age of computers\n  * FusionInventory agents\n\n* Logs distribution\n\nYou can also develop new report with the framework of plugin.  \nSee documentation : https://github.com/PluginsGLPI/mreporting/wiki\n         "
                },
                {
                    "lang": "fr",
                    "short_description": "Ajouter (et développer) de nouveaux rapports graphiques pour glpi",
                    "long_description": "Ajouter (et développer) de nouveaux rapports grahiques pour glpi.   \n\nCe plugin contient un ensemble de nouveaux rapports statistiques.\n\n* Assistance\n  * Backlog\n  * Ancienneté des tickets\n  * Tickets par groupes ou techniciens\n  * Top catégories ou groupes demandeurs\n  * Nombre de changement de groupes\n  * 5 rapports SLA\n\n* Inventaire\n  * Versions et distributions des OS\n  * Top fabricants\n  * top types (serveurs, portables, ...)\n  * Top statuts\n  * Age des ordinateurs\n  * Agents FusionInventory\n\n* Répartition des logs\n\nVous pouvez aussi ajouter vos propre rapports en utilisant le &#34;framework&#34; fourni par le plugin\nVoir documentation : https://github.com/PluginsGLPI/mreporting/wiki\n         "
                }
            ],
            "required_offers": None,
            "short_description": "Add (and develop) new graphical reports for glpi"
        },
        {
            "id": 99,
            "key": "escalade",
            "name": "Escalade ",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/escalade/main/escalade.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/escalade/main/escalade.xml",
            "homepage_url": "https://github.com/pluginsGLPI/escalade",
            "download_url": "https://github.com/pluginsGLPI/escalade/releases",
            "issues_url": "https://github.com/pluginsGLPI/escalade/issues",
            "readme_url": "https://glpi-plugins.readthedocs.io/en/latest/escalade/index.html",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2015-08-24T00:00:00.000000Z",
            "date_updated": "2025-03-11T00:00:00.000000Z",
            "download_count": 29568,
            "note": 2.92578125,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 31,
                    "name": "Alexandre Delaunay"
                },
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": {
                "13": {
                    "num": "2.9.11",
                    "compatibility": "~10.0.11",
                    "download_url": "https://github.com/pluginsGLPI/escalade/releases/download/2.9.11/glpi-escalade-2.9.11.tar.bz2",
                    "stability": "stable"
                },
                "14": {
                    "num": "2.9.10",
                    "compatibility": "~10.0.11",
                    "download_url": "https://github.com/pluginsGLPI/escalade/releases/download/2.9.10/glpi-escalade-2.9.10.tar.bz2",
                    "stability": "stable"
                },
                "8": {
                    "num": "2.9.9",
                    "compatibility": "~10.0.11",
                    "download_url": "https://github.com/pluginsGLPI/escalade/releases/download/2.9.9/glpi-escalade-2.9.9.tar.bz2",
                    "stability": "stable"
                },
                "9": {
                    "num": "2.9.8",
                    "compatibility": "~10.0.11",
                    "download_url": "https://github.com/pluginsGLPI/escalade/releases/download/2.9.8/glpi-escalade-2.9.8.tar.bz2",
                    "stability": "stable"
                },
                "10": {
                    "num": "2.9.7",
                    "compatibility": "~10.0.11",
                    "download_url": "https://github.com/pluginsGLPI/escalade/releases/download/2.9.7/glpi-escalade-2.9.7.tar.bz2",
                    "stability": "stable"
                },
                "11": {
                    "num": "2.9.6",
                    "compatibility": "~10.0.11",
                    "download_url": "https://github.com/pluginsGLPI/escalade/releases/download/2.9.6/glpi-escalade-2.9.6.tar.bz2",
                    "stability": "stable"
                },
                "12": {
                    "num": "2.9.5",
                    "compatibility": "~10.0.11",
                    "download_url": "https://github.com/pluginsGLPI/escalade/releases/download/2.9.5/glpi-escalade-2.9.5.tar.bz2",
                    "stability": "stable"
                },
                "15": {
                    "num": "2.9.4",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/escalade/releases/download/2.9.4/glpi-escalade-2.9.4.tar.bz2",
                    "stability": "stable"
                },
                "16": {
                    "num": "2.9.3",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/escalade/releases/download/2.9.3/glpi-escalade-2.9.3.tar.bz2",
                    "stability": "stable"
                },
                "17": {
                    "num": "2.9.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/escalade/releases/download/2.9.2/glpi-escalade-2.9.2.tar.bz2",
                    "stability": "stable"
                },
                "18": {
                    "num": "2.9.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/escalade/releases/download/2.9.1/glpi-escalade-2.9.1.tar.bz2",
                    "stability": "stable"
                },
                "19": {
                    "num": "2.9.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/escalade/releases/download/2.9.0/glpi-escalade-2.9.0.tar.bz2",
                    "stability": "stable"
                },
                "20": {
                    "num": "2.8.3",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/escalade/releases/download/2.8.3/glpi-escalade-2.8.3.tar.bz2",
                    "stability": "stable"
                },
                "21": {
                    "num": "2.8.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/escalade/releases/download/2.8.2/glpi-escalade-2.8.2.tar.bz2",
                    "stability": "stable"
                },
                "22": {
                    "num": "2.8.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/escalade/releases/download/2.8.1/glpi-escalade-2.8.1.tar.bz2",
                    "stability": "stable"
                },
                "23": {
                    "num": "2.8.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/escalade/releases/download/2.8.0/glpi-escalade-2.8.0.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "cs",
                    "short_description": "Tento zásuvný modul zjednodušuje eskalaci požadavku na jiné skupiny",
                    "long_description": "\nTento zásuvný modul zjednodušuje eskalaci požadavku na jiné skupiny.   \nPřidává následující funkce: \n\n* Zobrazení vizuální historie přiřazení požadavku skupinám.\n* Zrychlená eskalace na skupinu nacházející se v historii.\n* Přiřazení skupiny iniciátora když je poskytnuto řešení požadavku.\n* Poskytnutí automatického přiřazování požadavků při změně jeho kategorie.\n* Rychlé klonování požadavku.\n* Současné uzavření klonovaných požadavků.\n* Vzetí první nebo poslední skupiny technika (při změně požadavku).\n* Nové tlačítko pro zrychlené přiřazení požadavku sám sobě. \n         "
                },
                {
                    "lang": "en",
                    "short_description": "This plugin simplifies the ticket escalation to different groups",
                    "long_description": "\nThis plugin simplifies the ticket escalation to different groups.   \nIt adds the following features : \n\n* Display a visual history of the assignement groups on a ticket.\n* Rapid escalation to a group present in history.\n* Assign initiator group when ticket solution provided.\n* provide automatic assignment of tickets on ticket category change.\n* Fast cloning of ticket.\n* Closing cloned tickets simultaneously.\n* Take the first or last group of technician (on ticket modification).\n* New button for rapid self-assignment of a ticket. \n         "
                },
                {
                    "lang": "fr",
                    "short_description": "Cette extension permet de simplifier l&#039;escalade de ticket vers des groupes différents",
                    "long_description": "\nCette extension permet de simplifier l&#039;escalade de ticket vers des groupes différents.   \nElle ajoute les fonctionnalités suivantes :\n\n* Affichage d&#039;un historique visuel de l&#039;assignation des groupes sur un ticket.\n* Escalade rapide à un groupe présent dans cette historique.\n* Assignation du groupe initiateur lors de l&#039;apport d&#039;une solution.\n* Attribution du responsable et groupe technique lors d&#039;un changement de catégorie de ticket.\n* Clonage rapide de ticket.\n* Cloture des tickets clonés en même temps.\n* Prendre le premier ou dernier groupe du technicien (sur modification du ticket).\n* Bouton d&#039;assignation rapide à soi-même d&#039;un ticket.\n         "
                }
            ],
            "required_offers": None,
            "short_description": "This plugin simplifies the ticket escalation to different groups"
        },
        {
            "id": 100,
            "key": "moreticket",
            "name": "Moreticket",
            "logo_url": "https://raw.githubusercontent.com/InfotelGLPI/moreticket/master/moreticket.png",
            "xml_url": "https://raw.githubusercontent.com/InfotelGLPI/moreticket/master/moreticket.xml",
            "homepage_url": "https://github.com/InfotelGLPI/moreticket",
            "download_url": "https://github.com/InfotelGLPI/moreticket/releases",
            "issues_url": "https://github.com/InfotelGLPI/moreticket/issues",
            "readme_url": "https://raw.githubusercontent.com/InfotelGLPI/moreticket/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2015-08-24T00:00:00.000000Z",
            "date_updated": "2024-10-07T00:00:00.000000Z",
            "download_count": 21899,
            "note": 3.3714285714285714,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 63,
                    "name": "Ludovic Dupont"
                },
                {
                    "id": 49,
                    "name": "Infotel"
                }
            ],
            "versions": {
                "2": {
                    "num": "1.7.5",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/moreticket/releases/download/1.7.5/glpi-moreticket-1.7.5.tar.bz2",
                    "stability": "stable"
                },
                "3": {
                    "num": "1.7.4",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/moreticket/releases/download/1.7.4/glpi-moreticket-1.7.4.tar.bz2",
                    "stability": "stable"
                },
                "4": {
                    "num": "1.7.3",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/moreticket/releases/download/1.7.3/glpi-moreticket-1.7.3.tar.bz2",
                    "stability": "stable"
                },
                "5": {
                    "num": "1.7.2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/moreticket/releases/download/1.7.2/glpi-moreticket-1.7.2.tar.bz2",
                    "stability": "stable"
                },
                "6": {
                    "num": "1.7.1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/moreticket/releases/download/1.7.1/glpi-moreticket-1.7.1.tar.bz2",
                    "stability": "stable"
                },
                "8": {
                    "num": "1.7.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/moreticket/releases/download/1.7.0/glpi-moreticket-1.7.0.tar.bz2",
                    "stability": "stable"
                },
                "7": {
                    "num": "1.7.0-rc1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/moreticket/releases/download/1.7.0-rc1/glpi-moreticket-1.7.0-rc1.tar.bz2",
                    "stability": "RC"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Ce plugin permet d&#039;ajouter 4 nouvelles options sur un ticket GLPI",
                    "long_description": "Ce plugin permet d&#039;ajouter 4 nouvelles options sur un ticket GLPI<br />- A la création d&#039;un ticket, lors de la sélection du statut &#34;Résolu&#34; ou &#34;Clos&#34;, le ticket vous proposera de remplir la solution du ticket,<br />- A la création et à la modification d&#039;un ticket, lors de la sélection du statut &#34;En attente&#34;, vous pourrez définir des types d&#039;attente, la raison de la mise en attente ainsi qu&#039;une date de report,<br />- Une nouvelle zone sera disponible pour ajouter des informations suite à la clôture du ticket, <br />- A la création et à la modification d&#039;un ticket, lors de la sélection de l&#039;urgence en fonction du paramètrage effectué dans la configuration du plugin, vous pourrez définir une justification."
                },
                {
                    "lang": "en",
                    "short_description": "This plugin enables you to add 4 new options into a ticket.",
                    "long_description": ""
                },
                {
                    "lang": "cs",
                    "short_description": "Tento zásuvný modul umožňuje do požadavku přidat 4 nové volby.",
                    "long_description": "Tento zásuvný modul umožňuje do požadavku přidat 4 nové volby.<br />- Při vytváření požadavku při výběru stavu „vyřešeno“ nebo „Uzavřeno“ požadavek nabídne vyplnění jeho řešení,<br />- Při vytváření nebo úpravě požadavku při výběru stavu „čekající“ je možné určit typy čekání, důvod čekání a datum hlášení,<br />- K dispozici bude nová zóna pro přidání informace po uzavření požadavku, <br />- Při vytváření a úpravě požadavku při výběru naléhavosti v závislosti na nastavení zásuvného modulu je možné určit odůvodnění."
                }
            ],
            "required_offers": None,
            "short_description": "This plugin enables you to add 4 new options into a ticket."
        },
        {
            "id": 101,
            "key": "itilcategorygroups",
            "name": "ItilCategory Groups",
            "logo_url": "https://raw.githubusercontent.com/PluginsGLPI/itilcategorygroups/main/itilcategorygroups.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/itilcategorygroups/main/itilcategorygroups.xml",
            "homepage_url": "https://github.com/pluginsGLPI/itilcategorygroups",
            "download_url": "https://github.com/pluginsGLPI/itilcategorygroups/releases",
            "issues_url": "https://github.com/pluginsGLPI/itilcategorygroups/issues",
            "readme_url": "https://raw.githubusercontent.com/pluginsGLPI/itilcategorygroups/main/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2015-08-26T00:00:00.000000Z",
            "date_updated": "2024-02-08T00:00:00.000000Z",
            "download_count": 12939,
            "note": 2.717948717948718,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                },
                {
                    "id": 14,
                    "name": "Walid Nouh"
                },
                {
                    "id": 31,
                    "name": "Alexandre Delaunay"
                },
                {
                    "id": 48,
                    "name": "Emmanuel HAGUET"
                },
                {
                    "id": 16,
                    "name": "François Legastelois"
                }
            ],
            "versions": {
                "3": {
                    "num": "2.5.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/itilcategorygroups/releases/download/2.5.1/glpi-itilcategorygroups-2.5.1.tar.bz2",
                    "stability": "stable"
                },
                "4": {
                    "num": "2.5.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/itilcategorygroups/releases/download/2.5.0/glpi-itilcategorygroups-2.5.0.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "This plugins aims to filter assignable groups in ticket by selected category",
                    "long_description": "This plugins aims to filter assignable groups in ticket by selected category.\n\nYou can define a level to your glpi groups.\nThen, for each of your ticket&#039;s categories, you can define which group will be viewed or not."
                },
                {
                    "lang": "fr",
                    "short_description": "Ce plugin apporte le filtrage des groupes &#34;attribués à&#34; en fonction de la catégorie du ticket",
                    "long_description": "Ce plugin apporte le filtrage des groupes &#34;attribués à&#34; en fonction de la catégorie du ticket.\n\nVous pouvez définir un niveau (parmis 4) pour vos groupes glpi.\nEnsuite, pour chacune des vos catégories, vous pouvez définir quel group sera visible ou non.\n         "
                },
                {
                    "lang": "cs",
                    "short_description": "Tento zásuvný modul cílí na filtrování skupin přiřaditelných v požadavku v závislosti na vybrané kategorii",
                    "long_description": "Tento zásuvný modul cílí na filtrování skupin přiřaditelných v požadavku v závislosti na vybrané kategorii.\n\nJe možné určit stupeň k vašim glpi skupinám.\nPotom, pro každou z kategorií požadavku je možné určit která skupina bude zobrazena a které ne."
                }
            ],
            "required_offers": None,
            "short_description": "This plugins aims to filter assignable groups in ticket by selected category"
        },
        {
            "id": 102,
            "key": "consumables",
            "name": "Consumables",
            "logo_url": "https://raw.githubusercontent.com/InfotelGLPI/consumables/master/consumables.png",
            "xml_url": "https://raw.githubusercontent.com/InfotelGLPI/consumables/master/consumables.xml",
            "homepage_url": "https://github.com/InfotelGLPI/consumables",
            "download_url": "https://github.com/InfotelGLPI/consumables/releases",
            "issues_url": "https://github.com/InfotelGLPI/consumables/issues",
            "readme_url": "https://raw.githubusercontent.com/InfotelGLPI/consumables/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2015-09-17T00:00:00.000000Z",
            "date_updated": "2023-08-28T00:00:00.000000Z",
            "download_count": 10188,
            "note": 3.3958333333333335,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 63,
                    "name": "Ludovic Dupont"
                },
                {
                    "id": 49,
                    "name": "Infotel"
                }
            ],
            "versions": {
                "0": {
                    "num": "2.0.1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/consumables/releases/download/2.0.1/glpi-consumables-2.0.1.tar.bz2",
                    "stability": "stable"
                },
                "2": {
                    "num": "2.0.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/consumables/releases/download/2.0.0/glpi-consumables-2.0.0.tar.bz2",
                    "stability": "stable"
                },
                "1": {
                    "num": "2.0.0-rc1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/consumables/releases/download/2.0.0-rc1/glpi-consumables-2.0.0-rc1.tar.bz2",
                    "stability": "RC"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Ce plugin vous permet de gérer les demandes de consommables pour les utilisateur finaux.",
                    "long_description": "Ce plugin vous permet de gérer les demandes de consommables pour les utilisateur finaux.<br />- Système de validation de demande de consommables,<br />- Notifications associées,<br />- Wizard utilisateur basé sur le stock disponible."
                },
                {
                    "lang": "en",
                    "short_description": "This plugin allows you to manage consumable requests for end user.",
                    "long_description": "This plugin allows you to manage consumable requests for end user.<br />- Validation system of consumable request,<br />- Associated notifications,<br />- Wizard user based on available stock."
                }
            ],
            "required_offers": None,
            "short_description": "This plugin allows you to manage consumable requests for end user."
        },
        {
            "id": 104,
            "key": "fields",
            "name": "Fields",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/fields/main/docs/logo.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/fields/main/plugin.xml",
            "homepage_url": "https://github.com/pluginsGLPI/fields",
            "download_url": "https://github.com/pluginsGLPI/fields/releases",
            "issues_url": "https://github.com/pluginsGLPI/fields/issues",
            "readme_url": "https://glpi-plugins.readthedocs.io/en/latest/fields/index.html",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2015-09-18T00:00:00.000000Z",
            "date_updated": "2025-02-03T00:00:00.000000Z",
            "download_count": 80491,
            "note": 3.331858407079646,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                },
                {
                    "id": 31,
                    "name": "Alexandre Delaunay"
                },
                {
                    "id": 65,
                    "name": "Jérémy Moreau"
                },
                {
                    "id": 16,
                    "name": "François Legastelois"
                },
                {
                    "id": 14,
                    "name": "Walid Nouh"
                },
                {
                    "id": 71,
                    "name": "Johan Cwiklinski"
                },
                {
                    "id": 39,
                    "name": "Olivier Moron"
                }
            ],
            "versions": {
                "26": {
                    "num": "1.21.19",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/fields/releases/download/1.21.19/glpi-fields-1.21.19.tar.bz2",
                    "stability": "stable"
                },
                "27": {
                    "num": "1.21.18",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/fields/releases/download/1.21.18/glpi-fields-1.21.18.tar.bz2",
                    "stability": "stable"
                },
                "28": {
                    "num": "1.21.17",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/fields/releases/download/1.21.17/glpi-fields-1.21.17.tar.bz2",
                    "stability": "stable"
                },
                "29": {
                    "num": "1.21.16",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/fields/releases/download/1.21.16/glpi-fields-1.21.16.tar.bz2",
                    "stability": "stable"
                },
                "30": {
                    "num": "1.21.15",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/fields/releases/download/1.21.15/glpi-fields-1.21.15.tar.bz2",
                    "stability": "stable"
                },
                "31": {
                    "num": "1.21.14",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/fields/releases/download/1.21.14/glpi-fields-1.21.14.tar.bz2",
                    "stability": "stable"
                },
                "32": {
                    "num": "1.21.13",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/fields/releases/download/1.21.13/glpi-fields-1.21.13.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "cs",
                    "short_description": "Zásuvný modul kolonky umožňuje přidávat vlastní kolonky do glpi typů: požadavky, počítače, uživatelé…",
                    "long_description": "\nZásuvný modul kolonky umožňuje přidávat vlastní kolonky do glpi typů: požadavky, počítače, uživatelé…  \n\nJe možné přidat další údaje do: \n\n* Karty objektu\n* Hlavního formuláře objektu (nad tlačítko uložit)\n* Formuláře karty (varování – tato funkce je experimentální)\n\nMOžné typy kolonek jsou: \n\n* Hlavička (blok titulku)\n* Text (jeden řádek)\n* Text (více řádek)\n* Číslo\n* Rozbalovací nabídka (vždy stromová rozbalovací nabídka)\n* Ano/Ne\n* Datum\n* Datum/hodina\n* Seznam Glpi uživatelů\n\nJe k dispozici [skript pro migraci](https://github.com/pluginsGLPI/customfields/blob/master/scripts/migrate-to-fields.php) z modulu „customfields“.  \n**VAROVÁNÍ: tento skript je experimentální a potřebuje být ještě více otestován. Vřele doporučujeme před jeho použitím zálohvat data**\n         "
                },
                {
                    "lang": "en",
                    "short_description": "The fields plugin allows you to add custom fields on glpi types : tickets, computers, users…",
                    "long_description": "\nThe fields plugin allows you to add custom fields on glpi types : tickets, computers, users…  \n\nAddionnal data can be added : \n\n* In object tab\n* In main form of object (above save button)\n* In form of a tab (Warning, this feature is experimental)\n\nPossible fields type are : \n\n* Header (title bloc)\n* Text (single line)\n* Text (multiple lines)\n* Number\n* Dropdown (always a tree dropdown)\n* Yes / No\n* Date\n* Date / Hour\n* Glpi User list\n\nThere is a [migration script](https://github.com/pluginsGLPI/customfields/blob/master/scripts/migrate-to-fields.php) from &#34;customfields&#34; plugin.  \n**WARNING : this one is experimental and deserved to be more tested. We strongly advise you to backup your data before using it**\n         "
                },
                {
                    "lang": "fr",
                    "short_description": "Le plugin &#039;Champs supplémentaires&#039; (Fields) permet d’ajouter des champs personnalisés sur les différents objets gérés par GLPI : tickets, ordinateurs, utilisateurs…",
                    "long_description": "\nLe plugin &#039;Champs supplémentaires&#039; (Fields) permet d’ajouter des champs personnalisés sur les différents objets gérés par GLPI : tickets, ordinateurs, utilisateurs...  \n\nLes données supplémentaires peuvent être ajoutées : \n\n* Dans un onglet de l&#039;objet\n* Dans le formulaire principal de l&#039;objet (au dessus du bouton sauvegarder)\n* Dans le formulaire d&#039;un onglet existant (attention, cette fonctionnalité est expérimental)\n\nLes types de champs possibles sont : \n\n* Entête (bloc de titre)\n* Texte (ligne simple)\n* Texte (ligne multiples)\n* Nombre\n* Liste déroulante (intitulés, forcement un arbre)\n* Oui / Non\n* Date\n* Date / Heure\n* liste d&#039;utilisateurs de glpi\n\nIl existe un [script de migration](https://github.com/pluginsGLPI/customfields/blob/master/scripts/migrate-to-fields.php) depuis le plugin &#34;customfields&#34;.  \n**Attention : celui ci est expérimental et mérité d&#039;être testé plus fortement. Nous vous conseillons fortement de sauvegarder vos données avant de l&#039;utiliser**\n         "
                }
            ],
            "required_offers": None,
            "short_description": "The fields plugin allows you to add custom fields on glpi types : tickets, computers, users…"
        },
        {
            "id": 124,
            "key": "tasklists",
            "name": "Tasks List (Kanban)",
            "logo_url": "https://raw.githubusercontent.com/InfotelGLPI/tasklists/master/tasklists.png",
            "xml_url": "https://raw.githubusercontent.com/InfotelGLPI/tasklists/master/tasklists.xml",
            "homepage_url": "https://github.com/InfotelGLPI/tasklists",
            "download_url": "https://github.com/InfotelGLPI/tasklists/releases",
            "issues_url": "https://github.com/InfotelGLPI/tasklists/issues",
            "readme_url": "https://github.com/InfotelGLPI/tasklists/wiki",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2016-01-08T00:00:00.000000Z",
            "date_updated": "2024-12-30T00:00:00.000000Z",
            "download_count": 21043,
            "note": 3.2063492063492065,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                },
                {
                    "id": 49,
                    "name": "Infotel"
                }
            ],
            "versions": {
                "2": {
                    "num": "2.0.4",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/tasklists/releases/download/2.0.4/glpi-tasklists-2.0.4.tar.bz2",
                    "stability": "stable"
                },
                "3": {
                    "num": "2.0.3",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/tasklists/releases/download/2.0.3/glpi-tasklists-2.0.3.tar.bz2",
                    "stability": "stable"
                },
                "4": {
                    "num": "2.0.2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/tasklists/releases/download/2.0.2/glpi-tasklists-2.0.2.tar.bz2",
                    "stability": "stable"
                },
                "5": {
                    "num": "2.0.1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/tasklists/releases/download/2.0.1/glpi-tasklists-2.0.1.tar.bz2",
                    "stability": "stable"
                },
                "8": {
                    "num": "2.0.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/tasklists/releases/download/2.0.0/glpi-tasklists-2.0.0.tar.bz2",
                    "stability": "stable"
                },
                "6": {
                    "num": "2.0.0-rc2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/tasklists/releases/download/2.0.0-rc2/glpi-tasklists-2.0.0-rc2.tar.bz2",
                    "stability": "RC"
                },
                "7": {
                    "num": "2.0.0-rc1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/tasklists/releases/download/2.0.0-rc1/glpi-tasklists-2.0.0-rc1.tar.bz2",
                    "stability": "RC"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Ajout d&#039;une gestion de tâches &amp; kanban. Ce plugin permet d&#039;ajouter dans GLPI, une interface pour saisir des tâches simples et de les gérer dans un kanban.",
                    "long_description": "Ce plugin permet d&#039;ajouter dans GLPI, une interface pour saisir des tâches simples et de les gérer dans un kanban.<br />- Ajout de commentaires sur les tâches.<br />- Lien avec les tickets.<br />- Utilisation de gabarits<br />- Gestion des tâches archivées.<br />- Ajout de notes possibles sur les tâches.<br />- Peut être utilisé avec le collecteur de mail pour créer des tâches.<br />- Peut être utilisé avec le plugin mydashboard d&#039;Infotel."
                },
                {
                    "lang": "en",
                    "short_description": "Adding a management of tasks &amp; kanban. This plugin adds in GLPI, an interface to input simple tasks &amp; manage them in a kanban.",
                    "long_description": "This plugin adds in GLPI, an interface to input simple tasks &amp; manage them in a kanban.<br />- Can add comments on tasks.<br />- Link with tickets.<br />- Can use templates.<br />- Manage archived tasks.<br />- Can add notes on tasks.<br />- Can be used with mail collector to create tasks.<br />- Can be used with mydashboard plugin of Infotel"
                },
                {
                    "lang": "cs",
                    "short_description": "Přidání správy jednoduchých úkolů. Tento zásuvný modul do GLPI přidá rozhraní pro zadávání jednoduchých úkolů.",
                    "long_description": "Tento zásuvný modul do GLPI přidá rozhraní pro zadávání jednoduchých úkolů.<br />- K úkolům je možné přidávat poznámky.<br />- Je možné použít s přivaděčem e-mailů a vytvářet úkoly skrze něj.<br />- Je možné použít se zásuvným modulem Moje nástěnka"
                }
            ],
            "required_offers": None,
            "short_description": "Adding a management of tasks &amp; kanban. This plugin adds in GLPI, an interface to input simple tasks &amp; manage them in a kanban."
        },
        {
            "id": 131,
            "key": "mydashboard",
            "name": "My Dashboard",
            "logo_url": "https://raw.githubusercontent.com/InfotelGLPI/mydashboard/master/mydashboard.png",
            "xml_url": "https://raw.githubusercontent.com/InfotelGLPI/mydashboard/master/mydashboard.xml",
            "homepage_url": "https://github.com/InfotelGLPI/mydashboard",
            "download_url": "https://github.com/InfotelGLPI/mydashboard/releases",
            "issues_url": "https://github.com/InfotelGLPI/mydashboard/issues",
            "readme_url": "https://github.com/InfotelGLPI/mydashboard/wiki",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2016-07-25T00:00:00.000000Z",
            "date_updated": "2023-06-07T00:00:00.000000Z",
            "download_count": 46013,
            "note": 3.191919191919192,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                },
                {
                    "id": 49,
                    "name": "Infotel"
                }
            ],
            "versions": {
                "3": {
                    "num": "2.1.5",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/mydashboard/releases/download/2.1.5/glpi-mydashboard-2.1.5.tar.bz2",
                    "stability": "stable"
                },
                "4": {
                    "num": "2.1.4",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/mydashboard/releases/download/2.1.4/glpi-mydashboard-2.1.4.tar.bz2",
                    "stability": "stable"
                },
                "5": {
                    "num": "2.1.3",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/mydashboard/releases/download/2.1.3/glpi-mydashboard-2.1.3.tar.bz2",
                    "stability": "stable"
                },
                "6": {
                    "num": "2.1.2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/mydashboard/releases/download/2.1.2/glpi-mydashboard-2.1.2.tar.bz2",
                    "stability": "stable"
                },
                "7": {
                    "num": "2.1.1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/mydashboard/releases/download/2.1.1/glpi-mydashboard-2.1.1.tar.bz2",
                    "stability": "stable"
                },
                "8": {
                    "num": "2.1.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/mydashboard/releases/download/2.1.0/glpi-mydashboard-2.1.0.tar.bz2",
                    "stability": "stable"
                },
                "9": {
                    "num": "2.0.9",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/mydashboard/releases/download/2.0.9/glpi-mydashboard-2.0.9.tar.bz2",
                    "stability": "stable"
                },
                "10": {
                    "num": "2.0.8",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/mydashboard/releases/download/2.0.8/glpi-mydashboard-2.0.8.tar.bz2",
                    "stability": "stable"
                },
                "11": {
                    "num": "2.0.7",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/mydashboard/releases/download/2.0.7/glpi-mydashboard-2.0.7.tar.bz2",
                    "stability": "stable"
                },
                "12": {
                    "num": "2.0.6",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/mydashboard/releases/download/2.0.6/glpi-mydashboard-2.0.6.tar.bz2",
                    "stability": "stable"
                },
                "13": {
                    "num": "2.0.5",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/mydashboard/releases/download/2.0.5/glpi-mydashboard-2.0.5.tar.bz2",
                    "stability": "stable"
                },
                "14": {
                    "num": "2.0.4",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/mydashboard/releases/download/2.0.4/glpi-mydashboard-2.0.4.tar.bz2",
                    "stability": "stable"
                },
                "15": {
                    "num": "2.0.3",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/mydashboard/releases/download/2.0.3/glpi-mydashboard-2.0.3.tar.bz2",
                    "stability": "stable"
                },
                "16": {
                    "num": "2.0.2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/mydashboard/releases/download/2.0.2/glpi-mydashboard-2.0.2.tar.bz2",
                    "stability": "stable"
                },
                "17": {
                    "num": "2.0.1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/mydashboard/releases/download/2.0.1/glpi-mydashboard-2.0.1.tar.bz2",
                    "stability": "stable"
                },
                "21": {
                    "num": "2.0.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/mydashboard/releases/download/2.0.0/glpi-mydashboard-2.0.0.tar.bz2",
                    "stability": "stable"
                },
                "18": {
                    "num": "2.0.0-rc3",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/mydashboard/releases/download/2.0.0-rc3/glpi-mydashboard-2.0.0-rc3.tar.bz2",
                    "stability": "RC"
                },
                "19": {
                    "num": "2.0.0-rc2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/mydashboard/releases/download/2.0.0-rc2/glpi-mydashboard-2.0.0-rc2.tar.bz2",
                    "stability": "RC"
                },
                "20": {
                    "num": "2.0.0-rc1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/mydashboard/releases/download/2.0.0-rc1/glpi-mydashboard-2.0.0-rc1.tar.bz2",
                    "stability": "RC"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Ce plugin permet de remplacer le central GLPI par un dashboard",
                    "long_description": "Ce plugin permet de remplacer le central GLPI par un dashboard<br />- Redimensionnement des widgets<br />- Mode édition pour charger de nouveaux widgets<br />- Utilisation de Font Awesome<br />- Nouveaux widgets graphiques basés aussi sur une nouvelle librairie graphique : ChartJs (http://www.chartjs.org/)<br />- Affichage responsive du Dashboard<br />- Génération d’alertes sur le Dashboard à partir d’un problème"
                },
                {
                    "lang": "en",
                    "short_description": "This plugin enables you to replace GLPI central by a dashboard.",
                    "long_description": "This plugin enables you to replace GLPI central by a dashboard<br />- Scaling widgets<br />- Editing mode to load new widgets<br />- Using Awesome Font <br />- New graphic widgets also based on a new graphic library: ChartJs (http: //www.chartjs .org /)<br />- Responsive display of the Dashboard<br />Generation of alerts on the Dashboard from a problem"
                }
            ],
            "required_offers": None,
            "short_description": "This plugin enables you to replace GLPI central by a dashboard."
        },
        {
            "id": 133,
            "key": "timelineticket",
            "name": "Timelineticket",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/timelineticket/master/timelineticket.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/timelineticket/master/timelineticket.xml",
            "homepage_url": "https://github.com/pluginsGLPI/timelineticket",
            "download_url": "https://github.com/pluginsGLPI/timelineticket/releases",
            "issues_url": "https://github.com/pluginsGLPI/timelineticket/issues",
            "readme_url": "https://raw.githubusercontent.com/pluginsGLPI/timelineticket/master/README.md",
            "changelog_url": "",
            "license": "AGPL v3",
            "date_added": "2016-09-11T00:00:00.000000Z",
            "date_updated": "2024-01-28T00:00:00.000000Z",
            "download_count": 16507,
            "note": 2.96,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 8,
                    "name": "David Durieux"
                },
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                }
            ],
            "versions": [
                {
                    "num": "10.0+1.2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/timelineticket/releases/download/10.0+1.2/glpi-timelineticket-10.0+1.2.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "10.0+1.1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/timelineticket/releases/download/10.0+1.1/glpi-timelineticket-10.0+1.1.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "10.0+1.0-rc1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/timelineticket/releases/download/10.0+1.0-rc1/glpi-timelineticket-10.0+1.0-rc1.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "10.0+1.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/timelineticket/releases/download/10.0+1.0/glpi-timelineticket-10.0+1.0.tar.bz2",
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Ce plugin vous permet d&#039;ajouter un onglet Chronologie sur les tickets",
                    "long_description": "Ce plugin vous permet d&#039;ajouter un onglet Chronologie sur les tickets\n         &gt; * Historisation et statistiques sur les différents statuts du tickets\n&gt; * Historisation et statistiques sur les différents techniciens du tickets\n&gt; * Historisation et statistiques sur les différents groupes de techniciens du tickets\n&gt; * Rapport sur les temps passés sur les tickets clos"
                },
                {
                    "lang": "en",
                    "short_description": "This plugin allows you to add a Timeline tab on tickets",
                    "long_description": "This plugin allows you to add a Timeline tab on tickets\n         &gt; * History and statistics for differents status of the tickets\n&gt; * History and statistics for differents technicians of the tickets\n&gt; * History and statistics for differents technicians groups of the tickets\n&gt; * Report time spent on closed tickets "
                },
                {
                    "lang": "cs",
                    "short_description": "Tento zásuvný modul umožňuje v požadavcích přidat kartu časové osy",
                    "long_description": "Tento zásuvný modul umožňuje v požadavcích přidat kartu časové osy\n         &gt; * Historie a statistiky pro různé stavy požadavků\n&gt; * Historie a statistiky pro různé techniky požadavků\n&gt; * Historie a statistiky pro různé skupiny techniků požadavků\n&gt; * Výkaz času stráveného na uzavřených požadavcích "
                }
            ],
            "required_offers": None,
            "short_description": "This plugin allows you to add a Timeline tab on tickets"
        },
        {
            "id": 134,
            "key": "airwatch",
            "name": "Airwatch connector",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/airwatch/master/airwatch.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/airwatch/master/airwatch.xml",
            "homepage_url": "https://github.com/pluginsGLPI/airwatch",
            "download_url": "https://github.com/pluginsGLPI/airwatch/releases",
            "issues_url": "https://github.com/pluginsGLPI/airwatch/issues",
            "readme_url": "https://raw.githubusercontent.com/pluginsGLPI/airwatch/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2016-09-14T00:00:00.000000Z",
            "date_updated": "2021-04-16T00:00:00.000000Z",
            "download_count": 2221,
            "note": 3.125,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 44,
                    "name": "Teclib"
                },
                {
                    "id": 14,
                    "name": "Walid Nouh"
                }
            ],
            "versions": [],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Connector to gather inventory information from Airwatch",
                    "long_description": "Gather inventory data from Airwatch MDM tool. Data import using FusionInventory XML format. Ability to manually force a device inventory. This plugin is part of the GLPi Network subscription."
                },
                {
                    "lang": "cs",
                    "short_description": "Napojení pro získávání inventárních údajů z Airwatch",
                    "long_description": "Získávání inventárních údajů z MDM nástroje Ariwatch. Import dat ve formátu FusionInventory XML. Schopnost ručního vynucení inventarizace zařízení. Tento zásuvný modul je součástí předplatného služby GLPi Network."
                },
                {
                    "lang": "fr",
                    "short_description": "Connecteur pour récupérer les données d&#039;inventaire depuis Airwatch",
                    "long_description": "Récupération des données d&#039;inventaire de l&#039;outil de MDM Airwatch. Import des données au format XML FusionInventory. Possibilité de forcer l&#039;inventaire manuellement d&#039;un device. Ce plugin fait partie de la souscription GLPi Network."
                }
            ],
            "required_offers": None,
            "short_description": "Connector to gather inventory information from Airwatch"
        },
        {
            "id": 135,
            "key": "useditemsexport",
            "name": "Used items export",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/useditemsexport/main/plugin.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/useditemsexport/main/plugin.xml",
            "homepage_url": "https://pluginsglpi.github.io/useditemsexport/",
            "download_url": "https://github.com/pluginsGLPI/useditemsexport/releases",
            "issues_url": "https://github.com/pluginsGLPI/useditemsexport/issues",
            "readme_url": "https://raw.githubusercontent.com/pluginsGLPI/useditemsexport/main/README.md",
            "changelog_url": "",
            "license": "GPLv3",
            "date_added": "2016-11-18T00:00:00.000000Z",
            "date_updated": "2024-07-08T00:00:00.000000Z",
            "download_count": 15317,
            "note": 3.45,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": {
                "1": {
                    "num": "2.5.2",
                    "compatibility": "~10.0.1",
                    "download_url": "https://github.com/pluginsGLPI/useditemsexport/releases/download/2.5.2/glpi-useditemsexport-2.5.2.tar.bz2",
                    "stability": "stable"
                },
                "2": {
                    "num": "2.5.1",
                    "compatibility": "~10.0.1",
                    "download_url": "https://github.com/pluginsGLPI/useditemsexport/releases/download/2.5.1/glpi-useditemsexport-2.5.1.tar.bz2",
                    "stability": "stable"
                },
                "3": {
                    "num": "2.5.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/useditemsexport/releases/download/2.5.0/glpi-useditemsexport-2.5.0.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "cs",
                    "short_description": "Tento zásuvný modul umožňuje exportovat do PDF položky, evidované u daného uživatele.",
                    "long_description": "Tento zásuvný modul umožňuje exportovat do PDF položky, evidované u daného uživatele."
                },
                {
                    "lang": "en",
                    "short_description": "This plugin allows you to export a PDF of the used items by a user.",
                    "long_description": "This plugin allows you to export a PDF of the used items by a user."
                },
                {
                    "lang": "fr",
                    "short_description": "Ce plugin permet d&#039;exporter en PDF une liste des éléments utilisés par un utilisateur.",
                    "long_description": "Ce plugin permet d&#039;exporter en PDF une liste des éléments utilisés par un utilisateur."
                }
            ],
            "required_offers": None,
            "short_description": "This plugin allows you to export a PDF of the used items by a user."
        },
        {
            "id": 147,
            "key": "credit",
            "name": "Credit",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/credit/main/plugin-icon2.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/credit/main/plugin.xml",
            "homepage_url": "https://pluginsglpi.github.io/credit/",
            "download_url": "https://github.com/pluginsGLPI/credit/releases",
            "issues_url": "https://github.com/pluginsGLPI/credit/issues",
            "readme_url": "https://glpi-plugins.readthedocs.io/en/latest/credit/index.html",
            "changelog_url": "",
            "license": "GPLv3",
            "date_added": "2017-03-21T00:00:00.000000Z",
            "date_updated": "2024-06-25T00:00:00.000000Z",
            "download_count": 8184,
            "note": 4.766666666666667,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": {
                "7": {
                    "num": "1.14.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/credit/releases/download/1.14.0/glpi-credit-1.14.0.tar.bz2",
                    "stability": "stable"
                },
                "8": {
                    "num": "1.13.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/credit/releases/download/1.13.2/glpi-credit-1.13.2.tar.bz2",
                    "stability": "stable"
                },
                "9": {
                    "num": "1.13.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/credit/releases/download/1.13.1/glpi-credit-1.13.1.tar.bz2",
                    "stability": "stable"
                },
                "10": {
                    "num": "1.13.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/credit/releases/download/1.13.0/glpi-credit-1.13.0.tar.bz2",
                    "stability": "stable"
                },
                "11": {
                    "num": "1.12.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/credit/releases/download/1.12.1/glpi-credit-1.12.1.tar.bz2",
                    "stability": "stable"
                },
                "12": {
                    "num": "1.12.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/credit/releases/download/1.12.0/glpi-credit-1.12.0.tar.bz2",
                    "stability": "stable"
                },
                "13": {
                    "num": "1.11.3",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/credit/releases/download/1.11.3/glpi-credit-1.11.3.tar.bz2",
                    "stability": "stable"
                },
                "14": {
                    "num": "1.11.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/credit/releases/download/1.11.2/glpi-credit-1.11.2.tar.bz2",
                    "stability": "stable"
                },
                "15": {
                    "num": "1.11.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/credit/releases/download/1.11.1/glpi-credit-1.11.1.tar.bz2",
                    "stability": "stable"
                },
                "16": {
                    "num": "1.11.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/credit/releases/download/1.11.0/glpi-credit-1.11.0.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Ce plugin vous permet de déclarer et suivre (par entité) les consommations de différents coupons de crédits directement à partir du formulaire Ticket.",
                    "long_description": "Ce plugin vous permet de déclarer et suivre (par entité) les consommations de différents coupons de crédits directement à partir du formulaire Ticket."
                },
                {
                    "lang": "en",
                    "short_description": "This plugin allows you to declare and follow (by entity) the consumptions of different credit vouchers directly from the Ticket form.",
                    "long_description": "This plugin allows you to declare and follow (by entity) the consumptions of different credit vouchers directly from the Ticket form."
                },
                {
                    "lang": "cs",
                    "short_description": "Tento zásuvný modul umožňuje deklarovat a evidovat (podle entity) spotřebu různých kuponů s kredity přímo z formuláře požadavku.",
                    "long_description": "Tento zásuvný modul umožňuje deklarovat a evidovat (podle entity) spotřebu různých kuponů s kredity přímo z formuláře požadavku."
                }
            ],
            "required_offers": None,
            "short_description": "This plugin allows you to declare and follow (by entity) the consumptions of different credit vouchers directly from the Ticket form."
        },
        {
            "id": 149,
            "key": "xivo",
            "name": "xivo",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/xivo/main/xivo.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/xivo/main/xivo.xml",
            "homepage_url": "https://github.com/pluginsGLPI/xivo",
            "download_url": "https://github.com/pluginsGLPI/xivo/releases",
            "issues_url": "https://github.com/pluginsGLPI/xivo/issues",
            "readme_url": "https://github.com/pluginsGLPI/xivo/blob/main/README.md",
            "changelog_url": "",
            "license": "GPL V3+",
            "date_added": "2017-06-14T00:00:00.000000Z",
            "date_updated": "2024-02-08T00:00:00.000000Z",
            "download_count": 2094,
            "note": 3.3043478260869565,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                },
                {
                    "id": 31,
                    "name": "Alexandre Delaunay"
                }
            ],
            "versions": [],
            "descriptions": [
                {
                    "lang": "cs",
                    "short_description": "Napojení GLPI na XIVO nebo WAZO",
                    "long_description": "Napojení GLPI na XIVO nebo WAZO\n\nToto je seznam nyní dostupných/plánovaných funkcí:\n\n* [x] Inventorizace telefonů\n* [x] Inventarizace linek\n* [x] Přítomnost uživatelů\n* [x] Automatické otvírání požadavků nebo formulářů uživatele\n* [x] Zavolání kliknutím\n* [ ] Výpis hovorů\n* [ ] Adresář kontaktů\n\nPokud byste stáli o přidání dalších, obraťte se na Teclib e-mailem (info&#64;glpi-project.org) nebo telefonicky (&#43;33 1 79 97 02 78).\n         "
                },
                {
                    "lang": "en",
                    "short_description": "Connector for GLPI with XIVO or WAZO",
                    "long_description": "Connector for GLPI with XIVO or WAZO\n\nHere is the list of currently working/planned features:\n\n* [x] Phones inventory\n* [x] Lines inventory\n* [x] Users presence\n* [x] Auto-open tickets or users form\n* [x] Click2call\n* [ ] Call logs\n* [ ] Directory\n\nPlease contact Teclib&#039; by mail (info&#64;glpi-project.org) or phone (&#43;33 1 79 97 02 78) if you want informations for developing futures one.\n         "
                },
                {
                    "lang": "fr",
                    "short_description": "Connecteur GLPI avec XIVO ou WAZO",
                    "long_description": "Connecteur GLPI avec XIVO\n\nVoici une list des fonctionnalités courantes / planifiées:\n\n* [x] Inventaire des téléphones\n* [x] Inventaire des lignes\n* [x] Présence des utilisateurs\n* [x] Auto ouverture des formulaires des tickets ou des utilisateurs\n* [x] Appel sur clic\n* [ ] Historique des appels\n* [ ] Annuaire\n\nMerci de contacter Teclib par mail (info&#64;glpi-project.org) ou par téléphone (01 79 97 02 78) pour toutes informations sur les développements futurs."
                }
            ],
            "required_offers": None,
            "short_description": "Connector for GLPI with XIVO or WAZO"
        },
        {
            "id": 157,
            "key": "geststock",
            "name": "Stock management",
            "logo_url": None,
            "xml_url": "https://raw.githubusercontent.com/yllen/geststock/master/geststock.xml",
            "homepage_url": "https://github.com/yllen/geststock",
            "download_url": "https://github.com/yllen/geststock/releases",
            "issues_url": "https://github.com/yllen/geststock/issues",
            "readme_url": "https://github.com/yllen/geststock/wiki",
            "changelog_url": "",
            "license": "AGPLv3",
            "date_added": "2018-01-09T00:00:00.000000Z",
            "date_updated": "2024-04-18T00:00:00.000000Z",
            "download_count": 5751,
            "note": 3.0396825396825395,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 6,
                    "name": "Nelly Mahu-Lasson"
                }
            ],
            "versions": {
                "1": {
                    "num": "2.1.1",
                    "compatibility": "~10.0.3",
                    "download_url": "https://github.com/yllen/geststock/releases/download/v2.1.1/glpi-geststock-2.1.1.tar.gz",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "cs",
                    "short_description": "Globální správa skladu majetku",
                    "long_description": "Tento zásuvný modul umožňuje spravovat globálním způsobem sklad položek majetku a toto pro všechny entity. Entita zarezervuje majetek a pohyb je sledován od vydání ze skladu až po požadující entitu."
                },
                {
                    "lang": "en",
                    "short_description": "Global management for stock of assets",
                    "long_description": "This plugin allows you to manage in a global way the stock of asset items and this for all entities. An entity reserves an asset and the routing is followed since the output of the stock to the requested entity."
                },
                {
                    "lang": "fr",
                    "short_description": "Gestion de stock centralisé pour le matériel",
                    "long_description": "Ce plugin permet de gérer d&#039;une manière globale le stock des éléments de l&#039;inventaire et ce pour toutes les entités. Une entité réserve un matériel et l&#039;acheminement est suivi du départ du stock jusqu&#039;à l&#039;entité demandresse."
                }
            ],
            "required_offers": None,
            "short_description": "Global management for stock of assets"
        },
        {
            "id": 160,
            "key": "satisfaction",
            "name": "More satisfaction",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/satisfaction/master/satisfaction.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/satisfaction/master/satisfaction.xml",
            "homepage_url": "https://github.com/pluginsGLPI/satisfaction",
            "download_url": "https://github.com/pluginsGLPI/satisfaction/releases",
            "issues_url": "https://github.com/pluginsGLPI/satisfaction/issues",
            "readme_url": "https://raw.githubusercontent.com/pluginsGLPI/satisfaction/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2018-05-16T00:00:00.000000Z",
            "date_updated": "2023-08-01T00:00:00.000000Z",
            "download_count": 15857,
            "note": 3.533333333333333,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 49,
                    "name": "Infotel"
                }
            ],
            "versions": {
                "3": {
                    "num": "1.6.2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/satisfaction/releases/download/1.6.2/glpi-satisfaction-1.6.2.tar.bz2",
                    "stability": "stable"
                },
                "4": {
                    "num": "1.6.1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/satisfaction/releases/download/1.6.1/glpi-satisfaction-1.6.1.tar.bz2",
                    "stability": "stable"
                },
                "6": {
                    "num": "1.6.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/satisfaction/releases/download/1.6.0/glpi-satisfaction-1.6.0.tar.bz2",
                    "stability": "stable"
                },
                "5": {
                    "num": "1.6.0-rc1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/pluginsGLPI/satisfaction/releases/download/1.6.0-rc1/glpi-satisfaction-1.6.0-rc1.tar.bz2",
                    "stability": "RC"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Plus de satisfaction",
                    "long_description": "\n                Satisfaction est un plugin qui vous permet d&#039;ajouter des questions à l&#039;enquête de satisfaction.\n\n                Fonctionnalités\n                ---------------\n\n                - Différents questionnaires (un pour chaque entité)\n\n                - Questions multiples avec trois types de questions :\n                &#43; Liste déroulante Oui / Non\n                &#43; Zone de texte\n                &#43; Note : Il sera possible de configurer la nombre total d’étoiles.\n\n                - Ce plugin va permettre d’ajouter l’ensemble des questions configurés dans le plugin avec les deux\n                questions du cœur de GLPI.\n\n                - Ce plugin va ajouter deux nouvelles balises dans les notifications concernant les événements « Enquête\n                de satisfaction » et « Réponse à l’enquête de satisfaction ».\n                &#43; La balise « ##satisfaction.question## » va permettre d’ajouter la liste des questions du plugin.\n                &#43; La balise « ##satisfaction.answer## » va permettre d’ajouter la liste des questions et réponses du\n                plugin.\n\n            "
                },
                {
                    "lang": "en",
                    "short_description": "More satisfaction",
                    "long_description": "\n                Satisfaction is a plugin which allows you to add questions to the satisfaction survey.\n\n                Features:\n                ---------------\n\n                - Different surveys (one for each entity)\n\n                - Multiple questions with three types:\n                &#43; Yes / No dropdown list\n                &#43; Text box - Text box\n                &#43; Note: It will be possible to configure the total number of stars.\n\n                - This plugin will allow you to add all the questions configured in the plugin with the two questions of\n                the GLPI core in the satisfaction survey.\n\n                - This plugin will add two new tags to the notifications for &#34;Satisfaction survey&#34; and &#34;Satisfaction\n                survey answer&#34; events.\n                &#43; The tag &#34;##satisfaction. question##&#34; will allow you to add the list of questions of the plugin.\n                &#43; The tag &#34;##satisfaction. answer##&#34; will allow you to add the list of questions and answers of the\n                plugin.\n            "
                },
                {
                    "lang": "cs",
                    "short_description": "Více ke spokojenosti",
                    "long_description": "\n                Spokojenost je zásuvný modul který umožňuje přidávat do průzkumu o spokojenosti další otázky.\n\n                Funkce:\n                ---------------\n\n                - Různé průzkumy (jeden pro každou entitu)\n\n                - Vícero dotazů třech typů\n                &#43; Rozbalovací nabídka Ano/Ne\n                &#43; Textový box – Textový box\n                &#43; Pozn.: Bude možné nastavit celkový počet hvězdiček.\n\n                - Tento zásuvný modul zásuvný modul umožnuje přidat všechny v něm nastavené otázky ke dvěma otázkám\n                základního GLPI v průzkumu spokojenosti.\n\n                - Tento modul přidá dva nové štítky k oznámením pro události „Průzkum spokojenosti“ a „Odpověď v\n                průzkumu spokojenosti&#34;.\n                &#43; Štítek „##satisfaction. question##“ umožňí přidat seznam otázek zásuvného modulu.\n                &#43; Štítek „##satisfaction. answer##“ umožňí přidat seznam otázek a odpovědí zásuvného modulu..\n            "
                }
            ],
            "required_offers": None,
            "short_description": "More satisfaction"
        },
        {
            "id": 161,
            "key": "gdrive",
            "name": "GDrive",
            "logo_url": "https://github.com/ticgal/GDrive/raw/multimedia/gdrive.png",
            "xml_url": "https://raw.githubusercontent.com/ticgal/GDrive/multimedia/gdrive.xml",
            "homepage_url": "https://tic.gal/en/project/gdrive-integration-glpi-google-drive/",
            "download_url": "https://github.com/ticgal/GDrive/releases",
            "issues_url": "https://github.com/ticgal/GDrive/issues",
            "readme_url": "https://github.com/ticgal/GDrive/blob/master/README.md",
            "changelog_url": "",
            "license": "AGPL v3+",
            "date_added": "2018-05-31T00:00:00.000000Z",
            "date_updated": "2023-01-29T00:00:00.000000Z",
            "download_count": 7292,
            "note": 4.15,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 90,
                    "name": "TICgal"
                }
            ],
            "versions": {
                "1": {
                    "num": "2.0.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ticgal/gdrive/releases/download/2.0.0/glpi-gdrive-2.0.0.tar.tgz",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Google Drive plugin for GLPi",
                    "long_description": "GDrive allows Google Drive users to add files to every GLPI Item effortlessly."
                }
            ],
            "required_offers": None,
            "short_description": "Google Drive plugin for GLPi"
        },
        {
            "id": 165,
            "key": "archisw",
            "name": "Apps structure inventory",
            "logo_url": "https://raw.githubusercontent.com/ericferon/glpi-archisw/master/swcomponent.png",
            "xml_url": "https://raw.githubusercontent.com/ericferon/glpi-archisw/master/archisw.xml",
            "homepage_url": "https://github.com/ericferon/glpi-archisw",
            "download_url": "https://github.com/ericferon/glpi-archisw/releases",
            "issues_url": "https://github.com/ericferon/glpi-archisw/issues",
            "readme_url": "https://github.com/ericferon/glpi-archisw/blob/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2018-07-02T00:00:00.000000Z",
            "date_updated": "2024-07-05T00:00:00.000000Z",
            "download_count": 12891,
            "note": 3.357142857142857,
            "xml_state": "xml_error",
            "authors": [
                {
                    "id": 92,
                    "name": "Eric Feron"
                }
            ],
            "versions": {
                "38": {
                    "num": "3.0.20",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v3.0.20/archisw-v3.0.20.tar.gz",
                    "stability": "stable"
                },
                "40": {
                    "num": "3.0.19",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v3.0.19/archisw-v3.0.19.tar.gz",
                    "stability": "stable"
                },
                "41": {
                    "num": "3.0.18",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v3.0.18/archisw-v3.0.18.tar.gz",
                    "stability": "stable"
                },
                "42": {
                    "num": "3.0.17",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v3.0.17/archisw-v3.0.17.tar.gz",
                    "stability": "stable"
                },
                "43": {
                    "num": "3.0.16",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v3.0.16/archisw-v3.0.16.tar.gz",
                    "stability": "stable"
                },
                "44": {
                    "num": "3.0.15",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v3.0.15/archisw-v3.0.15.tar.gz",
                    "stability": "stable"
                },
                "45": {
                    "num": "3.0.14",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v3.0.14/archisw-v3.0.14.tar.gz",
                    "stability": "stable"
                },
                "46": {
                    "num": "3.0.13",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v3.0.13/archisw-v3.0.13.tar.gz",
                    "stability": "stable"
                },
                "47": {
                    "num": "3.0.12",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v3.0.12/archisw-v3.0.12.tar.gz",
                    "stability": "stable"
                },
                "48": {
                    "num": "3.0.11",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v3.0.11/archisw-v3.0.11.tar.gz",
                    "stability": "stable"
                },
                "49": {
                    "num": "3.0.10",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v3.0.10/archisw-v3.0.10.tar.gz",
                    "stability": "stable"
                },
                "31": {
                    "num": "3.0.9",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v3.0.9/archisw-v3.0.9.tar.gz",
                    "stability": "stable"
                },
                "32": {
                    "num": "3.0.8",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v3.0.8/archisw-v3.0.8.tar.gz",
                    "stability": "stable"
                },
                "33": {
                    "num": "3.0.7",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v3.0.7/archisw-v3.0.7.tar.gz",
                    "stability": "stable"
                },
                "34": {
                    "num": "3.0.6",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v3.0.6/archisw-v3.0.6.tar.gz",
                    "stability": "stable"
                },
                "35": {
                    "num": "3.0.5",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v3.0.5/archisw-v3.0.5.tar.gz",
                    "stability": "stable"
                },
                "36": {
                    "num": "3.0.4",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v3.0.4/archisw-v3.0.4.tar.gz",
                    "stability": "stable"
                },
                "37": {
                    "num": "3.0.3",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v3.0.3/archisw-v3.0.3.tar.gz",
                    "stability": "stable"
                },
                "39": {
                    "num": "3.0.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v3.0.2/archisw-v3.0.2.tar.gz",
                    "stability": "stable"
                },
                "50": {
                    "num": "3.0.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v3.0.1/archisw-v3.0.1.tar.gz",
                    "stability": "stable"
                },
                "51": {
                    "num": "3.0.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v3.0.0/archisw-v3.0.0.tar.gz",
                    "stability": "stable"
                },
                "53": {
                    "num": "2.2.15",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v2.2.15/archisw-v2.2.15.tar.gz",
                    "stability": "stable"
                },
                "54": {
                    "num": "2.2.14",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v2.2.14/archisw-v2.2.14.tar.gz",
                    "stability": "stable"
                },
                "55": {
                    "num": "2.2.13",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v2.2.13/archisw-v2.2.13.tar.gz",
                    "stability": "stable"
                },
                "56": {
                    "num": "2.2.12",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v2.2.12/archisw-v2.2.12.tar.gz",
                    "stability": "stable"
                },
                "57": {
                    "num": "2.2.11",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v2.2.11/archisw-v2.2.11.tar.gz",
                    "stability": "stable"
                },
                "58": {
                    "num": "2.2.10",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v2.2.10/archisw-v2.2.10.tar.gz",
                    "stability": "stable"
                },
                "52": {
                    "num": "2.2.9",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archisw/releases/download/v2.2.9/archisw-v2.2.9.tar.gz",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "pl",
                    "short_description": "Inwentarz twoich aplikacji. Aplikacja może składać się z kilku komponentów oprogramowania.",
                    "long_description": "Inwentarz twoich aplikacji.Aplikacja może składać się z drzewa z kilkoma poziomami komponentów oprogramowania.Możesz powiązać te komponenty oprogramowania z innymi zasobami (serwery, bazy danych, przepływy danych, ...). Możesz samodzielnie edytować właściwości poszczególnych elementów (zobacz https://github.com/ericferon/glpi-archisw/wiki/How-to-customize-the-fields)"
                },
                {
                    "lang": "cs",
                    "short_description": "Inventář vašich aplikací. Aplikace může být tvořena vícero softwarovými komponentami.",
                    "long_description": "Inventář vašich aplikací.Aplikace může být tvořena stromem o několika úrovních softwarových komponent.Tyto softwarové komponenty je možné přiřadit k ostatním prvkům inventáře (servery, databáze, toky dat, …)"
                },
                {
                    "lang": "en",
                    "short_description": "Inventory of your applications. An application can be composed by several software components.",
                    "long_description": "Inventory of your applications.An application can be composed by a tree with several levels of software components.You can associate these software components with other inventory elements (servers, databases, dataflows, ...). You can add or suppress yourself item characteristics (see https://github.com/ericferon/glpi-archisw/wiki/How-to-customize-the-fields)"
                },
                {
                    "lang": "fr",
                    "short_description": "Inventaire de vos applications. Une application peut être formée de plusieurs composants logiciels.",
                    "long_description": "Inventaire de vos applications.Une application peut être formée par une arborescence à plusieurs niveaux de composants logiciels.Ces composants logiciels peuvent être associés à d&#039;autres éléments d&#039;inventaire (serveurs, bases de données, flux de données, ...). Vous pouvez ajouter ou supprimer vous-même des caractéristiques de l&#039;application (voir https://github.com/ericferon/glpi-archisw/wiki/How-to-customize-the-fields)."
                }
            ],
            "required_offers": None,
            "short_description": "Inventory of your applications. An application can be composed by several software components."
        },
        {
            "id": 166,
            "key": "dataflows",
            "name": "Dataflows inventory",
            "logo_url": "https://raw.githubusercontent.com/ericferon/glpi-dataflows/master/dataflows.png",
            "xml_url": "https://raw.githubusercontent.com/ericferon/glpi-dataflows/master/dataflows.xml",
            "homepage_url": "https://github.com/ericferon/glpi-dataflows",
            "download_url": "https://github.com/ericferon/glpi-dataflows/releases",
            "issues_url": "https://github.com/ericferon/glpi-dataflows/issues",
            "readme_url": "https://github.com/ericferon/glpi-dataflows/blob/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2018-07-02T00:00:00.000000Z",
            "date_updated": "2024-10-31T00:00:00.000000Z",
            "download_count": 7359,
            "note": 3.5,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 92,
                    "name": "Eric Feron"
                }
            ],
            "versions": {
                "35": {
                    "num": "3.0.13",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v3.0.13/dataflows-v3.0.13.tar.gz",
                    "stability": "stable"
                },
                "36": {
                    "num": "3.0.12",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v3.0.12/dataflows-v3.0.12.tar.gz",
                    "stability": "stable"
                },
                "37": {
                    "num": "3.0.11",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v3.0.11/dataflows-v3.0.11.tar.gz",
                    "stability": "stable"
                },
                "38": {
                    "num": "3.0.10",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v3.0.10/dataflows-v3.0.10.tar.gz",
                    "stability": "stable"
                },
                "27": {
                    "num": "3.0.9",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v3.0.9/dataflows-v3.0.9.tar.gz",
                    "stability": "stable"
                },
                "28": {
                    "num": "3.0.8",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v3.0.8/dataflows-v3.0.8.tar.gz",
                    "stability": "stable"
                },
                "29": {
                    "num": "3.0.7",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v3.0.7/dataflows-v3.0.7.tar.gz",
                    "stability": "stable"
                },
                "30": {
                    "num": "3.0.6",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v3.0.6/dataflows-v3.0.6.tar.gz",
                    "stability": "stable"
                },
                "31": {
                    "num": "3.0.5",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v3.0.5/dataflows-v3.0.5.tar.gz",
                    "stability": "stable"
                },
                "32": {
                    "num": "3.0.4",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v3.0.4/dataflows-v3.0.4.tar.gz",
                    "stability": "stable"
                },
                "33": {
                    "num": "3.0.3",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v3.0.3/dataflows-v3.0.3.tar.gz",
                    "stability": "stable"
                },
                "34": {
                    "num": "3.0.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v3.0.2/dataflows-v3.0.2.tar.gz",
                    "stability": "stable"
                },
                "39": {
                    "num": "3.0.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v3.0.1/dataflows-v3.0.1.tar.gz",
                    "stability": "stable"
                },
                "40": {
                    "num": "3.0.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v3.0.0/dataflows-v3.0.0.tar.gz",
                    "stability": "stable"
                },
                "41": {
                    "num": "2.2.18",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v2.2.18/dataflows-v2.2.18.tar.gz",
                    "stability": "stable"
                },
                "42": {
                    "num": "2.2.17",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v2.2.17/dataflows-v2.2.17.tar.gz",
                    "stability": "stable"
                },
                "43": {
                    "num": "2.2.16",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v2.2.16/dataflows-v2.2.16.tar.gz",
                    "stability": "stable"
                },
                "44": {
                    "num": "2.2.15",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v2.2.15/dataflows-v2.2.15.tar.gz",
                    "stability": "stable"
                },
                "45": {
                    "num": "2.2.14",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v2.2.14/dataflows-v2.2.14.tar.gz",
                    "stability": "stable"
                },
                "46": {
                    "num": "2.2.13",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v2.2.13/dataflows-v2.2.13.tar.gz",
                    "stability": "stable"
                },
                "4": {
                    "num": "2.2.12",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v2.2.12/dataflows-v2.2.12.tar.gz",
                    "stability": "stable"
                },
                "5": {
                    "num": "2.2.11",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v2.2.11/dataflows-v2.2.11.tar.gz",
                    "stability": "stable"
                },
                "6": {
                    "num": "2.2.10",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v2.2.10/dataflows-v2.2.10.tar.gz",
                    "stability": "stable"
                },
                "0": {
                    "num": "2.2.9",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v2.2.9/dataflows-v2.2.9.tar.gz",
                    "stability": "stable"
                },
                "1": {
                    "num": "2.2.8",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v2.2.8/dataflows-v2.2.8.tar.gz",
                    "stability": "stable"
                },
                "2": {
                    "num": "2.2.7",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v2.2.7/dataflows-v2.2.7.tar.gz",
                    "stability": "stable"
                },
                "3": {
                    "num": "2.2.6",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-dataflows/releases/download/v2.2.6/dataflows-v2.2.6.tar.gz",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "cs",
                    "short_description": "Inventář toků vašich dat. Je možné zadat zdrojovou a cílovou aplikaci, typ spojení, formát výměny, četnost přenosů a kalendář, …a přiřadit datové toky k ostatním prvkům inventáře (účty pro připojení a hesla k nim, např.).",
                    "long_description": "Inventář toků vašich dat.Tento zásuvný modul umožňuje spravovat inventář datových toků (zdrojové a cílové aplikace, typ spojení, formát výměny, četnost přenosu a kalendář, …) a přiřadit tyto datové toky k prvkům inventáře.- Inventura aplikací- Je možné použít ve Službě podpory- Kontrolovat platnost údaje v kolonce zásuvným modulem Kontrola stavu- Účty pro správu přihlašovacích jmen a hesel"
                },
                {
                    "lang": "en",
                    "short_description": "Inventory of your dataflows. You can specify source and destination applications, connection type, exchange format, transfer frequency and calendar, ... (this list of characteristics can be modified and extended), and associate the dataflows with other elements of the inventory (accounts for connecting login and password, f.i).",
                    "long_description": "Inventory of your dataflows.This plugin enables you to manage the dataflows inventory (source and destination applications, connection type, exchange format, transfer frequency and calendar, ... : this list of characteristics can be modified and extended - see howto in plugin&#039;s wiki on github) and associate the dataflows with elements of the inventory.- Applications inventory- Can be used with helpdesk- Field validity check with Statecheck plugin- Accounts for connecting login/password management"
                },
                {
                    "lang": "fr",
                    "short_description": "Inventaire de vos flux de données. Vous pouvez spécifier les applications source et destination, le type de connexion, le format d&#039;échange, la fréquence et le calendrier d&#039;échange, ... (cette liste de caractéristiques peut être modifiée et étendue), et associer ces flux avec d&#039;autres éléments d&#039;inventaire (les comptes, pour les login et mot de passe de connexion aux applications, par exemple).",
                    "long_description": "Inventaire de vos flux de donnéesCe plugin vous permet de spécifier les applications source et destination, le type de connexion, le format d&#039;échange, la fréquence et le calendrier d&#039;échange, ...(cette liste de caractéristiques peut être modifiée et étendue - voir comment faire dans le wiki du plugin, sur github), et associer ces flux avec d&#039;autres éléments d&#039;inventaire- Inventaire des applications- Peut être utilisé avec le helpdesk- Contrôle de validté des champs, avec le plugin Statecheck- Comptes pour la gestion des login/mot de passe de connexion aux applications"
                }
            ],
            "required_offers": None,
            "short_description": "Inventory of your dataflows. You can specify source and destination applications, connection type, exchange format, transfer frequency and calendar, ... (this list of characteristics can be modified and extended), and associate the dataflows with other elements of the inventory (accounts for connecting login and password, f.i)."
        },
        {
            "id": 167,
            "key": "statecheck",
            "name": "Statecheck",
            "logo_url": "https://raw.githubusercontent.com/ericferon/glpi-statecheck/master/statecheck.png",
            "xml_url": "https://raw.githubusercontent.com/ericferon/glpi-statecheck/master/statecheck.xml",
            "homepage_url": "https://github.com/ericferon/glpi-statecheck",
            "download_url": "https://github.com/ericferon/glpi-statecheck/releases",
            "issues_url": "https://github.com/ericferon/glpi-statecheck/issues",
            "readme_url": "https://github.com/ericferon/glpi-statecheck/blob/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2018-07-02T00:00:00.000000Z",
            "date_updated": "2024-11-13T00:00:00.000000Z",
            "download_count": 8038,
            "note": 3.5,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 92,
                    "name": "Eric Feron"
                }
            ],
            "versions": {
                "25": {
                    "num": "2.4.4",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-statecheck/releases/download/v2.4.4/statecheck-v2.4.4.tar.gz",
                    "stability": "stable"
                },
                "26": {
                    "num": "2.4.3",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-statecheck/releases/download/v2.4.3/statecheck-v2.4.3.tar.gz",
                    "stability": "stable"
                },
                "27": {
                    "num": "2.4.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-statecheck/releases/download/v2.4.2/statecheck-v2.4.2.tar.gz",
                    "stability": "stable"
                },
                "28": {
                    "num": "2.4.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-statecheck/releases/download/v2.4.1/statecheck-v2.4.1.tar.gz",
                    "stability": "stable"
                },
                "29": {
                    "num": "2.4.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-statecheck/releases/download/v2.4.0/statecheck-v2.4.0.tar.gz",
                    "stability": "stable"
                },
                "30": {
                    "num": "2.3.9",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-statecheck/releases/download/v2.3.9/statecheck-v2.3.9.tar.gz",
                    "stability": "stable"
                },
                "31": {
                    "num": "2.3.8",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-statecheck/releases/download/v2.3.8/statecheck-v2.3.8.tar.gz",
                    "stability": "stable"
                },
                "32": {
                    "num": "2.3.7",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-statecheck/releases/download/v2.3.7/statecheck-v2.3.7.tar.gz",
                    "stability": "stable"
                },
                "33": {
                    "num": "2.3.6",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-statecheck/releases/download/v2.3.6/statecheck-v2.3.6.tar.gz",
                    "stability": "stable"
                },
                "0": {
                    "num": "2.3.5",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-statecheck/releases/download/v2.3.5/statecheck-v2.3.5.tar.gz",
                    "stability": "stable"
                },
                "1": {
                    "num": "2.3.4",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-statecheck/releases/download/v2.3.4/statecheck-v2.3.4.tar.gz",
                    "stability": "stable"
                },
                "2": {
                    "num": "2.3.3",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-statecheck/releases/download/v2.3.3/statecheck-v2.3.3.tar.gz",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "cs",
                    "short_description": "Tento zásuvný modul umožňuje ověřovat platnost kolonek formuláře.Například je možné udělat kolonku povinnou nebo ne, v závislosti na nějaké hodnotě v jiné kolonce.",
                    "long_description": "Tento zásuvný modul umožňuje ověřovat platnost kolonek formuláře.Například je možné udělat kolonku povinnou nebo ne, v závislosti na nějaké hodnotě v jiné kolonceK tomuto účelu určujete jedno nebo více pravidel:- pravidlo souvisí s 1 třídou inventáře (počítač, tok dat, …) a závisí na hodnotě 1 kolonky (&#61; 1 stav) v této třídě (např. hodnota typu nebo kategorie)- pro každé pravidlo je třeba zadat ostatní podmínky pro pravidlo, které má být spuštěno (např. je třeba, aby hodnota v jiné kolonce obsahovala nebo začínala na konkrétní hodnotu)- pro každé pravidlo určujete která kontrola je provedena (např. ještě další kolonka nemůže zůstat nevyplněná, nebo je třeba, aby odpovídala regulárnímu výrazu)Pro 1 stav je možné určit několik pravidel, s různými podpůrnými podmínkami."
                },
                {
                    "lang": "en",
                    "short_description": "This plugin let you check the validity of form fields.For instance you can make a field mandatory or not, depending on some value in another field.",
                    "long_description": "This plugin let you check the validity of form fields.For instance you can make a field mandatory or not, depending on some value in another fieldFor that purpose, you define one or more rules :- a rule is related to 1 inventory class (computer, dataflow, ...) and depends on the value of 1 field (&#61; 1 state) in this class (f.i a type or category value)- for each rule, you can specify other conditions for a rule to be fired (f.i the value of another field must contain or start with a certain value)- for each rule, you specify which check is performed (f.i yet another field may not be empty, or must comply with a regular expression)Several rules may be defined for 1 state, with different supplementary conditions."
                },
                {
                    "lang": "fr",
                    "short_description": "Ce plugin vous permet de contrôler la validité des champs d&#039;un formulaire. Par exemple, vous pouvez rendre un champ obligatoire ou pas, en fonction de certaines valeurs dans un autre champ.",
                    "long_description": "Ce plugin vous permet de contrôler la validité des champs d&#039;un formulaire.Par exemple, vous pouvez rendre un champ obligatoire ou pas, en fonction de certaines valeurs dans un autre champ.A cette fin, vous définissez une ou plusieurs règles :-Une règle est relative à une classe d&#039;inventaire (serveur, flux de données, ...) et dépend de la valeur d&#039;un champ (&#61; 1 état) dans cette classe (p.ex la valeur d&#039;un type ou d&#039;une catégorie) - Pour chaque règle, vous pouvez spécifier quelles autres conditions doivent être rencontrées pour activer la règle (p.ex la valeur d&#039;un autre champ doit contenir ou démarrer une certaine valeur)- Pour chaque règle, vous spécifiez quel contrôle doit être exécuté (p.ex un autre champ ne peut être vide, ou doit respecter une expression régulière)Plusieurs règles peuvent être définies pour un état, avec des conditions supplémentaires différentes"
                }
            ],
            "required_offers": None,
            "short_description": "This plugin let you check the validity of form fields.For instance you can make a field mandatory or not, depending on some value in another field."
        },
        {
            "id": 168,
            "key": "archifun",
            "name": "Functional area",
            "logo_url": "https://raw.githubusercontent.com/ericferon/glpi-archifun/master/funcarea.png",
            "xml_url": "https://raw.githubusercontent.com/ericferon/glpi-archifun/master/funcarea.xml",
            "homepage_url": "https://github.com/ericferon/glpi-archifun",
            "download_url": "https://github.com/ericferon/glpi-archifun/releases",
            "issues_url": "https://github.com/ericferon/glpi-archifun/issues",
            "readme_url": "https://raw.githubusercontent.com/ericferon/glpi-archifun/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2018-07-02T00:00:00.000000Z",
            "date_updated": "2024-12-29T00:00:00.000000Z",
            "download_count": 4879,
            "note": 2.260869565217391,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 92,
                    "name": "Eric Feron"
                }
            ],
            "versions": {
                "15": {
                    "num": "2.3.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archifun/releases/download/v2.3.0/archifun-v2.3.0.tar.gz",
                    "stability": "stable"
                },
                "20": {
                    "num": "2.2.11",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archifun/releases/download/v2.2.11/archifun-v2.2.11.tar.gz",
                    "stability": "stable"
                },
                "21": {
                    "num": "2.2.10",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archifun/releases/download/v2.2.10/archifun-v2.2.10.tar.gz",
                    "stability": "stable"
                },
                "16": {
                    "num": "2.2.9",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archifun/releases/download/v2.2.9/archifun-v2.2.9.tar.gz",
                    "stability": "stable"
                },
                "17": {
                    "num": "2.2.8",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archifun/releases/download/v2.2.8/archifun-v2.2.8.tar.gz",
                    "stability": "stable"
                },
                "18": {
                    "num": "2.2.7",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archifun/releases/download/v2.2.7/archifun-v2.2.7.tar.gz",
                    "stability": "stable"
                },
                "19": {
                    "num": "2.2.6",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archifun/releases/download/v2.2.6/archifun-v2.2.6.tar.gz",
                    "stability": "stable"
                },
                "0": {
                    "num": "2.2.5",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archifun/releases/download/v2.2.5/archifun-v2.2.5.tar.gz",
                    "stability": "stable"
                },
                "1": {
                    "num": "2.2.4",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archifun/releases/download/v2.2.4/archifun-v2.2.4.tar.gz",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "This plugin enables you to manage the functional areas of your enterprise architecture and associate them with elements of the inventory.",
                    "long_description": "This plugin enables you to manage the functional areas of your enterprise architecture and associate them with elements of the inventory.A functional area can be decomposed in subareas, helping you to associate inventory items (typically applications) to these functions"
                },
                {
                    "lang": "fr",
                    "short_description": "Ce plugin vous permet de définir les domaines fonctionnels de votre architecture d&#039;entreprise et de les associer à des éléments d&#039;inventaire.",
                    "long_description": "Ce plugin vous permet de définir les domaines fonctionnels de votre architecture d&#039;entreprise et de les associer à des éléments d&#039;inventaire.Un domaine fonctionnel peut être décomposé en sous-domaines, auxquels vous associez des éléments d&#039;inventaires (comme des applications, p.ex)."
                },
                {
                    "lang": "cs",
                    "short_description": "Tento zásuvný modul umožňuje spravovat oblasti funkcí podnikové architektury a přiřadit je k prvkům inventáře.",
                    "long_description": "Tento zásuvný modul umožňuje spravovat oblasti funkcí podnikové architektury a přiřadit je k prvkům inventáře.Oblast funkce může být rozčleněna do podpoblastí, což pomůže k přiřazení k položkám inventáře (typicky aplikacím) k těmto funkcím"
                }
            ],
            "required_offers": None,
            "short_description": "This plugin enables you to manage the functional areas of your enterprise architecture and associate them with elements of the inventory."
        },
        {
            "id": 169,
            "key": "archimap",
            "name": "Diagrams",
            "logo_url": "https://raw.githubusercontent.com/ericferon/glpi-archimap/master/graph.png",
            "xml_url": "https://raw.githubusercontent.com/ericferon/glpi-archimap/master/archimap.xml",
            "homepage_url": "https://github.com/ericferon/glpi-archimap",
            "download_url": "https://github.com/ericferon/glpi-archimap/releases",
            "issues_url": "https://github.com/ericferon/glpi-archimap/issues",
            "readme_url": "https://raw.githubusercontent.com/ericferon/glpi-archimap/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2018-07-02T00:00:00.000000Z",
            "date_updated": "2025-03-12T00:00:00.000000Z",
            "download_count": 17241,
            "note": 3.2717391304347827,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 92,
                    "name": "Eric Feron"
                }
            ],
            "versions": {
                "37": {
                    "num": "3.3.6",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.3.6/archimap-v3.3.6.zip",
                    "stability": "stable"
                },
                "38": {
                    "num": "3.3.5",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.3.5/archimap-v3.3.5.zip",
                    "stability": "stable"
                },
                "39": {
                    "num": "3.3.4",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.3.4/archimap-v3.3.4.zip",
                    "stability": "stable"
                },
                "40": {
                    "num": "3.3.3",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.3.3/archimap-v3.3.3.zip",
                    "stability": "stable"
                },
                "41": {
                    "num": "3.3.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.3.2/archimap-v3.3.2.zip",
                    "stability": "stable"
                },
                "42": {
                    "num": "3.3.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.3.1/archimap-v3.3.1.zip",
                    "stability": "stable"
                },
                "43": {
                    "num": "3.3.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.3.0/archimap-v3.3.0.zip",
                    "stability": "stable"
                },
                "46": {
                    "num": "3.2.21",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.2.21/archimap-v3.2.21.zip",
                    "stability": "stable"
                },
                "47": {
                    "num": "3.2.20",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.2.20/archimap-v3.2.20.zip",
                    "stability": "stable"
                },
                "48": {
                    "num": "3.2.19",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.2.19/archimap-v3.2.19.zip",
                    "stability": "stable"
                },
                "49": {
                    "num": "3.2.18",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.2.18/archimap-v3.2.18.zip",
                    "stability": "stable"
                },
                "50": {
                    "num": "3.2.17",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.2.17/archimap-v3.2.17.zip",
                    "stability": "stable"
                },
                "51": {
                    "num": "3.2.16",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.2.16/archimap-v3.2.16.zip",
                    "stability": "stable"
                },
                "52": {
                    "num": "3.2.15",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.2.15/archimap-v3.2.15.zip",
                    "stability": "stable"
                },
                "53": {
                    "num": "3.2.14",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.2.14/archimap-v3.2.14.zip",
                    "stability": "stable"
                },
                "54": {
                    "num": "3.2.13",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.2.13/archimap-v3.2.13.zip",
                    "stability": "stable"
                },
                "55": {
                    "num": "3.2.12",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.2.12/archimap-v3.2.12.zip",
                    "stability": "stable"
                },
                "56": {
                    "num": "3.2.11",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.2.11/archimap-v3.2.11.zip",
                    "stability": "stable"
                },
                "57": {
                    "num": "3.2.10",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.2.10/archimap-v3.2.10.zip",
                    "stability": "stable"
                },
                "44": {
                    "num": "3.2.9",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.2.9/archimap-v3.2.9.zip",
                    "stability": "stable"
                },
                "45": {
                    "num": "3.2.8",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.2.8/archimap-v3.2.8.zip",
                    "stability": "stable"
                },
                "0": {
                    "num": "3.2.7",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.2.7/archimap-v3.2.7.zip",
                    "stability": "stable"
                },
                "1": {
                    "num": "3.2.6",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.2.6/archimap-v3.2.6.zip",
                    "stability": "stable"
                },
                "2": {
                    "num": "3.2.5",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.2.5/archimap-v3.2.5.zip",
                    "stability": "stable"
                },
                "3": {
                    "num": "3.2.4",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.2.4/archimap-v3.2.4.zip",
                    "stability": "stable"
                },
                "4": {
                    "num": "3.2.3",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.2.3/archimap-v3.2.3.zip",
                    "stability": "stable"
                },
                "5": {
                    "num": "3.2.2",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archimap/releases/download/v3.2.2/archimap-v3.2.2.tar.gz",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "cs",
                    "short_description": "Tento zásuvný modul umožňuje vytvářet diagramy jako ve Visio (architektura) s prvky inventáře (počítače, databáze, aplikace, toky dat, umístění, dodavatele). Zásuvný modul implementuje grafický nástroj (https://www.draw.io) Draw.io v kontextu GLPI",
                    "long_description": "This plugin enables you to create Visio-like (architecture) diagrams with elements of the inventory (computers, databases, applications, dataflows, locations, suppliers). The plugin implements the Draw.io (http://www.draw.io)&#039;s graphical tool in the GLPI context.V porovnání se standardním nástrojem draw.io byla přidána jedna karta, obsahující položky z GLPI.Stejně jako všechny ostatní šablony (archimate, uml, atd), je možné i tyto přidat na panel kreslení.Ale tyto šablony jsou každá propojené na třídu inventáře: při psaní popisky v šabloně, funkce automatického dokončování hledá v GLPI položky obsahující tento štítek a tyto položky je možné volit z rozbalovací nabídky. Když je nějaká vybrána, její GLPI vlastnosti jsou propojeny s grafickým objektem.V závislosti na těchto GLPI vlastnostech, může být upraven vzhled objektu na panelu kreslení (barva pozadí, barva obrysu) nebo je možné v grafickém objektu zobrazovat některé další vlastnosti (popis, typ, stav…).Když se tyto vlastnosti změní v inventáři, popisek a/nebo vzhled grafický objektů se také přizůsobí: takže, když změníte název aplikace v GLPI, všechny grafické objekty ve všech diagramech se přizpůsobí, nebo když změníte stav aplikace v GLPI, její vzhled ve všech diagramech se změní také. Následně, vaše diagramy jsou centralizované v databázi GLPI database, a mají jednotnou prezentaci, s aktuálními informacemi a vzhledem."
                },
                {
                    "lang": "en",
                    "short_description": "This plugin enables you to create Visio-like (architecture) diagrams with elements of the inventory (computers, databases, applications, dataflows, locations, suppliers). The plugin implements the Draw.io (https://www.draw.io) graphical tool in the GLPI context",
                    "long_description": "This plugin enables you to create Visio-like (architecture) diagrams with elements of the inventory (computers, databases, applications, dataflows, locations, suppliers).The plugin implements the [Draw.io](&#34;http://www.draw.io&#34;)&#039;s graphical tool in the GLPI context.Compared to the standard draw.io tool, one tab has been added, containing the GLPI assets.You can add these shapes to the drawing pane as any other shape (archimate, uml, etc). But these shapes are each linked to an inventory class : when you type a label in the shape, an autocomplete function is looking into GLPI for inventory assets containing this label and these items can be chosen in a dropdown list. When one item of the list is selected, its GLPI properties are linked to the graphical object.Based on these GLPI properties, the appearance of the object on the drawing pane can be modified (background color, contour line) or some additional properties can be displayed in the graphical object (description, type, status, ...).When these properties are changed in the inventory, the label and/or appearance of the graphical object is also adapted : so, when you change the name of an application in GLPI, all the graphical objects in all the diagrams are adapted, or when you change the status of an application, its appearance changes in all diagrams too. Consequently, your diagrams are centralized in the GLPI database, and have a uniform presentation, with up to date information and appearance.You can add new GLPI assets by creating a new library or by modifying the provided default one.You can find more details in the wiki (https://github.com/ericferon/glpi-archimap/wiki)Per diagram, you can specify which are your display preferences (look in the menu File-&gt;Preferences) : you can choose which properties are displayed as label (name, description, ...) and whether icons are also displayed to further identify the graphical objects."
                },
                {
                    "lang": "fr",
                    "short_description": "Ce plugin vous permet de créer des diagrammes d&#039;architecture, du style Visio, avec des éléments d&#039;inventaire (server, bases de données, applications, flux de données, emplacements, fournisseurs). Le plugin implémente l&#039;outil graphique Draw.io (https://www.draw.io) dans le contexte GLPI.",
                    "long_description": "Ce plugin vous permet de créer des diagrammes d&#039;architecture, du style Visio, avec des éléments d&#039;inventaire (server, bases de données, applications, flux de données, emplacements, fournisseurs). Le plugin implémente l&#039;outil graphique Draw.io (http://www.draw.io) dans le contexte GLPI.En comparaison de l&#039;outil draw.io standard, un onglet contenant les éléments d&#039;inventaire GLPI a été ajouté.Vous pouvez ajouter ces objets graphiques sur la table à dessin, comme les autres objets graphiques (archimate, uml, etc ...). Mais ces objets graphiques sont chacunes liées à une classe d&#039;inventaire : quand vous entrez un nom dans l&#039;objet graphique, une fonction d&#039;autocomplétion cherche dans GLPI les éléments d&#039;inventaire contenant ce nom, qui apparaissent dans une liste déroulante. Quand un élément est sélectionné dans la liste, ses propriétés GLPI (description, type, statut, ...) sont liées à l&#039;objet graphique.  Quand ces propriétés sont changées dans l&#039;inventaire, la dénomination et/ou l&#039;apparence de l&#039;objet graphique est aussi adaptée : ainsi, quand vous changez le nom d&#039;une application dans GLPI, tous les objets graphiques dans tous les diagrammes sont adaptés, ou quand vous changez le statut d&#039;une application, son apparence change dans tous les diagrammes également. En conséquence, vos diagrammes sont centralisés dans la base de données de GLPI et ont une présentation uniforme, avec une information et une apparence actuelles.  Vous pouvez ajouter de nouveaux éléments d&#039;inventaire en créant une nouvelle librairie ou en modifiant celle fournie par défaut. Vous pouvez trouver plus de détails dans le wiki (https://github.com/ericferon/glpi-archimap/wiki)Par diagramme, vous pouvez spécifier quelles sont vos préférences d&#039;affichage (via le menu Fichier-&gt;Préférences) : vous pouvez choisir quelles propriétés sont affichées comme label (nom, description, ...) et si les icônes sont affichées pour mieux identifier les objets graphiques"
                }
            ],
            "required_offers": None,
            "short_description": "This plugin enables you to create Visio-like (architecture) diagrams with elements of the inventory (computers, databases, applications, dataflows, locations, suppliers). The plugin implements the Draw.io (https://www.draw.io) graphical tool in the GLPI context"
        },
        {
            "id": 171,
            "key": "metabase",
            "name": "Metabase",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/metabase/main/logo.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/metabase/main/metabase.xml",
            "homepage_url": "https://github.com/pluginsGLPI/metabase",
            "download_url": "https://github.com/pluginsGLPI/metabase/releases",
            "issues_url": "https://github.com/pluginsGLPI/metabase/issues",
            "readme_url": "https://github.com/pluginsGLPI/metabase/blob/main/Readme.md",
            "changelog_url": "",
            "license": "AGPLv3",
            "date_added": "2018-08-17T00:00:00.000000Z",
            "date_updated": "2024-02-08T00:00:00.000000Z",
            "download_count": 11621,
            "note": 3.0483870967741935,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": {
                "6": {
                    "num": "1.3.3",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/metabase/releases/download/1.3.3/glpi-metabase-1.3.3.tar.bz2",
                    "stability": "stable"
                },
                "7": {
                    "num": "1.3.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/metabase/releases/download/1.3.2/glpi-metabase-1.3.2.tar.bz2",
                    "stability": "stable"
                },
                "8": {
                    "num": "1.3.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/metabase/releases/download/1.3.1/glpi-metabase-1.3.1.tar.bz2",
                    "stability": "stable"
                },
                "9": {
                    "num": "1.3.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/metabase/releases/download/1.3.0/glpi-metabase-1.3.0.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "This plugin eases integration of GLPI with Metabase",
                    "long_description": "\nThis plugin eases integration of GLPI with [Metabase](https://www.metabase.com/). \n\nIt currently permits to: \n\n* Connect to Metabase API.\n* Push database configuration or use existing configured db in Metabase.\n* Push GLPI foreign keys in Metabase datamodel\n* Push GLPI enumeration (tickets impacts/urgency/priority/types) in metabase datamodel\n* Push questions, collections and dashboards (if exists).\n* Integrate Metabase dashboards into GLPI (on Central).\n* Manage profiles (dashboards publication)\n* import existing questions/dashboards/collection from Metabase and save them as json\n\n[Teclib&#039;](http://www.teclib-group.com/) provides with [GLPI Network](https://services.glpi-network.com/) distribution, additional services like support for installation, questions and dashboards conception.\n         "
                },
                {
                    "lang": "fr",
                    "short_description": "Ce plugin facilite l&#039;intégration de GLPI avec Metabase",
                    "long_description": "\nCe plugin facilite l&#039;intégration de GLPI avec [Metabase](https://www.metabase.com/). \n\nIl permet actuellement de: \n\n* Se connecter à l&#039;API de Metabase.\n* Pousser la configuration de la base de données ou d&#039;utiliser une base de données configurée dans Metabase.\n* Pousser les clefs étrangère dans le modèle de données de Metabase\n* Pousser les énumérations (champs impact/urgence/priorité/type des tickets) dans le modèle de données\n* Pousser les questions, collections et tableaux de bords (si ils existent)\n* Intégrer les tableaux de bord de Metabase dans GLPI (sur la page centrale)\n* Gérer les profils (publication des tableaux de bord)\n* Importer les questions, collections et tableaux de bord existant depuis Metabase et les enregistrer au format JSON\n\n[Teclib&#039;](http://www.teclib-group.com/) fournit avec la distribution [GLPI Network](https://services.glpi-network.com/) des services additionnels comme du support pour l&#039;installation, de la conception de questions et tableaux de bord.\n         "
                }
            ],
            "required_offers": None,
            "short_description": "This plugin eases integration of GLPI with Metabase"
        },
        {
            "id": 179,
            "key": "costs",
            "name": "Costs",
            "logo_url": "https://raw.githubusercontent.com/ticgal/costs/multimedia/costs.png",
            "xml_url": "https://raw.githubusercontent.com/ticgal/costs/multimedia/costs.xml",
            "homepage_url": "https://tic.gal/en/project/costs-control-plugin-glpi/",
            "download_url": "https://github.com/ticgal/costs/releases",
            "issues_url": "https://github.com/ticgal/costs/issues",
            "readme_url": "https://github.com/ticgal/costs/blob/master/README.md",
            "changelog_url": "",
            "license": "AGPL v3+",
            "date_added": "2018-10-10T00:00:00.000000Z",
            "date_updated": "2024-03-05T00:00:00.000000Z",
            "download_count": 9953,
            "note": 4.3125,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 90,
                    "name": "TICgal"
                }
            ],
            "versions": {
                "2": {
                    "num": "3.0.3",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ticgal/costs/releases/download/3.0.3/glpi-costs-3.0.3.tar.tgz",
                    "stability": "stable"
                },
                "3": {
                    "num": "3.0.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ticgal/costs/releases/download/3.0.1/glpi-costs-3.0.1.tar.tgz",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Automatic costs generation for GLPI",
                    "long_description": "Costs plugin helps your organisation generating ticket costs automatically using a per entity configuration."
                },
                {
                    "lang": "es",
                    "short_description": "Generación automática de costes para GLPI",
                    "long_description": "El módulo Costs se alinea con tu organización generando los costes de las peticiones de manera automática, según la configuración de cada entidad."
                }
            ],
            "required_offers": None,
            "short_description": "Automatic costs generation for GLPI"
        },
        {
            "id": 180,
            "key": "metademands",
            "name": "MetaDemands",
            "logo_url": "https://raw.githubusercontent.com/InfotelGLPI/metademands/master/metademands.png",
            "xml_url": "https://raw.githubusercontent.com/InfotelGLPI/metademands/master/metademands.xml",
            "homepage_url": "https://github.com/InfotelGLPI/metademands",
            "download_url": "https://github.com/InfotelGLPI/metademands/releases",
            "issues_url": "https://github.com/InfotelGLPI/metademands/issues",
            "readme_url": "https://github.com/InfotelGLPI/metademands/wiki",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2018-11-13T00:00:00.000000Z",
            "date_updated": "2025-03-13T00:00:00.000000Z",
            "download_count": 10696,
            "note": 2.95,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                },
                {
                    "id": 49,
                    "name": "Infotel"
                }
            ],
            "versions": {
                "17": {
                    "num": "3.3.19",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.3.19/glpi-metademands-3.3.19.tar.bz2",
                    "stability": "stable"
                },
                "18": {
                    "num": "3.3.18",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.3.18/glpi-metademands-3.3.18.tar.bz2",
                    "stability": "stable"
                },
                "19": {
                    "num": "3.3.17",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.3.17/glpi-metademands-3.3.17.tar.bz2",
                    "stability": "stable"
                },
                "20": {
                    "num": "3.3.16",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.3.16/glpi-metademands-3.3.16.tar.bz2",
                    "stability": "stable"
                },
                "21": {
                    "num": "3.3.15",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.3.15/glpi-metademands-3.3.15.tar.bz2",
                    "stability": "stable"
                },
                "22": {
                    "num": "3.3.14",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.3.14/glpi-metademands-3.3.14.tar.bz2",
                    "stability": "stable"
                },
                "23": {
                    "num": "3.3.13",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.3.13/glpi-metademands-3.3.13.tar.bz2",
                    "stability": "stable"
                },
                "24": {
                    "num": "3.3.12",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.3.12/glpi-metademands-3.3.12.tar.bz2",
                    "stability": "stable"
                },
                "25": {
                    "num": "3.3.11",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.3.11/glpi-metademands-3.3.11.tar.bz2",
                    "stability": "stable"
                },
                "26": {
                    "num": "3.3.10",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.3.10/glpi-metademands-3.3.10.tar.bz2",
                    "stability": "stable"
                },
                "9": {
                    "num": "3.3.9",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.3.9/glpi-metademands-3.3.9.tar.bz2",
                    "stability": "stable"
                },
                "10": {
                    "num": "3.3.8",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.3.8/glpi-metademands-3.3.8.tar.bz2",
                    "stability": "stable"
                },
                "11": {
                    "num": "3.3.7",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.3.7/glpi-metademands-3.3.7.tar.bz2",
                    "stability": "stable"
                },
                "12": {
                    "num": "3.3.6",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.3.6/glpi-metademands-3.3.6.tar.bz2",
                    "stability": "stable"
                },
                "13": {
                    "num": "3.3.5",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.3.5/glpi-metademands-3.3.5.tar.bz2",
                    "stability": "stable"
                },
                "14": {
                    "num": "3.3.4",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.3.4/glpi-metademands-3.3.4.tar.bz2",
                    "stability": "stable"
                },
                "15": {
                    "num": "3.3.3",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.3.3/glpi-metademands-3.3.3.tar.bz2",
                    "stability": "stable"
                },
                "16": {
                    "num": "3.3.2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.3.2/glpi-metademands-3.3.2.tar.bz2",
                    "stability": "stable"
                },
                "27": {
                    "num": "3.3.1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.3.1/glpi-metademands-3.3.1.tar.bz2",
                    "stability": "stable"
                },
                "28": {
                    "num": "3.3.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.3.0/glpi-metademands-3.3.0.tar.bz2",
                    "stability": "stable"
                },
                "37": {
                    "num": "3.2.19",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.2.19/glpi-metademands-3.2.19.tar.bz2",
                    "stability": "stable"
                },
                "38": {
                    "num": "3.2.18",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.2.18/glpi-metademands-3.2.18.tar.bz2",
                    "stability": "stable"
                },
                "39": {
                    "num": "3.2.17",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.2.17/glpi-metademands-3.2.17.tar.bz2",
                    "stability": "stable"
                },
                "40": {
                    "num": "3.2.16",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.2.16/glpi-metademands-3.2.16.tar.bz2",
                    "stability": "stable"
                },
                "41": {
                    "num": "3.2.15",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.2.15/glpi-metademands-3.2.15.tar.bz2",
                    "stability": "stable"
                },
                "42": {
                    "num": "3.2.14",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.2.14/glpi-metademands-3.2.14.tar.bz2",
                    "stability": "stable"
                },
                "43": {
                    "num": "3.2.13",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.2.13/glpi-metademands-3.2.13.tar.bz2",
                    "stability": "stable"
                },
                "44": {
                    "num": "3.2.12",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.2.12/glpi-metademands-3.2.12.tar.bz2",
                    "stability": "stable"
                },
                "45": {
                    "num": "3.2.11",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.2.11/glpi-metademands-3.2.11.tar.bz2",
                    "stability": "stable"
                },
                "46": {
                    "num": "3.2.10",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.2.10/glpi-metademands-3.2.10.tar.bz2",
                    "stability": "stable"
                },
                "29": {
                    "num": "3.2.9",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.2.9/glpi-metademands-3.2.9.tar.bz2",
                    "stability": "stable"
                },
                "30": {
                    "num": "3.2.8",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.2.8/glpi-metademands-3.2.8.tar.bz2",
                    "stability": "stable"
                },
                "31": {
                    "num": "3.2.7",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.2.7/glpi-metademands-3.2.7.tar.bz2",
                    "stability": "stable"
                },
                "32": {
                    "num": "3.2.6",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.2.6/glpi-metademands-3.2.6.tar.bz2",
                    "stability": "stable"
                },
                "33": {
                    "num": "3.2.5",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.2.5/glpi-metademands-3.2.5.tar.bz2",
                    "stability": "stable"
                },
                "34": {
                    "num": "3.2.4",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.2.4/glpi-metademands-3.2.4.tar.bz2",
                    "stability": "stable"
                },
                "35": {
                    "num": "3.2.3",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.2.3/glpi-metademands-3.2.3.tar.bz2",
                    "stability": "stable"
                },
                "36": {
                    "num": "3.2.2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.2.2/glpi-metademands-3.2.2.tar.bz2",
                    "stability": "stable"
                },
                "47": {
                    "num": "3.2.1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.2.1/glpi-metademands-3.2.1.tar.bz2",
                    "stability": "stable"
                },
                "48": {
                    "num": "3.2.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.2.0/glpi-metademands-3.2.0.tar.bz2",
                    "stability": "stable"
                },
                "49": {
                    "num": "3.1.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.1.0/glpi-metademands-3.1.0.tar.bz2",
                    "stability": "stable"
                },
                "50": {
                    "num": "3.0.1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.0.1/glpi-metademands-3.0.1.tar.bz2",
                    "stability": "stable"
                },
                "53": {
                    "num": "3.0.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.0.0/glpi-metademands-3.0.0.tar.bz2",
                    "stability": "stable"
                },
                "51": {
                    "num": "3.0.0-rc2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.0.0-rc2/glpi-metademands-3.0.0-rc2.tar.bz2",
                    "stability": "RC"
                },
                "52": {
                    "num": "3.0.0-rc1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/metademands/releases/download/3.0.0-rc1/glpi-metademands-3.0.0-rc1.tar.bz2",
                    "stability": "RC"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Ce plugin permet de créer des wizards pour gérer des demandes complexes dans GLPI qui génèreront des tickets enfants attribués à des groupes de techniciens différents",
                    "long_description": "Ce plugin permet de créer des wizards pour gérer des demandes complexes dans GLPI qui génèreront des tickets enfants attribués à des groupes de techniciens différents.<br /> Caractéristiques: <br /> - Générez vos propres assistants <br /> - Lien avec la catégorie de ticket pour la lancer automatiquement <br /> - Créez un ticket père / enfant <br /> - Création semi-automatique de tickets enfants <br /> - Planification des tickets créés <br /> - Créer un panier de vos demandes<br /> - Créer un PDF pour vos demandes <br /> - Traduction des formulaires<br /> - Meta Incidents <br /> - Meta Changements<br /> - Enregistrez vos formulaires comme brouillon <br /> - Utilisez des balises pour les titres <br /> - Boutons Bootstrap"
                },
                {
                    "lang": "en",
                    "short_description": "This plugin allows you to create wizards to handle complex requests in GLPI that will generate child tickets assigned to different groups of technicians",
                    "long_description": "This plugin allows you to create wizards to handle complex requests in GLPI that will generate child tickets assigned to different groups of technicians.<br />Characteristics :<br />- Generate your own assistants<br />- Link with the ticket category to launch it automatically<br />- Create a father / childs tickets<br />- Semi-automatic creation of child tickets<br />- Scheduling created tickets<br />- Create basket for your demands<br />- Create PDF for your demands<br />- Translation of forms<br />- Meta Incidents<br />- Meta Changes<br />- Save your forms as Draft<br />- Use tags for titles<br />- Bootstrap Buttons"
                }
            ],
            "required_offers": None,
            "short_description": "This plugin allows you to create wizards to handle complex requests in GLPI that will generate child tickets assigned to different groups of technicians"
        },
        {
            "id": 181,
            "key": "actualtime",
            "name": "ActualTime",
            "logo_url": "https://raw.githubusercontent.com/ticgal/actualtime/multimedia/actualtime.png",
            "xml_url": "https://raw.githubusercontent.com/ticgal/actualtime/multimedia/actualtime.xml",
            "homepage_url": "https://tic.gal/glpi/glpi-plugins/actualtime-the-time-tracking-plugin-for-glpi/",
            "download_url": "https://github.com/ticgal/actualtime/releases",
            "issues_url": "https://github.com/ticgal/actualtime/issues",
            "readme_url": "https://github.com/ticgal/actualtime/blob/master/README.md",
            "changelog_url": "",
            "license": "AGPL v3+",
            "date_added": "2018-11-16T00:00:00.000000Z",
            "date_updated": "2025-02-28T00:00:00.000000Z",
            "download_count": 23035,
            "note": 3.426470588235294,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 90,
                    "name": "TICgal"
                }
            ],
            "versions": {
                "3": {
                    "num": "3.2.0",
                    "compatibility": "~10.0.10",
                    "download_url": "https://github.com/ticgal/actualtime/releases/download/3.2.0/glpi-actualtime-3.2.0.tar.bz2",
                    "stability": "stable"
                },
                "4": {
                    "num": "3.0.0",
                    "compatibility": "~10.0.10",
                    "download_url": "https://github.com/ticgal/actualtime/releases/download/3.0.0/glpi-actualtime-3.0.0.tar.tgz",
                    "stability": "stable"
                },
                "5": {
                    "num": "2.2.0",
                    "compatibility": "~10.0.10",
                    "download_url": "https://github.com/ticgal/actualtime/releases/download/2.2.0/glpi-actualtime-2.2.0.tar.tgz",
                    "stability": "stable"
                },
                "6": {
                    "num": "2.1.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ticgal/actualtime/releases/download/2.1.0/glpi-actualtime-2.1.0.tar.tgz",
                    "stability": "stable"
                },
                "7": {
                    "num": "2.0.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ticgal/actualtime/releases/download/2.0.0/glpi-actualtime-2.0.0.tar.tgz",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Adds actual time tracking for GLPI tasks",
                    "long_description": "ActualTime tracks actual task time tracking for GLPI ticket tasks and compares it to planned time."
                },
                {
                    "lang": "es",
                    "short_description": "Registrar el tiempo real de ejecución de cada tarea para GLPI",
                    "long_description": "El módulo ActualTime se alinea con tu organización añadiendo la posibilidad de registrar el tiempo real de ejecución de cada tarea en GLPI"
                }
            ],
            "required_offers": None,
            "short_description": "Adds actual time tracking for GLPI tasks"
        },
        {
            "id": 183,
            "key": "taskdrop",
            "name": "Task'n'Drop",
            "logo_url": "https://raw.githubusercontent.com/ticgal/taskdrop/multimedia/taskdrop.png",
            "xml_url": "https://raw.githubusercontent.com/ticgal/taskdrop/multimedia/taskdrop.xml",
            "homepage_url": "https://tic.gal/glpi/glpi-plugins/taskndrop-easy-task-scheduling-for-glpi/",
            "download_url": "https://github.com/ticgal/taskdrop/releases",
            "issues_url": "https://github.com/ticgal/taskdrop/issues",
            "readme_url": "https://github.com/ticgal/taskdrop/blob/master/README.md",
            "changelog_url": "",
            "license": "AGPL v3+",
            "date_added": "2019-01-17T00:00:00.000000Z",
            "date_updated": "2024-12-31T00:00:00.000000Z",
            "download_count": 8989,
            "note": 3.9166666666666665,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 90,
                    "name": "TICgal"
                }
            ],
            "versions": {
                "1": {
                    "num": "2.1.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ticgal/taskdrop/releases/download/2.1.0/glpi-taskdrop-2.1.0.tar.tgz",
                    "stability": "stable"
                },
                "2": {
                    "num": "2.0.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ticgal/taskdrop/releases/download/2.0.0/glpi-taskdrop-2.0.0.tar.tgz",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Enables drag&#039;n&#039;drop for not scheduled ticket tasks and reminders",
                    "long_description": "Drag&#039;n&#039;dropping ticket tasks are the fastest and most efficient way to schedule your recurrent tickets and Reminders. Combine it with GLPI Reminders extension for Chrome and Firefox to reduce your planning time."
                }
            ],
            "required_offers": None,
            "short_description": "Enables drag&#039;n&#039;drop for not scheduled ticket tasks and reminders"
        },
        {
            "id": 187,
            "key": "yagp",
            "name": "YAGP",
            "logo_url": "https://raw.githubusercontent.com/ticgal/yagp/multimedia/yagp.png",
            "xml_url": "https://raw.githubusercontent.com/ticgal/yagp/multimedia/yagp.xml",
            "homepage_url": "https://tic.gal/en/project/yagp-yet-another-glpi-plugin/",
            "download_url": "https://github.com/ticgal/yagp/releases",
            "issues_url": "https://github.com/ticgal/yagp/issues",
            "readme_url": "https://github.com/ticgal/yagp/blob/master/README.md",
            "changelog_url": "",
            "license": "AGPL v3+",
            "date_added": "2019-04-16T00:00:00.000000Z",
            "date_updated": "2024-03-16T00:00:00.000000Z",
            "download_count": 7300,
            "note": 3.8333333333333335,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 90,
                    "name": "TICgal"
                }
            ],
            "versions": {
                "4": {
                    "num": "2.3.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ticgal/yagp/releases/download/2.3.1/glpi-yagp-2.3.1.tar.tgz",
                    "stability": "stable"
                },
                "5": {
                    "num": "2.2.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ticgal/yagp/releases/download/2.2.2/glpi-yagp-2.2.2.tar.tgz",
                    "stability": "stable"
                },
                "6": {
                    "num": "2.2.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ticgal/yagp/releases/download/2.2.1/glpi-yagp-2.2.1.tar.tgz",
                    "stability": "stable"
                },
                "7": {
                    "num": "2.2.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ticgal/yagp/releases/download/2.2.0/glpi-yagp-2.2.0.tar.tgz",
                    "stability": "stable"
                },
                "8": {
                    "num": "2.1.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ticgal/yagp/releases/download/2.1.1/glpi-yagp-2.1.1.tar.tgz",
                    "stability": "stable"
                },
                "9": {
                    "num": "2.0.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ticgal/yagp/releases/download/2.0.0/glpi-yagp-2.0.0.tar.tgz",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Yet Another GLPI Plugin",
                    "long_description": "YAGP is meant to be a place where small GLPI tweaks that don&#039;t justify a full-fledged plugin.\n        It can enable this enhacements:\n        *Change ticket solved date to last task end time\n        *Auto renew tacit contracts\n        *Fixed Menu\n\t*Go to ticket\t\t\n        "
                },
                {
                    "lang": "es",
                    "short_description": "Yet Another GLPI Plugin",
                    "long_description": "YAGP es un &#34;cajón de sastre&#34; donde añadiremos todas las pequeñas mejoras de GLPI que no justifiquen un plugin específico.\n        Puede habilitar estas dos mejoras:\n        * Cambiar fecha de solución por la fecha de fin de la ultima tarea\n        * Auto renovación de contratos tácitos\n\t* Menú fijo\n\t* Ir a ticket\n        "
                }
            ],
            "required_offers": None,
            "short_description": "Yet Another GLPI Plugin"
        },
        {
            "id": 188,
            "key": "activity",
            "name": "Activity",
            "logo_url": "https://raw.githubusercontent.com/InfotelGLPI/activity/master/wiki/activity.png",
            "xml_url": "https://raw.githubusercontent.com/InfotelGLPI/activity/master/activity.xml",
            "homepage_url": "https://github.com/InfotelGLPI/activity",
            "download_url": "https://github.com/InfotelGLPI/activity/releases",
            "issues_url": "https://github.com/InfotelGLPI/activity/issues",
            "readme_url": "https://raw.githubusercontent.com/InfotelGLPI/activity/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2019-04-29T00:00:00.000000Z",
            "date_updated": "2024-07-16T00:00:00.000000Z",
            "download_count": 9206,
            "note": 2.875,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                },
                {
                    "id": 49,
                    "name": "Infotel"
                }
            ],
            "versions": [
                {
                    "num": "3.1.5",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/activity/releases/download/3.1.5/glpi-activity-3.1.5.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "3.1.4",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/activity/releases/download/3.1.4/glpi-activity-3.1.4.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "3.1.2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/activity/releases/download/3.1.2/glpi-activity-3.1.2.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "3.1.1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/activity/releases/download/3.1.1/glpi-activity-3.1.1.tar.bz2",
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Gestion de vos activités. Ce plugin vous permet d&#039;ajouter des activités dans le planning. Gestion des congés.",
                    "long_description": "Gestion de vos activités. Ce plugin vous permet d&#039;ajouter des activités dans le planning. Gestion des congés."
                },
                {
                    "lang": "en",
                    "short_description": "Activity management. This plugin allows you add your activities into planning. Holidays management.",
                    "long_description": "Activity management. This plugin allows you add your activities into planning. Holidays management.n"
                }
            ],
            "required_offers": None,
            "short_description": "Activity management. This plugin allows you add your activities into planning. Holidays management."
        },
        {
            "id": 191,
            "key": "holiday",
            "name": "holiday",
            "logo_url": "https://services.glpi-network.com/api/glpi-network/1579/logo.png",
            "xml_url": "https://services.glpi-network.com/api/glpi-network/1579/plugin.xml",
            "homepage_url": "https://services.glpi-network.com/",
            "download_url": "https://services.glpi-network.com/",
            "issues_url": "https://services.glpi-network.com/",
            "readme_url": "https://services.glpi-network.com/documentation/1579/file/README.md",
            "changelog_url": "",
            "license": "GPL V2+",
            "date_added": "2019-05-03T00:00:00.000000Z",
            "date_updated": "2024-02-12T00:00:00.000000Z",
            "download_count": 3304,
            "note": 3.142857142857143,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": [
                {
                    "num": "1.2.0",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "holiday GLPI plugin.",
                    "long_description": "\nThis GLPI plugin fills the holidays based on the user locale.\n\nAs a data source, it uses the library [Yasumi](https://azuyalabs.github.io/yasumi),\nthe list of supported countries is available on [this page](https://azuyalabs.github.io/yasumi/features/).\n\nSubscribe to [GLPI-Network](https://services.glpi-network.com/) to get it.\n         "
                },
                {
                    "lang": "fr",
                    "short_description": "Plugin GLPI holiday",
                    "long_description": "\nCe plugin GLPI remplis les dates de congés en se basant sur la langue utilisateur.\n\nComme source de données, il utilise la bibliothèque [Yasumi](https://azuyalabs.github.io/yasumi), \nla liste des pays pris en charge est disponible sur [cette page](https://azuyalabs.github.io/yasumi/features/).\n\nSouscrivez à [GLPI-Network](https://services.glpi-network.com/) pour en bénéficier.\n         "
                }
            ],
            "required_offers": [
                "network-basic",
                "network-standard",
                "network-advanced"
            ],
            "short_description": "holiday GLPI plugin."
        },
        {
            "id": 192,
            "key": "splitcat",
            "name": "Splitcat",
            "logo_url": "https://services.glpi-network.com/api/glpi-network/1336/logo.png",
            "xml_url": "https://services.glpi-network.com/api/glpi-network/1336/plugin.xml",
            "homepage_url": "https://services.glpi-network.com/",
            "download_url": "https://services.glpi-network.com/",
            "issues_url": "https://services.glpi-network.com/",
            "readme_url": "https://services.glpi-network.com/documentation/1336/file/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2019-05-03T00:00:00.000000Z",
            "date_updated": "2024-09-09T00:00:00.000000Z",
            "download_count": 3552,
            "note": 3.015625,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": [
                {
                    "num": "1.6.2",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.6.1",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.6.0",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.5.3",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.5.2",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.5.1",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.5.0",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Split of ITIL categories tree",
                    "long_description": "\nThis plugin transforms ITIL categories dropdown into multiple selects (one for each level of the tree).\nSubscribe to [GLPI-Network](https://services.glpi-network.com/) to get it.\n         "
                },
                {
                    "lang": "fr",
                    "short_description": "Division de l&#039;arbre des catégories ITIL",
                    "long_description": "\nCe plugin GLPI qui transforme la liste de choix de catégorie ITIL en plusieurs listes (une pour chaque niveau de l&#039;arbre).\nSouscrivez à [GLPI-Network](https://services.glpi-network.com/) pour en bénéficier.\n         "
                }
            ],
            "required_offers": [
                "network-basic",
                "network-standard",
                "network-advanced"
            ],
            "short_description": "Split of ITIL categories tree"
        },
        {
            "id": 193,
            "key": "branding",
            "name": "Branding",
            "logo_url": "https://services.glpi-network.com/api/glpi-network/1565/logo.png",
            "xml_url": "https://services.glpi-network.com/api/glpi-network/1565/plugin.xml",
            "homepage_url": "https://services.glpi-network.com/",
            "download_url": "https://services.glpi-network.com/",
            "issues_url": "https://services.glpi-network.com/",
            "readme_url": "https://services.glpi-network.com/documentation/1565/file/README.md",
            "changelog_url": "",
            "license": "GPL V2+",
            "date_added": "2019-05-06T00:00:00.000000Z",
            "date_updated": "2025-03-06T00:00:00.000000Z",
            "download_count": 15453,
            "note": 3.4210526315789473,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": [
                {
                    "num": "3.0.0",
                    "compatibility": "~10.0.11",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "2.0.3",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "2.0.2",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "2.0.1",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "2.0.0",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.4.1",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.4.0",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.3.3",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.3.2",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.3.1",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.3.0",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Branding GLPI plugin.",
                    "long_description": "\nChange your GLPI logo.\nSubscribe to [GLPI-Network](https://services.glpi-network.com/) to get it.\n         "
                },
                {
                    "lang": "fr",
                    "short_description": "Plugin GLPI Branding",
                    "long_description": "\nModifiez votre logo GLPI.\nSouscrivez à [GLPI-Network](https://services.glpi-network.com/) pour en bénéficier.\n         "
                }
            ],
            "required_offers": [
                "network-basic",
                "network-standard",
                "network-advanced"
            ],
            "short_description": "Branding GLPI plugin."
        },
        {
            "id": 205,
            "key": "jamf",
            "name": "JAMF Plugin for GLPI",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/jamf/master/Logo.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/jamf/master/jamf.xml",
            "homepage_url": "https://github.com/pluginsGLPI/jamf",
            "download_url": "https://github.com/pluginsGLPI/jamf/releases",
            "issues_url": "https://github.com/pluginsGLPI/jamf/issues",
            "readme_url": "https://github.com/pluginsGLPI/jamf/blob/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2019-07-01T00:00:00.000000Z",
            "date_updated": "2024-07-03T00:00:00.000000Z",
            "download_count": 2868,
            "note": 3.4375,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                },
                {
                    "id": 103,
                    "name": "Curtis Conard"
                }
            ],
            "versions": {
                "15": {
                    "num": "3.1.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/jamf/releases/download/v3.1.2/glpi-jamf-v3.1.2.tar.bz2",
                    "stability": "stable"
                },
                "16": {
                    "num": "3.1.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/jamf/releases/download/v3.1.1/glpi-jamf-v3.1.1.tar.bz2",
                    "stability": "stable"
                },
                "17": {
                    "num": "3.0.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/jamf/releases/download/v3.0.2/glpi-jamf-v3.0.2.tar.bz2",
                    "stability": "stable"
                },
                "18": {
                    "num": "3.0.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/jamf/releases/download/v3.0.1/glpi-jamf-v3.0.1.tar.bz2",
                    "stability": "stable"
                },
                "19": {
                    "num": "3.0.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/jamf/releases/download/v3.0.0/glpi-jamf-v3.0.0.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Sync devices and data from Jamf to GLPI",
                    "long_description": "\nThis plugin allows you to sync mobile devices and computers from Jamf Pro to GLPI along with their associated data. It also allows you to issue mobile device commands from GLPI.\n\nUsage\n- Server/sync configuration is found in Setup &gt; Config under the JAMF Plugin tab.\n- JSS User account used must have read access to mobile devices and computers at least. Additional access may be required depending on what items are synced (software, etc).\n- The two automatic actions &#34;importJamf&#039; and &#039;syncJamf&#34; can only be run in CLI/Cron mode due to how long they can take.\n- There is a rule engine used to filter out imported devices. The default import action is to allow the import.\n            "
                }
            ],
            "required_offers": None,
            "short_description": "Sync devices and data from Jamf to GLPI"
        },
        {
            "id": 207,
            "key": "gappessentials",
            "name": "Gapp Essentials",
            "logo_url": "https://raw.githubusercontent.com/ticgal/gappessentials/multimedia/gappessentials.png",
            "xml_url": "https://raw.githubusercontent.com/ticgal/gappessentials/multimedia/gappessentials.xml",
            "homepage_url": "https://tic.gal/en/project/gappessentials/",
            "download_url": "https://github.com/ticgal/gappessentials/releases",
            "issues_url": "https://github.com/ticgal/gappessentials/issues",
            "readme_url": "https://github.com/ticgal/gappessentials/blob/master/README.md",
            "changelog_url": "",
            "license": "AGPL v3+",
            "date_added": "2019-09-12T00:00:00.000000Z",
            "date_updated": "2024-03-06T00:00:00.000000Z",
            "download_count": 16583,
            "note": 3.482142857142857,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 90,
                    "name": "TICgal"
                }
            ],
            "versions": {
                "8": {
                    "num": "2.3.0",
                    "compatibility": "^10.0.3",
                    "download_url": "https://github.com/ticgal/gappessentials/releases/download/2.3.0/glpi-gappessentials-2.3.0.tar.tgz",
                    "stability": "stable"
                },
                "9": {
                    "num": "2.2.0",
                    "compatibility": "^10.0.3",
                    "download_url": "https://github.com/ticgal/gappessentials/releases/download/2.2.0/glpi-gappessentials-2.2.0.tar.tgz",
                    "stability": "stable"
                },
                "10": {
                    "num": "2.1.2",
                    "compatibility": "^10.0.3",
                    "download_url": "https://github.com/ticgal/gappessentials/releases/download/2.1.2/glpi-gappessentials-2.1.2.tar.tgz",
                    "stability": "stable"
                },
                "11": {
                    "num": "2.1.1",
                    "compatibility": "^10.0.3",
                    "download_url": "https://github.com/ticgal/gappessentials/releases/download/2.1.1/glpi-gappessentials-2.1.1.tar.tgz",
                    "stability": "stable"
                },
                "12": {
                    "num": "2.1.0",
                    "compatibility": "^10.0.3",
                    "download_url": "https://github.com/ticgal/gappessentials/releases/download/2.1.0/glpi-gappessentials-2.1.0.tar.tgz",
                    "stability": "stable"
                },
                "3": {
                    "num": "2.0.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ticgal/gappessentials/releases/download/2.0.2/glpi-gappessentials-2.0.2.tar.tgz",
                    "stability": "stable"
                },
                "4": {
                    "num": "2.0.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ticgal/gappessentials/releases/download/2.0.1/glpi-gappessentials-2.0.1.tar.tgz",
                    "stability": "stable"
                },
                "5": {
                    "num": "2.0.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ticgal/gappessentials/releases/download/2.0.0/glpi-gappessentials-2.0.0.tar.tgz",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Gapp essentials is a mandatory plugin to enable extended functionalities on Gapp, a GLPI mobile app.",
                    "long_description": "\n\t\tGapp Essentials is a mandatory plugin for enabling \n\t\tadvanced functionalities within Gapp, the mobile application\n\t\tfor GLPI.\n           \n\t\tBeginning with Gapp 2, the Gapp Essentials plugin has \n\t\tbecome a prerequisite for the app&#039;s operation.\n\n\t\tWe strongly recommend updating GLPI to safeguard against\n\t\tsecurity vulnerabilities. \n\t\tThe versions currently supported are:\n                -10.0.3&#43;\n\t\t     \n                Currently enables:\n                -Access to ticket documents\n                -Plugins list to Self-service users\n                -Max. uploadable file size \n                -Allowed filetypes\n                -Download file size\n            \n                "
                }
            ],
            "required_offers": None,
            "short_description": "Gapp essentials is a mandatory plugin to enable extended functionalities on Gapp, a GLPI mobile app."
        },
        {
            "id": 212,
            "key": "collaborativetools",
            "name": "Collaborative tools",
            "logo_url": "https://services.glpi-network.com/api/glpi-network/1533/logo.png",
            "xml_url": "https://services.glpi-network.com/api/glpi-network/1533/plugin.xml",
            "homepage_url": "https://services.glpi-network.com/",
            "download_url": "https://services.glpi-network.com/",
            "issues_url": "https://services.glpi-network.com/",
            "readme_url": "https://services.glpi-network.com/documentation/1533/file/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2020-04-03T00:00:00.000000Z",
            "date_updated": "2024-08-22T00:00:00.000000Z",
            "download_count": 6236,
            "note": 3.727272727272727,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": [
                {
                    "num": "1.2.5",
                    "compatibility": "~10.0.11",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.2.4",
                    "compatibility": "~10.0.11",
                    "download_url": None,
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Collaborative tools connectors",
                    "long_description": "\nThis plugin aims to provide connectors for web collaborative tools.  \nIt currently push notifications to HTTP &#96;incoming webhooks&#96; for the following services:\n\n* Mattermost\n* Microsoft Teams\n* Rocket.Chat\n* Slack\n* Telegram\n\nSubscribe to [GLPI-Network](https://services.glpi-network.com/) to get it.\n         "
                },
                {
                    "lang": "fr",
                    "short_description": "Connecteurs outils collaboratifs",
                    "long_description": "\nCe plugin fournit des connecteur pour les outils de collaborations Web.  \nIl envoit actuellement des notificationss aux &#96;webhooks entrants&#96; HTTP pour les services suivants :\n\n* Mattermost\n* Microsoft Teams\n* Rocket.Chat\n* Slack\n* Telegram\n\nSouscrivez à [GLPI-Network](https://services.glpi-network.com/) pour en bénéficier.\n         "
                }
            ],
            "required_offers": [
                "network-basic",
                "network-standard",
                "network-advanced"
            ],
            "short_description": "Collaborative tools connectors"
        },
        {
            "id": 214,
            "key": "advancedplanning",
            "name": "advancedplanning",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/advancedplanning/main/advancedplanning.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/advancedplanning/main/advancedplanning.xml",
            "homepage_url": "https://github.com/pluginsGLPI/advancedplanning",
            "download_url": "https://github.com/pluginsGLPI/advancedplanning/releases",
            "issues_url": "https://github.com/pluginsGLPI/advancedplanning/issues",
            "readme_url": "https://github.com/pluginsGLPI/advancedplanning/blob/main/README.md",
            "changelog_url": "",
            "license": "GPL V3+",
            "date_added": "2020-04-23T00:00:00.000000Z",
            "date_updated": "2025-01-15T00:00:00.000000Z",
            "download_count": 13538,
            "note": 3.1964285714285716,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": {
                "3": {
                    "num": "1.1.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/advancedplanning/releases/download/1.1.1/glpi-advancedplanning-1.1.1.tar.bz2",
                    "stability": "stable"
                },
                "4": {
                    "num": "1.1.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/advancedplanning/releases/download/1.1.0/glpi-advancedplanning-1.1.0.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "This plugin unlock advanced planning features (Scheduler view) in GLPI (Home &gt; Assistance &gt; Planning)",
                    "long_description": "\nThis plugin unlock advanced planning features (Scheduler view) in GLPI (Home &gt; Assistance &gt; Planning).\n\nGlpi uses [Fullcalendar lib](fullcalendar.io/) to display its planning.\nThe [scheduler part](https://fullcalendar.io/license/premium) is triple licenced, the GLPI case is supported by the option 3 : open source.\nAs the option 3 is released under GLPV3, we can&#039;t use it directly in GLPI as it&#039;s incompatible with our licence (GPLv2&#43;).\n\nSo this plugin just include the lib and add the option &#96;schedulerLicenseKey: &#039;GPL-My-Project-Is-Open-Source&#039;&#96; to avoid licence incompatibility.\n         "
                },
                {
                    "lang": "fr",
                    "short_description": "Ce plugin débloque les fonctionnalités avancées (Vue planification) dans GLPI (menu Accueil &gt; Assistance &gt; Planning)",
                    "long_description": "\nCe plugin débloque les fonctionnalités avancées (Vue planification) dans GLPI (menu Accueil &gt; Assistance &gt; Planning).\n\nGlpi inclut [la bibliothèque Fullcalendar](fullcalendar.io/) pour afficher son planning.\nLa [partie planification](https://fullcalendar.io/license/premium) est sous triple licences, le cas de GLPI est couvert par l&#039;option 3: open source.\nComme l&#039;option est sous licence GLPV3, nous ne pouvous pas l&#039;utiliser directement dans GLPI, celle ci étant incompatible avec notre licence (GPLv2&#43;).\n\nDonc ce plugin inclut juste la bibliothèque et ajouter l&#039;option &#96;schedulerLicenseKey: &#039;GPL-My-Project-Is-Open-Source&#039;&#96; pour éviter les incompatibilités.\n         "
                }
            ],
            "required_offers": None,
            "short_description": "This plugin unlock advanced planning features (Scheduler view) in GLPI (Home &gt; Assistance &gt; Planning)"
        },
        {
            "id": 220,
            "key": "webresources",
            "name": "Web Resources",
            "logo_url": "https://raw.githubusercontent.com/cconard96/glpi-webresources-plugin/master/Logo40.png",
            "xml_url": "https://raw.githubusercontent.com/cconard96/glpi-webresources-plugin/master/webresources.xml",
            "homepage_url": "https://github.com/cconard96/glpi-webresources-plugin",
            "download_url": "https://github.com/cconard96/glpi-webresources-plugin/releases",
            "issues_url": "https://github.com/cconard96/glpi-webresources-plugin/issues",
            "readme_url": "https://github.com/cconard96/glpi-webresources-plugin/blob/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2020-07-19T00:00:00.000000Z",
            "date_updated": "2024-04-15T00:00:00.000000Z",
            "download_count": 9886,
            "note": 4.5,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 103,
                    "name": "Curtis Conard"
                }
            ],
            "versions": {
                "7": {
                    "num": "2.0.4",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/glpi-webresources-plugin/releases/download/v2.0.4/glpi-webresources-v2.0.4.tar.bz2",
                    "stability": "stable"
                },
                "8": {
                    "num": "2.0.3",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/glpi-webresources-plugin/releases/download/v2.0.3/glpi-webresources-v2.0.3.tar.bz2",
                    "stability": "stable"
                },
                "9": {
                    "num": "2.0.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/glpi-webresources-plugin/releases/download/v2.0.2/glpi-webresources-v2.0.2.tar.bz2",
                    "stability": "stable"
                },
                "10": {
                    "num": "2.0.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/glpi-webresources-plugin/releases/download/v2.0.1/glpi-webresources-v2.0.1.tar.bz2",
                    "stability": "stable"
                },
                "13": {
                    "num": "2.0.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/glpi-webresources-plugin/releases/download/v2.0.0/glpi-webresources-v2.0.0.tar.bz2",
                    "stability": "stable"
                },
                "11": {
                    "num": "2.0.0-beta2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/glpi-webresources-plugin/releases/download/v2.0.0-beta2/glpi-webresources-v2.0.0-beta2.tar.bz2",
                    "stability": "beta"
                },
                "12": {
                    "num": "2.0.0-beta1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/glpi-webresources-plugin/releases/download/v2.0.0-beta1/glpi-webresources-v2.0.0-beta1.tar.bz2",
                    "stability": "beta"
                }
            },
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Adds a dashboard for web resources",
                    "long_description": "\nAdds a dashboard for web resources.\nResources can be scoped to specific Entities, Profiles, Groups, or Users (or a mix).\nResources can have an image icon (favicon for example), or a FontAwesome icon like &#039;fab fa-github&#34;.\nNon-image icons can have their colors changed as you see fit.\n\nResources can be any weblink or a link with a special URI scheme. For example these links are all valid:\n- https://glpi-project.org (Standard URL)\n- market://details?id&#61;org.glpi.inventory.agent&amp;hl&#61;en_US (Link to app on Android&#039;s Play Store)\n- softwarecenter://Page&#61;AvailableSoftware (Link to the Available Software page in the SCCM/MEM Software Center)\nFor more information about URI schemes please refer to https://en.wikipedia.org/wiki/List_of_URI_schemes.\n            "
                }
            ],
            "required_offers": None,
            "short_description": "Adds a dashboard for web resources"
        },
        {
            "id": 223,
            "key": "cmdb",
            "name": "Cmdb",
            "logo_url": "https://raw.githubusercontent.com/InfotelGLPI/cmdb/master/pics/service.png",
            "xml_url": "https://raw.githubusercontent.com/InfotelGLPI/cmdb/master/cmdb.xml",
            "homepage_url": "https://github.com/InfotelGLPI/cmdb",
            "download_url": "https://github.com/InfotelGLPI/cmdb/releases",
            "issues_url": "https://github.com/InfotelGLPI/cmdb/issues",
            "readme_url": "https://github.com/InfotelGLPI/cmdb/wiki",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2020-07-30T00:00:00.000000Z",
            "date_updated": "2022-06-14T00:00:00.000000Z",
            "download_count": 6444,
            "note": 3.35,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                },
                {
                    "id": 49,
                    "name": "Infotel"
                }
            ],
            "versions": [
                {
                    "num": "3.0.3",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/cmdb/releases/download/3.0.3/glpi-cmdb-3.0.3.tar.bz2",
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Ce plugin permet d&#039;ajouter un objet Service et d&#039;autres objets divers pour l&#039;analyse d&#039;impact",
                    "long_description": "Ce plugin permet d&#039;ajouter un objet Service et d&#039;autres objets divers pour l&#039;analyse d&#039;impact"
                },
                {
                    "lang": "en",
                    "short_description": "This plugin allows you to add a Service object and other miscellaneous objects for impact analysis",
                    "long_description": "This plugin allows you to add a Service object and other miscellaneous objects for impact analysis"
                }
            ],
            "required_offers": None,
            "short_description": "This plugin allows you to add a Service object and other miscellaneous objects for impact analysis"
        },
        {
            "id": 225,
            "key": "anonymize",
            "name": "anonymize",
            "logo_url": "https://services.glpi-network.com/api/glpi-network/1688/logo.png",
            "xml_url": "https://services.glpi-network.com/api/glpi-network/1688/plugin.xml",
            "homepage_url": "https://services.glpi-network.com/",
            "download_url": "https://services.glpi-network.com/",
            "issues_url": "https://services.glpi-network.com/",
            "readme_url": "https://services.glpi-network.com/documentation/1688/file/README.md",
            "changelog_url": "",
            "license": "GPL V3+",
            "date_added": "2020-09-03T00:00:00.000000Z",
            "date_updated": "2024-07-31T00:00:00.000000Z",
            "download_count": 2093,
            "note": 4.038461538461538,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": [
                {
                    "num": "2.7.1",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "2.7.0",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "GLPI data Anonymization",
                    "long_description": "\nThis plugin will allow the data anonymization in GLPI, directly from the web interface or with the command line, either unitarily or massively.\n\nSubscribe to [GLPI-Network](https://services.glpi-network.com/) to get it.\n         "
                },
                {
                    "lang": "fr",
                    "short_description": "Anonymisation des données GLPI",
                    "long_description": "\nCe plugin permet d&#039;anonymiser des données contenues dans la base de GLPI.\n\nL&#039;anonymisation se fait à partir d&#039;un profil (qui défini quelles données rendre anonyme, et de quelle manière), que l&#039;on applique soit en action massive, soit en ligne de commande (obligatoire en cas de base de données importante).\n\nSouscrivez à [GLPI-Network](https://services.glpi-network.com/) pour en bénéficier.\n         "
                }
            ],
            "required_offers": [
                "network-basic",
                "network-standard",
                "network-advanced"
            ],
            "short_description": "GLPI data Anonymization"
        },
        {
            "id": 226,
            "key": "approvalbymail",
            "name": "ApprovalByMail",
            "logo_url": "https://services.glpi-network.com/api/glpi-network/1465/logo.png",
            "xml_url": "https://services.glpi-network.com/api/glpi-network/1465/plugin.xml",
            "homepage_url": "https://services.glpi-network.com/",
            "download_url": "https://services.glpi-network.com/",
            "issues_url": "https://services.glpi-network.com/",
            "readme_url": "https://services.glpi-network.com/documentation/1465/file/README.md",
            "changelog_url": "",
            "license": "GPL V2+",
            "date_added": "2020-09-03T00:00:00.000000Z",
            "date_updated": "2025-02-26T00:00:00.000000Z",
            "download_count": 5352,
            "note": 3.736111111111111,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": [
                {
                    "num": "2.2.3",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "2.2.2",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "2.2.1",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "2.2.0",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "2.1.2",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "2.1.1",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "2.1.0",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "ApprovalByMail GLPI plugin.",
                    "long_description": "\nThis plugin allows to answer a validation request directly from mail without logging to GLPI\nThis plugin allows to answer a satisfaction survey directly from mail without logging to GLPI\nThis plugin allows you to respond to a solution directly from the email\n\nSubscribe to [GLPI-Network](https://services.glpi-network.com/) to get it.\n            "
                },
                {
                    "lang": "fr",
                    "short_description": "Plugin GLPI ApprovalByMail",
                    "long_description": "\nCe plugin permet de répondre à une demande d&#039;approbation directement depuis le mail\nCe plugin permet de répondre à une enquête de satisfaction directement depuis le mail\nCe plugin permet de répondre à une solution directement depuis le mail\n\nSouscrivez à [GLPI-Network](https://services.glpi-network.com/) pour en bénéficier.\n            "
                }
            ],
            "required_offers": [
                "network-standard",
                "network-advanced"
            ],
            "short_description": "ApprovalByMail GLPI plugin."
        },
        {
            "id": 227,
            "key": "screenshot",
            "name": "Screenshot",
            "logo_url": "https://raw.githubusercontent.com/cconard96/glpi-screenshot-plugin/master/Logo.png",
            "xml_url": "https://raw.githubusercontent.com/cconard96/glpi-screenshot-plugin/master/screenshot.xml",
            "homepage_url": "https://github.com/cconard96/glpi-screenshot-plugin",
            "download_url": "https://github.com/cconard96/glpi-screenshot-plugin/releases",
            "issues_url": "https://github.com/cconard96/glpi-screenshot-plugin/issues",
            "readme_url": "https://github.com/cconard96/glpi-screenshot-plugin/blob/master/README.md",
            "changelog_url": "",
            "license": "GPLv2+",
            "date_added": "2020-09-29T00:00:00.000000Z",
            "date_updated": "2024-01-12T00:00:00.000000Z",
            "download_count": 17268,
            "note": 3.46875,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 103,
                    "name": "Curtis Conard"
                }
            ],
            "versions": {
                "8": {
                    "num": "2.0.3",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/glpi-screenshot-plugin/releases/download/v2.0.3/glpi-screenshot-v2.0.3.tar.bz2",
                    "stability": "stable"
                },
                "9": {
                    "num": "2.0.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/glpi-screenshot-plugin/releases/download/v2.0.2/glpi-screenshot-v2.0.2.tar.bz2",
                    "stability": "stable"
                },
                "10": {
                    "num": "2.0.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/glpi-screenshot-plugin/releases/download/v2.0.1/glpi-screenshot-v2.0.1.tar.bz2",
                    "stability": "stable"
                },
                "12": {
                    "num": "2.0.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/glpi-screenshot-plugin/releases/download/v2.0.0/glpi-screenshot-v2.0.0.tar.bz2",
                    "stability": "stable"
                },
                "11": {
                    "num": "2.0.0-beta1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/glpi-screenshot-plugin/releases/download/v2.0.0-beta1/glpi-screenshot-v2.0.0-beta1.tar.bz2",
                    "stability": "beta"
                }
            },
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Take a screenshot or screen recording directly from GLPI and attach it to a ticket, change or problem",
                    "long_description": "\nTake a screenshot directly from GLPI and attach it to a ticket, change or problem. Only works from the timeline for now.\n\nThis plugin should work on any modern desktop browser, but it won&#039;t work on mobile browsers.\n\nAdditionally, browsers only expose this feature when it is being used over HTTPS (or running over localhost). If your GLPI server doesn&#039;t use HTTPS yet, this plugin will not work.\n        "
                }
            ],
            "required_offers": None,
            "short_description": "Take a screenshot or screen recording directly from GLPI and attach it to a ticket, change or problem"
        },
        {
            "id": 228,
            "key": "releases",
            "name": "Releases management",
            "logo_url": "https://raw.githubusercontent.com/InfotelGLPI/releases/master/releases.png",
            "xml_url": "https://raw.githubusercontent.com/InfotelGLPI/releases/master/releases.xml",
            "homepage_url": "https://github.com/InfotelGLPI/releases",
            "download_url": "https://github.com/InfotelGLPI/releases/releases",
            "issues_url": "https://github.com/InfotelGLPI/releases/issues",
            "readme_url": "https://raw.githubusercontent.com/InfotelGLPI/releases/master/README.md",
            "changelog_url": "",
            "license": "GPLv2+",
            "date_added": "2020-09-29T00:00:00.000000Z",
            "date_updated": "2024-11-02T00:00:00.000000Z",
            "download_count": 4306,
            "note": 4.166666666666667,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                },
                {
                    "id": 114,
                    "name": "Alban Lesellier"
                },
                {
                    "id": 49,
                    "name": "Infotel"
                }
            ],
            "versions": {
                "0": {
                    "num": "2.0.4",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/releases/releases/download/2.0.4/glpi-releases-2.0.4.tar.bz2",
                    "stability": "stable"
                },
                "1": {
                    "num": "2.0.3",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/releases/releases/download/2.0.3/glpi-releases-2.0.3.tar.bz2",
                    "stability": "stable"
                },
                "2": {
                    "num": "2.0.2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/releases/releases/download/2.0.2/glpi-releases-2.0.2.tar.bz2",
                    "stability": "stable"
                },
                "3": {
                    "num": "2.0.1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/releases/releases/download/2.0.1/glpi-releases-2.0.1.tar.bz2",
                    "stability": "stable"
                },
                "5": {
                    "num": "2.0.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/releases/releases/download/2.0.0/glpi-releases-2.0.0.tar.bz2",
                    "stability": "stable"
                },
                "4": {
                    "num": "2.0.0-rc1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/releases/releases/download/2.0.0-rc1/glpi-releases-2.0.0-rc1.tar.bz2",
                    "stability": "RC"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Plugin de gestion de mises en production de changements",
                    "long_description": "Plugin de gestion de mises en production de changements.\nLe plugin permet de créer des mises en productions de changement ayant lieu au sein du service informatique.\nLe plugin permet :\n        <br />- De lancer la mise en production de changements grâce à des modèles prédéfinis\n        <br />- De définir des risques, retours arrières, tâches de déploiements et des tests\n        <br />- De finaliser les mises en productions ou de les marquer comme échouées\n   "
                },
                {
                    "lang": "en",
                    "short_description": "Change releases management plugin",
                    "long_description": "Plugin for managing changes in production.\nThe plugin allows you to create productions of change taking place within the IT department.\nThe plugin allows:\n         <br /> - To start the production of changes thanks to predefined models\n         <br /> - Define risks, backtracking, deployment tasksand tests\n         <br /> - To finalize the releases or to mark them as failed\n    "
                }
            ],
            "required_offers": None,
            "short_description": "Change releases management plugin"
        },
        {
            "id": 229,
            "key": "oauthimap",
            "name": "Oauth IMAP",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/oauthimap/main/docs/logo.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/oauthimap/main/oauthimap.xml",
            "homepage_url": "https://github.com/pluginsGLPI/oauthimap/",
            "download_url": "https://github.com/pluginsGLPI/oauthimap/releases",
            "issues_url": "https://github.com/pluginsGLPI/oauthimap/issues",
            "readme_url": "https://glpi-plugins.readthedocs.io/en/latest/oauthimap/index.html",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2020-10-09T00:00:00.000000Z",
            "date_updated": "2024-02-08T00:00:00.000000Z",
            "download_count": 25260,
            "note": 3.4930555555555554,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": {
                "12": {
                    "num": "1.4.3",
                    "compatibility": "~10.0.7",
                    "download_url": "https://github.com/pluginsGLPI/oauthimap/releases/download/1.4.3/glpi-oauthimap-1.4.3.tar.bz2",
                    "stability": "stable"
                },
                "13": {
                    "num": "1.4.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/oauthimap/releases/download/1.4.2/glpi-oauthimap-1.4.2.tar.bz2",
                    "stability": "stable"
                },
                "14": {
                    "num": "1.4.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/oauthimap/releases/download/1.4.1/glpi-oauthimap-1.4.1.tar.bz2",
                    "stability": "stable"
                },
                "15": {
                    "num": "1.4.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/oauthimap/releases/download/1.4.0/glpi-oauthimap-1.4.0.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Ce plugin supporte la connexion Oauth pour les collecteurs de mails",
                    "long_description": "\nCe plugin supporte la connexion Oauth pour les collecteurs de mails.\nCeci permet de collecter des emails sur les boîtes mail des domaines G Suite et Azure AD.\n         "
                },
                {
                    "lang": "en",
                    "short_description": "This plugin supports Oauth connection for emails receivers",
                    "long_description": "\nThis plugin supports Oauth connection for emails receivers\nIt permits emails fetching from G Suite and Azure AD mailboxes.\n         "
                }
            ],
            "required_offers": None,
            "short_description": "This plugin supports Oauth connection for emails receivers"
        },
        {
            "id": 230,
            "key": "jsaddons",
            "name": "JS Addons",
            "logo_url": "https://raw.githubusercontent.com/ticgal/jsaddons/multimedia/jsaddons.png",
            "xml_url": "https://raw.githubusercontent.com/ticgal/jsaddons/multimedia/jsaddons.xml",
            "homepage_url": "https://tic.gal/en/project/jsaddons/",
            "download_url": "https://github.com/ticgal/jsaddons/releases",
            "issues_url": "https://github.com/ticgal/jsaddons/issues",
            "readme_url": "https://github.com/ticgal/jsaddons/blob/master/README.md",
            "changelog_url": "",
            "license": "AGPL v3+",
            "date_added": "2020-10-09T00:00:00.000000Z",
            "date_updated": "2022-11-06T00:00:00.000000Z",
            "download_count": 3477,
            "note": 4.625,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 90,
                    "name": "TICgal"
                }
            ],
            "versions": {
                "1": {
                    "num": "2.0.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ticgal/jsaddons/releases/download/2.0.0/glpi-jsaddons-2.0.0.tar.tgz",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Allows the use of several useful web tools by inserting their JS snippets",
                    "long_description": "JS Addons is developed to allow the use of several useful web tools in GLPI by inserting JavaScript snippets for them to execute. Currently, JS Addons supports:<ul><li>Analytics:</li><ul><li><a href=\"http://mtr.cool/yfuhbk\">Metricool</a></li><li>Google Analytics</li></ul><li>Chat:</li><ul><li><a href=\"https://www.tawk.to/?pid&#61;snaotzu\">Tawk.to</a></li></ul></ul>"
                }
            ],
            "required_offers": None,
            "short_description": "Allows the use of several useful web tools by inserting their JS snippets"
        },
        {
            "id": 232,
            "key": "oauthsso",
            "name": "Oauthsso",
            "logo_url": "https://services.glpi-network.com/api/glpi-network/1731/logo.png",
            "xml_url": "https://services.glpi-network.com/api/glpi-network/1731/plugin.xml",
            "homepage_url": "https://services.glpi-network.com/",
            "download_url": "https://services.glpi-network.com/",
            "issues_url": "https://services.glpi-network.com/",
            "readme_url": "https://services.glpi-network.com/documentation/1731/file/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2020-10-23T00:00:00.000000Z",
            "date_updated": "2024-05-10T00:00:00.000000Z",
            "download_count": 9093,
            "note": 3.3055555555555554,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": [
                {
                    "num": "1.10.1",
                    "compatibility": "~10.0.7",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.10.0",
                    "compatibility": "~10.0.7",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.9.10",
                    "compatibility": "~10.0.7",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.9.9",
                    "compatibility": "~10.0.7",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.9.8",
                    "compatibility": "~10.0.7",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.9.7",
                    "compatibility": "~10.0.7",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.9.6",
                    "compatibility": "~10.0.7",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.9.5",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.9.4",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.9.3",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.9.2",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.9.1",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.9.0",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.8.1",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.8.0",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.7.1",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.7.0",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.6.1",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.6.0",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Ce plugin permet la connexion automatique à GLPI via des fournisseurs externes (google, facebook, openid, etc)",
                    "long_description": "\nCe plugin permet la connexion automatique à GLPI via des fournisseurs externes (google, facebook, openid, etc)\nSouscrivez à [GLPI-Network](https://services.glpi-network.com/) pour en bénéficier.\n         "
                },
                {
                    "lang": "en",
                    "short_description": "This plugin allows to auto-login on GLPI vwith external provider (google, facebook, openid, etc)",
                    "long_description": "\nThis plugin allows to auto-login on GLPI vwith external provider (google, facebook, openid, etc)\nSubscribe to [GLPI-Network](https://services.glpi-network.com/) to get it.\n         "
                }
            ],
            "required_offers": [
                "network-basic",
                "network-standard",
                "network-advanced"
            ],
            "short_description": "This plugin allows to auto-login on GLPI vwith external provider (google, facebook, openid, etc)"
        },
        {
            "id": 233,
            "key": "advanceddashboard",
            "name": "Advanced GLPI dashboards",
            "logo_url": "https://services.glpi-network.com/api/glpi-network/1726/logo.png",
            "xml_url": "https://services.glpi-network.com/api/glpi-network/1726/plugin.xml",
            "homepage_url": "https://services.glpi-network.com",
            "download_url": "https://services.glpi-network.com",
            "issues_url": "https://services.glpi-network.com",
            "readme_url": "https://services.glpi-network.com/documentation/1726/file/README.md",
            "changelog_url": "",
            "license": "GPL V3+",
            "date_added": "2020-11-05T00:00:00.000000Z",
            "date_updated": "2024-12-24T00:00:00.000000Z",
            "download_count": 13713,
            "note": 3.373684210526316,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": [
                {
                    "num": "1.6.2",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.6.1",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.6.0",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.5.3",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.5.2",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.5.1",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.5.0",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.4.5",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.4.4",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.4.3",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.4.2",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.4.1",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.4.0",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "SQL queries for GLPI dashboards.",
                    "long_description": "\nThis plugin allows administrators to create new data providers for the GLPI dasboards.\nIt currently permits to:\n\n- create connections to external MySQL databases;\n- write SQL queries (with cool autocompletion) and save them as a data provider for a dashboard;\n- query GLPI database or external ones\n- export or embed results.\n- use saved searches in dashboards\n         "
                },
                {
                    "lang": "fr",
                    "short_description": "Requêtes SQL pour les tableaux de bord GLPI",
                    "long_description": "\nCe plugin autorise les administrateurs à créer des nouveaux fournisseurs de données pour les tableaux de bord GLPI.\nIl permet actuellement de :\n\n- créer des connexions vers des bases de données MySQL externes;\n- écrire des requêtes SQL (avec une completion sympa) et les sauvegarder comme fournisseurs de données pour un tableau de bord;\n- requêter vers la BDD GLPI ou des externes\n- exporter ou intégrer les résultats.\n- utiliser les recherches sauvegardées dans les tableaux de bords\n         "
                }
            ],
            "required_offers": [
                "network-standard",
                "network-advanced"
            ],
            "short_description": "SQL queries for GLPI dashboards."
        },
        {
            "id": 237,
            "key": "localeoverride",
            "name": "Rename GLPI strings",
            "logo_url": "https://services.glpi-network.com/api/glpi-network/1725/logo.png",
            "xml_url": "https://services.glpi-network.com/api/glpi-network/1725/plugin.xml",
            "homepage_url": "https://services.glpi-network.com",
            "download_url": "https://services.glpi-network.com",
            "issues_url": "https://services.glpi-network.com",
            "readme_url": "https://services.glpi-network.com/documentation/1725/file/README.md",
            "changelog_url": "",
            "license": "GPL V3+",
            "date_added": "2021-01-21T00:00:00.000000Z",
            "date_updated": "2024-07-19T00:00:00.000000Z",
            "download_count": 6251,
            "note": 2.813008130081301,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": [
                {
                    "num": "1.1.9",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.1.8",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.1.7",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.1.6",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.1.5",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.1.4",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.1.3",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.1.2",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.1.1",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.1.0",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Modify texts in GLPI UI.",
                    "long_description": "This plugin allows an administrator to easily change localizable strings of GLPI and its plugins."
                },
                {
                    "lang": "fr",
                    "short_description": "Modifier les textes de l&#039;interface de GLPI.",
                    "long_description": "Ce plugin permet à un administrateur de changer facilement des chaînes de traduction dans GLPI et ses plugins."
                }
            ],
            "required_offers": [
                "network-basic",
                "network-standard",
                "network-advanced"
            ],
            "short_description": "Modify texts in GLPI UI."
        },
        {
            "id": 240,
            "key": "camerainput",
            "name": "Camera Input",
            "logo_url": "https://raw.githubusercontent.com/cconard96/glpi-camerainput-plugin/master/Logo.png",
            "xml_url": "https://raw.githubusercontent.com/cconard96/glpi-camerainput-plugin/master/camerainput.xml",
            "homepage_url": "https://github.com/cconard96/glpi-camerainput-plugin",
            "download_url": "https://github.com/cconard96/glpi-camerainput-plugin/releases",
            "issues_url": "https://github.com/cconard96/glpi-camerainput-plugin/issues",
            "readme_url": "https://github.com/cconard96/glpi-camerainput-plugin/blob/master/README.md",
            "changelog_url": "",
            "license": "GPLv2+",
            "date_added": "2021-02-14T00:00:00.000000Z",
            "date_updated": "2023-11-12T00:00:00.000000Z",
            "download_count": 10726,
            "note": 3.2666666666666666,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 103,
                    "name": "Curtis Conard"
                }
            ],
            "versions": {
                "3": {
                    "num": "2.1.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/glpi-camerainput-plugin/releases/download/v2.1.0/glpi-camerainput-plugin-2.1.0.tar.bz2",
                    "stability": "stable"
                },
                "4": {
                    "num": "2.0.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/glpi-camerainput-plugin/releases/download/v2.0.2/glpi-camerainput-v2.0.2.tar.bz2",
                    "stability": "stable"
                },
                "5": {
                    "num": "2.0.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/glpi-camerainput-plugin/releases/download/v2.0.1/glpi-camerainput-v2.0.1.tar.bz2",
                    "stability": "stable"
                },
                "6": {
                    "num": "2.0.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/glpi-camerainput-plugin/releases/download/v2.0.0/glpi-camerainput-v2.0.0.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Use your camera to scan QR codes or barcodes as a way to input text into some fields.",
                    "long_description": "Use your camera to scan QR codes or barcodes as a way to input text into some fields. This ties into the global search box, Physical Inventory plugin&#039;s search box, and my Asset Audit plugin&#039;s search box and allows you to use your camera as a digital barcode reader. Since browsers can only use webcams/cameras in a secure context, you must be connected to your GLPI instance over HTTPS or localhost."
                }
            ],
            "required_offers": None,
            "short_description": "Use your camera to scan QR codes or barcodes as a way to input text into some fields."
        },
        {
            "id": 243,
            "key": "archibp",
            "name": "Business Process",
            "logo_url": "https://raw.githubusercontent.com/ericferon/glpi-archibp/master/bp.png",
            "xml_url": "https://raw.githubusercontent.com/ericferon/glpi-archibp/master/bp.xml",
            "homepage_url": "https://github.com/ericferon/glpi-archibp",
            "download_url": "https://github.com/ericferon/glpi-archibp/releases",
            "issues_url": "https://github.com/ericferon/glpi-archibp/issues",
            "readme_url": "https://raw.githubusercontent.com/ericferon/glpi-archibp/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2021-06-21T00:00:00.000000Z",
            "date_updated": "2024-12-08T00:00:00.000000Z",
            "download_count": 6669,
            "note": 2.7,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 92,
                    "name": "Eric Feron"
                }
            ],
            "versions": {
                "13": {
                    "num": "2.0.12",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v2.0.12/archibp-v2.0.12.tar.gz",
                    "stability": "stable"
                },
                "14": {
                    "num": "2.0.11",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v2.0.11/archibp-v2.0.11.tar.gz",
                    "stability": "stable"
                },
                "15": {
                    "num": "2.0.10",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v2.0.10/archibp-v2.0.10.tar.gz",
                    "stability": "stable"
                },
                "5": {
                    "num": "2.0.9",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v2.0.9/archibp-v2.0.9.tar.gz",
                    "stability": "stable"
                },
                "6": {
                    "num": "2.0.8",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v2.0.8/archibp-v2.0.8.tar.gz",
                    "stability": "stable"
                },
                "7": {
                    "num": "2.0.7",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v2.0.7/archibp-v2.0.7.tar.gz",
                    "stability": "stable"
                },
                "8": {
                    "num": "2.0.6",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v2.0.6/archibp-v2.0.6.tar.gz",
                    "stability": "stable"
                },
                "9": {
                    "num": "2.0.5",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v2.0.5/archibp-v2.0.5.tar.gz",
                    "stability": "stable"
                },
                "10": {
                    "num": "2.0.4",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v2.0.4/archibp-v2.0.4.tar.gz",
                    "stability": "stable"
                },
                "11": {
                    "num": "2.0.3",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v2.0.3/archibp-v2.0.3.tar.gz",
                    "stability": "stable"
                },
                "12": {
                    "num": "2.0.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v2.0.2/archibp-v2.0.2.tar.gz",
                    "stability": "stable"
                },
                "16": {
                    "num": "2.0.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v2.0.1/archibp-v2.0.1.tar.gz",
                    "stability": "stable"
                },
                "17": {
                    "num": "2.0.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v2.0.0/archibp-v2.0.0.tar.gz",
                    "stability": "stable"
                },
                "23": {
                    "num": "1.0.14",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v1.0.14/archibp-v1.0.14.tar.gz",
                    "stability": "stable"
                },
                "24": {
                    "num": "1.0.13",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v1.0.13/archibp-v1.0.13.tar.gz",
                    "stability": "stable"
                },
                "25": {
                    "num": "1.0.12",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v1.0.12/archibp-v1.0.12.tar.gz",
                    "stability": "stable"
                },
                "26": {
                    "num": "1.0.11",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v1.0.11/archibp-v1.0.11.tar.gz",
                    "stability": "stable"
                },
                "27": {
                    "num": "1.0.10",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v1.0.10/archibp-v1.0.10.tar.gz",
                    "stability": "stable"
                },
                "18": {
                    "num": "1.0.9",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v1.0.9/archibp-v1.0.9.tar.gz",
                    "stability": "stable"
                },
                "19": {
                    "num": "1.0.8",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v1.0.8/archibp-v1.0.8.tar.gz",
                    "stability": "stable"
                },
                "20": {
                    "num": "1.0.7",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v1.0.7/archibp-v1.0.7.tar.gz",
                    "stability": "stable"
                },
                "21": {
                    "num": "1.0.6",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v1.0.6/archibp-v1.0.6.tar.gz",
                    "stability": "stable"
                },
                "22": {
                    "num": "1.0.5",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v1.0.5/archibp-v1.0.5.tar.gz",
                    "stability": "stable"
                },
                "0": {
                    "num": "1.0.4",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v1.0.4/archibp-v1.0.4.tar.gz",
                    "stability": "stable"
                },
                "1": {
                    "num": "1.0.3",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v1.0.3/archibp-v1.0.3.tar.gz",
                    "stability": "stable"
                },
                "2": {
                    "num": "1.0.2",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archibp/releases/download/v1.0.2/archibp-v1.0.2.tar.gz",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "This plugin enables you to manage the business processes of your enterprise architecture and associate them with elements of the inventory.",
                    "long_description": "This plugin enables you to manage the business processes of your enterprise architecture and associate them with elements of the inventory.A business process can be decomposed in tasks, helping you to associate inventory items (typically applications) to these tasks.The fields with the task details can be configured according to your needs. This plugin requires 2 other plugins : Apps Structure (archisw) and Statecheck."
                },
                {
                    "lang": "fr",
                    "short_description": "Ce plugin vous permet de définir les processus métiers de votre architecture d&#039;entreprise et de les associer à des éléments d&#039;inventaire.",
                    "long_description": "Ce plugin vous permet de définir les processus métiers de votre architecture d&#039;entreprise et de les associer à des éléments d&#039;inventaire.Un processus métier peut être décomposé en tâches, auxquels vous associez des éléments d&#039;inventaires (comme des applications, p.ex).Les champs contenant les détails d&#039;une tâche peuvent être configurés selon votre besoin. Ce plugin requiert 2 autres plugins : Apps Structure (archisw) et Statecheck."
                }
            ],
            "required_offers": None,
            "short_description": "This plugin enables you to manage the business processes of your enterprise architecture and associate them with elements of the inventory."
        },
        {
            "id": 247,
            "key": "agentconfig",
            "name": "GLPI Android Agent configuration",
            "logo_url": "https://services.glpi-network.com/api/glpi-network/1656/logo.png",
            "xml_url": "https://services.glpi-network.com/api/glpi-network/1656/plugin.xml",
            "homepage_url": "https://services.glpi-network.com",
            "download_url": "https://services.glpi-network.com",
            "issues_url": "https://services.glpi-network.com",
            "readme_url": "https://services.glpi-network.com/documentation/1656/file/README.md",
            "changelog_url": "",
            "license": "GPL V3+",
            "date_added": "2021-10-01T00:00:00.000000Z",
            "date_updated": "2024-02-12T00:00:00.000000Z",
            "download_count": 3522,
            "note": 3.138888888888889,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": [
                {
                    "num": "1.3.1",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.3.0",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.2.0",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "This plugin simplify and automates the GLPI Android Agent configuration.",
                    "long_description": "\nThis plugin generates QR Code and Deeplink to automatically configure server informations in the GLPI Android Agent.\nSubscribe to [GLPI-Network](https://services.glpi-network.com/) to get it.\n         "
                },
                {
                    "lang": "fr",
                    "short_description": "Ce plugin simplifie et automatise la configuration de l&#039;Agent GLPI pour Android.",
                    "long_description": "\nCe plugin génère un code QR et un lien pour configurer automatiquement les informations du serveur dans l&#039;agent GLPI pour Android.\nSouscrivez à [GLPI-Network](https://services.glpi-network.com/) pour en bénéficier.\n         "
                }
            ],
            "required_offers": [
                "network-basic",
                "network-standard",
                "network-advanced"
            ],
            "short_description": "This plugin simplify and automates the GLPI Android Agent configuration."
        },
        {
            "id": 249,
            "key": "onetimesecret",
            "name": "One-Time Secret",
            "logo_url": "https://raw.githubusercontent.com/ticgal/one-timesecret/multimedia/onetimesecret.png",
            "xml_url": "https://raw.githubusercontent.com/ticgal/one-timesecret/multimedia/onetimesecret.xml",
            "homepage_url": "https://tic.gal/en/project/onetimesecret/",
            "download_url": "https://github.com/ticgal/one-timesecret/releases",
            "issues_url": "https://github.com/ticgal/one-timesecret/issues",
            "readme_url": "https://github.com/ticgal/one-timesecret/blob/master/README.md",
            "changelog_url": "",
            "license": "AGPL v3+",
            "date_added": "2021-11-22T00:00:00.000000Z",
            "date_updated": "2024-05-16T00:00:00.000000Z",
            "download_count": 5094,
            "note": 4.583333333333333,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 90,
                    "name": "TICgal"
                }
            ],
            "versions": {
                "5": {
                    "num": "2.1.3",
                    "compatibility": "~10.0.10",
                    "download_url": "https://github.com/ticgal/one-timesecret/releases/download/2.1.3/glpi-onetimesecret-2.1.3.tar.tgz",
                    "stability": "stable"
                },
                "6": {
                    "num": "2.1.1",
                    "compatibility": "~10.0.10",
                    "download_url": "https://github.com/ticgal/one-timesecret/releases/download/2.1.1/glpi-onetimesecret-2.1.1.tar.tgz",
                    "stability": "stable"
                },
                "7": {
                    "num": "2.0.3",
                    "compatibility": "~10.0.10",
                    "download_url": "https://github.com/ticgal/one-timesecret/releases/download/2.0.3/glpi-onetimesecret-2.0.3.tar.tgz",
                    "stability": "stable"
                },
                "8": {
                    "num": "2.0.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ticgal/one-timesecret/releases/download/2.0.0/glpi-onetimesecret-2.0.0.tar.tgz",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "One-Time Secret integration. Share your passwords securely on GLPI.",
                    "long_description": "Secure password sharing integration for GLPI.\nSharing passwords is an IT nightmare, no matter which ITSM tool you use. Zero-trust is the way to go, although it is only sometimes possible and only for some scenarios.\nOne-Time Secret is an excellent tool to overcome this common issue. By sharing a burnable one-time open link with your interlocutor, you will forever forget passwords stored in emails or messaging tools, available for indiscrete eyes.\nSecret Link expiration and additional Passphrase are the icings on the cake.\n\nBut opening a website, copying and pasting, sending a message…, well, the whole process may be improved.\n\nThis is where our One-Time Secret GLPI integration excels.\n\nA streamlined experience for both techs and end-users.\n         "
                }
            ],
            "required_offers": None,
            "short_description": "One-Time Secret integration. Share your passwords securely on GLPI."
        },
        {
            "id": 250,
            "key": "glpiinventory",
            "name": "GLPI Inventory",
            "logo_url": None,
            "xml_url": "https://raw.githubusercontent.com/glpi-project/glpi-inventory-plugin/main/glpiinventory.xml",
            "homepage_url": None,
            "download_url": "https://github.com/glpi-project/glpi-inventory-plugin/releases",
            "issues_url": "https://github.com/glpi-project/glpi-inventory-plugin/issues",
            "readme_url": "https://raw.githubusercontent.com/glpi-project/glpi-inventory-plugin/main/README.md",
            "changelog_url": "",
            "license": "AGPLv3+",
            "date_added": "2021-12-15T00:00:00.000000Z",
            "date_updated": "2025-02-25T00:00:00.000000Z",
            "download_count": 69614,
            "note": 3.307392996108949,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": {
                "9": {
                    "num": "1.5.0",
                    "compatibility": "~10.0.11",
                    "download_url": "https://github.com/glpi-project/glpi-inventory-plugin/releases/download/1.5.0/glpi-glpiinventory-1.5.0.tar.bz2",
                    "stability": "stable"
                },
                "10": {
                    "num": "1.4.0",
                    "compatibility": "~10.0.11",
                    "download_url": "https://github.com/glpi-project/glpi-inventory-plugin/releases/download/1.4.0/glpi-glpiinventory-1.4.0.tar.bz2",
                    "stability": "stable"
                },
                "11": {
                    "num": "1.3.5",
                    "compatibility": "~10.0.11",
                    "download_url": "https://github.com/glpi-project/glpi-inventory-plugin/releases/download/1.3.5/glpi-glpiinventory-1.3.5.tar.bz2",
                    "stability": "stable"
                },
                "12": {
                    "num": "1.3.4",
                    "compatibility": "~10.0.10",
                    "download_url": "https://github.com/glpi-project/glpi-inventory-plugin/releases/download/1.3.4/glpi-glpiinventory-1.3.4.tar.bz2",
                    "stability": "stable"
                },
                "13": {
                    "num": "1.3.3",
                    "compatibility": "~10.0.10",
                    "download_url": "https://github.com/glpi-project/glpi-inventory-plugin/releases/download/1.3.3/glpi-glpiinventory-1.3.3.tar.bz2",
                    "stability": "stable"
                },
                "14": {
                    "num": "1.3.2",
                    "compatibility": "~10.0.10",
                    "download_url": "https://github.com/glpi-project/glpi-inventory-plugin/releases/download/1.3.2/glpi-glpiinventory-1.3.2.tar.bz2",
                    "stability": "stable"
                },
                "15": {
                    "num": "1.3.1",
                    "compatibility": "~10.0.10",
                    "download_url": "https://github.com/glpi-project/glpi-inventory-plugin/releases/download/1.3.1/glpi-glpiinventory-1.3.1.tar.bz2",
                    "stability": "stable"
                },
                "16": {
                    "num": "1.3.0",
                    "compatibility": "~10.0.10",
                    "download_url": "https://github.com/glpi-project/glpi-inventory-plugin/releases/download/1.3.0/glpi-glpiinventory-1.3.0.tar.bz2",
                    "stability": "stable"
                },
                "0": {
                    "num": "1.2.3",
                    "compatibility": "~10.0.8",
                    "download_url": "https://github.com/glpi-project/glpi-inventory-plugin/releases/download/1.2.3/glpi-glpiinventory-1.2.3.tar.bz2",
                    "stability": "stable"
                },
                "1": {
                    "num": "1.2.2",
                    "compatibility": "~10.0.8",
                    "download_url": "https://github.com/glpi-project/glpi-inventory-plugin/releases/download/1.2.2/glpi-glpiinventory-1.2.2.tar.bz2",
                    "stability": "stable"
                },
                "2": {
                    "num": "1.2.1",
                    "compatibility": "~10.0.2",
                    "download_url": "https://github.com/glpi-project/glpi-inventory-plugin/releases/download/1.2.1/glpi-glpiinventory-1.2.1.tar.bz2",
                    "stability": "stable"
                },
                "3": {
                    "num": "1.2.0",
                    "compatibility": "~10.0.2",
                    "download_url": "https://github.com/glpi-project/glpi-inventory-plugin/releases/download/1.2.0/glpi-glpiinventory-1.2.0.tar.bz2",
                    "stability": "stable"
                },
                "4": {
                    "num": "1.1.0",
                    "compatibility": "~10.0.2",
                    "download_url": "https://github.com/glpi-project/glpi-inventory-plugin/releases/download/1.1.0/glpi-glpiinventory-1.1.0.tar.bz2",
                    "stability": "stable"
                },
                "5": {
                    "num": "1.0.6",
                    "compatibility": "~10.0.2",
                    "download_url": "https://github.com/glpi-project/glpi-inventory-plugin/releases/download/1.0.6/glpi-glpiinventory-1.0.6.tar.bz2",
                    "stability": "stable"
                },
                "6": {
                    "num": "1.0.5",
                    "compatibility": "~10.0.2",
                    "download_url": "https://github.com/glpi-project/glpi-inventory-plugin/releases/download/1.0.5/glpi-glpiinventory-1.0.5.tar.bz2",
                    "stability": "stable"
                },
                "7": {
                    "num": "1.0.4",
                    "compatibility": "~10.0.2",
                    "download_url": "https://github.com/glpi-project/glpi-inventory-plugin/releases/download/1.0.4/glpi-glpiinventory-1.0.4.tar.bz2",
                    "stability": "stable"
                },
                "8": {
                    "num": "1.0.3",
                    "compatibility": "~10.0.2",
                    "download_url": "https://github.com/glpi-project/glpi-inventory-plugin/releases/download/1.0.3/glpi-glpiinventory-1.0.3.tar.bz2",
                    "stability": "stable"
                },
                "17": {
                    "num": "1.0.2",
                    "compatibility": "~10.0.1",
                    "download_url": "https://github.com/glpi-project/glpi-inventory-plugin/releases/download/1.0.2/glpi-glpiinventory-1.0.2.tar.bz2",
                    "stability": "stable"
                },
                "18": {
                    "num": "1.0.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/glpi-project/glpi-inventory-plugin/releases/download/1.0.1/glpi-glpiinventory-1.0.1.tar.bz2",
                    "stability": "stable"
                },
                "19": {
                    "num": "1.0.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/glpi-project/glpi-inventory-plugin/releases/download/1.0.0/glpi-glpiinventory-1.0.0.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "cs",
                    "short_description": "GLPI Inventory je svobodný a opensource projekt, poskytující inventarizaci hardware a software, nasazování software a prozkoumávání sítě a to jako doplněk do software pro správu IT vybavení a technické podpory, zvaný GLPI. „GLPI Inventory pro GLPI“ je sadou zásuvných modulů komunikující s agenty (GLPI Inventory-Agent), nasazenými na počítačích",
                    "long_description": "\n   GLPI Inventory je svobodný a opensource projekt, poskytující inventarizaci hardware a software, nasazování software a prozkoumávání sítě a to jako doplněk do software pro správu IT vybavení a technické podpory, zvaný GLPI.  \n   „GLPI Inventory pro GLPI“ je sadou zásuvných modulů komunikující s agenty (GLPI Inventory-Agent), nasazenými na počítačích\n   \n   - GLPI Inventory Core: poskytuje základní funkce:\n   \n      1. Komunikace s agenty pro inventarizaci a prozkoumávání sítě.\n      2. Správa úloh a plánování.\n      3. Centralizovaná pravidla pro import majetku do GLPI.\n      4. Správa neznámých zařízení (dočasná zóna, v GLPI, před skutečnou správou majetku).\n\n   - GLPI Inventory Inventory:\n      1. Inventura na počítačích (hardware, software, antivirus).\n      2. Zacházení s a aktualizace počítačů, které už jsou v GLPI.\n      \n   - GLPI Inventory SNMP:\n     \n      1. Prozkoumávání sítě, správa neznámých zařízení (pomocí zásuvného modulu GLPI Inventory core).\n      2. Vzdálená síťová zařízení a tiskárny (díky SNMP protokolu).\n      3. Získání informací o síťovém portu, VLAN sítích, propojení mezi síťovými porty přepínače a zařízeními, které už se nachází v GLPI (počítače, síťové tiskárny, síťová zařízení, atd.).\n      4. Historie změna a výkaz o každém ze síťových portů.\n      5. Stavy náplní v tiskárnách, denní čítače stránek a výkazy.\n      "
                },
                {
                    "lang": "en",
                    "short_description": "GLPI Inventory is a free and open source project providing hardware, software inventory, software deployment and network discovery to the IT asset management and helpdesk software called GLPI. &#34;GLPI Inventory for GLPI&#34; is a collection of plugins communicating with some agents (GLPI Inventory-Agent), deployed on computers",
                    "long_description": "\n   GLPI Inventory is a free and open source project providing hardware, software inventory, software deployment and network discovery to the IT asset management and helpdesk software called GLPI.  \n   &#34;GLPI Inventory for GLPI&#34; is a collection of plugins communicating with some agents (GLPI Inventory-Agent), deployed on computers\n   \n   - GLPI Inventory Core: provides core functionnalities:\n   \n      1. Communication with inventory and network discovery agents.\n      2. Tasks management and scheduling.\n      3. Centralized rules for assets import in GLPI.\n      4. Unknown devices management (temporary zone, in GLPI, before real asset management).\n\n   - GLPI Inventory Inventory:\n      1. Local inventory for computers (hardware, software, antivirus).\n      2. Handle and update computers already in GLPI.\n      \n   - GLPI Inventory SNMP:\n     \n      1. Network discovery, unknown devices management (using GLPI Inventory core plugin).\n      2. Remote network devices and printers (thanks to the SNMP protocol).\n      3. Get network port informations, VLANs, link between switchs network ports and assets already in GLPI (computers, network printers, network devices, etc.).\n      4. Change history and reports for each network port.\n      5. Printers cartridges&#039; ink levels, daily page counters and reports.\n      "
                },
                {
                    "lang": "fr",
                    "short_description": "GLPI Inventory est un projet libre dont les fonctionalités principales sont l&#039;inventaire du matériel, le télédéploiement et la découverte réseau et complète la gestion de parc et le helpdesk de l&#039;outil GLPI. &#34;GLPI Inventory for GLPI&#34; est composé d&#039;une collection de plugins (extensions) qui dialoguent avec un agent installé sur les postes clients (GLPI Inventory-Agent)",
                    "long_description": "\n   GLPI Inventory est un projet libre dont les fonctionalités principales sont l&#039;inventaire du matériel, le télédéploiement et la découverte réseau et complète la gestion de parc et le helpdesk de l&#039;outil GLPI.  \n   &#34;GLPI Inventory for GLPI&#34; est composé d&#039;une collection de plugins (extensions) qui dialoguent avec un agent installé sur les postes clients (GLPI Inventory-Agent).  \n\n   - GLPI Inventory Core, fournit les fonctionnalités centrales :\n\n      1. Communication avec les agents d&#039;inventaire et de découverte.\n      2. Gestion et planifications des tâches.\n      3. Règles centralisées pour ces plugins d&#039;import de matériel.\n      4. Gestion du matériel inconnu (zone tampon entre vos matériels gérés dans GLPI et ceux présents réellement sur le réseau).\n\n   - GLPI Inventory Inventory :\n\n      1. Inventaire local des ordinateurs (matériel, logiciel, antivirus).\n      2. Prise en charge et mise à jour des ordinateurs déjà dans GLPI.\n\n   - GLPI Inventory SNMP :\n\n      1. Découverte réseau avec gestion des matériels inconnus.\n      2. Inventaire distant des switchs et imprimantes (grâce au protocole SNMP).\n      3. Récupération des informations sur les ports, les VLANs et liaison entre ports des switchs et matériels présents dans GLPI (ordinateurs, imprimantes réseau, switchs...).\n      4. Historique des changements sur chaque port de switch et rapports.\n      5. Niveau des cartouches des imprimantes, relevé journalier des compteurs de pages et rapports.\n   "
                }
            ],
            "required_offers": None,
            "short_description": "GLPI Inventory is a free and open source project providing hardware, software inventory, software deployment and network discovery to the IT asset management and helpdesk software called GLPI. &#34;GLPI Inventory for GLPI&#34; is a collection of plugins communicating with some agents (GLPI Inventory-Agent), deployed on computers"
        },
        {
            "id": 251,
            "key": "purchaserequest",
            "name": "Purchaserequest",
            "logo_url": "https://raw.githubusercontent.com/InfotelGLPI/purchaserequest/master/purchaserequest.png",
            "xml_url": "https://raw.githubusercontent.com/InfotelGLPI/purchaserequest/main/purchaserequest.xml",
            "homepage_url": "https://github.com/InfotelGLPI/purchaserequest",
            "download_url": "https://github.com/InfotelGLPI/purchaserequest/releases",
            "issues_url": "https://github.com/InfotelGLPI/purchaserequest/issues",
            "readme_url": "https://raw.githubusercontent.com/InfotelGLPI/purchaserequest/master/README.md",
            "changelog_url": "",
            "license": "GPLv2+",
            "date_added": "2021-12-15T00:00:00.000000Z",
            "date_updated": "2024-07-15T00:00:00.000000Z",
            "download_count": 5751,
            "note": 3.25,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 49,
                    "name": "Infotel"
                }
            ],
            "versions": {
                "0": {
                    "num": "3.0.2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/purchaserequest/releases/download/3.0.2/glpi-purchaserequest-3.0.2.tar.bz2",
                    "stability": "stable"
                },
                "1": {
                    "num": "3.0.1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/purchaserequest/releases/download/3.0.1/glpi-purchaserequest-3.0.1.tar.bz2",
                    "stability": "stable"
                },
                "5": {
                    "num": "3.0.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/purchaserequest/releases/download/3.0.0/glpi-purchaserequest-3.0.0.tar.bz2",
                    "stability": "stable"
                },
                "2": {
                    "num": "3.0.0-rc3",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/purchaserequest/releases/download/3.0.0-rc3/glpi-purchaserequest-3.0.0-rc3.tar.bz2",
                    "stability": "RC"
                },
                "3": {
                    "num": "3.0.0-rc2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/purchaserequest/releases/download/3.0.0-rc2/glpi-purchaserequest-3.0.0-rc2.tar.bz2",
                    "stability": "RC"
                },
                "4": {
                    "num": "3.0.0-rc1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/purchaserequest/releases/download/3.0.0-rc1/glpi-purchaserequest-3.0.0-rc1.tar.bz2",
                    "stability": "RC"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Plugin de demandes d&#039;achats préalables au lancement de commandes avec le plugin order",
                    "long_description": "Plugin de demandes d&#039;achats préalables au lancement de commandes avec le plugin order"
                },
                {
                    "lang": "en",
                    "short_description": "Plugin for purchase requests prior to launching orders with the order plugin",
                    "long_description": "Plugin for purchase requests prior to launching orders with the order plugin"
                }
            ],
            "required_offers": None,
            "short_description": "Plugin for purchase requests prior to launching orders with the order plugin"
        },
        {
            "id": 252,
            "key": "ldaptools",
            "name": "LDAP Tools",
            "logo_url": "https://services.glpi-network.com/api/glpi-network/1792/logo.png",
            "xml_url": "https://services.glpi-network.com/api/glpi-network/1792/plugin.xml",
            "homepage_url": "https://services.glpi-network.com/",
            "download_url": "https://services.glpi-network.com/",
            "issues_url": "https://services.glpi-network.com/",
            "readme_url": "https://services.glpi-network.com/documentation/1792/file/README.md",
            "changelog_url": "",
            "license": "GPL V3+",
            "date_added": "2021-12-23T00:00:00.000000Z",
            "date_updated": "2025-01-06T00:00:00.000000Z",
            "download_count": 0,
            "note": 3.125,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": [
                {
                    "num": "0.1.0",
                    "compatibility": "~9.5.0 | ~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "0.0.3",
                    "compatibility": "~9.5.0 | ~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "0.0.2",
                    "compatibility": "~9.5.0 | ~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "0.0.1",
                    "compatibility": "~9.5.0 | ~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "LDAP Tools for GLPI",
                    "long_description": "\nThis plugin offers several tools related to LDAP directories declared in GLPI.\n\n# First tool : LDAP configurations tests\n\nPerforms various tests on all the LDAP directories declared in GLPI:\n\n1. test if TCP stream is opened from GLPI to LDAP server hostname / port\n2. check is &#34;BaseDN&#34; field is filled in correctly\n3. initiate an &#34;ldap_connect&#34; to validate the LDAP URI\n4. execute or not an LDAP BIND authentication (with user/password, or TLS cert/key)\n5. perform a generic LDAP Search (with cn&#61;\\*) and try to count first entries\n6. perform a specific LDAP Search (with LDAP Filter configured) and try to count first entries\n7. get and display all LDAP attributes available on the first entry found\n\nSubscribe to [GLPI-Network](https://services.glpi-network.com/) to get it.\n         "
                },
                {
                    "lang": "fr",
                    "short_description": "Outils LDAP pour GLPI",
                    "long_description": "\nCe plugin offre plusieurs outils en lien avec les annuaires LDAP déclarés dans GLPI.\n\n# Premier outil : LDAP test des configurations\n\nEffectue différents tests sur tous les annuaires LDAP déclarés dans GLPI :\n\n1. test si le flux TCP est ouvert entre GLPI et le hostname/port du serveur LDAP\n2. vérifie que le champ &#34;BaseDN&#34; est correctement rempli\n3. lance un &#34;ldap_connect&#34; pour valider l&#039;URI LDAP\n4. exécute ou non une authentification LDAP BIND (avec utilisateur/mot de passe, ou certificat/clé TLS)\n5. effectue une recherche LDAP générique (avec cn&#61;\\*) et essaye de compter les premières entrées\n6. effectue une recherche LDAP spécifique (avec le filtre LDAP configuré) et essaye de compter les premières entrées \n7. récupère et affiche les attributs LDAP disponible sur la première entrée trouvée\n\nSouscrivez à [GLPI-Network](https://services.glpi-network.com/) pour en bénéficier.\n         "
                }
            ],
            "required_offers": [
                "network-basic",
                "network-standard",
                "network-advanced"
            ],
            "short_description": "LDAP Tools for GLPI"
        },
        {
            "id": 253,
            "key": "gdpr",
            "name": "GDPR Tools",
            "logo_url": "https://services.glpi-network.com/api/glpi-network/1711/logo.png",
            "xml_url": "https://services.glpi-network.com/api/glpi-network/1711/plugin.xml",
            "homepage_url": "https://services.glpi-network.com/",
            "download_url": "https://services.glpi-network.com/",
            "issues_url": "https://services.glpi-network.com/",
            "readme_url": "https://services.glpi-network.com/documentation/1711/file/README.md",
            "changelog_url": "",
            "license": "GPL V3+",
            "date_added": "2025-03-16T16:04:19.512182Z",
            "date_updated": "2024-04-05T00:00:00.000000Z",
            "download_count": 0,
            "note": 3.6875,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": [
                {
                    "num": "2.0.4",
                    "compatibility": "~9.5.0 | ~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "2.0.3",
                    "compatibility": "~9.5.0 | ~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "2.0.2",
                    "compatibility": "~9.5.0 | ~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "2.0.1",
                    "compatibility": "~9.5.0 | ~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "2.0.0",
                    "compatibility": "~9.5.0 | ~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "This plugin offer tools to help you comply with GDPR regulation.",
                    "long_description": "\nThis plugin offer tools to help you comply with GDPR regulation.\n\n# Cleaning inactive users\n\nThe main feature of this plugin is the automated cleaning or removal of inactive users.\n\nThere is two possible way of handling inactive users:\n- Cleaning the user data\n- Deleting the user\n\n# Scope restriction\n\nThe automated removal process can be limited to the given scopes:\n- All inactives users\n- Inactive users with no ongoing tickets\n- Inactive users with no tickets\n\nThe removal will be done through a standard GLPI automatic action that can be configured to run as often as you want.\n\nSubscribe to [GLPI-Network](https://services.glpi-network.com/) to get it.\n         "
                },
                {
                    "lang": "fr",
                    "short_description": "Ce plugin propose des outils pour vous aider à respecter les contraintes du RGPD.",
                    "long_description": "\nCe plugin propose des outils pour vous aider à respecter les contraintes du RGPD.\n\n# Nettoyage des utilisateurs inactifs\n\nLa fonctionnalité principale de ce plugin est le nettoyage ou suppression des utilisateurs inactifs.\n\nLe plugin propose deux manières de gérer cela :\n- Nettoyage des données des utilisateurs\n- Suppression des utilisateurs\n\n# Restriction de périmètre\n\nLa suppression automatique peut être limitée aux périmètres suivants :\n- Tous les utilisateurs inactifs\n- Les utilisateurs inactifs sans tickets en cours.\n- Les utilisateurs inactifs sans tickets.\n\nCette suppression sera faite via une action automatique standard de GLPI qui peut donc être configuré pour être exécutée aussi souvent que nécessaire.\n\nSouscrivez à [GLPI-Network](https://services.glpi-network.com/) pour en bénéficier.\n         "
                }
            ],
            "required_offers": [
                "network-basic",
                "network-standard",
                "network-advanced"
            ],
            "short_description": "This plugin offer tools to help you comply with GDPR regulation."
        },
        {
            "id": 254,
            "key": "stab",
            "name": "Split Timeline Action Buttons (STAB)",
            "logo_url": "https://raw.githubusercontent.com/cconard96/glpi-stab-plugin/main/logo.png",
            "xml_url": "https://raw.githubusercontent.com/cconard96/glpi-stab-plugin/main/stab.xml",
            "homepage_url": "https://github.com/cconard96/glpi-stab-plugin",
            "download_url": "https://github.com/cconard96/glpi-stab-plugin/releases",
            "issues_url": "https://github.com/cconard96/glpi-stab-plugin/issues",
            "readme_url": "https://github.com/cconard96/glpi-stab-plugin/blob/main/README.md",
            "changelog_url": "",
            "license": "GPLv2+",
            "date_added": "2022-01-03T00:00:00.000000Z",
            "date_updated": "2023-11-21T00:00:00.000000Z",
            "download_count": 4637,
            "note": 3.9,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 103,
                    "name": "Curtis Conard"
                }
            ],
            "versions": [
                {
                    "num": "1.1.3",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/glpi-stab-plugin/releases/download/v1.1.3/glpi-stab-v1.1.3.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "1.1.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/glpi-stab-plugin/releases/download/v1.1.2/glpi-stab-v1.1.2.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "1.1.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/glpi-stab-plugin/releases/download/v1.1.0/glpi-stab-v1.1.0.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "1.0.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/glpi-stab-plugin/releases/download/v1.0.2/glpi-stab-v1.0.2.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "1.0.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/glpi-stab-plugin/releases/download/v1.0.1/glpi-stab-v1.0.1.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "1.0.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/cconard96/glpi-stab-plugin/releases/download/v1.0.0/glpi-stab-v1.0.0.tar.bz2",
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Allows optionally setting the Ticket, Change or Problem status when creating a followup or task",
                    "long_description": "\nRestores the functionality from before GLPI version 10.0 where you could add a followup or task and update the parent Ticket, Change, or Problem status in a single action.\n        "
                }
            ],
            "required_offers": None,
            "short_description": "Allows optionally setting the Ticket, Change or Problem status when creating a followup or task"
        },
        {
            "id": 256,
            "key": "roundrobin",
            "name": "RoundRobin",
            "logo_url": "https://raw.githubusercontent.com/initiativa/roundrobin/master/pics/roundrobin-logo.png",
            "xml_url": "https://raw.githubusercontent.com/initiativa/roundrobin/master/roundrobin.xml",
            "homepage_url": "https://github.com/initiativa/roundrobin",
            "download_url": "https://github.com/initiativa/roundrobin/releases",
            "issues_url": "https://github.com/initiativa/roundrobin/issues",
            "readme_url": "https://raw.githubusercontent.com/initiativa/roundrobin/master/README.md",
            "changelog_url": "",
            "license": "GPL v3",
            "date_added": "2022-02-16T00:00:00.000000Z",
            "date_updated": "2025-03-08T00:00:00.000000Z",
            "download_count": 2537,
            "note": 3.5,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 122,
                    "name": "Andrea Caracciolo"
                },
                {
                    "id": 123,
                    "name": "initiativa srl"
                }
            ],
            "versions": [
                {
                    "num": "1.0.5",
                    "compatibility": "~10.0 || 9.5",
                    "download_url": "https://github.com/initiativa/roundrobin/releases/download/1.0.5/roundrobin-1.0.5.tar.gz",
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "This plugin allow the assignation of a ticket using a roundrobin policy.",
                    "long_description": "This plugin allow the assignation of a ticket using a roundrobin policy. It considers &#34;the group in charge of the hardware&#34; linked to a category to get the member of the group and assigning a ticket to one of them using a roundrobin policy."
                },
                {
                    "lang": "it",
                    "short_description": "Questo plugin permette l&#039;assegnazione di un ticket ad un tecnico utilizzando una politica di roundrobin.",
                    "long_description": "Questo plugin permette l&#039;assegnazione di un ticket ad un tecnico utilizzando una politica di roundrobin. Il plugin valuta il gruppo indicato nel campo &#34;gruppo incaricato dell&#039;hardware&#34; nelle varie categorie, ed assegna il ticket ad uno dei membri del gruppo, ruotnado i membri ad goni nuovo ticket con una politica di tipo roundrobin"
                }
            ],
            "required_offers": None,
            "short_description": "This plugin allow the assignation of a ticket using a roundrobin policy."
        },
        {
            "id": 258,
            "key": "archidata",
            "name": "Data structure inventory",
            "logo_url": "https://raw.githubusercontent.com/ericferon/glpi-archidata/master/dataelement.png",
            "xml_url": "https://raw.githubusercontent.com/ericferon/glpi-archidata/master/archidata.xml",
            "homepage_url": "https://github.com/ericferon/glpi-archidata",
            "download_url": "https://github.com/ericferon/glpi-archidata/releases",
            "issues_url": "https://github.com/ericferon/glpi-archidata/issues",
            "readme_url": "https://github.com/ericferon/glpi-archidata/blob/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2022-04-21T00:00:00.000000Z",
            "date_updated": "2024-07-05T00:00:00.000000Z",
            "download_count": 5111,
            "note": 0,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 92,
                    "name": "Eric Feron"
                }
            ],
            "versions": {
                "6": {
                    "num": "1.0.15",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archidata/releases/download/v1.0.15/archidata-v1.0.15.tar.gz",
                    "stability": "stable"
                },
                "7": {
                    "num": "1.0.14",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archidata/releases/download/v1.0.14/archidata-v1.0.14.tar.gz",
                    "stability": "stable"
                },
                "8": {
                    "num": "1.0.13",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archidata/releases/download/v1.0.13/archidata-v1.0.13.tar.gz",
                    "stability": "stable"
                },
                "9": {
                    "num": "1.0.12",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archidata/releases/download/v1.0.12/archidata-v1.0.12.tar.gz",
                    "stability": "stable"
                },
                "10": {
                    "num": "1.0.11",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archidata/releases/download/v1.0.11/archidata-v1.0.11.tar.gz",
                    "stability": "stable"
                },
                "11": {
                    "num": "1.0.10",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archidata/releases/download/v1.0.10/archidata-v1.0.10.tar.gz",
                    "stability": "stable"
                },
                "0": {
                    "num": "1.0.9",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archidata/releases/download/v1.0.9/archidata-v1.0.9.tar.gz",
                    "stability": "stable"
                },
                "1": {
                    "num": "1.0.8",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archidata/releases/download/v1.0.8/archidata-v1.0.8.tar.gz",
                    "stability": "stable"
                },
                "2": {
                    "num": "1.0.7",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archidata/releases/download/v1.0.7/archidata-v1.0.7.tar.gz",
                    "stability": "stable"
                },
                "3": {
                    "num": "1.0.6",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archidata/releases/download/v1.0.6/archidata-v1.0.6.tar.gz",
                    "stability": "stable"
                },
                "4": {
                    "num": "1.0.5",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archidata/releases/download/v1.0.5/archidata-v1.0.5.tar.gz",
                    "stability": "stable"
                },
                "5": {
                    "num": "1.0.4",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-archidata/releases/download/v1.0.4/archidata-v1.0.4.tar.gz",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Inventory of your data structures. A data structure can be composed by several data elements.",
                    "long_description": "Inventory of your data structures.An data structures can be composed by a tree with several levels of data elements.You can associate these data structures with other inventory elements (master application, databases, dataflows, ...)"
                },
                {
                    "lang": "fr",
                    "short_description": "Inventaire de vos structures de données. Une structure de donnée peut être formée de plusieurs éléments.",
                    "long_description": "Inventaire de vos structures de données.Une structures de données peut être formée par une arborescence à plusieurs niveaux d&#039;autres éléments.Ces structures de données peuvent être associés à d&#039;autres éléments d&#039;inventaire (application maître, serveurs, bases de données, flux de données, ...)"
                }
            ],
            "required_offers": None,
            "short_description": "Inventory of your data structures. A data structure can be composed by several data elements."
        },
        {
            "id": 259,
            "key": "gantt",
            "name": "gantt",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/gantt/main/gantt.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/gantt/main/gantt.xml",
            "homepage_url": "https://github.com/pluginsGLPI/gantt",
            "download_url": "https://github.com/pluginsGLPI/gantt/releases",
            "issues_url": "https://github.com/pluginsGLPI/gantt/issues",
            "readme_url": "https://github.com/pluginsGLPI/gantt/blob/master/README.md",
            "changelog_url": "",
            "license": "GPL-2.0-or-later",
            "date_added": "2022-05-05T00:00:00.000000Z",
            "date_updated": "2024-03-15T00:00:00.000000Z",
            "download_count": 10870,
            "note": 3.3846153846153846,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": [
                {
                    "num": "1.1.0",
                    "compatibility": "^10.0.1",
                    "download_url": "https://github.com/pluginsGLPI/gantt/releases/download/1.1.0/glpi-gantt-1.1.0.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "1.0.4",
                    "compatibility": "^10.0.1",
                    "download_url": "https://github.com/pluginsGLPI/gantt/releases/download/1.0.4/glpi-gantt-1.0.4.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "1.0.3",
                    "compatibility": "^10.0.1",
                    "download_url": "https://github.com/pluginsGLPI/gantt/releases/download/1.0.3/glpi-gantt-1.0.3.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "1.0.2",
                    "compatibility": "^10.0.1",
                    "download_url": "https://github.com/pluginsGLPI/gantt/releases/download/1.0.2/glpi-gantt-1.0.2.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "1.0.1",
                    "compatibility": "^10.0.1",
                    "download_url": "https://github.com/pluginsGLPI/gantt/releases/download/1.0.1/glpi-gantt-1.0.1.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "1.0.0",
                    "compatibility": "^10.0.1",
                    "download_url": "https://github.com/pluginsGLPI/gantt/releases/download/1.0.0/glpi-gantt-1.0.0.tar.bz2",
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "gantt GLPI plugin.",
                    "long_description": "Add a gantt tab to GLPI projects items. The feature was removed in GLPI core from 10.0.1 version."
                },
                {
                    "lang": "fr",
                    "short_description": "Plugin GLPI gantt",
                    "long_description": "Ajoute un onglet Gantt aux objets projet de GLPI. La fonctionnalité a été retiré du coeur de GLPI depuis la version 10.0.1."
                }
            ],
            "required_offers": None,
            "short_description": "gantt GLPI plugin."
        },
        {
            "id": 263,
            "key": "webhook",
            "name": "Webhook",
            "logo_url": "https://raw.githubusercontent.com/ericferon/glpi-webhook/master/webhook.svg",
            "xml_url": "https://raw.githubusercontent.com/ericferon/glpi-webhook/master/webhook.xml",
            "homepage_url": "https://github.com/ericferon/glpi-webhook",
            "download_url": "https://github.com/ericferon/glpi-webhook/releases",
            "issues_url": "https://github.com/ericferon/glpi-webhook/issues",
            "readme_url": "https://github.com/ericferon/glpi-webhook/blob/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2022-08-19T00:00:00.000000Z",
            "date_updated": "2023-11-15T00:00:00.000000Z",
            "download_count": 6819,
            "note": 3.4285714285714284,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 92,
                    "name": "Eric Feron"
                }
            ],
            "versions": {
                "10": {
                    "num": "1.0.18",
                    "compatibility": ">=10.0.3",
                    "download_url": "https://github.com/ericferon/glpi-webhook/releases/download/v1.0.18/webhook-v1.0.18.tar.gz",
                    "stability": "stable"
                },
                "11": {
                    "num": "1.0.17",
                    "compatibility": ">=10.0.3",
                    "download_url": "https://github.com/ericferon/glpi-webhook/releases/download/v1.0.17/webhook-v1.0.17.tar.gz",
                    "stability": "stable"
                },
                "12": {
                    "num": "1.0.16",
                    "compatibility": ">=10.0.3",
                    "download_url": "https://github.com/ericferon/glpi-webhook/releases/download/v1.0.16/webhook-v1.0.16.tar.gz",
                    "stability": "stable"
                },
                "13": {
                    "num": "1.0.15",
                    "compatibility": ">=10.0.3",
                    "download_url": "https://github.com/ericferon/glpi-webhook/releases/download/v1.0.15/webhook-v1.0.15.tar.gz",
                    "stability": "stable"
                },
                "14": {
                    "num": "1.0.14",
                    "compatibility": ">=10.0.3",
                    "download_url": "https://github.com/ericferon/glpi-webhook/releases/download/v1.0.14/webhook-v1.0.14.tar.gz",
                    "stability": "stable"
                },
                "15": {
                    "num": "1.0.13",
                    "compatibility": ">=10.0.3",
                    "download_url": "https://github.com/ericferon/glpi-webhook/releases/download/v1.0.13/webhook-v1.0.13.tar.gz",
                    "stability": "stable"
                },
                "16": {
                    "num": "1.0.12",
                    "compatibility": ">=10.0.3",
                    "download_url": "https://github.com/ericferon/glpi-webhook/releases/download/v1.0.12/webhook-v1.0.12.tar.gz",
                    "stability": "stable"
                },
                "17": {
                    "num": "1.0.11",
                    "compatibility": ">=10.0.3",
                    "download_url": "https://github.com/ericferon/glpi-webhook/releases/download/v1.0.11/webhook-v1.0.11.tar.gz",
                    "stability": "stable"
                },
                "18": {
                    "num": "1.0.10",
                    "compatibility": ">=10.0.3",
                    "download_url": "https://github.com/ericferon/glpi-webhook/releases/download/v1.0.10/webhook-v1.0.10.tar.gz",
                    "stability": "stable"
                },
                "4": {
                    "num": "1.0.9",
                    "compatibility": ">=10.0.3",
                    "download_url": "https://github.com/ericferon/glpi-webhook/releases/download/v1.0.9/webhook-v1.0.9.tar.gz",
                    "stability": "stable"
                },
                "5": {
                    "num": "1.0.8",
                    "compatibility": ">=10.0.3",
                    "download_url": "https://github.com/ericferon/glpi-webhook/releases/download/v1.0.8/webhook-v1.0.8.tar.gz",
                    "stability": "stable"
                },
                "6": {
                    "num": "1.0.7",
                    "compatibility": ">=10.0.3",
                    "download_url": "https://github.com/ericferon/glpi-webhook/releases/download/v1.0.7/webhook-v1.0.7.tar.gz",
                    "stability": "stable"
                },
                "7": {
                    "num": "1.0.6",
                    "compatibility": ">=10.0.3",
                    "download_url": "https://github.com/ericferon/glpi-webhook/releases/download/v1.0.6/webhook-v1.0.6.tar.gz",
                    "stability": "stable"
                },
                "8": {
                    "num": "1.0.5",
                    "compatibility": ">=10.0.3",
                    "download_url": "https://github.com/ericferon/glpi-webhook/releases/download/v1.0.5/webhook-v1.0.5.tar.gz",
                    "stability": "stable"
                },
                "9": {
                    "num": "1.0.4",
                    "compatibility": ">=10.0.3",
                    "download_url": "https://github.com/ericferon/glpi-webhook/releases/download/v1.0.4/webhook-v1.0.4.tar.gz",
                    "stability": "stable"
                },
                "2": {
                    "num": "1.0.3",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-webhook/releases/download/v1.0.3/webhook-v1.0.3.tar.gz",
                    "stability": "stable"
                },
                "3": {
                    "num": "1.0.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-webhook/releases/download/v1.0.2/webhook-v1.0.2.tar.gz",
                    "stability": "stable"
                },
                "0": {
                    "num": "1.0.1",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-webhook/releases/download/v1.0.1/webhook-v1.0.1.tar.gz",
                    "stability": "stable"
                },
                "1": {
                    "num": "1.0.0",
                    "compatibility": "~9.5.0 || ~10.0.0",
                    "download_url": "https://github.com/ericferon/glpi-webhook/releases/download/v1.0.0/webhook-v1.0.0.tar.gz",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "This plugin let you notify another application about changes in inventoy items.Then, an API call to this other application can be performed to reflect this change into this other application.",
                    "long_description": "This plugin let you notify another application about changes in inventoy items.Then, an API call to this other application can be performed to reflect this change into this other application.See the plugin wiki on github for the user manual (https://github.com/ericferon/glpi-webhook/wiki)."
                },
                {
                    "lang": "fr",
                    "short_description": "Ce greffon vous permet de notifier, à une autre application, des changements relatifs à un élément d&#039;inventaire.Un appel API peut alors être exécuté, pour reporter ce changement dans cette autre application.",
                    "long_description": "Ce greffon vous permet de notifier, à une autre application, des changements relatifs à un élément d&#039;inventaire.Un appel API peut alors être exécuté, pour reporter ce changement dans cette autre application.Consultez le wiki sur github pour le manuel d&#039;utilisation(https://github.com/ericferon/glpi-webhook/wiki)."
                }
            ],
            "required_offers": None,
            "short_description": "This plugin let you notify another application about changes in inventoy items.Then, an API call to this other application can be performed to reflect this change into this other application."
        },
        {
            "id": 268,
            "key": "borgbase",
            "name": "Borgbase",
            "logo_url": "https://raw.githubusercontent.com/ticgal/borgbase/multimedia/borgbase.png",
            "xml_url": "https://raw.githubusercontent.com/ticgal/borgbase/multimedia/borgbase.xml",
            "homepage_url": "https://tic.gal/en/borgbase/",
            "download_url": "https://github.com/ticgal/borgbase/releases",
            "issues_url": "https://github.com/ticgal/borgbase/issues",
            "readme_url": "https://github.com/ticgal/borgbase/blob/master/README.md",
            "changelog_url": "",
            "license": "AGPL v3+",
            "date_added": "2022-11-26T00:00:00.000000Z",
            "date_updated": "2022-11-28T00:00:00.000000Z",
            "download_count": 1314,
            "note": 2.5,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 90,
                    "name": "TICgal"
                }
            ],
            "versions": [
                {
                    "num": "1.0.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ticgal/borgbase/releases/download/1.0.0/glpi-borgbase-1.0.0.tar.tgz",
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "A Borgbase integration",
                    "long_description": "Borgbase is a simple and secure offsite backup based on the opensource Backup utility Borg.\nLogin into Borgbase has a couple of challenges: \n1. There is only one user.\n2. User has complete access to every area\nWith the Borgbase GLPI integration we can:\n1. Show relevant backup information: when the repo was last updated; how much space is using...\n2. Get some:native Dashboard Widgets to track that information from GLPI. \n        "
                }
            ],
            "required_offers": None,
            "short_description": "A Borgbase integration"
        },
        {
            "id": 270,
            "key": "mfa",
            "name": "MFA",
            "logo_url": "https://raw.githubusercontent.com/ticgal/mfa/multimedia/mfa.png",
            "xml_url": "https://raw.githubusercontent.com/ticgal/mfa/multimedia/mfa.xml",
            "homepage_url": "https://tic.gal/mfa-for-glpi",
            "download_url": "https://github.com/ticgal/mfa/releases",
            "issues_url": "https://github.com/ticgal/mfa/issues",
            "readme_url": "https://github.com/ticgal/mfa/blob/master/README.md",
            "changelog_url": "",
            "license": "AGPL v3+",
            "date_added": "2022-12-26T00:00:00.000000Z",
            "date_updated": "2024-05-29T00:00:00.000000Z",
            "download_count": 3543,
            "note": 3.1666666666666665,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 90,
                    "name": "TICgal"
                }
            ],
            "versions": [
                {
                    "num": "1.0.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ticgal/mfa/releases/download/1.0.2/glpi-mfa-1.0.2.tar.tgz",
                    "stability": "stable"
                },
                {
                    "num": "1.0.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/ticgal/mfa/releases/download/1.0.1/glpi-mfa-1.0.1.tar.tgz",
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "A OTP plugin for GLPI",
                    "long_description": "\nAdds an extra security layer to GLPI login by asking for a One-Time Security Code. \nCurrently, it only supports OTP via email.\n        "
                }
            ],
            "required_offers": None,
            "short_description": "A OTP plugin for GLPI"
        },
        {
            "id": 274,
            "key": "nutanix",
            "name": "Nutanix",
            "logo_url": "https://services.glpi-network.com/api/glpi-network/1650/logo.png",
            "xml_url": "https://services.glpi-network.com/api/glpi-network/1650/plugin.xml",
            "homepage_url": "https://services.glpi-network.com/",
            "download_url": "https://services.glpi-network.com/",
            "issues_url": "https://services.glpi-network.com/",
            "readme_url": "https://services.glpi-network.com/documentation/1650/file/README.md",
            "changelog_url": "",
            "license": "GPL v3+",
            "date_added": "2023-02-23T00:00:00.000000Z",
            "date_updated": "2023-07-04T00:00:00.000000Z",
            "download_count": 234,
            "note": 4,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": [
                {
                    "num": "1.0.0-beta3",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "beta"
                },
                {
                    "num": "1.0.0-beta2",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "beta"
                },
                {
                    "num": "1.0.0-beta1",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "beta"
                }
            ],
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Ce plugin permet de faire l&#039;inventaire des systèmes Nutanix",
                    "long_description": "\nCe plugin permet de faire l&#039;inventaire des systèmes Nutanix.\nSouscrivez à [GLPI-Network](https://services.glpi-network.com/) pour en bénéficier.\n         "
                },
                {
                    "lang": "en",
                    "short_description": "This plugin allows to do Nutanix systems inventory",
                    "long_description": "\nThis plugin allows to do Nutanix systems inventory.\nSubscribe to [GLPI-Network](https://services.glpi-network.com/) to get it.\n         "
                }
            ],
            "required_offers": [
                "network-advanced"
            ],
            "short_description": "This plugin allows to do Nutanix systems inventory"
        },
        {
            "id": 275,
            "key": "scim",
            "name": "SCIM",
            "logo_url": "https://services.glpi-network.com/api/glpi-network/1841/logo.png",
            "xml_url": "https://services.glpi-network.com/api/glpi-network/1841/plugin.xml",
            "homepage_url": "https://services.glpi-network.com/",
            "download_url": "https://services.glpi-network.com/",
            "issues_url": "https://services.glpi-network.com/",
            "readme_url": "https://services.glpi-network.com/documentation/1841/file/README.md",
            "changelog_url": "",
            "license": "GPL v3+",
            "date_added": "2023-03-06T00:00:00.000000Z",
            "date_updated": "2025-01-16T00:00:00.000000Z",
            "download_count": 1543,
            "note": 3.75,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": [
                {
                    "num": "1.7.0",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "SCIM GLPI plugin",
                    "long_description": "This plugin let you provision your users and groups from an external identity provider using the SCIM protocol."
                },
                {
                    "lang": "fr",
                    "short_description": "Plugin GLPI SCIM",
                    "long_description": "Ce plugin vous permet de provisionner vos utilisateurs et groupes depuis un fournisseur d&#039;identité externe en utilisant le protocole SCIM."
                }
            ],
            "required_offers": [
                "network-basic",
                "network-standard",
                "network-advanced"
            ],
            "short_description": "SCIM GLPI plugin"
        },
        {
            "id": 279,
            "key": "ticketfilter",
            "name": "Ticket Filter",
            "logo_url": "https://codeberg.org/QuinQuies/ticketfilter/raw/branch/main/donut.png",
            "xml_url": "https://codeberg.org/QuinQuies/ticketfilter/raw/branch/main/ticketfilter.xml",
            "homepage_url": "https://codeberg.org/QuinQuies",
            "download_url": "https://codeberg.org/QuinQuies/ticketfilter/releases",
            "issues_url": "https://codeberg.org/QuinQuies/ticketfilter/issues",
            "readme_url": "https://codeberg.org/QuinQuies/ticketfilter/src/branch/main/README.md",
            "changelog_url": "",
            "license": "GPLv2+",
            "date_added": "2023-06-19T00:00:00.000000Z",
            "date_updated": "2025-02-04T00:00:00.000000Z",
            "download_count": 3534,
            "note": 3.25,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 130,
                    "name": "Chris Gralike"
                }
            ],
            "versions": [
                {
                    "num": "1.4.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://codeberg.org/QuinQuies/ticketfilter/releases/download/v1.4.0/ticketfilter.zip",
                    "stability": "stable"
                },
                {
                    "num": "1.1.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://codeberg.org/QuinQuies/ticketfilter/releases/download/v1.2.0/ticketfilter.zip",
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Matches foreign (ticket, monitoring, crm) identifiers in the mailsubject of mailgate processed tickets or manually created tickets \n            and adds successfully matched tickets as followups in existing tickets with the same identifier and more.",
                    "long_description": "The TicketFilter plugin will allow you to add additional regular expressions that \n            TicketFilter will use locate unique identifiers in received tickets. If a match is found, \n            TicketFilter will use the found identifier to locate existing tickets with the same identifier and \n            add the received email as followup in all tickets that contain that identifier. If configured ticketfilter \n            will try to prevent notifications to be send to prevent email runaway issues, reopen closed tickets with status\n            new, or update the ticket to a solved state if specific keywords where found in the received email subject.\n        "
                }
            ],
            "required_offers": None,
            "short_description": "Matches foreign (ticket, monitoring, crm) identifiers in the mailsubject of mailgate processed tickets or manually created tickets \n            and adds successfully matched tickets as followups in existing tickets with the same identifier and more."
        },
        {
            "id": 282,
            "key": "databaseinventory",
            "name": "Database inventory",
            "logo_url": "https://raw.githubusercontent.com/pluginsGLPI/databaseinventory/main/docs/logo.png",
            "xml_url": "https://raw.githubusercontent.com/pluginsGLPI/databasecredentials/main/databaseinventory.xml",
            "homepage_url": "https://github.com/pluginsGLPI/databaseinventory",
            "download_url": "https://github.com/pluginsGLPI/databaseinventory/releases",
            "issues_url": "https://github.com/pluginsGLPI/databaseinventory/issues",
            "readme_url": "https://github.com/pluginsGLPI/databaseinventory/blob/main/README.md",
            "changelog_url": "",
            "license": "GPL V3+",
            "date_added": "2023-09-22T00:00:00.000000Z",
            "date_updated": "2024-12-13T00:00:00.000000Z",
            "download_count": 3435,
            "note": 1.9,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": [
                {
                    "num": "1.0.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/databaseinventory/releases/download/1.0.2/glpi-databaseinventory-1.0.2.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "1.0.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/databaseinventory/releases/download/1.0.1/glpi-databaseinventory-1.0.1.tar.bz2",
                    "stability": "stable"
                },
                {
                    "num": "1.0.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://github.com/pluginsGLPI/databaseinventory/releases/download/1.0.0/glpi-databaseinventory-1.0.0.tar.bz2",
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "DatabaseInventory GLPI plugin.",
                    "long_description": "This plugin allows you to &#34;manage&#34; the Teclib&#039; inventory agents in order to perform an inventory of the databases present on the workstation."
                },
                {
                    "lang": "fr",
                    "short_description": "Plugin GLPI d&#039;inventaire des bases de données",
                    "long_description": "Ce plugin permet de &#34;piloter&#34; les agents d&#039;inventaire Teclib&#039; afin d&#039;executer un inventaire des bases de données présentes sur le poste."
                }
            ],
            "required_offers": None,
            "short_description": "DatabaseInventory GLPI plugin."
        },
        {
            "id": 284,
            "key": "powerdns",
            "name": "PowerDNS",
            "logo_url": "https://services.glpi-network.com/api/glpi-network/1665/logo.png",
            "xml_url": "https://services.glpi-network.com/api/glpi-network/1665/plugin.xml",
            "homepage_url": "https://services.glpi-network.com/",
            "download_url": "https://services.glpi-network.com/",
            "issues_url": "https://services.glpi-network.com/",
            "readme_url": "https://services.glpi-network.com/documentation/1665/file/README.md",
            "changelog_url": "",
            "license": "GPL V3+",
            "date_added": "2023-11-17T00:00:00.000000Z",
            "date_updated": "2023-11-20T00:00:00.000000Z",
            "download_count": 310,
            "note": 4.75,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": [
                {
                    "num": "1.0.0",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "PowerDNS GLPI plugin.",
                    "long_description": "\n**Subscribe to [GLPI-Network](https://services.glpi-network.com/) to get it.**\n\nImport and manage domains/records from and to PowerDNS by using GLPI interface.\nWe use PowerDNS API to retrieve these objects and insert them in the corresponding GLPI tables.\n\nOn plugin first installation and when configuration is done, we import all domains and records from PowerDNS to GLPI.\nThen, we keep them synchronized with the help of a GLPI crontask.\n\nMore, every actions done on GLPI side on related objects will be replicated on PowerDNS side. Domains deleted or updated, records deleted or updated, etc.\n         "
                },
                {
                    "lang": "fr",
                    "short_description": "Plugin GLPI PowerDNS",
                    "long_description": "\n**Souscrivez à [GLPI-Network](https://services.glpi-network.com/) pour en bénéficier.**\n\nImportez et gérez vos domaines/enregistrements depuis et vers PowerDNS en utilisant l&#039;interface de GLPI.\nNous utilisons l&#039;API PowerDNS pour récupérer ces objets et les insérer dans les tables GLPI correspondantes.\n\nLors de la première installation du plugin et lorsque la configuration est terminée, nous importons tous les domaines et enregistrements de PowerDNS vers GLPI.\nEnsuite, nous les maintenons synchronisés à l&#039;aide d&#039;une tâche planifiée GLPI.\n\nDe plus, toutes les actions effectuées du côté GLPI sur les objets associés seront répliquées du côté PowerDNS. Domaines supprimés ou mis à jour, enregistrements supprimés ou mis à jour, etc.\n         "
                }
            ],
            "required_offers": [
                "network-basic",
                "network-standard",
                "network-advanced"
            ],
            "short_description": "PowerDNS GLPI plugin."
        },
        {
            "id": 285,
            "key": "translate",
            "name": "Translate",
            "logo_url": "https://services.glpi-network.com/api/glpi-network/1848/logo.png",
            "xml_url": "https://services.glpi-network.com/api/glpi-network/1848/plugin.xml",
            "homepage_url": "https://services.glpi-network.com",
            "download_url": "https://services.glpi-network.com",
            "issues_url": "https://services.glpi-network.com",
            "readme_url": "https://services.glpi-network.com/documentation/1848/file/README.md",
            "changelog_url": "",
            "license": "GPL v3",
            "date_added": "2023-11-22T00:00:00.000000Z",
            "date_updated": "2025-01-20T00:00:00.000000Z",
            "download_count": 638,
            "note": 4.9375,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": [
                {
                    "num": "1.1.0",
                    "compatibility": "~10.0.10",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.0.3",
                    "compatibility": "~10.0.10",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.0.2",
                    "compatibility": "~10.0.10",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.0.1",
                    "compatibility": "~10.0.10",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.0.0",
                    "compatibility": "~10.0.10",
                    "download_url": None,
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Translate ticket timeline items.",
                    "long_description": "\nThis plugin adds the ability to translate ticket timeline items using the DeepL API.\nSubscribe to [GLPI-Network](https://services.glpi-network.com/) to get it.\n        "
                },
                {
                    "lang": "fr",
                    "short_description": "Traduction des éléments de la timeline des tickets.",
                    "long_description": "\nCe plugin ajoute la possibilité de traduire les éléments de la timeline des tickets en utilisant l&#039;API DeepL.\nSouscrivez à [GLPI-Network](https://services.glpi-network.com/) pour en bénéficier.\n        "
                }
            ],
            "required_offers": [
                "network-basic",
                "network-standard",
                "network-advanced"
            ],
            "short_description": "Translate ticket timeline items."
        },
        {
            "id": 286,
            "key": "unread",
            "name": "Unread messages",
            "logo_url": "https://services.glpi-network.com/api/glpi-network/1738/logo.png",
            "xml_url": "https://services.glpi-network.com/api/glpi-network/1738/plugin.xml",
            "homepage_url": "https://services.glpi-network.com",
            "download_url": "https://services.glpi-network.com",
            "issues_url": "https://services.glpi-network.com",
            "readme_url": "https://services.glpi-network.com/documentation/1738/file/README.md",
            "changelog_url": "",
            "license": "GPL V2+",
            "date_added": "2023-12-18T00:00:00.000000Z",
            "date_updated": "2024-11-14T00:00:00.000000Z",
            "download_count": 2362,
            "note": 3.35,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": [
                {
                    "num": "1.0.8",
                    "compatibility": "~10.0.10",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.0.7",
                    "compatibility": "~10.0.10",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.0.6",
                    "compatibility": "~10.0.10",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.0.5",
                    "compatibility": "~10.0.10",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.0.4",
                    "compatibility": "~10.0.10",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.0.3",
                    "compatibility": "~10.0.10",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.0.2",
                    "compatibility": "~10.0.10",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.0.1",
                    "compatibility": "~10.0.10",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.0.0",
                    "compatibility": "~10.0.10",
                    "download_url": None,
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Unread messages GLPI plugin.",
                    "long_description": "This plugin helps you to keep track of unread messages."
                },
                {
                    "lang": "fr",
                    "short_description": "Plugin GLPI Unread messages",
                    "long_description": "Ce plugin permet de garder un suivi des messages non lus."
                }
            ],
            "required_offers": [
                "network-basic",
                "network-standard",
                "network-advanced"
            ],
            "short_description": "Unread messages GLPI plugin."
        },
        {
            "id": 288,
            "key": "glpiai",
            "name": "GLPI AI",
            "logo_url": "https://services.glpi-network.com/api/glpi-network/1864/logo.png",
            "xml_url": "https://services.glpi-network.com/api/glpi-network/1864/plugin.xml",
            "homepage_url": "https://services.glpi-network.com",
            "download_url": "https://services.glpi-network.com",
            "issues_url": "https://services.glpi-network.com",
            "readme_url": "https://services.glpi-network.com/documentation/1864/file/README.md",
            "changelog_url": "",
            "license": "GPL V3+",
            "date_added": "2024-02-20T00:00:00.000000Z",
            "date_updated": "2024-03-01T00:00:00.000000Z",
            "download_count": 1691,
            "note": 3.5714285714285716,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 24,
                    "name": "TECLIB'"
                }
            ],
            "versions": [
                {
                    "num": "1.0.1",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                },
                {
                    "num": "1.0.0",
                    "compatibility": "~10.0.0",
                    "download_url": None,
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Summary tickets timeline items.",
                    "long_description": "This plugin adds the ability to summarize the timeline items of tickets using the Open AI API. Subscribe to [GLPI-Network](https://services.glpi-network.com/) to get it it."
                },
                {
                    "lang": "fr",
                    "short_description": "Résumé des éléments de la timeline des tickets.",
                    "long_description": "Ce plugin ajoute la possibilité de résumer les éléments de la timeline des tickets en utilisant l&#039;API Open AI. Souscrivez à [GLPI-Network](https://services.glpi-network.com/) pour en bénéficier."
                }
            ],
            "required_offers": [
                "network-basic",
                "network-standard",
                "network-advanced"
            ],
            "short_description": "Summary tickets timeline items."
        },
        {
            "id": 293,
            "key": "glpisaml",
            "name": "glpisaml",
            "logo_url": "https://codeberg.org/QuinQuies/glpisaml/raw/branch/main/donut.png",
            "xml_url": "https://codeberg.org/QuinQuies/glpisaml/raw/branch/Donuts-v1.2.0/glpisaml.xml",
            "homepage_url": "https://codeberg.org/QuinQuies/glpisaml/wiki",
            "download_url": "https://codeberg.org/QuinQuies/glpisaml/releases/",
            "issues_url": "https://codeberg.org/QuinQuies/glpisaml/issues",
            "readme_url": "https://codeberg.org/QuinQuies/glpisaml/src/branch/main/README.md",
            "changelog_url": "",
            "license": "GPLv3+",
            "date_added": "2024-04-14T00:00:00.000000Z",
            "date_updated": "2024-10-20T00:00:00.000000Z",
            "download_count": 2749,
            "note": 4.35,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 130,
                    "name": "Chris Gralike"
                }
            ],
            "versions": {
                "6": {
                    "num": "1.1.10",
                    "compatibility": "~10.0.0",
                    "download_url": "https://codeberg.org/QuinQuies/glpisaml/releases/download/v1.1.10/glpisaml.zip",
                    "stability": "stable"
                },
                "0": {
                    "num": "1.1.9",
                    "compatibility": "~10.0.0",
                    "download_url": "https://codeberg.org/QuinQuies/glpisaml/releases/download/v1.1.9/glpisaml.zip",
                    "stability": "stable"
                },
                "1": {
                    "num": "1.1.6",
                    "compatibility": "~10.0.0",
                    "download_url": "https://codeberg.org/QuinQuies/glpisaml/releases/download/v1.1.6/glpisaml.zip",
                    "stability": "stable"
                },
                "2": {
                    "num": "1.1.5",
                    "compatibility": "~10.0.0",
                    "download_url": "https://codeberg.org/QuinQuies/glpisaml/releases/download/v1.1.5/glpisaml.zip",
                    "stability": "stable"
                },
                "3": {
                    "num": "1.1.4",
                    "compatibility": "~10.0.0",
                    "download_url": "https://codeberg.org/QuinQuies/glpisaml/releases/download/v1.1.4/glpisaml.zip",
                    "stability": "stable"
                },
                "4": {
                    "num": "1.1.3",
                    "compatibility": "~10.0.0",
                    "download_url": "https://codeberg.org/QuinQuies/glpisaml/releases/download/v1.1.3/glpisaml.zip",
                    "stability": "stable"
                },
                "5": {
                    "num": "1.1.2",
                    "compatibility": "~10.0.0",
                    "download_url": "https://codeberg.org/QuinQuies/glpisaml/releases/download/v1.1.2/glpisaml.zip",
                    "stability": "stable"
                },
                "7": {
                    "num": "1.1.1",
                    "compatibility": "~10.0.0",
                    "download_url": "https://codeberg.org/QuinQuies/glpisaml/releases/download/v1.1.1/glpisaml.zip",
                    "stability": "stable"
                },
                "8": {
                    "num": "1.1.0",
                    "compatibility": "~10.0.0",
                    "download_url": "https://codeberg.org/QuinQuies/glpisaml/releases/download/v1.1.0/glpisaml.zip",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "Enables you to configure SAML with an external IdP to authenticate and authorize users using the GLPI UI.",
                    "long_description": "Glpisaml provides SAML Single Sign On (SSO) capabilties for GLPI. Glpisaml is written with GLPI10&#43; \n            support in mind. It uses GLPI core components and best-practices for maximum compatibility and \n            maintainability. The plugin enables you to configure multiple SAML providers allowing your customers\n            SSO access as well. The plugin will create new GLPI users on the fly and apply jit rules to assign \n            entities, groups and profiles. For questions join our discord at: https://discord.gg/KyMdkqJcGz. \n            Find an issue, register it at my codeberg site. Written with passion for OSS, Enjoy!\n        "
                }
            ],
            "required_offers": None,
            "short_description": "Enables you to configure SAML with an external IdP to authenticate and authorize users using the GLPI UI."
        },
        {
            "id": 300,
            "key": "phpcas",
            "name": "phpcas",
            "logo_url": "https://raw.githubusercontent.com/InfotelGLPI/phpcas/main/phpcas.png",
            "xml_url": "https://raw.githubusercontent.com/InfotelGLPI/phpcas/main/phpcas.xml",
            "homepage_url": "https://github.com/infotelGLPI/phpcas",
            "download_url": "https://github.com/infotelGLPI/phpcas/releases",
            "issues_url": "https://github.com/infotelGLPI/phpcas/issues",
            "readme_url": "https://github.com/infotelGLPI/phpcas/blob/master/README.md",
            "changelog_url": "",
            "license": "GPL-2.0-or-later",
            "date_added": "2024-08-29T00:00:00.000000Z",
            "date_updated": "2025-01-15T00:00:00.000000Z",
            "download_count": 145,
            "note": 5,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 3,
                    "name": "Xavier Caillaud"
                },
                {
                    "id": 49,
                    "name": "Infotel"
                }
            ],
            "versions": [
                {
                    "num": "1.0.0",
                    "compatibility": "^10.0.10",
                    "download_url": "https://github.com/InfotelGLPI/phpcas/releases/download/1.0.0/glpi-phpcas-1.0.0.tar.bz2",
                    "stability": "stable"
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "short_description": "phpcas GLPI plugin.",
                    "long_description": "Add phpcas library"
                },
                {
                    "lang": "fr",
                    "short_description": "Plugin GLPI phpcas",
                    "long_description": "Ajoute la librairie php-cas"
                }
            ],
            "required_offers": None,
            "short_description": "phpcas GLPI plugin."
        },
        {
            "id": 305,
            "key": "autoexportsearches",
            "name": "AutoExportSearches",
            "logo_url": "https://raw.githubusercontent.com/InfotelGLPI/autoexportsearches/master/export.png",
            "xml_url": "https://raw.githubusercontent.com/InfotelGLPI/autoexportsearches/refs/heads/master/autoexportsearches.xml",
            "homepage_url": "https://github.com/InfotelGLPI/autoexportsearches",
            "download_url": "https://github.com/InfotelGLPI/autoexportsearches/releases",
            "issues_url": "https://github.com/InfotelGLPI/autoexportsearches/issues",
            "readme_url": "https://github.com/InfotelGLPI/autoexportsearches/blob/master/README.md",
            "changelog_url": "",
            "license": "GPL v2+",
            "date_added": "2025-02-21T00:00:00.000000Z",
            "date_updated": "2025-02-25T00:00:00.000000Z",
            "download_count": 112,
            "note": 0,
            "xml_state": "passing",
            "authors": [
                {
                    "id": 114,
                    "name": "Alban Lesellier"
                },
                {
                    "id": 49,
                    "name": "Infotel"
                }
            ],
            "versions": {
                "1": {
                    "num": "2.1.2",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/autoexportsearches/releases/download/2.1.2/glpi-autoexportsearches-2.1.2.tar.bz2",
                    "stability": "stable"
                },
                "2": {
                    "num": "2.1.1",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/autoexportsearches/releases/download/2.1.1/glpi-autoexportsearches-2.1.1.tar.bz2",
                    "stability": "stable"
                },
                "3": {
                    "num": "2.1.0",
                    "compatibility": "~10.0",
                    "download_url": "https://github.com/InfotelGLPI/autoexportsearches/releases/download/2.1.0/glpi-autoexportsearches-2.1.0.tar.bz2",
                    "stability": "stable"
                }
            },
            "descriptions": [
                {
                    "lang": "fr",
                    "short_description": "Ce plugin permet de créer des exports automatiques de recherches sauvegardées",
                    "long_description": "Ce plugin permet de créer des exports automatiques de recherches sauvegardées"
                },
                {
                    "lang": "en",
                    "short_description": "This plugin allows you to create automatic exports from saved searches",
                    "long_description": "This plugin allows you to create automatic exports from saved searches"
                }
            ],
            "required_offers": None,
            "short_description": "This plugin allows you to create automatic exports from saved searches"
        }
    ]

@app.get("/api/marketplace/plugin/{plugin_id}/download/{plugin_version}")
def marketplace_plugin_download(plugin_id: str, plugin_version: str):
    # Request Headers:
    # - X-Registration-Key: %%REGISTRATION_KEY%%
    # - X-Glpi-Network-Uid: %%GLPI_NETWORK_UID%%
    return

@app.get("/api/marketplace/tags/top")
def marketplace_tags_top():
    # Request Headers:
    # - X-Registration-Key: %%REGISTRATION_KEY%%
    # - X-Glpi-Network-Uid: %%GLPI_NETWORK_UID%%
    return [
        {
            "key": "inventaire",
            "tag": "Inventaire",
            "lang": "fr",
            "plugin_count": 48
        },
        {
            "key": "helpdesk",
            "tag": "Helpdesk",
            "lang": "fr",
            "plugin_count": 25
        },
        {
            "key": "gestion",
            "tag": "Gestion",
            "lang": "fr",
            "plugin_count": 25
        },
        {
            "key": "ticket",
            "tag": "ticket",
            "lang": "fr",
            "plugin_count": 19
        },
        {
            "key": "glpi-network",
            "tag": "GLPI-Network",
            "lang": "fr",
            "plugin_count": 14
        },
        {
            "key": "r-seau",
            "tag": "Réseau",
            "lang": "fr",
            "plugin_count": 13
        },
        {
            "key": "donn-es",
            "tag": "données",
            "lang": "fr",
            "plugin_count": 13
        },
        {
            "key": "import",
            "tag": "Import",
            "lang": "fr",
            "plugin_count": 9
        },
        {
            "key": "export",
            "tag": "Export",
            "lang": "fr",
            "plugin_count": 8
        },
        {
            "key": "graphiques",
            "tag": "Graphiques",
            "lang": "fr",
            "plugin_count": 7
        },
        {
            "key": "architecture",
            "tag": "Architecture",
            "lang": "fr",
            "plugin_count": 7
        },
        {
            "key": "rapports",
            "tag": "Rapports",
            "lang": "fr",
            "plugin_count": 6
        },
        {
            "key": "configuration",
            "tag": "Configuration",
            "lang": "fr",
            "plugin_count": 6
        },
        {
            "key": "r-servations",
            "tag": "Réservations",
            "lang": "fr",
            "plugin_count": 5
        },
        {
            "key": "tickets",
            "tag": "tickets",
            "lang": "fr",
            "plugin_count": 5
        }
    ]
