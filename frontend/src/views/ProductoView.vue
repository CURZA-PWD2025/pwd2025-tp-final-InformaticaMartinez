<template>
  <GestionLayout
    titulo="Gestión de Productos"
    entidad="productos"
    :mostrarForm="loginStore.isLogged"
  >
    <template #form>
      <ProductoForm />
    </template>

    <template #list>
      <ProductoList />
    </template>
  </GestionLayout>
</template>

<script setup lang="ts">
import GestionLayout from '@/components/layout/GestionLayout.vue'
import ProductoForm from '@/components/producto/ProductoForm.vue'
import ProductoList from '@/components/producto/ProductoList.vue'
import { useLoginStore } from '@/stores/loginStore'

const loginStore = useLoginStore()
</script>
