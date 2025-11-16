import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("database_titanic.csv")

st.write("CONTROL3")

with st.sidebar:
    st.write("barra")

st.header("Análisis de supervivientes")

div = st.slider('Número de bins:', 0, 10, 2)
st.write("Bins=", div)



datos_sexo = df.groupby('Sex')['Survived'].value_counts().unstack()
datos_sexo = datos_sexo.rename(columns={0: 'No Sobrevivió', 1: 'Sobrevivió'})


fig_sexo, ax_sexo = plt.subplots(figsize=(9, 5))


datos_sexo.plot(kind='bar', 
                stacked=False, 
                ax=ax_sexo, 
                colormap='coolwarm')


ax_sexo.set_title('Supervivencia por Sexo')
ax_sexo.set_ylabel('Número de Pasajeros')
ax_sexo.set_xlabel('Sexo')
ax_sexo.tick_params(axis='x', rotation=0) 
ax_sexo.legend(title='Destino')


st.pyplot(fig_sexo)