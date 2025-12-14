<template>
  <div class="app">
    <header>
      <img src="../public/cerveza-logo.png" alt="Cervecería" class="logo" />
      <h1>Gestor Cerveceria</h1>
      <nav>
        <router-link to="/" class="nav-link">Inicio</router-link>
        <router-link to="/productos" class="nav-link">Productos</router-link>
        <router-link to="/tipos" class="nav-link">Tipos</router-link>
        <router-link to="/categorias" class="nav-link">Categorías</router-link>
        <router-link to="/proveedores" class="nav-link">Proveedores</router-link>
        <button @click="toggleLogin" class="nav-link">
          {{ loginStore.isLogged ? "Cerrar sesión" : "Ingresar" }}
        </button>
      </nav>
    </header>
    <main>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router';
import { useLoginStore } from '@/stores/loginStore';

const loginStore = useLoginStore();

const toggleLogin = () => {
  if (loginStore.isLogged) {
    loginStore.logout();
  } else {
    loginStore.login();
  }
};
</script>

<style scoped>
.app {
  background-color: #1c1c1c; 
  color: #f0e6d2; 
  min-height: 100vh;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
 box-sizing: border-box;
  transition: background-color 0.3s, color 0.3s;
}

header {
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 1000;
  height: 150px;
  text-align: center;
  padding: 1rem;
  background-color: #292929;
  border-bottom: 1px solid #c8aa6e; 
}

.logo {
  width: 50px;
  display: flex;
  justify-content: flex-end
}

h1 {
  margin-top: -50px;
  font-size: 2rem;
  color: #c8aa6e;
  margin-bottom: 1rem;
}

nav {
  margin-top: 1rem;
  display: flex;
  justify-content: center;
  gap: 2rem;
}

.nav-link {
  color: #f0e6d2;
  text-decoration: none;
  font-weight: bold;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  background-color:teal; 
  transition: background-color 0.3s, color 0.3s;
}

.nav-link:hover {
  background-color: #004d4d;
  color: #fff;
}

main {
  margin-top: 120px;
  padding: 1rem;
  width: 100%;
  max-width: 1200px;
  box-sizing: border-box;
}
</style>
