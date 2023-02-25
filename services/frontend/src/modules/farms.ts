import { api } from 'boot/axios'

export async function getFarms () {
  return await api.get('farms/list').then(response => response.data)
}
