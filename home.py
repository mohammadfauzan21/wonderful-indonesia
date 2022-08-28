#library
import streamlit as st

from PIL import Image
image_monas = Image.open("monas.jpg")
image_labuanbj = Image.open("labuan bajo.jpg")
image_gualiangbua = Image.open("gua liang bua.jpg")

st.set_page_config (page_title="Here in Indonesia", layout="wide")

st.title("Here in Indonesia")

#side bar
add_selectbox = st.sidebar.selectbox(
    "Where do you want to go?",
    ("Jakarta", "Nusa Tenggara Timur", "Nusa Tenggara Barat", "Papua", "Bali", "Yogyakarta")
)

if add_selectbox == "Jakarta" :
    tab1, tab2, tab3 = st.tabs(["Jakarta Pusat", "Jakarta Timur", "Jakarta Utara"])

    with tab1:
        st.header("Monas")
        st.image(image_monas, width=500, caption= "Source = https://tirto.id/jadwal-buka-monas-2022-cara-pesan-tiket-online-dan-harga-tiket-gtDG ")
    with tab2:
        st.header("Ragunan")
    with tab3:
        st.header("Kota Tua")

if add_selectbox == "Nusa Tenggara Timur" :
    tab1, tab2 = st.tabs(["Manggarai Barat", "Manggarai"])

    with tab1:
        st.header("Labuan Bajo")
        st.image(image_labuanbj, width=500, caption= "Source = https://travel.okezone.com/read/2022/08/01/406/2640239/harga-tiket-masuk-pulau-komodo-naik-10-000-wisatawan-batal-kunjungi-labuan-bajo")
    with tab2:
        st.header("Gua Liang Bua")
        st.image(image_gualiangbua, width=500, caption= "https://merahputih.com/post/read/gua-liang-bua-rumah-si-hobbit-dari-flores")
