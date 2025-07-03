import { defineStore } from 'pinia';
import { categoriaService } from '@/services/categoriaService';

export const useCategoriaStore = defineStore('categoria', {
  state: () => ({ categorias: [] as any[] }),
  actions: {
    async fetch() {
      this.categorias = await categoriaService.fetch();
    },
    async create(data: any) {
      await categoriaService.create(data);
      await this.fetch();
    },
    async destroy(id: number) {
      await categoriaService.delete(id);
      await this.fetch();
    }
  }
});
