import { defineStore } from 'pinia';
import { proveedorService } from '@/services/proveedorService';

export const useProveedorStore = defineStore('proveedor', {
  state: () => ({ proveedores: [] as any[] }),
  actions: {
    async fetch() {
      this.proveedores = await proveedorService.fetch();
    },
    async create(data: any) {
      await proveedorService.create(data);
      await this.fetch();
    },
    async destroy(id: number) {
      await proveedorService.delete(id);
      await this.fetch();
    }
  }
});
