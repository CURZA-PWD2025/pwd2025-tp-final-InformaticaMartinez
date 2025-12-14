<template>
  <div class="listado">
    <h2>Listado de Categorias</h2>
  <ul>
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
  max-height: 400px;
  overflow-y: auto;
  max-width: 700px;
  margin: 0.5rem auto;
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
.modo-edicion {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  width: 100%;
}
.boton-actualizar {
  background-color: #ffa500;
  color: #000;
  border: none;
  border-radius: 6px;
  padding: 0.5rem 1rem;
  margin-right: 0.5rem;
  cursor: pointer;
}
.boton-eliminar {
  background-color: crimson;
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 0.5rem 1rem;
  cursor: pointer;
}
.boton-guardar {
  background-color: teal;
  color: #fff;
  border-radius: 6px;
  padding: 0.5rem 1rem;
  margin-top: 0.5rem;
  cursor: pointer;
}
.boton-cancelar {
  background-color: gray;
  color: #fff;
  border-radius: 6px;
  padding: 0.5rem 1rem;
  margin-top: 0.5rem;
  cursor: pointer;
}
</style>
