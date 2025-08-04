<template>
  <div>
    <h1>Gestión de Categorías</h1>
    <CategoriaForm  v-if="loginStore.isLogged"/>
    <p v-else class="aviso">⚠️ Debes ingresar para agregar o editar Categorias</p>
    <CategoriaList  />
  </div>
</template>

<script setup lang="ts">
import CategoriaForm from '@/components/categoria/CategoriaForm.vue';
import CategoriaList from '@/components/categoria/CategoriaList.vue';
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