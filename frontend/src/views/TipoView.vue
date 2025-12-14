<template>
  <GestionLayout titulo="Gestión de Tipos" 
    entidad="tipos" 
    :mostrarForm="loginStore.isLogged">
    <template #form>
      <TipoForm />
    </template>

    <template #list>
      <TipoList />
    </template>
  </GestionLayout>
</template>

<script setup lang="ts">
import GestionLayout from '@/components/layout/GestionLayout.vue'
import TipoForm from '@/components/tipo/TipoForm.vue'
import TipoList from '@/components/tipo/TipoList.vue'
import { useLoginStore } from '@/stores/loginStore'

const loginStore = useLoginStore()
</script>
