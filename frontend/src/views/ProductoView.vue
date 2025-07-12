<template>
  <div>
    <h1>Gestión de Productos</h1>
    <ProductoForm v-if="loginStore.isLogged" />
    <p v-else class="aviso">⚠️ Debes ingresar para agregar o editar productos</p>
    <ProductoList />
  </div>
</template>

<script setup lang="ts">
import ProductoList from '@/components/producto/ProductoList.vue';
import ProductoForm from '@/components/producto/ProductoForm.vue';
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