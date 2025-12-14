<template>
  <GestionLayout
    titulo="Gestión de Proveedores"
    entidad="proveedores"
    :mostrarForm="loginStore.isLogged"
  >
    <template #form>
      <ProveedorForm />
    </template>

    <template #list>
      <ProveedorList />
    </template>
  </GestionLayout>
</template>

<script setup lang="ts">
import GestionLayout from '@/components/layout/GestionLayout.vue'
import ProveedorForm from '@/components/proveedor/ProveedorForm.vue'
import ProveedorList from '@/components/proveedor/ProveedorList.vue'
import { useLoginStore } from '@/stores/loginStore'

const loginStore = useLoginStore()
</script>
