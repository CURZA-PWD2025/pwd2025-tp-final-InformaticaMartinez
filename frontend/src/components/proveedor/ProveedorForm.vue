<template>
  <form @submit.prevent="submit" class="formulario">
    <h2>Agregar Proveedor</h2>
    <input v-model="nombre" placeholder="Nombre del proveedor" class="input" />
    <input v-model="telefono" placeholder="Teléfono" class="input" />
    <input v-model="direccion" placeholder="Dirección" class="input" />
    <input v-model="email" placeholder="Email" class="input" />
    <button type="submit" class="boton">Agregar Proveedor</button>
  </form>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useProveedorStore } from '@/stores/proveedorStore';

const store = useProveedorStore();
const nombre = ref('');
const telefono = ref('');
const direccion = ref('');
const email = ref('');

const submit = async () => {
  if (!nombre.value) return;
  await store.create({
    nombre: nombre.value,
    telefono: telefono.value,
    direccion: direccion.value,
    email: email.value
  });
  nombre.value = '';
  telefono.value = '';
  direccion.value = '';
  email.value = '';
};
</script>

<style scoped>
.formulario {
  max-width: 600px;
  margin: 2rem auto;
  padding: 1.5rem;
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}
h2 {
  font-size: 2.5rem;
  color: #070707;
  margin-bottom: 1rem;
}
.input {
  width: 100%;
  margin-bottom: 1rem;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}
.boton {
  background-color: teal;
  color: #fff;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.boton:hover {
  background-color: #006666;
}
</style>
