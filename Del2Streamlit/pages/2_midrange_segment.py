import streamlit as st
from Home import *
from page_functions import page_function

pricerange_for_page = (2500 * 0.3, 6000 * 0.3)
lowest_quality_for_page = (("Ideal", "Premium", "Very Good"), ("D", "E", "F", "G"), ("IF", "VS1", "VS2", "VVS1", "VVS1"))
markdown_text = """
#### 2. Midrange segmentet

När vi går vidare till vårt nästa prissegment ser vi redan att antalet diamanter har ökat till 14091, detta ger oss
 lite större frihet att höja kvalitetsgraden på våra krav till följande:
- slipningsgrad - Very good
- färgkvalitet - G
- klarhet - VS2

Detta ger oss 6740 diamanter, en lägre procentuell andel på antalet diamanter i utfallet, ~47.8%, men om vi förväntar
 oss en 35% andel av våra produkter i detta segment har vi fortfarande en större tillgång till val även med dessa
  minimumkrav. Här rekomenderas ett primärt fokus på kvalitetsklasserna 7 till 2 för större andelen av våra inköp.
"""

page_function(df, pricerange_for_page, lowest_quality_for_page, markdown_text)