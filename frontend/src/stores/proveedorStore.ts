import { defineStore } from 'pinia';
import axios from 'axios';

export const useProveedorStore = defineStore('proveedor', {
  state: () => ({
    proveedores: [] as any[],
  }),

  actions: {
    async fetch() {
      try {
        const res = await axios.get('http://127.0.0.1:5000/proveedores');
        this.proveedores = res.data;
      } catch (error) {
        console.error('Error al obtener proveedores:', error);
      }
    },

    async create(proveedor: { nombre: string; telefono?: string; direccion?: string; email?: string }) {
      try {
        await axios.post('http://127.0.0.1:5000/proveedores', proveedor);
        await this.fetch();
      } catch (error) {
        console.error('Error al crear proveedor:', error);
      }
    },

    async update(proveedor: { id: number; nombre: string; telefono?: string; direccion?: string; email?: string }) {
      if (!proveedor.id) {
        console.error('Error: Falta el ID del proveedor');
        return;
      }
      try {
        await axios.put(`http://127.0.0.1:5000/proveedores/${proveedor.id}`, proveedor);
        await this.fetch();
      } catch (error) {
        console.error('Error al actualizar proveedor:', error);
      }
    },

    async destroy(id: number) {
      try {
        await axios.delete(`http://127.0.0.1:5000/proveedores/${id}`);
        await this.fetch();
      } catch (error) {
        console.error('Error al eliminar proveedor:', error);
      }
    },
  },
});
