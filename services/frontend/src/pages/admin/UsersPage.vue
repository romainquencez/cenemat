<template>
  <q-page class="q-pa-lg">
    <h1 class="text-h3 q-mt-none">
      Utilisateurs
    </h1>
    <Suspense>
      <template #fallback>
        <p>
          Chargement...
        </p>
      </template>

      <UsersTable />
    </Suspense>
  </q-page>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import UsersTable from 'src/components/UsersTable.vue'

export default defineComponent({
  name: 'UsersPage',
  components: {
    UsersTable
  }
})
</script>
