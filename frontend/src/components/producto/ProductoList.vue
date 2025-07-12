<template>
  <div class="listado">
    <h2>Listado de Productos</h2>
    <ul class="lista">
      <li v-for="p in store.productos" :key="p.id" class="item">
        <div class="info">
          <strong>Nombre:</strong> {{ p.nombre }}<br />
          <strong>Precio:</strong> ${{ p.precio }}<br />
          <strong>Tipo:</strong> {{ p.tipo_nombre }}<br />
          <strong>Categoría:</strong> {{ p.categoria_nombre }}<br />
          </div>
        <button v-if="loginStore.isLogged" @click="store.destroy(p.id)" class="boton-eliminar">Eliminar</button>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { useProductoStore } from '@/stores/productoStore';
import { useLoginStore } from '@/stores/loginStore';
const loginStore = useLoginStore();

const store = useProductoStore();
onMounted(() => store.fetch());
</script>

<style scoped>
.listado {
  max-width: 800px;
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
  position: relative;
  color: #fff;
}

.info {
  margin-right: 100px;
}

.boton-eliminar {
  background-color: crimson;
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  position: absolute;
  top: 1rem;
  right: 1rem;
  cursor: pointer;
}

.boton-eliminar:hover {
  background-color: darkred;
}
.aviso {
  color: #b71c1c;
  font-weight: bold;
  margin-top: 1rem;
}
</style>
