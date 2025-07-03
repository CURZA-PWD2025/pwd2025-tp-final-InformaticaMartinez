<template>
  <div>
    <h1>Gestión de Proveedores</h1>
    <ProveedorForm />
    <ProveedorList />
  </div>
</template>
<script setup lang="ts">
import ProveedorForm from '@/components/proveedor/ProveedorForm.vue';
import ProveedorList from '@/components/proveedor/ProveedorList.vue';
</script>