<template>
  <div>
    <h1>Gestión de Categorías</h1>
    <CategoriaForm />
    <CategoriaList />
  </div>
</template>

<script setup lang="ts">
import CategoriaForm from '@/components/categoria/CategoriaForm.vue';
import CategoriaList from '@/components/categoria/CategoriaList.vue';
</script>
