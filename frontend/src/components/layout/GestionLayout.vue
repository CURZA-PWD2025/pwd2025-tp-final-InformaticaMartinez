<template>
  <section class="gestion-wrapper">
    <h1 class="titulo">{{ titulo }}</h1>

    <p v-if="!mostrarForm" class="aviso">
      ⚠️ Debes ingresar para gestionar {{ entidad }}
    </p>

    <div
      class="contenedor"
      :class="{ soloLista: !mostrarForm }"
    >
      <div v-if="mostrarForm" class="card">
        <slot name="form" />
      </div>

      <div class="card lista">
        <slot name="list" />
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">

defineProps<{
  titulo: string
  entidad: string
  mostrarForm: boolean
}>()
</script>

<style scoped>
  
.gestion-wrapper {
  min-height: calc(100vh - 160px); 
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding-top: 3rem;
}

.titulo {
  color: var(--accent-main);
  font-size: 2rem;
  margin-bottom: 0.5rem;
  text-align: center;
}

.aviso {
  color: #ff5252;
  margin-bottom: 2rem;
  text-align: center;
}

.contenedor {
  width: 100%;
  max-width: 1100px;
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 2rem;
}

.contenedor.soloLista {
  grid-template-columns: 1fr;
  justify-items: center;
}

.lista {
  width: 100%;
}
</style>
