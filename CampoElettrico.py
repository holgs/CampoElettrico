import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Sidebar for selecting the number of charges
num_charges = st.sidebar.number_input('Number of Charges', min_value=1, max_value=10, value=1, step=1)

st.write(f"You have selected {num_charges} charges.")

grid_density = st.sidebar.slider('Grid Density', min_value=5, max_value=50, value=20, step=5)
stream_density = grid_density / 20
st.write(f"You have selected a grid density of {grid_density}x{grid_density}.")

x_min = st.sidebar.number_input('x-axis min value', min_value=-10, max_value=10, value=-10, step=1)
x_max = st.sidebar.number_input('x-axis max value', min_value=-10, max_value=10, value=10, step=1)
y_max = st.sidebar.number_input('y-axis max value', min_value=-10, max_value=10, value=10, step=1)
y_min = st.sidebar.number_input('y-axis min value', min_value=-10, max_value=10, value=-10, step=1)


charges = []
#for i in range(num_charges):
#  charge_x = st.sidebar.number_input(f'Charge {i+1} x-coordinate', value=0.0)
#  charge_y = st.sidebar.number_input(f'Charge {i+1} y-coordinate', value=0.0)
#  charge_value = st.sidebar.selectbox(f'Charge {i+1} value', options=[-1, 1])
#  charges.append((charge_x, charge_y, charge_value))

for i in range(num_charges):
    x = st.sidebar.number_input(f'Charge {i+1} x-coordinate', min_value=-10.0, max_value=10.0, value=0.0, step=0.5, format="%.1f")
    y = st.sidebar.number_input(f'Charge {i+1} y-coordinate', min_value=-10.0, max_value=10.0, value=0.0, step=0.5, format="%.1f")
    charge = st.sidebar.number_input(f'Charge {i+1} value', min_value=-10.0, max_value=10.0, value=1.0, step=0.1, format="%.1f")
    charges.append([x, y, charge])

st.write('Charges:')
for charge in charges:
  st.write(f"Position: ({charge[0]}, {charge[1]}), Value: {charge[2]}")


def electric_field(charge, r, r_charge):
  """Calcola il campo elettrico prodotto da una singola carica."""
  k = 8.99e9  # Costante di Coulomb in N(m^2)/C^2
  R = r - r_charge  # vettore di distanza
  R_norm = np.linalg.norm(R)  # norma del vettore di distanza
  E = k * charge * R / R_norm**3  # Campo elettrico
  return E


def electric_potential(charge, r, r_charge):
  """Calcola il potenziale elettrico prodotto da una singola carica."""
  k = 8.99e9  # Costante di Coulomb in N(m^2)/C^2
  R = r - r_charge  # vettore di distanza
  R_norm = np.linalg.norm(R)  # norma del vettore di distanza
  V = k * charge / R_norm  # Potenziale elettrico
  return V

@st.cache_data
def total_electric_field(charges, r):
  """Calcola il campo elettrico totale prodotto da un insieme di cariche."""
  E_total = np.array([0.0, 0.0])
  for charge in charges:
    E_total += electric_field(charge[2], r, np.array([charge[0], charge[1]]))
  return E_total

@st.cache_data
def total_electric_potential(charges, r):
  """Calcola il potenziale elettrico totale prodotto da un insieme di cariche."""
  V_total = 0.0
  for charge in charges:
    V_total += electric_potential(charge[2], r,
                                  np.array([charge[0], charge[1]]))
  return V_total

# Create a grid of points
# Sidebar slider for grid density
# Create a grid of points using the selected grid density
x = np.linspace(x_min, x_max, grid_density)
y = np.linspace(y_min, y_max, grid_density)
X, Y = np.meshgrid(x, y)

# Calculate electric field and potential at each point
E_x = np.zeros_like(X)
E_y = np.zeros_like(Y)

V = np.zeros_like(X)

for i in range(X.shape[0]):
  for j in range(X.shape[1]):
    r = np.array([X[i, j], Y[i, j]])
    E = total_electric_field(charges, r)
    E_x[i, j], E_y[i, j] = E
    V[i, j] = total_electric_potential(charges, r)

E_magnitude = np.sqrt(E_x**2 + E_y**2)
E_x_normalized = E_x / E_magnitude
E_y_normalized = E_y / E_magnitude

# Create electric field vector plot
plt.figure(figsize=(10, 5))
plt.quiver(X, Y, E_x_normalized, E_y_normalized, E_magnitude, scale=25, cmap='viridis')
plt.colorbar(label='Field Magnitude')
plt.title('Electric Field')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
st.pyplot(plt.gcf())
plt.clf()

# Create electric field stream plot (lines)
plt.figure(figsize=(10, 5))
plt.streamplot(X, Y, E_x_normalized, E_y_normalized, color=E_magnitude, linewidth=1, cmap='viridis', density=stream_density)
plt.colorbar(label='Field Magnitude')
plt.title('Electric Field Lines')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
st.pyplot(plt.gcf())
plt.clf()

# Create electric potential contour plot
plt.figure(figsize=(10, 5))
plt.contourf(X, Y, V, 50, cmap='RdYlBu')
plt.title('Electric Potential')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar(label='Potential (V)')
plt.grid(True)
st.pyplot(plt.gcf())  # Aggiungi questa riga
