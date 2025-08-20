import { defineStore } from 'pinia';
import axios from 'axios';

export const useProductoStore = defineStore('producto', {
  state: () => ({
    productos: [] as any[],
  }),

  actions: {
    async fetch() {
      try {
        const res = await axios.get('http://127.0.0.1:5000/productos');
        this.productos = res.data;
      } catch (error) {
        console.error('Error al obtener productos:', error);
      }
    },

    async create(producto: {
      nombre: string;
      precio: number;
      tipo_id: number;
      categoria_id: number;
    }) {
      try {
        await axios.post('http://127.0.0.1:5000/productos', producto);
        await this.fetch();
      } catch (error) {
        console.error('Error al crear producto:', error);
      }
    },

    async update(producto: {
      id: number;
      nombre: string;
      precio: number;
      tipo_id: number;
      categoria_id: number;
    }) {
      try {
        await axios.put(`http://127.0.0.1:5000/productos/${producto.id}`, producto);
        await this.fetch();
      } catch (error) {
        console.error('Error al actualizar producto:', error);
      }
    },

    async destroy(id: number) {
      try {
        await axios.delete(`http://127.0.0.1:5000/productos/${id}`);
        await this.fetch();
      } catch (error) {
        console.error('Error al eliminar producto:', error);
      }
    },
  },
});
