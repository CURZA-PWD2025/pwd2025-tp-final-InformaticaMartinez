import { defineStore } from 'pinia';

export const useLoginStore = defineStore('login', {
  state: () => ({
    isLogged: false
  }),
  actions: {
    login() {
      this.isLogged = true;
    },
    logout() {
      this.isLogged = false;
    }
  }
});
