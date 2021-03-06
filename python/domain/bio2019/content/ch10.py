# -*- coding: latin-1 -*-
"""
    fragments - define text fragments in the document
"""
from domain.norm_document.model import Chapter, Section, Norm, Verifier


CH10S01 = Section(
    identifier="10.01",
    title="Cryptografsche beheersmaatregelen",
    text="Doelstelling: Zorgen voor correct en doeltreffend gebruik van cryptografie om de verrtrouwelijkheid, "
         "authenticiteit en/of integriteit van informatie te beschermen.",
    fragments=[

        Norm(
            identifier="10.01.01",
            title="Beleid inzake het gebruik van cryptografische beheersmaatregelen",
            text="Ter bescherming van informatie behoort een beleid voor het gebruik van cryptografische "
                 "beheersmaatregelen te worden ontwikkeld en ge&iuml;mplementeerd.",
            bbn=2,
            fragments=[
                Verifier(
                    identifier="10.01.01/01",
                    title="",
                    text="In het cryptografiebeleid zijn minimaal de volgende onderwerpen uitgewerkt:"
                         "<ol style='list-style-type: lower-alpha;'>"
                         "<li>wanneer cryptografie ingezet wordt;</li>"
                         "<li>wie verantwoordelijk is voor de implementatie;</li>"
                         "<li>wie verantwoordelijk is voor het sleutelbeheer;</li>"
                         "<li>welke normen als basis dienen voor cryptografie en de wijze waarop de normen van het "
                         "forum standaardisatie worden toegepast;</li>"
                         "<li>de wijze waarop het beschermingsniveau vastgesteld wordt;</li>"
                         "<li>bij inter-organisatie communicatie wordt het beleid onderling vastgesteld.</li>"
                    "</ol>",
                    bbn=2,
                ),
                Verifier(
                    identifier="10.01.01/02",
                    title="",
                    text="Crypografische toepassingen voldoen aan passende standaarden.",
                    bbn=2,
                ),
            ],
        ),

        Norm(
            identifier="10.01.02",
            title="Sleutelbeheer",
            text="Met betrekking tot het gebruik, de bescherming en de levensduur van cryptografische sleutels "
                 "behoort tijdens hun gehele levenscyclus een beleid te worden ontwikkeld en ge&iuml;mplementeerd.",
            bbn=1,
            fragments=[
                Verifier(
                    identifier="10.01.02/01",
                    title="",
                    text="Ingeval van PKI-overheid certificaten: hanteer de PKI-Overheid-eisen t.a.v. het "
                         "sleutelbeheer.<br/>"
                         "In overige situaties: hanteer de standaard ISO-11770 voor het beheer van "
                         "cryptografische sleutels.",
                    bbn=2,
                ),
                Verifier(
                    identifier="10.01.02/02",
                    title="",
                    text="Er zijn (contractuele) afspraken over reservecertificaten van een alternatieve leverancier "
                         "als uit risicoafweging blijkt dat deze noodzakelijk zijn.",
                    bbn=2,
                ),
            ],
        ),

    ],
)


CH10 = Chapter(
    identifier="10",
    title="Cryptografie",
    fragments=[
        CH10S01,
    ]
)
