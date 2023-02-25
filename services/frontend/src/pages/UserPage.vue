<template>
  <q-page class="q-pa-lg">
    <h3 class="q-mt-none">Mon compte</h3>

    <h4>Identité</h4>

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
    </q-list>

    <h4>Exploitations</h4>

    <Suspense>
      <template #fallback>
        <p>
          Chargement...
        </p>
      </template>

      <FarmsCard />
    </Suspense>
  </q-page>
</template>

<script lang="ts">
import { useUserStore } from 'stores/users'
import { defineComponent } from 'vue'
import FarmsCard from 'src/components/FarmsCard.vue'

export default defineComponent({
  name: 'UserPage',
  components: {
    FarmsCard
  },
  setup () {
    const userStore = useUserStore()
    const user = userStore.stateUser

    return {
      user,
    }
  }
})
</script>
