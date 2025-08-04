<template>
  <div class="listado">
    <h2>Listado de Categorias</h2>
  <ul class="lista">
    <li v-for="c in store.categorias" :key="c.id" class="item">
      {{ c.nombre }}
      <button v-if="loginStore.isLogged" @click="store.destroy(c.id)" class="boton-eliminar">Eliminar</button>
    </li>
  </ul>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { useCategoriaStore } from '@/stores/categoriaStore';
import { useLoginStore } from '@/stores/loginStore';
const loginStore = useLoginStore();
const store = useCategoriaStore();
onMounted(() => store.fetch());
</script>

<style scoped>
.listado {
  max-width: 700px;
  margin: 0.5rem;
  background: #292929;
  padding: 0.5rem;
  border-radius: 12px;
  color: #f0e6d2;
}
h2 {
  font-size: 1.25rem;
  color: #c8aa6e;
  margin-bottom: 0.5rem;
}
.item {
  background: #3b3b3b;
  padding: 0.5rem;
  border-radius: 8px;
  margin-bottom: 0.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
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
h2 {
  font-size: 1.5rem;
  color: #c8aa6e;
  margin-bottom: 1rem;
}
</style>
