#library
import streamlit as st

from PIL import Image
image_monas = Image.open("monas.jpg")
image_labuanbj = Image.open("labuan bajo.jpg")
image_kotatua = Image.open("kota tua.png")
image_rajaampat = Image.open('raja ampat papua.jpg')

st.set_page_config (page_title="Here in Indonesia", layout="wide")

st.title("Here in Indonesia")

#side bar
add_selectbox = st.sidebar.selectbox(
    "Where do you want to go?",
    ("Jakarta", "Nusa Tenggara Timur", "Papua")
)
#Jakarta
if add_selectbox == "Jakarta" :
    tab1, tab2 = st.tabs(["Jakarta Pusat", "Jakarta Utara"])

    with tab1:
        col1, col2 = st.columns(spec=[0.5,1], gap="large")
        with col1:
            st.header("Monas")
            st.image(image_monas, width=300, caption= "Sumber = https://tirto.id")
        with col2:
            st.write(
            "   Monumen nasional atau yang dikenal dengan monas adalah sebuah landmark Indonesia yang terletak di DKI Jakarta. Monas didirikan saat pemerintahan Soekarno dengan arsitek yang bernama Soedarsono. Soedarsono merancang monas dengan merepresentasikan lingga dan yoni. Lingga dan yoni terletak pada bentuk tugu yang menjulang tinggi dengan pelataran cawan yang luas mendatar. Dalam ajaran Hindu, penyatuan lingga dan yoni akan menghasilkan kekuatan tertinggi. Selain itu, lingga dan yoni melambangkan kekhasan Indonesia, di mana lingga menyerupai alu dan yoni menyerupai wadah yang berupa lumpang. Alu dan lumpang adalah dua alat yang dianggap penting dan dimiliki oleh setiap keluarga di Indonesia, khususnya rakyat pedesaan."
            )
            st.write("\n")
            st.write("Sumber : Adryamarthanino. 2022. Sejarah Monumen Nasional (Monas). Kompas.com")
    with tab2:
        col1, col2 = st.columns(spec=[0.5,1], gap="large")
        with col1:
            st.header("Kota Tua")
            st.image(image_kotatua, width=300, caption= "Foto = Instagram.com/iyan_93 ")
        with col2:
            st.write(
                    "The Pearl of Orient atau Mutiara dari Timur merupakan salah satu julukan yang diberikan oleh penjajah kepada Kota Tua Jakarta. Kota Jakarta (Batavia) dipersiapkan untuk menjadi duplikat ibukota Belanda oleh para penjajah sehingga diberi nama Koningen van Oosten atau Ratu dari Timur. Kota Batavia didirikan di sebuah wilayah yang dulunya bernama Jayakarta (1527-1619). Daerah ini berdekatan dengan pelabuhan Kesultanan Banten yang bernama Sunda Kalapa. Pelabuhan tersebut sudah ada sejak zaman Kerajaan Sunda sebagai sarana perdagangan antar pulau di Nusantara."
            )
            st.write(
                "Pada tahun 1610, pelabuhan Sunda Kelapa dan Jayakarta diserang oleh perusahaan dagang Belanda VOC (Verenigde Oostindische Compagnie) yang dipimpin Jan Pieterzoon Coen. Kemudian, pada tahun 1620, VOC membangun kota yang baru, tepat di atas reruntuhan Kota Jayakarta dan selesai dibangun pada tahun 1650. VOC menamai kota baru itu sebagai Batavia. Sejak saat itu, VOC mengendalikan semua kegiatan perdagangan, militer, dan politiknya selama menguasai Nusantara, hingga dilanjutkan oleh Pemerintahan Hindia Belanda. Nama Batavia digunakan sejak tahun 1621 hingga tahun 1942 Belanda ditaklukkan oleh Jepang. Kemudian, Jepang mengganti nama Batavia menjadi Jakarta dan bertahan hingga saat ini."
            )
            st.write("\n")
            st.write("Sumber : Mutiarasari. 2022. Sejarah Kota Tua Jakarta yang Baru Direvitalisasi, Yuk Disimak!. Detik.com")


