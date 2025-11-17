import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("database_titanic.csv")

st.header("Control3")
st.write("En esta pagina reunimos datos sobre las personas que abordaron el titanic, los cuales veremos representados tanto de forma grafica y tabulados.")

with st.sidebar:
    div = st.slider('Número de bins:', 0, 10, 2)
    st.write("Bins=", div)

fig, ax = plt.subplots(1, 2, figsize=(10, 3))
ax[0].hist(df["Age"], bins=div)
ax[0].set_title("Edad")
ax[0].set_ylabel("Frecuencia")
ax[0].set_xlabel("Histograma de edades")

df_male = df[df["Sex"] == "male"]
cant_male = len(df_male)

df_female = df[df["Sex"] == "female"]
cant_female = len(df_female)

ax[1].bar(["Masculino", "Femenino"], [cant_male, cant_female], color = "red")
ax[1].set_title("Sexo")
ax[1].set_ylabel("Cantidad")
ax[1].set_xlabel('Distribucion de hombres y mujeres')

datos_sexo = df.groupby('Sex')['Survived'].value_counts().unstack()
datos_sexo = datos_sexo.rename(columns={0: 'No Sobrevivió', 1: 'Sobrevivió'})


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

st.header("Analisis de pasajeros")
st.pyplot(fig)

st.header("Analisis de supervivientes")
st.write("En el grafico a continuacion podemos ver la cantidad de personas que sobrevivieron y las que no en el titanic, ademas de su sexo.")
st.pyplot(fig_sexo)

st.header("Datos")
st.table(df.head())
