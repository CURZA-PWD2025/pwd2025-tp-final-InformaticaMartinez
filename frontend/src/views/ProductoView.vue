<template>
  <main>
    <h1>Gestión de Productos</h1>
    <ProductoForm />
    <ProductoList />
  </main>
</template>

<script setup lang="ts">
import ProductoForm from '@/components/producto/ProductoForm.vue';
import ProductoList from '@/components/producto/ProductoList.vue';
</script>