#Nusa Tenggara Timur
if add_selectbox == "Nusa Tenggara Timur" :
    col1, col2 = st.columns(spec=[0.5,1], gap="large")
    with col1:
        st.header("Labuan Bajo")
        st.image(image_labuanbj, width=300, caption= "Foto = https://travel.okezone.com")
    with col2:
        st.write(
            "Labuan Bajo memiliki banyak sekali tempat obyek wisata. Obyek-obyek wisata yang terkenal di labuan bajo yaitu Pulau Komodo, Pantai Pink, Manta Point, Pulau-pulau kecil seperti kanawa, loh liang, air terjun bahkan goa pun terdapat di Labuan Bajo. Pulau yang paling terkenal diantara semuanya adalah Pulau Komodo. Pulau Komodo disebut demikian oleh karena terdapat hewan-hewan komodo."
        )
        st.write(
            "Hewan komodo ini yang merupakan hewan satu-satunya yang selamat setelah dahulu kala terjadi letusan gunung Krakatau yang menyebabkan terjadinya tsunami besar. Dengan keberadaannya yang lengendaris, hewan komodo ini merupakan salah satu hewan yang dilindungi. Begitu juga Pulau Komodo menjadi Taman Nasional yang diakui sebagai kategori situs warisan dunia oleh badan perserikatan bangsa-bangsa yaitu UNESCO."
        )
        st.write(
            "Selain Pulau Komodo, yang juga terkenal adalah Pantai bewarna Pink dan Manta Point. Pantai pink adalah pantai dengan pasir yang berwarna pink yang sangat menarik dan unik pemandangannya sedangkan Manta Point adalah patung yang terdapat didasar salah satu pantai yang ada di Labuan Bajo, Patung ini yang menjadi salah satu spot diving yang juga memiliki keunikan."
        )
        st.write("\n")
        st.write("Sumber : Ruqyah Cirebon, 2021. Mengenal Sejarah Labuan Bajo; Destinasi Wisata Eksotis di Indonesia. www.indonesiana.id")

#Nusa Tenggara Barat
if add_selectbox == "Papua" :
    col1, col2 = st.columns(spec=[0.5,1], gap="large")
    with col1:
        st.header("Raja Ampat")
        st.image(image_rajaampat, width=300, caption= "Foto = http://sengpaku.blogspot.com")
    with col2:
        st.write(
            "Melansir dari indonesia.travel, diterangkan bahwa Raja Ampat terletak di bagian barat Papua dan memiliki luas kurang lebih 4,6 juta hektar. Raja Ampat merupakan surga yang berada di wilayah Indonesia timur.Menurut laporan dari The Nature Conservancy and Conservation Internasional, ada kurang lebih 75% spesies karang dunia di kepulauan ini. Selain itu, Raja Ampat juga memiliki 1.318 jenis ikan, 699 moluska, dan 547 terumbu karang. Mengutip dari kkprajaampat.com, kepulauan ini diketahui berada di jantung Segitiga Terumbu Karang Dunia. Arus laut dalam yang kuat membawa banyak nutrisi di perairan ini hingga ke hutan bakau, danau air asin, dan hamparan padang lamuan."
        )
        st.write(
            "Kepulauan ini memiliki terumbu karang yang sangat melimpah. Terumbu karang di kepulauan ini menjadi tempat tinggal bagi biota laut lainnya. Keindahan bawah laut Raja Ampat membuat banyak orang ingin menyaksikan langsung dengan cara menyelam ke dalam lautan. Di tempat wisata ini, ada beberapa spot menyelam terbaik seperti Kabui Passage, di sekitar Dermaga Pulau Arborek, Sauwandarek, Yenbuba, Dinding Friwen, dan masih banyak lagi. Tak hanya pemandangan bawah laut yang indah, Raja Ampat juga juga memiliki pemandangan daratan yang indah. Anda bisa menikmati pemandangan pulau batu dari atas bukit."
        )
        st.write("\n")
        st.write("Sumber : Siti Nur Aeni, 2021. Raja Ampat, Destinasi Wisata Favorit yang Memiliki Banyak Keindahan. Katadata.co.id")
