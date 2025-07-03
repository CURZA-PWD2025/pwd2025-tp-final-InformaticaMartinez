<template>
  <form @submit.prevent="submit" class="formulario">
    <h2>Agregar Categoria</h2>
    <input v-model="nombre" placeholder="Nombre de la categoría" class="input" />
    <button button type="submit" class="boton">Agregar Categoría</button>
  </form>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useCategoriaStore } from '@/stores/categoriaStore';

const store = useCategoriaStore();
const nombre = ref('');

const submit = async () => {
  if (nombre.value.trim()) {
    await store.create({ nombre: nombre.value });
    nombre.value = '';
  }
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

