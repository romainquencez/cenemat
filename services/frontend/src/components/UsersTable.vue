<template>
  <q-table
    :rows="rows"
    separator="cell"
    :columns="columns"
    :pagination="{ rowsPerPage: 20 }"
    no-data-label="Aucun utilisateur."
    row-key="name"
  />
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { getUsers } from 'src/modules/users'

export default defineComponent({
  name: 'UsersPage',
  async setup () {
    return {
      columns: [
        {
          align: 'left',
          name: 'identifier',
          field: 'identifier',
          label: 'Identifiant',
          sortable: true,
        },
        {
          align: 'left',
          name: 'first_name',
          field: 'first_name',
          label: 'Prénom',
          sortable: true,
        },
        {
          align: 'left',
          name: 'last_name',
          field: 'last_name',
          label: 'Nom',
          sortable: true,
        },
        {
          align: 'left',
          name: 'email',
          field: 'email',
          label: 'Email',
          sortable: true,
        },
        {
          align: 'left',
          name: 'membership_year',
          field: 'membership_year',
          label: 'Adhésion',
          sortable: true,
        },
      ],
      rows: await getUsers()
    }
  }
})
</script>
