<template>
  <div class="home">
    <h2>Bienvenido al Sistema de Gestión de Cervecería</h2>
    <p>
      Este sistema te permite administrar de manera eficiente todos los aspectos de la cervecería:
    </p>
    <ul>
      <li>✔️ Gestionar productos disponibles y sus precios.</li>
      <li>✔️ Organizar tipos y categorías de cervezas.</li>
      <li>✔️ Mantener un control sobre proveedores asociados.</li>
      <li>✔️ Proteger el acceso con autenticación de usuarios.</li>
    </ul>
    <p>
      Navega por las secciones usando el menú superior para comenzar a gestionar tu cervecería.
    </p>
    </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.home {
  max-width: 900px;
  margin: 60px auto;
  text-align: center;
}


h2 {
  font-size: 2rem;
  color: #c8aa6e;
  margin-bottom: 1rem;
  text-align: center;
}

p {
  margin-bottom: 1rem;
  font-size: 1.1rem;
}

ul {
  list-style: none;
  padding: 0;
  margin: 1rem 0;
}

ul li {
  background: #3b3b3b;
  padding: 0.8rem;
  margin-bottom: 0.5rem;
  border-radius: 8px;
}


</style>
