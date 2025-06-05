import streamlit as st
from Home import *
from page_functions import page_function


pricerange_for_page = (0, 2500 * 0.3)
lowest_quality_for_page = (("Ideal", "Premium", "Very Good"), ("D", "E", "F", "G", "H"),
                           ("IF", "VS1", "VS2", "VVS1", "VVS1", "SI1"))
markdown_text = """
    #### 1. Budgetsegment
Nedan visas kvalitetsdistrubitionen för vårt lägsta prissegment innehållande totalt 8428 diamanter. För att bibehålla en relativt
 hög kvalitetsgrad väljer vi att filtera på endast de diamanter med kvalitetsattribut med följande lägstagrad:
- slipningsgrad - Very good
- färgkvalitet - H
- klarhet - SI1

Vi får vi ett filter på de 4855 diamanter i denna kvalitetsklass. Detta motsvarar ungefär 57.6% av diamanterna i datasettet.
Om vi skulle öka kvalitetsgraden skulle vi ha problem att uppfylla önskan om att hålla detta som vår största marknadsdel då antalet
 diamanter sorterade på kvalitet skulle falla kraftigt. Därmed rekomenderar jag detta som lägsta kvalitetsgrad för budgetsegmentet.
  Som primär fokus bör kvalitetsgraden ligga mellan 9 och 4 för större andelen av våra inköp, med fokus på högre kvalitet 
  för produkter längre upp i segmentet för att kunna rättfärdiga den ökade kvaliten i vår marginal.

"""

page_function(df, pricerange_for_page, lowest_quality_for_page, markdown_text)