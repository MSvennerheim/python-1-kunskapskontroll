import streamlit as st
from Home import *
from page_functions import page_function

pricerange_for_page = (6000 * 0.3, 20000 * 0.3)
lowest_quality_for_page = (("Ideal", "Premium", "Very Good"), ("D", "E", "F", "G"), ("IF", "VS1", "VS2", "VVS1", "VVS1"))
markdown_text = """
#### 3. Lägre Premium

I vårt lägre premium segment hittar vi den största andelen av diamanter i vårt dataset, 19870 st, men vi har även en
 större andel av våra diamanter i lägre kvalitetsgrad, runt grad 9. Däremot har vi mycket större spridning av karat, där genomsnittet skiljer sig över 1 ct från lägsta till högsta kvalitetsgrad. I detta fall har jag valt att behålla den lägsta kvalitetsgraden från midrange segmentet ovan:
- slipningsgrad - Very good
- färgkvalitet - G
- klarhet - VS2

Vilket ger oss 3928 diamanter, ~19.7% av segmentet, som jag anser är en godtagbar andel för denna andel av sortimentet.
För detta segment rekomenderar jag kvalitetsklasser mellan 7 och 3 för största valmöjlighet.
Dessa diamanter innehåller dock i genomsnitt diamanter i lägre karat. Hade vi hade önskat att få in större diamanter i
 sortimentet hade vi fått sänka kvalitetsgraden ytterligare.
"""

page_function(df, pricerange_for_page, lowest_quality_for_page, markdown_text)