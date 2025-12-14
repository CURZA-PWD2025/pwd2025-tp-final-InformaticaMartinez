<template>
  <GestionLayout
    titulo="Gestión de Categorías"
    entidad="categorías"
    :mostrarForm="loginStore.isLogged"
  >
    <template #form>
      <CategoriaForm />
    </template>

    <template #list>
      <CategoriaList />
    </template>
  </GestionLayout>
</template>

<script setup lang="ts">
import GestionLayout from '@/components/layout/GestionLayout.vue'
import CategoriaForm from '@/components/categoria/CategoriaForm.vue'
import CategoriaList from '@/components/categoria/CategoriaList.vue'
import { useLoginStore } from '@/stores/loginStore'

const loginStore = useLoginStore()
</script>
