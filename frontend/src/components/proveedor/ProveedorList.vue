<template>
  <div class="listado">
    <h2>Listado de Proveedores</h2>
    <ul>
      <li v-for="prov in store.proveedores" :key="prov.id" class="item">
        <div v-if="editandoId === prov.id" class="modo-edicion">
          <input v-model="prov.nombre" placeholder="Nombre" />
          <input v-model="prov.telefono" placeholder="Teléfono" />
          <input v-model="prov.direccion" placeholder="Dirección" />
          <input v-model="prov.email" placeholder="Email" />
          <button @click="guardarEdicion(prov)" class="boton-guardar">Guardar</button>
          <button @click="cancelarEdicion" class="boton-cancelar">Cancelar</button>
        </div>
        <div v-else>
          <strong>Nombre:</strong> {{ prov.nombre }}<br />
          <strong>Teléfono:</strong> {{ prov.telefono || '-' }}<br />
          <strong>Dirección:</strong> {{ prov.direccion || '-' }}<br />
          <strong>Email:</strong> {{ prov.email || '-' }}
        </div>

        <div class="acciones">
          <button
            v-if="loginStore.isLogged && editandoId !== prov.id"
            @click="editar(prov.id)"
            class="boton-actualizar"
          >
            Actualizar
          </button>
          <button
            v-if="loginStore.isLogged && editandoId !== prov.id"
            @click="store.destroy(prov.id)"
            class="boton-eliminar"
          >
            Eliminar
          </button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useProveedorStore } from '@/stores/proveedorStore'
import { useLoginStore } from '@/stores/loginStore'

const store = useProveedorStore()
const loginStore = useLoginStore()

const editandoId = ref<number | null>(null)

onMounted(async () => {
  await store.fetch()
})

const editar = (id: number) => {
  editandoId.value = id
}

const guardarEdicion = async (prov: any) => {
  if (!prov.id) {
    alert('Error: El proveedor no tiene ID válido.')
    return
  }
  await store.update({
    id: prov.id,
    nombre: prov.nombre,
    telefono: prov.telefono,
    direccion: prov.direccion,
    email: prov.email,
  })
  await store.fetch()
  editandoId.value = null
}

const cancelarEdicion = () => {
  editandoId.value = null
}
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
