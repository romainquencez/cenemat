<template>
  <q-page class="q-pa-md">
    <h3>Mon compte</h3>

    <q-list separator>
      <q-item>
        <q-item-section>
          <q-item-label overline>Identité</q-item-label>
          <q-item-label>{{ user.firstName }} {{ user.lastName }}</q-item-label>
        </q-item-section>
      </q-item>

      <q-item>
        <q-item-section>
          <q-item-label overline>Identifiant</q-item-label>
          <q-item-label>{{ user.identifier }}</q-item-label>
        </q-item-section>
      </q-item>

      <q-item>
        <q-item-section>
          <q-item-label overline>E-mail</q-item-label>
          <q-item-label>{{ user.email }}</q-item-label>
        </q-item-section>
      </q-item>

      <q-item>
        <q-item-section>
          <q-item-label overline>Exploitation</q-item-label>
          <q-item-label>{{ user.farm }}</q-item-label>
        </q-item-section>
      </q-item>
    </q-list>
  </q-page>
</template>

<script lang="ts">
import { useUserStore } from 'stores/users'
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'UserPage',
  setup () {
    const userStore = useUserStore()
    const user = userStore.stateUser

    return {
      user,
    }
  }
})
</script>
