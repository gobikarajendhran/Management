import axios from 'axios'

export const API_BASE = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8001/api'
const api = axios.create({ baseURL: API_BASE, timeout: 12000 })
api.interceptors.request.use(config => {
  const token = localStorage.getItem('kbm_token')
  if (token) config.headers.Authorization = `Token ${token}`
  return config
})
api.interceptors.response.use(r=>r, err=>{ if(err.response?.status===401){localStorage.removeItem('kbm_token'); localStorage.removeItem('kbm_user'); window.dispatchEvent(new Event('auth-expired'))} return Promise.reject(err) })
export const auth = {
  login: async (username,password)=> (await api.post('/auth/token/',{username,password})).data
}
export async function listResource(resource, params={}) { const r=await api.get(`/${resource}/`,{params}); return Array.isArray(r.data)?r.data:(r.data.results||[]) }
export async function createResource(resource,data){return (await api.post(`/${resource}/`,data)).data}
export async function updateResource(resource,id,data){return (await api.patch(`/${resource}/${id}/`,data)).data}
export async function deleteResource(resource,id){return (await api.delete(`/${resource}/${id}/`)).data}
export async function getDashboard(){return (await api.get('/dashboard/')).data}
export default api
