<template>
  <div>
    <h1>Gestión de Tipos</h1>
    <TipoForm v-if="loginStore.isLogged"/>
    <p v-else class="aviso">⚠️ Debes ingresar para agregar o editar proveedor</p>
    <TipoList />
  </div>
</template>
<script setup lang="ts">
import TipoForm from '@/components/tipo/TipoForm.vue';
import TipoList from '@/components/tipo/TipoList.vue';
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
