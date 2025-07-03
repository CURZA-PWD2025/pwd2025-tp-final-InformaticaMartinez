import { defineStore } from 'pinia';
import { productoService } from '@/services/productoService';

export const useProductoStore = defineStore('producto', {
  state: () => ({
    productos: [] as any[],
  }),
  actions: {
    async fetch() {
      this.productos = await productoService.getAll();
    },
    async create(data: any) {
      await productoService.create(data);
      this.fetch();
    },
    async update(id: number, data: any) {
      await productoService.update(id, data);
      this.fetch();
    },
    async destroy(id: number) {
      await productoService.destroy(id);
      this.fetch();
    }
  }
});
