<template>
  <q-card class="my-card">
    <q-card-section
      v-for="farm in farms"
      :key="farm.id"
    >
      <h5>{{ farm.legal_status_name }} {{ farm.name }}</h5>
    </q-card-section>
  </q-card>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { getFarms } from 'src/modules/farms'

export default defineComponent({
  name: 'FarmsCard',
  async setup () {
    return {
      farms: await getFarms()
    }
  }
})
</script>
