<template>
  <div>
    <h1>Gestión de Proveedores</h1>
    <ProveedorForm v-if="loginStore.isLogged"/>
    <p v-else class="aviso">⚠️ Debes ingresar para agregar o editar Proveedor</p>
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
h1 {
  font-size: 2rem;
  color: #c8aa6e;  
}
.aviso {
  color: #b71c1c;
    
}
</style>