<template>
  <form @submit.prevent="onSubmit" class="formulario">
    <h2>Crear Producto</h2>
    <input v-model="nombre" placeholder="Nombre" class="input" />
    <input v-model.number="precio" placeholder="Precio" type="number" class="input" />

    <select v-model.number="tipo_id" class="input">
      <option disabled value="">Seleccione Tipo</option>
      <option v-for="t in tipos" :key="t.id" :value="t.id">{{ t.nombre }}</option>
    </select>

    <select v-model.number="categoria_id" class="input">
      <option disabled value="">Seleccione Categoría</option>
      <option v-for="c in categorias" :key="c.id" :value="c.id">{{ c.nombre }}</option>
    </select>
    <select v-model.number="proveedor_id" class="input">
      <option disabled value="">Seleccione Proveedor</option>
      <option v-for="p in proveedores" :key="p.id" :value="p.id">{{ p.nombre }}</option>
    </select>
    <button type="submit" class="boton">Agregar Producto</button>
  </form>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useProductoStore } from '@/stores/productoStore'
import { useTipoStore } from '@/stores/tipoStore'
import { useCategoriaStore } from '@/stores/categoriaStore'
import { useProveedorStore } from '@/stores/proveedorStore' 

const store = useProductoStore()
const tipoStore = useTipoStore()
const categoriaStore = useCategoriaStore()
const proveedorStore = useProveedorStore()


const nombre = ref('')
const precio = ref('')
const tipo_id = ref('')
const categoria_id = ref('')
const proveedor_id = ref('')

const tipos = ref([])
const categorias = ref([])
const proveedores = ref([]);

onMounted(async () => {
  await tipoStore.fetch()
  await categoriaStore.fetch()

  tipos.value = tipoStore.tipos
  categorias.value = categoriaStore.categorias
  proveedores.value = proveedorStore.proveedores
})

const onSubmit = async () => {
  await store.create({
    nombre: nombre.value,
    precio: precio.value,
    tipo_id: tipo_id.value,
    categoria_id: categoria_id.value,
    proveedor_id: proveedor_id.value,
  })

  nombre.value = ''
  precio.value = ''
  tipo_id.value = ''
  categoria_id.value = ''
  proveedor_id.value = ''

}
</script>

<style scoped>
  
.formulario {
  max-width: 600px;
  margin: 1rem auto;
  padding: 1.5rem;
  background-color: #3b3b3b;
  border-radius: 12px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}
h2 {
  font-size: 2.5rem;
  color: #c8aa6e;
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
