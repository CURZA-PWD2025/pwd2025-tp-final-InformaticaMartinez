<template>
  <div class="listado">
    <h2>Listado de Proveedores</h2>
    <ul class="lista">
      <li v-for="p in store.proveedores" :key="p.id" class="item">
        <div class="info">
          <strong>Nombre:</strong> {{ p.nombre }}<br />
          <strong>Teléfono:</strong> {{ p.telefono || '-' }}<br />
          <strong>Dirección:</strong> {{ p.direccion || '-' }}<br />
          <strong>Email:</strong> {{ p.email || '-' }}
        </div>
        <button v-if="loginStore.isLogged" @click="store.destroy(p.id)" class="boton-eliminar">Eliminar</button>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { useProveedorStore } from '@/stores/proveedorStore';
import { useLoginStore } from '@/stores/loginStore';
const loginStore = useLoginStore();

const store = useProveedorStore();
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
.aviso {
  color: #b71c1c;
  font-weight: bold;
  margin-top: 1rem;
}
</style>
