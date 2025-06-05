import streamlit as st
from Home import selection_per_product_group, selection_quality, quality_piecharts, quality_point_barchart_carat_and_price_avgs

def page_function(df, price_range, lowest_quality_for_sorting, md_text):

    st_selection_per_product_group = selection_per_product_group(df, price_range)
    df_page = st_selection_per_product_group

    st_selection_quality = selection_quality(df_page, lowest_quality_for_sorting[0], lowest_quality_for_sorting[1], lowest_quality_for_sorting[2])
    df_page_sorted_quality = st_selection_quality

    st_quality_piecharts = quality_piecharts(df_page, show=False)
    st_quality_point_barchart_carat_and_price_avgs = quality_point_barchart_carat_and_price_avgs(df_page, show=False)

    st_quality_piecharts_sorted = quality_piecharts(df_page_sorted_quality, show=False)
    st_quality_point_barchart_carat_and_price_avgs_sorted = quality_point_barchart_carat_and_price_avgs(
        df_page_sorted_quality, show=False)

    st.markdown(md_text)

    st.markdown(f""" ### Hela datasettet i detta prissegment
    Antal diamanter: {len(df_page)}""")

    st.pyplot(st_quality_piecharts)
    st.pyplot(st_quality_point_barchart_carat_and_price_avgs)

    st.markdown(f""" ### Sorterat efter vår önskade lägsta kvalitetsgrad
    Antal diamanter sorterat efter kvalitet: {len(df_page_sorted_quality)}""")

    st.pyplot(st_quality_piecharts_sorted)
    st.pyplot(st_quality_point_barchart_carat_and_price_avgs_sorted)
