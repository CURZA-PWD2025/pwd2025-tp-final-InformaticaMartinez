import axios from 'axios';

const API = 'http://localhost:5000/tipos';

export const tipoService = {
  async fetch() {
    const res = await axios.get(API);
    return res.data;
  },
  async create(data: any) {
    const res = await axios.post(API, data);
    return res.data;
  },
  async delete(id: number) {
    const res = await axios.delete(`${API}/${id}`);
    return res.data;
  }
};