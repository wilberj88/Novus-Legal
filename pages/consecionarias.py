import streamlit as st

st.set_page_config(layout="wide", page_title="Novus Legal ⚖️", page_icon="⚖️")

st.title('Novus Legal ⚖️')

st.header("🛣 Defensa Jurídica ante Consecionarios Viales 🚧")

st.markdown(
  """
  - 🔎_    Dimensiona cuantos riesgos implican las obras de conseciones viales en tu territorio
  - 🛒_    Presupuesta tus potenciales pérdidas y activa plan jurídico de defensa
  - 🧾_    Monitoriza en tiempo real el estado de tu defensa y la conquista de tus derechos
  
  EMPIEZA TU 🔎 DIAGNÓSTICO AHORA 🕰
  """
)

col1, col2 = st.columns(2)

with col1:
    territorio = st.selectbox(
        "Indica el tramo donde se encuentra tu terreno adjunto a la vía Panamericana",
        ("Km0-Km50", "Km50-Km120", "Km120-Km200", "Km200-Km300", "Km300-Km500"),
    )
    categoria = st.radio(
        "Tipo de uso de tu terreno",
        options=['Gasolinera', 'Restaurante','Hotel', 'Montallantas', 'Casa', 'Rastrojo'],
    )

with col2:
    redsocial = st.selectbox(
        "Antiguedad de la contabiliad del negocio",
        ("No tengo contabilidad", "Menos de 1 año", "Más de 2 años", "Más de 3 años"),
    )
    perfil = st.text_input('Ingrese número de matrícula mercantil del predio', '''
    ''')
    otroscandidatos =  st.text_input('Ingrese número de cédula de propietario o NIT de operador', '''
    ''')

a = st.selectbox('Elige cuál derecho quisieras priorizar en tu defensa:', ['Facturación comercial diaria', 'Ubicación del negocio', 'Daños Ecosistémicos', 'Daño de Cultivos'])
b = st.selectbox('Indica en cuál horario te queda mejor el acompañamiento jurídico:', ['Mañanas laborales', 'Tardes laborales', 'Fines de Semana'])
c = st.selectbox('¿Cuéntas con el presupuesto para los estudios ambientales y de suelos?:', ['Sí', 'No'])

h = st.slider('Años de propiedad del predio?', 0, 24)

i = st.button('Enviar solicitud de defensa a Novus Legal ⚖️')

st.write('¡Solicitud enviada! En breve te compartiremos un plan personalizado de ', h,' horas semanales, mediante ejemplos asociados a <<', c, '>> para que aprendas <<', a, '>> y logres aportar a salvar al planeta en <<', b, '>>.')

