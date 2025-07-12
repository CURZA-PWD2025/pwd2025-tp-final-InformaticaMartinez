<template>
  <div class="listado">
     <h2>Listado de Tipos</h2>
  <ul class="lista">
    <li v-for="t in store.tipos" :key="t.id" class="item">
      {{ t.nombre }}
      <button v-if="loginStore.isLogged" @click="store.destroy(t.id)" class="boton-eliminar">Eliminar</button>
    </li>
  </ul>
  </div>
</template>
<script setup lang="ts">
import { onMounted } from 'vue';
import { useTipoStore } from '@/stores/tipoStore';
import { useLoginStore } from '@/stores/loginStore';
const loginStore = useLoginStore();
const store = useTipoStore();
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
h2 {
  font-size: 2.5rem;
  color: #070707;
  margin-bottom: 1rem;
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