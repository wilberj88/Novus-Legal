import streamlit as st

st.set_page_config(layout="wide", page_title="Novus Legal ⚖️", page_icon="⚖️")

st.title('Novus Legal ⚖️')

st.header("🛣 Defensa Jurídica ante Consecionarios Viales 🚧")

st.markdown(
  """
  - 🔎_    Dimensiona cuantos riesgos implican las obras de conseciones viales en tu territorio
  - 🛒_    Presupuesta tus potenciales pérdidas y activa un Plan Jurídico de Defensa
  - 🧾_    Controla en tiempo real el estado de tu defensa y garantía de tus derechos
  
  EMPIEZA TU 🔎 DIAGNÓSTICO AHORA 🕰
  """
)

col1, col2 = st.columns(2)

with col1:
    tramo = st.selectbox(
        "Indica el tramo donde se encuentra tu terreno adyacente o sobre la vía Panamericana",
        ("Km0-Km50", "Km50-Km120", "Km120-Km200", "Km200-Km300", "Km300-Km500"),
    )
    uso = st.radio(
        "Tipo de uso de tu terreno",
        options=['Gasolinera', 'Restaurante','Hotel', 'Montallantas', 'Casa', 'Mejoras_Vivienda', 'Rastrojo'],
    )
    antiguedad = st.selectbox(
        "Antiguedad de la contabiliad del negocio",
        ("No tengo contabilidad", "Menos de 1 año", "Más de 2 años", "Más de 3 años"),
    )

with col2:
    correo = st.text_input('Ingrese su correo electrónico:', '''
    ''')
    matricula = st.text_input('Ingrese número de matrícula mercantil del predio:', '''
    ''')
    cedula =  st.text_input('Ingrese número de cédula de propietario o NIT de operador:', '''
    ''')
    predial =  st.text_input('Ingrese el número predial:', '''
    ''')
    a = st.selectbox('Elige cuál derecho quisieras priorizar en tu defensa:', ['Facturación comercial diaria', 'Ubicación del negocio', 'Daños Ecosistémicos', 'Daño de Cultivos', 'Daños a la Construcción'])


b = st.selectbox('Indica en cuál horario te queda mejor el acompañamiento jurídico:', ['Mañanas laborales', 'Tardes laborales', 'Fines de Semana'])
c = st.selectbox('¿Cuéntas con el presupuesto para los estudios ambientales y de suelos?:', ['Sí', 'No'])

d = st.slider('¿Años de propiedad del predio?', 0, 24)

h = st.button('Enviar solicitud de defensa a Novus Legal ⚖️')

if h:
    st.write('¡Solicitud enviada! En breve te compartiremos a ', correo, 'tu plan personalizado con atención de blindaje del predio con matrícula ', matricula,' durante las horarios de <<', b, '>>')

