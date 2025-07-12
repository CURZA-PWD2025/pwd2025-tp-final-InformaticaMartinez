<template>
  <div>
    <h1>Gestión de Proveedores</h1>
    <ProveedorForm v-if="loginStore.isLogged"/>
    <p v-else class="aviso">⚠️ Debes ingresar para agregar o editar proveedor</p>
    <ProveedorList />
  </div>
</template>
<script setup lang="ts">
import ProveedorForm from '@/components/proveedor/ProveedorForm.vue';
import ProveedorList from '@/components/proveedor/ProveedorList.vue';
import { useLoginStore } from '@/stores/loginStore';
const loginStore = useLoginStore();
</script>
<style scoped>
.aviso {
  color: #b71c1c;
  font-weight: bold;
  margin-top: 1rem;
}
</style>