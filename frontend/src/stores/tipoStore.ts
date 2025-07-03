import { defineStore } from 'pinia';
import { tipoService } from '@/services/tipoService';

export const useTipoStore = defineStore('tipo', {
  state: () => ({ tipos: [] as any[] }),
  actions: {
    async fetch() {
      this.tipos = await tipoService.fetch();
    },
    async create(data: any) {
      await tipoService.create(data);
      await this.fetch();
    },
    async destroy(id: number) {
      await tipoService.delete(id);
      await this.fetch();
    }
  }
});