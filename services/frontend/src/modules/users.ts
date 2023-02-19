import { api } from 'boot/axios'

export async function getUsers () {
  return await api.get('users/list').then(response => response.data)
}
