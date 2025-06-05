import streamlit as st
from Home import *
from page_functions import page_function

pricerange_for_page = (20000 * 0.3, df["price"].max())
lowest_quality_for_page = (("Ideal", "Premium", "Very Good"), ("D", "E", "F", "G"), ("IF", "VS1", "VS2", "VVS1", "VVS1"))
markdown_text = """
#### 4. **Högre Premium**

I vårt övre segment finner vi 11551 diamanter, fördelat runt en något högre kvalitetsgrad jämfört med vårt föregående 
segment, runt 7. Där segmentet däremot skilljer sig mer markant är genosnittsgraden av diamanterna. Där endast
 toppsegmentet av 0 ligger under en karat.

Som i våra föregående segment väljer jag här att lägga vårt minimumfokus som följande:
- slipningsgrad - Very good
- färgkvalitet - G
- klarhet - VS2

Detta ger oss 3520 diamanter i segmentet, ~30.5% av segmentet. Här bör vi primärt fokusera på grupperna 8-4 för
 våra inköp. Likt det lägre premiumsegmentet bör vi sänka kvalitetsgraden om vi önskar större diamanter i dessa smycken.
"""

page_function(df, pricerange_for_page, lowest_quality_for_page, markdown_text)