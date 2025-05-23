import streamlit as st
import xml.etree.ElementTree as ET
import tempfile

def extract_info_from_ir21(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    info = {
        "Adresses IP": [],
        "MSISDN": [],
        "ASN": [],
        "IPX Provider": []
    }

    for elem in root.iter():
        tag = elem.tag.lower()
        text = elem.text.strip() if elem.text else ""

        if "ipaddress" in tag and text:
            info["Adresses IP"].append(text)
        elif "msisdn" in tag and text:
            info["MSISDN"].append(text)
        elif "asn" in tag and text:
            info["ASN"].append(text)
        elif "ipx" in tag and "provider" in tag and text:
            info["IPX Provider"].append(text)

    return info

st.title("📄 IR21 Extractor")

uploaded_file = st.file_uploader("Choisissez un fichier IR21 au format XML", type="xml")

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".xml") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    data = extract_info_from_ir21(tmp_path)

    option = st.selectbox(
        "Quel type d'information voulez-vous extraire ?",
        list(data.keys())
    )

    if st.button("Extraire les données"):
        st.subheader(f"Résultats : {option}")
        if data[option]:
            for val in data[option]:
                st.markdown(f"- `{val}`")
        else:
            st.info("Aucune donnée trouvée.")
