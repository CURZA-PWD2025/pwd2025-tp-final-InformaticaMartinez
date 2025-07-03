<template>
  <div class="app">
    <header>
      <img src="../public/cerveza-logo.png" alt="Cervecería" class="logo" />
      <h1>Gestor Cerveceria</h1>
      <nav>
        <router-link to="/productos" class="nav-link">Productos</router-link>
        <router-link to="/tipos" class="nav-link">Tipos</router-link>
        <router-link to="/categorias" class="nav-link">Categorías</router-link>
        <router-link to="/proveedores" class="nav-link">Proveedores</router-link>
      </nav>
    </header>
    <main>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { RouterView, RouterLink } from 'vue-router';
</script>

<style scoped>
.app {
  background-color: #1c1c1c; 
  color: #f0e6d2; 
  min-height: 100vh;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

header {
  text-align: center;
  padding: 2rem 1rem;
  background-color: #292929;
  border-bottom: 3px solid #c8aa6e; 
}

.logo {
  width: 120px;
  margin-bottom: 1rem;
}

h1 {
  font-size: 2.5rem;
  color: #c8aa6e;
  margin-bottom: 1rem;
}

nav {
  margin-top: 1rem;
  display: flex;
  justify-content: center;
  gap: 1.5rem;
}

.nav-link {
  color: #f0e6d2;
  text-decoration: none;
  font-weight: bold;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  background-color: #006666; /* Teal */
  transition: background-color 0.3s, color 0.3s;
}

.nav-link:hover {
  background-color: #004d4d;
  color: #fff;
}

main {
  padding: 2rem;
}
</style>
