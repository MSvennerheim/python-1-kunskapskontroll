import streamlit as st
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
diamonds_path = os.path.join(parent_dir, 'diamonds.csv')
from functions import *
df = pd.read_csv(diamonds_path)



st.title("Del 2 - Streamlit applikation")
st.markdown("""
## Antagande om Guldfynd:

- Guldfynd letar primärt efter enstaka diamanter per smycke för varje prisklass som defineras här under
- 30% av slutpriset hos ett smycke går till inköp av diamanter och att inköpspriset samt försäljningspriset är i sek.
- Icke-numeriska kvalitativa attribut värderas lika högt från bästa till sämsta
- Guldfynd har önskade (och i rapporten antagna) minstakrav på varje kvalitetsatribut
- Att detta är ett mindre pilotprojekt för ett mindre antal av företagets butiker och att inköp till detta sker utifrån datasettet
-  Att datasettet är representativt av den större diamantmarkaden

### Antagande om priskategorier för försäljningspristet av smycken samt andelen av diamantprodukter i deras sortiment:
- budgetprodukter - <2500 sek, 40% av soritmentet
- midrangeprodukter - 2500 - 6000 sek, 35% av sortimentet
- lägre premium - 6000 - 20000 sek, 15% av sortimentet
- högre premium - 20000+ sek, 10% av sortimentet

## Bakgrund
I följande analys tolkas vårt dataset för diamanter och potentiella fokusområden utifrån vår tillgängliga data och för varje prissegment.
Vi sätter även upp ett system för att kvantifiera icke-numerisk kvalitetsdata, där ett lägre värde innebär högre kvalitet på diamanten. Detta för att undvika att datapunkter med fler typer påverkar kvalitetspoängen i en högre grad än för datapunkter med färre typer. Detta innebär att en diamant med kvalitetspoäng 0 har en ideel slipning, högsta klarhet och bästa färg och att en diamant med kvalitetspoäng 17 har den sämsta graden av samtliga attribut.
För att förenkla analysen har även datapunkterna table, x, y och z ignorerats då dessa ungefärligt beskrivs av karat och slipningsgrad.

### Notering
I streamlitapplikationen har den första delen av analysen lämnats ur, endast analysen för prisklasserna finns här.
""")