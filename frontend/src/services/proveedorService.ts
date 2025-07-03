import axios from 'axios';
const API = 'http://localhost:5000/proveedores';

export const proveedorService = {
  async fetch() {
    const res = await axios.get(API);
    return res.data;
  },
  async create(data: any) {
    return (await axios.post(API, data)).data;
  },
  async delete(id: number) {
    return (await axios.delete(`${API}/${id}`)).data;
  }
};