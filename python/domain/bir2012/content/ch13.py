# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


S1301 = Section(
    identifier="13.01",
    title="Rapportage van informatiebeveiligingsgebeurtenissen en zwakke plekken",
    fragments=[
        Norm(
            identifier="13.01.01",
            title="Rapportage van informatiebeveiligingsgebeurtenissen",
            text="Informatiebeveiligingsgebeurtenissen behoren zo snel mogelijk via de juiste leidinggevende niveaus "
                 "te worden gerapporteerd.",
            fragments=[
                Verifier(
                    identifier="13.01.01/01",
                    title="",
                    text="Er is een procedure voor het rapporteren van beveiligingsgebeurtenissen vastgesteld, "
                         "in combinatie met een reactie- en escalatieprocedure voor incidenten, waarin de "
                         "handelingen worden vastgelegd die moeten worden genomen na het ontvangen van een rapport "
                         "van een beveiligingsincident.",
                ),
                Verifier(
                    identifier="13.01.01/02",
                    title="",
                    text="Er is een contactpersoon aangewezen voor het rapporteren van beveiligingsincidenten. "
                         "Voor integriteitsschendingen is ook een vertrouwenspersoon aangewezen die meldingen in "
                         "ontvangst neemt.",
                ),
                Verifier(
                    identifier="13.01.01/03",
                    title="",
                    text="Vermissing of diefstal van apparatuur of media die gegevens van de Rijksdienst kunnen "
                         "bevatten wordt altijd ook aangemerkt als informatiebeveiligingsincident.",
                ),
                Verifier(
                    identifier="13.01.01/04",
                    title="",
                    text="Informatie over de beveiligingsrelevante handelingen van de gebruiker wordt regelmatig "
                         "nagekeken. De BVA bekijkt maandelijks een samenvatting van de informatie.",
                ),
            ],
        ),
        Norm(
            identifier="13.01.02",
            title="Rapportage van zwakke plekken in de beveiliging",
            text="Van alle werknemers, ingehuurd personeel en externe gebruikers van informatiesystemen en -diensten "
                 "behoort te worden ge�ist dat zij alle waargenomen of verdachte zwakke plekken in systemen of "
                 "diensten registreren en rapporteren.",
            fragments=[
                Verifier(
                    identifier="13.01.02/01",
                    title="",
                    text="Er is een proces om eenvoudig en snel beveiligingsincidenten en zwakke plekken in de "
                         "beveiliging te melden.",
                ),
            ],
        ),
    ],
)


S1302 = Section(
    identifier="13.02",
    title="Beheer van informatiebeveiligingsincidenten en -verbeteringen",
    fragments=[
        Norm(
            identifier="13.02.01",
            title="Verantwoordelijkheden en procedures",
            text="Er behoren leidinggevende verantwoordelijkheden en procedures te worden vastgesteld om een snelle, "
                 "doeltreffende en ordelijke reactie op informatiebeveiligingsincidenten te bewerkstelligen.",
            fragments=[
                Verifier(
                    identifier="13.02.01/01",
                    title="",
                    text="Er zijn procedures voor rapportage van gebeurtenissen en escalatie. Alle medewerkers "
                         "behoren op de hoogte te zijn van deze procedures.",
                ),
            ],
        ),
        Norm(
            identifier="13.02.02",
            title="Leren van informatiebeveiligingsincidenten",
            text="Er behoren mechanismen te zijn ingesteld waarmee de aard, omvang en kosten van "
                 "informatiebeveiligingsincidenten kunnen worden gekwantificeerd en gecontroleerd.",
            fragments=[
                Verifier(
                    identifier="13.02.02/01",
                    title="",
                    text="De informatie verkregen uit het beoordelen van beveiligingsmeldingen wordt ge�valueerd met "
                         "als doel beheersmaatregelen te verbeteren.",
                ),
            ],
        ),
        Norm(
            identifier="13.02.03",
            title="Verzamelen van bewijsmateriaal",
            text="Waar een vervolgprocedure tegen een persoon of organisatie na een informatiebeveiligingsincident "
                 "juridische maatregelen omvat (civiel of strafrechtelijk), behoort bewijsmateriaal te worden "
                 "verzameld, bewaard en gepresenteerd overeenkomstig de voorschriften voor bewijs die voor het "
                 "relevante rechtsgebied zijn vastgelegd.",
            fragments=[
                Verifier(
                    identifier="13.02.03/01",
                    title="",
                    text="Voor een vervolgprocedure naar aanleiding van een beveiligingsincident behoort "
                         "bewijsmateriaal te worden verzameld, bewaard en gepresenteerd overeenkomstig de "
                         "voorschriften voor bewijs die voor het relevante rechtsgebied zijn vastgelegd.",
                ),
            ],
        ),
    ],
)


CH13 = Chapter(
    identifier="13",
    title="Beheer van Informatiebeveiligingsincidenten",
    fragments=[
        S1301,
        S1302,
    ]
)
