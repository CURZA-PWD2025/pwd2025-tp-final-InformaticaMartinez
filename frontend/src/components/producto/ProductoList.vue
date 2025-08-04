<template>
  <div class="listado">
    <h2>Listado de Productos</h2>
    <ul>
      <li v-for="p in store.productos" :key="p.id" class="item">
        <div>
          <strong>Nombre:</strong> {{ p.nombre }}<br />
          <strong>Precio:</strong> ${{ p.precio }}<br />
          <strong>Tipo:</strong> {{ p.tipo_nombre }}<br />
          <strong>Categoría:</strong> {{ p.categoria_nombre }}
        </div>
        <div class="acciones">
          <button v-if="loginStore.isLogged" @click="editar(p)" class="boton-actualizar">Actualizar</button>
          <button v-if="loginStore.isLogged" @click="store.destroy(p.id)" class="boton-eliminar">Eliminar</button>
        </div>
      </li>
    </ul>

    <div v-if="editando" class="listado">
      <h2>Editar Producto</h2>
      <input v-model="editItem.nombre" placeholder="Nombre" />
      <input v-model.number="editItem.precio" placeholder="Precio" type="number" />
      <select v-model.number="editItem.tipo_id">
        <option disabled value="">Seleccione Tipo</option>
        <option v-for="t in tipos" :key="t.id" :value="t.id">{{ t.nombre }}</option>
      </select>
      <select v-model.number="editItem.categoria_id">
        <option disabled value="">Seleccione Categoría</option>
        <option v-for="c in categorias" :key="c.id" :value="c.id">{{ c.nombre }}</option>
      </select>
      <button @click="guardarEdicion" class="boton-guardar">Guardar Cambios</button>
      <button @click="cancelarEdicion" class="boton-cancelar">Cancelar</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useProductoStore } from '@/stores/productoStore';
import { useTipoStore } from '@/stores/tipoStore';
import { useCategoriaStore } from '@/stores/categoriaStore';
import { useLoginStore } from '@/stores/loginStore';
const loginStore = useLoginStore();
const store = useProductoStore();
const tipoStore = useTipoStore();
const categoriaStore = useCategoriaStore();
const editando = ref(false);
const editItem = ref<any>({});
const tipos = ref([]);
const categorias = ref([]);

onMounted(async () => {
  await store.fetch();
  await tipoStore.fetch();
  await categoriaStore.fetch();
  tipos.value = tipoStore.tipos;
  categorias.value = categoriaStore.categorias;
});

const editar = (producto: any) => {
  editItem.value = { ...producto };
  editando.value = true;           
};

const guardarEdicion = async () => {
  if (!editItem.value.id) {
    alert("Error: El producto no tiene ID válido.");
    return;
  }
  await store.update({
    id: editItem.value.id,
    nombre: editItem.value.nombre,
    precio: editItem.value.precio,
    tipo_id: editItem.value.tipo_id,
    categoria_id: editItem.value.categoria_id,
  });

  await store.fetch(); 
  editando.value = false; 
};

const cancelarEdicion = () => {
  editando.value = false;
  editItem.value = {};
};
</script>

<style scoped>
.listado {
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
  margin-right: 0.5rem;
  cursor: pointer;
} 
.boton-cancelar {
  background-color: crimson;
  color: #fff;
  border: none;
  border-radius: 4px;
  padding: 0.5rem 1rem;
  margin-right: 1rem;
  cursor: pointer;
}
</style>
