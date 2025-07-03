<template>
  <div class="listado">
    <h2>Listado de Categorias</h2>
  <ul class="lista">
    <li v-for="c in store.categorias" :key="c.id" class="item">
      {{ c.nombre }}
      <button @click="store.destroy(c.id)" class="boton-eliminar">Eliminar</button>
    </li>
  </ul>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { useCategoriaStore } from '@/stores/categoriaStore';

const store = useCategoriaStore();
onMounted(() => store.fetch());
</script>

<style scoped>
.listado {
  max-width: 700px;
  margin: 2rem auto;
  padding: 1.5rem;
  background-color: #f5f5f5;
  border-radius: 12px;
}
h2 {
  font-size: 2.5rem;
  color: #070707;
  margin-bottom: 1rem;
}
.lista {
  list-style: none;
  padding: 0;
}
.item {
  background: #4b4a4a;
  border: 1px solid #bbb;
  padding: 1rem;
  margin-bottom: 1rem;
  border-radius: 8px;
}
.boton-eliminar {
  background-color: crimson;
  color: white;
  padding: 0.5rem;
  border: none;
  border-radius: 4px;
  float: right;
  cursor: pointer;
}
</style>
